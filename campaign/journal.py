"""Single-host, append-only synthetic research receipts with optional HMAC custody.

This stores hashes and verdicts, not market prices, trading signals or model memory.
The lab remains public; caller MUST select private storage path for real receipts.
A GitHub Actions artifact does not itself provide persistence between CI runs.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import fcntl
import hashlib
import hmac
import json
import os
import re

from .controller import canonical, digest, verify_result

SCHEMA = "OracleResearchJournal/1"
ID = re.compile(r"^[A-Za-z0-9_.:-]{1,96}$")
FIELDS = {"schema", "sequence", "run_id", "experiment_id", "report_sha256",
          "fixture_sha256", "event_log_head_sha256", "classification", "promotion_allowed",
          "recorded_at_utc", "previous_sha256", "entry_sha256", "hmac_sha256"}
ROW_BUDGET = 8192
FILE_BUDGET = 16 * 1024 * 1024

class JournalError(ValueError):
    pass

def _safe_file(path: Path):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise JournalError("UNSAFE_JOURNAL_PATH")

def _valid_id(run_id):
    if not isinstance(run_id, str) or not ID.fullmatch(run_id):
        raise JournalError("INVALID_RUN_ID")

class ResearchJournal:
    def __init__(self, path: str | Path, *, key: bytes | None = None,
                 allow_unsigned_synthetic: bool = False, clock=None):
        self.path = Path(path)
        if not isinstance(key, (type(None), bytes)) or (key is not None and len(key) < 32):
            raise JournalError("CUSTODY_KEY_MUST_BE_AT_LEAST_32_BYTES")
        if key is None and not allow_unsigned_synthetic:
            raise JournalError("UNSIGNED_JOURNAL_DISABLED")
        self.key = key
        self.clock = clock or (lambda: datetime.now(timezone.utc))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        _safe_file(self.path)

    def _signature(self, entry_sha: str):
        if self.key is None:
            return None
        return hmac.new(self.key, entry_sha.encode("ascii"), hashlib.sha256).hexdigest()

    def _check(self, row, sequence, previous):
        if not isinstance(row, dict) or set(row) != FIELDS:
            raise JournalError("INVALID_JOURNAL_RECORD")
        if (row["schema"] != SCHEMA or type(row["sequence"]) is not int
            or row["sequence"] != sequence or row["previous_sha256"] != previous
            or row["classification"] != "SYNTHETIC_ONLY"
            or row["promotion_allowed"] is not False):
            raise JournalError("JOURNAL_CHAIN_OR_AUTHORITY_TAMPERED")
        _valid_id(row["run_id"])
        _valid_id(row["experiment_id"])
        for name in ("report_sha256", "fixture_sha256", "event_log_head_sha256", "entry_sha256"):
            if not isinstance(row[name], str) or not re.fullmatch(r"[a-f0-9]{64}", row[name]):
                raise JournalError("INVALID_HASH")
        try:
            stamp = datetime.fromisoformat(row["recorded_at_utc"].replace("Z", "+00:00"))
        except (TypeError, ValueError) as exc:
            raise JournalError("INVALID_RECORD_TIME") from exc
        if stamp.tzinfo is None or stamp.utcoffset() != timezone.utc.utcoffset(stamp):
            raise JournalError("NON_UTC_RECORD_TIME")
        unsigned = {k: v for k, v in row.items() if k not in ("entry_sha256", "hmac_sha256")}
        if not hmac.compare_digest(digest(unsigned), row["entry_sha256"]):
            raise JournalError("RECORD_HASH_MISMATCH")
        expected = self._signature(row["entry_sha256"])
        if expected is None:
            if row["hmac_sha256"] is not None:
                raise JournalError("SIGNED_JOURNAL_REQUIRES_KEY")
        elif not isinstance(row["hmac_sha256"], str) or not hmac.compare_digest(expected, row["hmac_sha256"]):
            raise JournalError("SIGNATURE_MISMATCH")

    def _read_unlocked(self):
        _safe_file(self.path)
        if not self.path.exists():
            return []
        if self.path.stat().st_size > FILE_BUDGET:
            raise JournalError("JOURNAL_EXCEEDS_SIZE_BUDGET")
        rows = []
        previous = None
        with self.path.open("rb") as src:
            for lineno, line in enumerate(src, 1):
                if len(line) > ROW_BUDGET or not line.endswith(b"\n"):
                    raise JournalError(f"TRUNCATED_OR_OVERSIZED_RECORD_{lineno}")
                try:
                    item = json.loads(line)
                except (ValueError, UnicodeDecodeError) as exc:
                    raise JournalError(f"INVALID_JSON_RECORD_{lineno}") from exc
                self._check(item, lineno, previous)
                previous = item["entry_sha256"]
                rows.append(item)
        if len({r["run_id"] for r in rows}) != len(rows):
            raise JournalError("DUPLICATE_RUN_IDS")
        return rows

    def read(self):
        lock_path = self.path.with_name(self.path.name + ".lock")
        _safe_file(lock_path)
        fd = os.open(str(lock_path), os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_SH)
            return self._read_unlocked()
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)

    def record(self, run_id: str, result: dict):
        _valid_id(run_id)
        # Mandatory scientific validation before anything is written.
        verify_result(result)
        if (result.get("origin") != "DETERMINISTIC_SYNTHETIC_ONLY"
            or result["independent_review"]["can_promote"] is not False):
            raise JournalError("INELIGIBLE_RESEARCH_RESULT")
        lock_path = self.path.with_name(self.path.name + ".lock")
        _safe_file(lock_path)
        fd = os.open(str(lock_path), os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            history = self._read_unlocked()
            report_sha = digest(result)
            found = next((r for r in history if r["run_id"] == run_id), None)
            if found:
                if found["report_sha256"] != report_sha:
                    raise JournalError("RUN_ID_CONFLICT")
                return {"status": "EXISTING_IDENTICAL_RUN", "receipt": found, "total": len(history)}
            when = self.clock()
            if not isinstance(when, datetime) or when.tzinfo is None:
                raise JournalError("NON_UTC_CLOCK")
            head = {
                "schema": SCHEMA, "sequence": len(history) + 1, "run_id": run_id,
                "experiment_id": result["experiment_id"],
                "report_sha256": report_sha,
                "fixture_sha256": result["fixture_sha256"],
                "event_log_head_sha256": result["event_log_head_sha256"],
                "classification": "SYNTHETIC_ONLY", "promotion_allowed": False,
                "recorded_at_utc": when.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
                "previous_sha256": history[-1]["entry_sha256"] if history else None,
            }
            entry_sha = digest(head)
            record = {**head, "entry_sha256": entry_sha, "hmac_sha256": self._signature(entry_sha)}
            self._check(record, len(history) + 1, head["previous_sha256"])
            payload = canonical(record) + b"\n"
            if len(payload) > ROW_BUDGET or (self.path.exists() and self.path.stat().st_size + len(payload) > FILE_BUDGET):
                raise JournalError("JOURNAL_CAPACITY_EXCEEDED")
            out_fd = os.open(str(self.path), os.O_WRONLY | os.O_APPEND | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
            try:
                with os.fdopen(out_fd, "ab") as out:
                    out.write(payload)
                    out.flush()
                    os.fsync(out.fileno())
            finally:
                pass
            # On-disk journal MUST independently pass the parser after writing.
            current = self._read_unlocked()
            if current[-1] != record:
                raise JournalError("POST_WRITE_REPLAY_MISMATCH")
            return {"status": "RECORDED_SYNTHETIC_ONLY", "receipt": record, "total": len(current)}
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
