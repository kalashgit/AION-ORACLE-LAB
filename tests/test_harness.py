"""Invariants for a synthetic-only evaluation pipeline."""
import unittest
from datetime import datetime
from oracle_lab.harness import Costs, fixture_hash, passive_hold, smoke_report, synthetic_bars

class TestSyntheticHarness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bars = synthetic_bars()

    def test_replay(self):
        self.assertEqual(fixture_hash(self.bars), fixture_hash(synthetic_bars()))
        self.assertNotEqual(fixture_hash(self.bars), fixture_hash(synthetic_bars(seed=422)))

    def test_864_five_minute_bars(self):
        self.assertEqual(len(self.bars), 864)
        seconds = (datetime.fromisoformat(self.bars[-1].timestamp) -
                   datetime.fromisoformat(self.bars[0].timestamp)).total_seconds()
        self.assertEqual(seconds, 863 * 300)

    def test_ohlcv_consistency(self):
        for b in self.bars:
            self.assertGreater(b.low, 0)
            self.assertLessEqual(b.low, min(b.opening, b.close))
            self.assertGreaterEqual(b.high, max(b.opening, b.close))
            self.assertGreater(b.volume, 0)

    def test_no_leverage_or_fake_completed_trades(self):
        capped = passive_hold(self.bars, 100)
        full = passive_hold(self.bars, 1000)
        self.assertLessEqual(capped["entry_mid_notional_usdt"], 100)
        self.assertGreaterEqual(capped["cash_usdt"], 899.9)
        self.assertEqual(capped["completed_round_trips"], 0)
        self.assertEqual(full["completed_round_trips"], 0)
        self.assertGreater(full["entry_mid_notional_usdt"], capped["entry_mid_notional_usdt"])

    def test_costs_degrade_return(self):
        no_cost = passive_hold(self.bars, 100, Costs(0, 0, 0))
        fee_cost = passive_hold(self.bars, 100)
        self.assertGreater(no_cost["net_return_pct_if_liquidated"],
                           fee_cost["net_return_pct_if_liquidated"])

    def test_never_claim_real_return(self):
        result = smoke_report()
        self.assertIn("NOT_REAL_MARKET_RETURN", result["status"])
        self.assertEqual(result["real_trading_returns"], "NOT_MEASURED")
        self.assertFalse(result["live_orders_enabled"])

    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):
            Costs(-1, 0, 0)
