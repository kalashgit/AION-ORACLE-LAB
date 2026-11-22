"""Deterministic synthetic-only spot evaluation; never submits orders."""
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import json
import random

@dataclass(frozen=True)
class Bar:
    timestamp: str
    opening: float
    high: float
    low: float
    close: float
    volume: float

@dataclass(frozen=True)
class Costs:
    fee_bps: float = 10.0
    slippage_bps: float = 5.0
    full_spread_bps: float = 10.0

    def __post_init__(self):
        if min(self.fee_bps, self.slippage_bps, self.full_spread_bps) < 0:
            raise ValueError("Negative costs")

    def fill(self, price, buy):
        adverse_bps = self.slippage_bps + self.full_spread_bps / 2
        return price * (1 + (adverse_bps if buy else -adverse_bps) / 10000)

def synthetic_bars(seed=421, count=864):
    if count < 2:
        raise ValueError("Require two or more bars")
    rand = random.Random(seed)
    start = datetime(2026, 10, 1, tzinfo=timezone.utc)
    price = 60000.0
    bars = []
    for i in range(count):
        regime = min(2, i * 3 // count)
        vol = (0.0008, 0.0035, 0.0015)[regime]
        drift = (0.0001, -0.00015, 0.00008)[regime]
        op = price
        price = max(1, op * (1 + drift + rand.gauss(0, vol)))
        hi = max(op, price) * (1 + abs(rand.gauss(0, vol / 5)))
        lo = min(op, price) * (1 - min(0.5, abs(rand.gauss(0, vol / 5))))
        bars.append(Bar((start + timedelta(minutes=5 * i)).isoformat(),
                        round(op, 8), round(hi, 8), round(lo, 8),
                        round(price, 8), round(1 + rand.random(), 8)))
    return bars

def fixture_hash(bars):
    source = json.dumps([asdict(b) for b in bars], sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(source.encode()).hexdigest()

def passive_hold(bars, position_budget, costs=Costs(), starting_capital=1000.0):
    if len(bars) < 2 or not (0 < position_budget <= starting_capital):
        raise ValueError("Invalid benchmark")
    fee = costs.fee_bps / 10000
    entry = costs.fill(bars[0].opening, True)
    qty = position_budget / (entry * (1 + fee))
    cash = starting_capital - qty * entry * (1 + fee)
    if cash < -1e-8:
        raise AssertionError("No leverage")
    equity = [starting_capital]
    for b in bars:
        liquidation_value = qty * costs.fill(b.close, False) * (1 - fee)
        equity.append(cash + liquidation_value)
    peak = equity[0]
    drawdown = 0.0
    for value in equity:
        peak = max(peak, value)
        drawdown = max(drawdown, 100 * (peak - value) / peak)
    return {
        "initial_usdt": starting_capital,
        "position_budget_usdt": position_budget,
        "entry_mid_notional_usdt": round(qty * bars[0].opening, 8),
        "cash_usdt": round(cash, 8),
        "net_return_pct_if_liquidated": round(100 * (equity[-1] / starting_capital - 1), 8),
        "max_drawdown_pct": round(drawdown, 8),
        "completed_round_trips": 0,
        "open_holdings": 1,
        "costs": asdict(costs)
    }

def smoke_report():
    bars = synthetic_bars()
    return {
        "status": "SYNTHETIC_TECHNICAL_SMOKE_NOT_REAL_MARKET_RETURN",
        "origin": "DETERMINISTIC_SYNTHETIC_GENERATOR",
        "market": "SIMULATED_BTC_USDT_NOT_EXCHANGE_PRICES",
        "bar_minutes": 5,
        "count": len(bars),
        "fixture_sha256": fixture_hash(bars),
        "data_rights": "NO_EXTERNAL_DATA_USED",
        "control_A_capped": passive_hold(bars, 100.0),
        "control_A_full_reference": passive_hold(bars, 1000.0),
        "controls_B_C_D": "NOT_IMPLEMENTED_NOT_MEASURED",
        "real_trading_returns": "NOT_MEASURED",
        "live_orders_enabled": False,
    }
