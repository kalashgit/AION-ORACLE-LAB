"""Scientifically conservative tests for bounded offline campaign execution."""
from copy import deepcopy
import unittest
from campaign.controller import (
    CampaignError, digest, load_registration, run_cycle,
    verify_event_chain, verify_result,
)
from campaign.evaluator import ReviewFailure, independently_review

class CampaignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_cycle()
        cls.protocol = load_registration()

    def test_registered_small_budget_only(self):
        p = self.protocol
        self.assertEqual(p["trial_cost_multipliers"], [1, 2, 5])
        self.assertEqual(p["max_trials"], 3)
        self.assertFalse(p["promotion_allowed"])
        self.assertFalse(p["training_allowed"])
        self.assertFalse(p["live_trading_allowed"])
        self.assertEqual(self.result["bars"], 864)

    def test_three_trials_and_nontrade_control(self):
        self.assertEqual(len(self.result["trials"]), 3)
        self.assertEqual(self.result["control_no_trade"]["net_return_pct"], 0)
        self.assertTrue(all(t["measurement"]["completed_round_trips"] == 0
                            for t in self.result["trials"]))
        self.assertTrue(all(t["measurement"]["open_holdings"] == 1
                            for t in self.result["trials"]))

    def test_no_model_market_network_or_broker_order(self):
        r = self.result
        self.assertEqual(r["model_calls"], 0)
        self.assertEqual(r["market_data_requests"], 0)
        self.assertEqual(r["broker_orders"], 0)
        self.assertFalse(r["execution_authority"])

    def test_returns_never_claimed_as_live_or_verified(self):
        r = self.result
        self.assertEqual(r["actual_real_market_return"], "NOT_MEASURED")
        self.assertEqual(r["actual_live_return"], "NOT_MEASURED")
        self.assertEqual(r["learning_effectiveness"], "NOT_MEASURED")
        self.assertFalse(r["independent_review"]["can_promote"])
        self.assertFalse(r["memory_proposal"]["memory_write_approved"])
        self.assertFalse(r["memory_proposal"]["model_weights_updated"])

    def test_event_hash_chain_valid(self):
        self.assertEqual(verify_event_chain(self.result["event_log"]),
                         self.result["event_log_head_sha256"])
        self.assertEqual(self.result["event_log"][0]["kind"], "REGISTERED")
        self.assertEqual(len(self.result["event_log"]), 9)

    def test_event_tampering_detected(self):
        bad = deepcopy(self.result["event_log"])
        bad[2]["payload"]["factor"] = 999
        with self.assertRaises(CampaignError):
            verify_event_chain(bad)

    def test_chain_reorder_detected(self):
        bad = deepcopy(self.result["event_log"])
        bad[1], bad[2] = bad[2], bad[1]
        with self.assertRaises(CampaignError):
            verify_event_chain(bad)

    def test_unregistered_policy_rejected(self):
        altered = deepcopy(self.protocol)
        altered["training_allowed"] = True
        with self.assertRaises(CampaignError):
            run_cycle(altered)
        altered = deepcopy(self.protocol)
        altered["trial_cost_multipliers"] = [1, 2, 5, 8]
        with self.assertRaises(CampaignError):
            run_cycle(altered)

    def test_independent_reviewer_rejects_fabricated_return(self):
        trials = deepcopy(self.result["trials"])
        trials[0]["measurement"]["net_return_pct_if_liquidated"] = 5
        with self.assertRaises(ReviewFailure):
            independently_review(self.protocol, trials, self.result["fixture_sha256"])

    def test_independent_reviewer_rejects_cost_change(self):
        trials = deepcopy(self.result["trials"])
        trials[0]["measurement"]["costs"]["fee_bps"] = 0
        with self.assertRaises(ReviewFailure):
            independently_review(self.protocol, trials, self.result["fixture_sha256"])

    def test_results_replay_exactly(self):
        self.assertTrue(verify_result(self.result))
        self.assertEqual(digest(self.result), digest(run_cycle()))

    def test_modified_report_rejected(self):
        mutated = deepcopy(self.result)
        mutated["trials"][0]["measurement"]["net_return_pct_if_liquidated"] = 5
        with self.assertRaises((CampaignError, ReviewFailure)):
            verify_result(mutated)

    def test_all_three_same_data_hash(self):
        h = self.result["fixture_sha256"]
        self.assertTrue(all(x["fixture_sha256"] == h for x in self.result["trials"]))

if __name__ == "__main__":
    unittest.main()
