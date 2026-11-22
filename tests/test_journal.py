"""Durability and tamper-resistance tests for synthetic-only local custody."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from copy import deepcopy

from campaign.controller import run_cycle
from campaign.journal import JournalError, ResearchJournal

class JournalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_cycle()

    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.p = Path(self.temp.name) / "research" / "evidence.jsonl"
        self.key = b"not-a-production-secret-use-test-material" * 2
        self.j = ResearchJournal(self.p, key=self.key)

    def test_persist_two_runs_across_new_objects(self):
        self.j.record("runner-a", self.report)
        second = ResearchJournal(self.p, key=self.key)
        out = second.record("runner-b", self.report)
        self.assertEqual(out["total"], 2)
        self.assertEqual(len(ResearchJournal(self.p, key=self.key).read()), 2)
        self.assertEqual(out["receipt"]["previous_sha256"], self.j.read()[0]["entry_sha256"])

    def test_idempotent_run_id_does_not_duplicate_results(self):
        first = self.j.record("runner-a", self.report)
        same = self.j.record("runner-a", self.report)
        self.assertEqual(same["status"], "EXISTING_IDENTICAL_RUN")
        self.assertEqual(same["total"], 1)
        self.assertEqual(first["receipt"], same["receipt"])

    def test_no_key_disallowed_except_explicit_synthetic(self):
        with self.assertRaises(JournalError):
            ResearchJournal(self.p)
        local = ResearchJournal(self.p.with_name("unsigned.jsonl"), allow_unsigned_synthetic=True)
        local.record("synthetic-local", self.report)
        self.assertIsNone(local.read()[0]["hmac_sha256"])

    def test_hmac_detects_rewritten_history_even_with_recomputed_hashes(self):
        self.j.record("runner-a", self.report)
        row = json.loads(self.p.read_text())
        row["report_sha256"] = "a" * 64
        from campaign.controller import digest
        row["entry_sha256"] = digest({k:v for k,v in row.items() if k not in ("entry_sha256","hmac_sha256")})
        self.p.write_text(json.dumps(row) + "\n")
        with self.assertRaises(JournalError):
            self.j.read()

    def test_truncation_is_detected(self):
        self.j.record("runner-a", self.report)
        with self.p.open("ab") as f:
            f.write(b'{"sequence": 2')
        with self.assertRaises(JournalError):
            self.j.read()

    def test_mutated_economic_claim_refused_before_write(self):
        r = deepcopy(self.report)
        r["actual_live_return"] = "5%"
        with self.assertRaises(Exception):
            self.j.record("forged", r)
        self.assertFalse(self.p.exists())

    def test_result_always_unpromotable(self):
        row = self.j.record("runner-a", self.report)["receipt"]
        self.assertEqual(row["classification"], "SYNTHETIC_ONLY")
        self.assertIs(row["promotion_allowed"], False)

    def test_invalid_run_id(self):
        with self.assertRaises(JournalError):
            self.j.record("../../outside", self.report)

    def test_wrong_custody_key_cannot_read(self):
        self.j.record("runner-a", self.report)
        other = ResearchJournal(self.p, key=b"different-custody-key-material" * 2)
        with self.assertRaises(JournalError):
            other.read()

    def test_symlink_path_denied(self):
        target = Path(self.temp.name) / "target"
        target.write_text("nothing")
        symlink = Path(self.temp.name) / "linked"
        symlink.symlink_to(target)
        with self.assertRaises(JournalError):
            ResearchJournal(symlink, key=self.key)

if __name__ == "__main__":
    unittest.main()
