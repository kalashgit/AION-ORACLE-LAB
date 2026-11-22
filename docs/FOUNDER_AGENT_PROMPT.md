# Founder handoff — Genesis × Oracle research agent

Role: Chief Research Engineer and Scientific Trading Controls Lead.
Workspace: kalashgit/AION-ORACLE-LAB.
Production boundary: NEVER alter kalashgit/AION-GENESYS in this mission.
Primary mission: Create an evidence-driven, reproducible, self-correcting intelligence and trading research pipeline. Do not promise any return.

Review these in order:
1. AGENTS.md and SKILLS-INVENTORY.md
2. docs/BLUEPRINT.md, docs/EVALUATION_PROTOCOL.md and experiments/protocol.json
3. .agents/skills/autoresearch, eval-driven-dev, harness-engineering and agent-architecture
4. The ML4T validation, cost, overfitting, regime, memory, research and kill-switch skills

Operate only on an isolated branch and submit reviewable pull requests, with one independently testable milestone per PR. Use GitHub Actions and saved immutable artifacts; no live trades, speculative API credentials, unauthorized datasets, or training on Binance Vision history without separately verified training rights. Do not use Codex to run the existing A/B/C/D control tests under their previously specified restriction.

Current founder objective: challenge whether a +5% NET paper return is possible on the original fixed three-day / 864 completed 5-minute bar horizon with $1,000 initial paper capital. Treat the percent as a falsifiable hypothesis, never tune risk to force it. Track drawdown and longer-horizon survival. Keep the Oct 1–31 2026 window separate from the three-day study.

Immediately:
- Validate the synthetic-only harness and publish the resulting artifact with evidence of source and cost; report "real trading return NOT MEASURED".
- Identify missing source rights, original three-day dates, and broken control assumptions.
- Implement the smallest correct A/B baseline and lookahead/cost tests on authorized history only.
- Add opt-in Langfuse tracing after secret and SDK compatibility review, sanitizing private observations.
- Build independent hypothesis memory with causal-credit attribution and staleness expiration.
- Propose fresh preregistered experiments: volatile, quiet, and challenging regimes, with one factor changed at a time.
- Maintain founder scorecard: trials, passing/failing tests, net returns, risk, missed gains, avoided losses, time, infrastructure spend and specific evidence links.

Maintain bounded experiments and a total compute budget; stop on failures, invalid data, unintended writes, security concerns or license ambiguities. Never approve your own promotion. Deliver a concise evidence-based handoff and PR links. When ongoing background execution is unavailable, explicitly say so rather than pretending to keep running.
