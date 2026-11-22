"""Synthetic-only connector contract tests. Zero network and broker access."""
import json
import unittest
from oracle_lab.evidence_bridge import RejectedEvidence, assess_summary, ingest_json

def fixture():
    return {
        "schema": "FounderMetricSummary/1",
        "run_id": "synthetic-001",
        "candidate_version": "fixed_rule",
        "comparison_run_id": "synthetic-frozen",
        "comparable": True,
        "provider": "SYNTHETIC_LAB",
        "rights_scope": "SYNTHETIC_CONTRACT_ONLY_NOT_PROVIDER_PERMISSION",
        "instrument": "BTCUSD",
        "quote_currency": "USD",
        "period_start_utc": "2026-10-01T00:00:00Z",
        "period_end_utc": "2026-10-04T00:00:00Z",
        "simulated": True,
        "starting_equity": "1000",
        "ending_equity": "1050",
        "net_return_pct": "5",
        "net_return_change_pp": "6",
        "completed_round_trips": 5,
        "trade_count_change": -2,
        "learning_option_A_pp_per_iteration": "6",
        "learning_option_B_fraction": "0.5",
        "efficiency_composite_pct_or_null": None,
        "efficiency_evidence": "NOT_MEASURED",
        "source_report_sha256": "a" * 64,
    }

class BridgeTests(unittest.TestCase):
    def assert_rejected(self, patch):
        v = fixture()
        v.update(patch)
        with self.assertRaises(RejectedEvidence):
            assess_summary(v)

    def test_valid_synthetic_but_five_percent_never_promotes(self):
        out = assess_summary(fixture())
        self.assertEqual(out["status"], "SYNTHETIC_ONLY")
        self.assertFalse(out["decision"]["five_percent_target_proven"])
        self.assertFalse(out["decision"]["automatic_memory_promotion"])
        self.assertFalse(out["decision"]["strategy_promotion"])
        self.assertFalse(out["decision"]["live_trading_authorized"])
        self.assertFalse(out["checks"]["causal_learning_verified"])

    def test_repeated_intake_is_content_identical(self):
        a = assess_summary(fixture())
        b = ingest_json(json.dumps(fixture()))[0]
        self.assertEqual(a, b)
        self.assertRegex(a["intake_sha256"], "^[0-9a-f]{64}$")

    def test_negative_return_is_valid_diagnostic(self):
        obj = fixture()
        obj.update(ending_equity="940", net_return_pct="-6")
        out = assess_summary(obj)
        self.assertEqual(out["metrics"]["net_return_pct"], "-6")

    def test_reject_tampered_return(self):
        self.assert_rejected({"net_return_pct": "10"})

    def test_reject_live_scope_or_unknown_provider(self):
        self.assert_rejected({"simulated": False})
        self.assert_rejected({"provider": "LIVE_ETORO"})
        self.assert_rejected({"rights_scope": "TRAINING_AND_EXECUTION"})

    def test_reject_not_finite_or_strings_as_trades(self):
        self.assert_rejected({"net_return_pct": "NaN"})
        self.assert_rejected({"completed_round_trips": "5"})
        self.assert_rejected({"completed_round_trips": -1})

    def test_reject_broker_keys_and_raw_price_fields(self):
        self.assert_rejected({"api_key": "do-not-import"})
        self.assert_rejected({"raw_bars": []})

    def test_reject_bad_time_and_report_hash(self):
        self.assert_rejected({"period_end_utc": "2026-09-30T00:00:00Z"})
        self.assert_rejected({"source_report_sha256": "not-a-hash"})

    def test_reject_oversized_payload(self):
        with self.assertRaises(RejectedEvidence):
            ingest_json(b"x" * 32769)

    def test_reject_false_comparability(self):
        self.assert_rejected({"comparison_run_id": None})

    def test_diagnostic_rights_only_not_training(self):
        obj = fixture()
        obj.update(provider="BINANCE_VISION",
                   rights_scope="PERSONAL_NONPRODUCTION_BACKTEST_ONLY",
                   instrument="BTCUSDT", quote_currency="USDT")
        out = assess_summary(obj)
        self.assertEqual(out["status"], "RETROSPECTIVE_RESEARCH_ONLY")
        self.assertFalse(out["decision"]["model_training_authorized"])
        self.assertFalse(out["checks"]["data_rights_independently_verified"])

    def test_multiple_rows_and_atomic_rejection(self):
        a = fixture()
        b = fixture()
        b["run_id"] = "synthetic-002"
        self.assertEqual(len(ingest_json(json.dumps([a, b]))), 2)
        b["net_return_pct"] = "999"
        with self.assertRaises(RejectedEvidence):
            ingest_json(json.dumps([a, b]))
