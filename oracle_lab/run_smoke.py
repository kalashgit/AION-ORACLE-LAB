"""Write a reproducible synthetic smoke artifact; not a live-market evaluation."""
import argparse
import json
from pathlib import Path
from .harness import smoke_report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/synthetic-smoke.json")
    args = parser.parse_args()
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    result = smoke_report()
    p.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"])
    print("Fixture SHA256:", result["fixture_sha256"])
    print("Artifact:", p)

if __name__ == "__main__":
    main()
