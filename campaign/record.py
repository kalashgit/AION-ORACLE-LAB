"""Explicit offline receipt command. Real-market imports are deliberately unsupported."""
import argparse
import json
from pathlib import Path
from .controller import run_cycle
from .journal import ResearchJournal

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True, help="Local synthetic-only JSONL path; prefer private workspace")
    p.add_argument("--run-id", required=True)
    p.add_argument("--allow-unsigned-synthetic", action="store_true", default=False)
    a = p.parse_args()
    j = ResearchJournal(Path(a.ledger), allow_unsigned_synthetic=a.allow_unsigned_synthetic)
    result = j.record(a.run_id, run_cycle())
    print(json.dumps({"status": result["status"], "run_id": result["receipt"]["run_id"],
                      "event_count": result["total"], "classification": "SYNTHETIC_ONLY",
                      "real_trading_return": "NOT_MEASURED", "ledger_head": result["receipt"]["entry_sha256"]},
                     sort_keys=True))

if __name__ == "__main__":
    main()
