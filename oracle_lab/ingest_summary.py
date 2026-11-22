"""No-network aggregate evidence intake for research-only Genesis result files."""
import argparse
import json
from pathlib import Path
from .evidence_bridge import ingest_json

def main():
    p = argparse.ArgumentParser(description="Fail-closed intake of aggregate research metrics.")
    p.add_argument("input", help="Local aggregate JSON only; never raw price data")
    p.add_argument("--output", default="artifacts/research-intake.json")
    a = p.parse_args()
    data = ingest_json(Path(a.input).read_bytes())
    dest = Path(a.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Research-only receipts:", len(data))
    print("Real return, learning and trading certification: NOT ESTABLISHED")

if __name__ == "__main__":
    main()
