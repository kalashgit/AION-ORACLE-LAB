"""Fail CI on missing declared local ML4T skill dependencies. Pure stdlib."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / ".agents" / "skills"
DEPENDENCY = re.compile(r"(?m)^dependencies:\s*\[([^\]]*)\]\s*$")
NAME = re.compile(r"(?m)^name:\s*([a-zA-Z0-9_-]+)\s*$")

def validate(root: Path = ROOT):
    issues = []
    docs = list(root.glob("*/SKILL.md"))
    names = {}
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        header = text.split("---", 2)[1] if text.startswith("---") else ""
        m = NAME.search(header)
        if not m:
            issues.append(f"{doc.parent.name}: missing skill name")
            continue
        if m.group(1) != doc.parent.name:
            issues.append(f"{doc.parent.name}: frontmatter name differs ({m.group(1)})")
        names[m.group(1)] = doc
    for name, doc in names.items():
        header = doc.read_text(encoding="utf-8").split("---", 2)[1]
        m = DEPENDENCY.search(header)
        if m:
            for dep in [s.strip().strip("'\"") for s in m.group(1).split(",") if s.strip()]:
                normalized = dep if dep.startswith("ml4t-") else f"ml4t-{dep}"
                if normalized not in names:
                    issues.append(f"{name}: missing companion {normalized}")
    return issues, len(names)

if __name__ == "__main__":
    errors, count = validate()
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    print(f"Skill dependency scan: {count} installed skills, {len(errors)} missing or mismatched")
    sys.exit(bool(errors))
