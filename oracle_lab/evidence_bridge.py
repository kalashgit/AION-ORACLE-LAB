"""Strict, one-way, dependency-free import of aggregate Genesis research metrics.

No raw market data, model training, private strategy code, credentials or broker routes.
Source summaries are assertions, NOT independently verified market results.
"""
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import re

SCHEMA = "FounderMetricSummary/1"
OUTPUT_SCHEMA = "OracleEvidenceIntake/1"
MAX_ROWS = 50
MAX_INPUT_BYTES = 32_768
HEX_SHA = re.compile(r"^[a-f0-9]{64}$")
KEYS = frozenset((
    "schema", "run_id", "candidate_version", "comparison_run_id", "comparable",
    "provider", "rights_scope", "instrument", "quote_currency",
    "period_start_utc", "period_end_utc", "simulated", "starting_equity",
    "ending_equity", "net_return_pct", "net_return_change_pp",
    "completed_round_trips", "trade_count_change",
    "learning_option_A_pp_per_iteration", "learning_option_B_fraction",
    "efficiency_composite_pct_or_null", "efficiency_evidence",
    "source_report_sha256",
))
RIGHTS = {
    ("SYNTHETIC_LAB", "SYNTHETIC_CONTRACT_ONLY_NOT_PROVIDER_PERMISSION"),
    ("BINANCE_VISION", "PERSONAL_NONPRODUCTION_BACKTEST_ONLY"),
}

class RejectedEvidence(ValueError):
    """Fail closed when an aggregate metric cannot be safely imported."""

def _decimal(v, name, nullable=False):
    if nullable and v is None:
        return None
    if not isinstance(v, str) or not re.fullmatch(r"-?(?:0|[1-9]\d*)(?:\.\d{1,15})?", v):
        raise RejectedEvidence(f"INVALID_DECIMAL_{name}")
    try:
        n = Decimal(v)
    except InvalidOperation as exc:
        raise RejectedEvidence(f"INVALID_DECIMAL_{name}") from exc
    if not n.is_finite():
        raise RejectedEvidence(f"NONFINITE_{name}")
    return n

def _utc(s, name):
    if not isinstance(s, str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", s):
        raise RejectedEvidence(f"INVALID_UTC_{name}")
    try:
        stamp = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError as exc:
        raise RejectedEvidence(f"INVALID_UTC_{name}") from exc
    if stamp.tzinfo != timezone.utc:
        raise RejectedEvidence(f"INVALID_UTC_{name}")
    return stamp

def _text(v, name):
    if not isinstance(v, str) or not v.strip() or len(v) > 180:
        raise RejectedEvidence(f"INVALID_TEXT_{name}")
    if "\n" in v or "\r" in v or "\x00" in v:
        raise RejectedEvidence(f"INVALID_TEXT_{name}")
    return v

def assess_summary(row):
    if not isinstance(row, dict) or set(row) != KEYS or row["schema"] != SCHEMA:
        raise RejectedEvidence("SCHEMA_OR_FIELD_MISMATCH")
    if row["simulated"] is not True or type(row["comparable"]) is not bool:
        raise RejectedEvidence("NOT_SIMULATED_OR_UNDECLARED_COMPARABILITY")
    for name in ("run_id", "candidate_version", "provider", "rights_scope",
                 "instrument", "quote_currency", "efficiency_evidence"):
        _text(row[name], name)
    if row["comparison_run_id"] is not None:
        _text(row["comparison_run_id"], "comparison_run_id")
    if (row["provider"], row["rights_scope"]) not in RIGHTS:
        raise RejectedEvidence("UNAPPROVED_RIGHTS_SCOPE_OR_PROVIDER_PAIR")
    if row["provider"] == "BINANCE_VISION" and (row["instrument"] != "BTCUSDT" or row["quote_currency"] != "USDT"):
        raise RejectedEvidence("UNEXPECTED_BINANCE_INSTRUMENT")
    if row["comparable"] and not row["comparison_run_id"]:
        raise RejectedEvidence("COMPARABLE_WITHOUT_COMPARISON_ID")
    start, end = _utc(row["period_start_utc"], "start"), _utc(row["period_end_utc"], "end")
    if end <= start:
        raise RejectedEvidence("NONPOSITIVE_WINDOW")
    start_equity = _decimal(row["starting_equity"], "starting_equity")
    end_equity = _decimal(row["ending_equity"], "ending_equity")
    reported = _decimal(row["net_return_pct"], "net_return_pct")
    if start_equity <= 0 or end_equity < 0:
        raise RejectedEvidence("INVALID_EQUITY")
    calculated = (end_equity / start_equity - Decimal("1")) * Decimal("100")
    if abs(calculated - reported) > Decimal("0.000001"):
        raise RejectedEvidence("RETURN_DOES_NOT_RECONCILE")
    for name in ("net_return_change_pp", "learning_option_A_pp_per_iteration",
                 "learning_option_B_fraction", "efficiency_composite_pct_or_null"):
        _decimal(row[name], name, nullable=True)
    for name in ("completed_round_trips", "trade_count_change"):
        if row[name] is not None and (type(row[name]) is not int or abs(row[name]) > 100_000):
            raise RejectedEvidence(f"INVALID_INTEGER_{name}")
    if row["completed_round_trips"] is None or row["completed_round_trips"] < 0:
        raise RejectedEvidence("INVALID_ROUND_TRIPS")
    if not isinstance(row["source_report_sha256"], str) or not HEX_SHA.fullmatch(row["source_report_sha256"]):
        raise RejectedEvidence("INVALID_SOURCE_HASH")

    # Reconciliation/shape checks are not independent evidence of data rights,
    # source authenticity, lookahead freedom, successful learning or good trades.
    status = "RETROSPECTIVE_RESEARCH_ONLY" if row["provider"] != "SYNTHETIC_LAB" else "SYNTHETIC_ONLY"
    envelope = {
        "schema": OUTPUT_SCHEMA,
        "status": status,
        "source_schema": SCHEMA,
        "run_id": row["run_id"],
        "candidate_version": row["candidate_version"],
        "comparison_run_id": row["comparison_run_id"],
        "reported_source_sha256": row["source_report_sha256"],
        "source": {
            "provider": row["provider"],
            "rights_scope_claim": row["rights_scope"],
            "instrument": row["instrument"],
            "quote_currency": row["quote_currency"],
            "period_start_utc": row["period_start_utc"],
            "period_end_utc": row["period_end_utc"],
        },
        "metrics": {
            "net_return_pct": row["net_return_pct"],
            "completed_round_trips_reported": row["completed_round_trips"],
            "net_return_change_pp": row["net_return_change_pp"],
            "learning_option_A_pp_per_iteration": row["learning_option_A_pp_per_iteration"],
            "learning_option_B_fraction": row["learning_option_B_fraction"],
        },
        "checks": {
            "schema_and_economic_identity_validated": True,
            "independent_source_hash_verified": False,
            "data_rights_independently_verified": False,
            "independent_forward_validation": False,
            "lookahead_free_verified": False,
            "replay_reproducibility_verified": False,
            "causal_learning_verified": False,
        },
        "decision": {
            "research_review_candidate": True,
            "automatic_memory_promotion": False,
            "strategy_promotion": False,
            "model_training_authorized": False,
            "live_trading_authorized": False,
            "five_percent_target_proven": False,
            "next_gate": "INDEPENDENT_DATA_RIGHTS_AND_REPLAY_REVIEW",
        },
    }
    envelope["intake_sha256"] = hashlib.sha256(
        json.dumps(envelope, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return envelope

def ingest_json(raw):
    if not isinstance(raw, (bytes, str)):
        raise RejectedEvidence("INVALID_INPUT_TYPE")
    payload = raw.encode("utf-8") if isinstance(raw, str) else raw
    if len(payload) > MAX_INPUT_BYTES:
        raise RejectedEvidence("INPUT_TOO_LARGE")
    try:
        doc = json.loads(payload)
    except (ValueError, UnicodeDecodeError) as exc:
        raise RejectedEvidence("INVALID_JSON") from exc
    rows = doc if isinstance(doc, list) else [doc]
    if not 1 <= len(rows) <= MAX_ROWS:
        raise RejectedEvidence("ROW_BUDGET_EXCEEDED")
    return [assess_summary(row) for row in rows]
