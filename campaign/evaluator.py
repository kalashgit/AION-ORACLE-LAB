"""Independent, deterministic synthetic experiment reviewer.

Designed to be a separate import boundary from the experiment proposer.
Even a positive synthetic return is NEVER approved as a strategy or live edge.
"""
from decimal import Decimal

class ReviewFailure(ValueError):
    pass

def independently_review(registration, trials, fixture_sha256):
    factors = registration.get("trial_cost_multipliers")
    if factors != [1, 2, 5] or len(trials) != 3:
        raise ReviewFailure("NOT_PREREGISTERED")
    if registration.get("research_mode") != "SYNTHETIC_ONLY":
        raise ReviewFailure("SOURCE_RIGHTS_NOT_APPROVED")
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
        equity = Decimal(str(m["cash_usdt"])) + (
            Decimal(str(m["final_equity_after_estimated_exit_costs_usdt"]))
            - Decimal(str(m["cash_usdt"]))
        )
        reported = Decimal(str(m["net_return_pct"]))
        reconciled = (equity / Decimal("1000") - 1) * 100
        if abs(reported - reconciled) > Decimal("0.000001"):
            raise ReviewFailure("RETURN_ACCOUNTING_MISMATCH")
        values.append(reported)
    if not (values[0] > values[1] > values[2]):
        raise ReviewFailure("COST_MONOTONICITY_FAILED")
    return {
        "schema": "IndependentCampaignReview/1",
        "verdict": "TECHNICAL_SYNTHETIC_DIAGNOSTIC_ONLY",
        "valid_trial_count": len(trials),
        "registered_cost_factors": list(factors),
        "same_data_and_calendar": True,
        "no_trade_control_net_pct": 0,
        "effect": "Higher modeled execution cost reduces synthetic passive holding liquidation return, with cost-dependent position size.",
        "source_provenance_reverified_independently": False,
        "historical_profitability_established": False,
        "forward_profitability_established": False,
        "causal_model_learning_established": False,
        "can_promote": False,
        "live_trading_approved": False,
        "reason": "Synthetic prices, modeled costs and no completed round-trip trades cannot establish economic edge.",
    }
