"""Bounded offline research controller (synthetic-only, no model or broker tools).

This implements a real, replayable sequence of registered *cost-sensitivity*
trials. It does NOT discover a profitable strategy or train AION Genesis.
"""
from __future__ import annotations

from dataclasses import asdict
from decimal import Decimal
from pathlib import Path
import hashlib
import json

from oracle_lab.harness import Costs, fixture_hash, passive_hold, synthetic_bars
from .evaluator import independently_review

HERE = Path(__file__).resolve().parent
VERSION = "CampaignResearchCycle/1"

class CampaignError(ValueError):
    pass

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")

def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()

def append_event(events, kind, payload):
    if not isinstance(payload, dict) or not isinstance(kind, str):
        raise CampaignError("INVALID_EVENT")
    e = {
        "sequence": len(events),
        "kind": kind,
        "previous_event_sha256": events[-1]["event_sha256"] if events else None,
        "payload": payload,
    }
    e["event_sha256"] = digest(e)
    events.append(e)
    return e

def verify_event_chain(events):
    if not isinstance(events, list) or not events:
        raise CampaignError("EMPTY_EVENT_LOG")
    previous = None
    for i, ev in enumerate(events):
        if not isinstance(ev, dict) or set(ev) != {
            "sequence", "kind", "previous_event_sha256", "payload", "event_sha256"
        }:
            raise CampaignError("INVALID_EVENT_SHAPE")
        if type(ev["sequence"]) is not int or ev["sequence"] != i:
            raise CampaignError("EVENT_SEQUENCE_TAMPERED")
        if ev["previous_event_sha256"] != previous:
            raise CampaignError("EVENT_LINK_TAMPERED")
        raw = {k: v for k, v in ev.items() if k != "event_sha256"}
        if digest(raw) != ev["event_sha256"]:
            raise CampaignError("EVENT_HASH_TAMPERED")
        previous = ev["event_sha256"]
    return previous

def load_registration(path=None):
    f = Path(path) if path is not None else HERE / "registration.json"
    doc = json.loads(f.read_text(encoding="utf-8"))
    if (set(doc) != {
        "schema", "research_mode", "experiment_id", "data", "capital",
        "costs", "trial_cost_multipliers", "hypothesis", "null_hypothesis",
        "promotion_allowed", "training_allowed", "live_trading_allowed",
        "max_trials", "execution_policy"
    } or doc["schema"] != "RegisteredCampaignExperiment/1"):
        raise CampaignError("INVALID_REGISTRATION")
    data = doc["data"]
    if (doc["research_mode"] != "SYNTHETIC_ONLY"
        or set(data) != {"generator", "seed", "bars", "bar_minutes", "source_rights"}
        or data["generator"] != "oracle_lab.harness.synthetic_bars"
        or data["source_rights"] != "NO_EXTERNAL_MARKET_DATA"
        or type(data["seed"]) is not int or data["seed"] != 421
        or type(data["bars"]) is not int or data["bars"] != 864
        or type(data["bar_minutes"]) is not int or data["bar_minutes"] != 5):
        raise CampaignError("DATA_BOUNDARY_MISMATCH")
    cap = doc["capital"]
    if (cap != {"starting_usdt": 1000, "position_budget_usdt": 100,
                "no_leverage": True, "market": "SYNTHETIC_BTC_USDT"}):
        raise CampaignError("CAPITAL_OR_MARKET_CHANGE")
    if doc["costs"] != {"fee_bps_per_side": 10, "slippage_bps_per_side": 5,
                        "full_spread_bps": 10}:
        raise CampaignError("UNREGISTERED_COST_ASSUMPTIONS")
    factors = doc["trial_cost_multipliers"]
    if (factors != [1, 2, 5] or doc["max_trials"] != 3
        or not doc["hypothesis"] or not doc["null_hypothesis"]
        or doc["execution_policy"] != "OFFLINE_NO_ORDERS"
        or any(doc[key] is not False for key in (
            "promotion_allowed", "training_allowed", "live_trading_allowed"
        ))):
        raise CampaignError("UNREGISTERED_VARIATION_OR_AUTHORITY")
    return doc

def run_cycle(registration=None):
    protocol = registration if registration is not None else load_registration()
    # A supplied document is validated using the same immutable protocol rules.
    if registration is not None:
        if protocol != load_registration():
            raise CampaignError("UNREGISTERED_PROTOCOL_MUTATION")
    bars = synthetic_bars(seed=protocol["data"]["seed"], count=protocol["data"]["bars"])
    data_hash = fixture_hash(bars)
    sources = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
               for name in ("controller.py", "evaluator.py")}
    events = []
    append_event(events, "REGISTERED", {
        "experiment_id": protocol["experiment_id"],
        "registration_sha256": digest(protocol),
        "source_files_sha256": sources,
        "fixture_sha256": data_hash,
        "market_data_origin": "GENERATED_SYNTHETIC_ONLY",
    })
    trials = []
    for factor in protocol["trial_cost_multipliers"]:
        trial_id = f"cost_factor_{factor}x"
        append_event(events, "TRIAL_STARTED", {
            "trial_id": trial_id, "varied_factor": "EXECUTION_COST_MULTIPLIER",
            "factor": factor,
        })
        costs = Costs(
            fee_bps=protocol["costs"]["fee_bps_per_side"] * factor,
            slippage_bps=protocol["costs"]["slippage_bps_per_side"] * factor,
            full_spread_bps=protocol["costs"]["full_spread_bps"] * factor,
        )
        observed = passive_hold(
            bars, protocol["capital"]["position_budget_usdt"], costs,
            starting_capital=protocol["capital"]["starting_usdt"]
        )
        trial = {
            "trial_id": trial_id,
            "varied_factor": "EXECUTION_COST_MULTIPLIER",
            "factor": factor,
            "fixture_sha256": data_hash,
            "measurement": observed,
            "real_market_net_return": "NOT_MEASURED",
        }
        trials.append(trial)
        append_event(events, "TRIAL_RECORDED", {
            "trial_id": trial_id, "result_sha256": digest(trial),
            "closed_round_trips": observed["completed_round_trips"],
        })
    review = independently_review(protocol, trials, data_hash)
    append_event(events, "INDEPENDENT_REVIEW", {
        "review_sha256": digest(review), "verdict": review["verdict"],
        "can_promote": review["can_promote"],
    })
    future = {
        "type": "RESEARCH_QUESTION_ONLY",
        "finding": "Test whether cash abstention or reduced turnover helps under comparable after-cost constraints.",
        "confidence": "SYNTHETIC_DIAGNOSTIC_ONLY",
        "memory_write_approved": False,
        "model_weights_updated": False,
        "new_strategy_tested": False,
    }
    append_event(events, "FUTURE_WORK_PROPOSED", future)
    ledger_sha = verify_event_chain(events)
    result = {
        "schema": VERSION,
        "origin": "DETERMINISTIC_SYNTHETIC_ONLY",
        "experiment_id": protocol["experiment_id"],
        "registration_sha256": digest(protocol),
        "source_files_sha256": sources,
        "fixture_sha256": data_hash,
        "bars": len(bars),
        "trials": trials,
        "control_no_trade": {"net_return_pct": 0, "completed_round_trips": 0},
        "independent_review": review,
        "memory_proposal": future,
        "event_log": events,
        "event_log_head_sha256": ledger_sha,
        "actual_real_market_return": "NOT_MEASURED",
        "actual_live_return": "NOT_MEASURED",
        "learning_effectiveness": "NOT_MEASURED",
        "model_calls": 0,
        "market_data_requests": 0,
        "broker_orders": 0,
        "compute_spend": "NOT_MEASURED",
        "execution_authority": False,
    }
    # Verification is performed again before export by the CLI.
    return result

def verify_result(result):
    if not isinstance(result, dict) or result.get("schema") != VERSION:
        raise CampaignError("INVALID_REPORT")
    if result.get("registration_sha256") != digest(load_registration()):
        raise CampaignError("REGISTRATION_NOT_REPRODUCIBLE")
    if len(result.get("trials", [])) != 3 or result.get("broker_orders") != 0:
        raise CampaignError("UNAUTHORIZED_TRIALS_OR_BROKER_ACTIVITY")
    if result.get("actual_real_market_return") != "NOT_MEASURED" or result.get("actual_live_return") != "NOT_MEASURED":
        raise CampaignError("RETURN_PROVENANCE_TAMPERED")
    if result.get("execution_authority") is not False or result["independent_review"]["can_promote"] is not False:
        raise CampaignError("UNAUTHORIZED_PROMOTION")
    if verify_event_chain(result["event_log"]) != result["event_log_head_sha256"]:
        raise CampaignError("EVENT_HEAD_TAMPERED")
    if result["independent_review"] != independently_review(
        load_registration(), result["trials"], result["fixture_sha256"]
    ):
        raise CampaignError("EVALUATION_CHANGED")
    # Strictly reproduce underlying synthetic fixtures + complete report.
    actual = run_cycle()
    if digest(actual) != digest(result):
        raise CampaignError("REPLAY_MISMATCH")
    return True
