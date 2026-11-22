"""Produce one budgeted, self-contained, synthetic-only campaign artifact."""
import argparse
import json
from pathlib import Path
from .controller import run_cycle, verify_result

def main():
    p = argparse.ArgumentParser(description="Genesis Oracle synthetic research cycle")
    p.add_argument("--output", default="artifacts/campaign-synthetic.json")
    args = p.parse_args()
    result = run_cycle()
    if not verify_result(result):
        raise SystemExit("FAILED: evidence verification")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("CAMPAIGN_CYCLE: VERIFIED_SYNTHETIC_TECHNICAL_ONLY")
    print("REGISTERED_TRIALS:", len(result["trials"]))
    print("EVENT_LOG_HEAD:", result["event_log_head_sha256"])
    print("FINANCIAL_RETURN_LIVE:", result["actual_live_return"])
    print("MODEL_LEARNING:", result["learning_effectiveness"])
    print("OUTPUT:", out)

if __name__ == "__main__":
    main()
