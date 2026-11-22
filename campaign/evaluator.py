"""A separate, fail-closed synthetic-only evaluation boundary.

This independently reconciles one-position liquidation arithmetic using Decimal
and the frozen bars. It does NOT independently verify real data provenance, a
strategy edge, model learning, broker fills or a live outcome.
"""
from decimal import Decimal
from oracle_lab.harness import synthetic_bars, fixture_hash

class ReviewFailure(ValueError):
    pass

def independently_review(registration, trials, fixture_sha256):
    factors = registration.get("trial_cost_multipliers")
    if factors != [1, 2, 5] or len(trials) != 3:
        raise ReviewFailure("NOT_PREREGISTERED")
    if registration.get("research_mode") != "SYNTHETIC_ONLY":
        raise ReviewFailure("SOURCE_RIGHTS_NOT_APPROVED")
    bars = synthetic_bars(seed=421, count=864)
    if fixture_hash(bars) != fixture_sha256:
        raise ReviewFailure("REPLAYED_FIXTURE_HASH_MISMATCH")
    D = Decimal
    open_price, last_close = D(str(bars[0].opening)), D(str(bars[-1].close))
    values = []
    for factor, row in zip(factors, trials):
        if (row.get("trial_id") != f"cost_factor_{factor}x"
            or row.get("factor") != factor
            or row.get("varied_factor") != "EXECUTION_COST_MULTIPLIER"
            or row.get("fixture_sha256") != fixture_sha256
            or row.get("real_market_net_return") != "NOT_MEASURED"):
            raise ReviewFailure("TRIAL_IDENTITY_MISMATCH")
        m = row.get("measurement", {})
        if (m.get("initial_usdt") != 1000 or m.get("position_budget_usdt") != 100
            or m.get("completed_round_trips") != 0 or m.get("open_holdings") != 1
            or m.get("entry_mid_notional_usdt", 10000) > 100):
            raise ReviewFailure("TRADING_ACCOUNTING_VIOLATION")
        if m.get("costs") != {
            "fee_bps": 10 * factor, "slippage_bps": 5 * factor,
            "full_spread_bps": 10 * factor
        }:
            raise ReviewFailure("OTHER_VARIABLE_CHANGED")
        fee = D(10 * factor) / 10000
        adverse = D(10 * factor) / 10000  # 5 bps slippage + 5 bps half spread, each * factor
        entry_fill = open_price * (1 + adverse)
        quantity = D(100) / (entry_fill * (1 + fee))
        cash = D(1000) - quantity * entry_fill * (1 + fee)
        liquidation_value = quantity * last_close * (1 - adverse) * (1 - fee)
        recomputed_return = (cash + liquidation_value) / D(1000) * 100 - 100
        try:
            reported = D(str(m["net_return_pct_if_liquidated"]))
            reported_cash = D(str(m["cash_usdt"]))
        except (KeyError, TypeError, ValueError, ArithmeticError):
            raise ReviewFailure("MALFORMED_RETURN")
        if (not reported.is_finite() or not reported_cash.is_finite()
            or abs(recomputed_return - reported) > D("0.000001")
            or abs(cash - reported_cash) > D("0.000001")):
            raise ReviewFailure("INDEPENDENT_LIQUIDATION_RECONCILIATION_FAILED")
        values.append(reported)
    if not (values[0] > values[1] > values[2]):
        raise ReviewFailure("COST_MONOTONICITY_FAILED")
    return {
        "schema": "IndependentCampaignReview/1",
        "verdict": "TECHNICAL_SYNTHETIC_DIAGNOSTIC_ONLY",
        "valid_trial_count": len(trials),
        "registered_cost_factors": list(factors),
        "same_data_and_calendar": True,
        "decimal_cash_and_liquidation_reconciled": True,
        "no_trade_control_net_pct": 0,
        "effect": "Increasing modeled execution cost reduces simulated passive liquidation return; traded quantity changes with cost.",
        "source_provenance_reverified_independently": False,
        "historical_profitability_established": False,
        "forward_profitability_established": False,
        "causal_model_learning_established": False,
        "can_promote": False,
        "live_trading_approved": False,
        "reason": "Synthetic prices, assumed costs and no completed round trips cannot establish an economic trading edge.",
    }
