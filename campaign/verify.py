"""Fail closed when a stored research artifact fails exact deterministic replay."""
import argparse
import json
from pathlib import Path
from .controller import verify_result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="artifacts/campaign-synthetic.json")
    args = p.parse_args()
    doc = json.loads(Path(args.input).read_text(encoding="utf-8"))
    verify_result(doc)
    print("ARTIFACT_REPLAY_VERIFIED_SYNTHETIC_ONLY")

if __name__ == "__main__":
    main()
