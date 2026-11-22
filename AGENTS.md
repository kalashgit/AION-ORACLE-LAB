# AION-ORACLE-LAB engineering guidance

This is an **isolated skill-library and research workspace**, not the production Genesis repository.

- Read the relevant `.agents/skills/<skill-name>/SKILL.md` and its references when engineering AION Genesis or Project Oracle.
- Design and evaluate proposed changes with hypotheses, baselines, error analysis, evidence and reproducible results.
- Preserve strict chronological evaluation, no lookahead, explicit transaction costs, independent risk limits and data rights.
- No live trading, credential access, or writes to `kalashgit/AION-GENESYS` from this repository without a separate explicit authorization.
- Distinguish synthetic technical tests from real authorized historical backtests; never invent performance metrics.
- This repository is PUBLIC: do not commit secrets, proprietary project details, customer records, or restricted datasets.
- Do not execute vendored setup scripts or install dependencies without explicit review.

See [SKILLS-INVENTORY.md](SKILLS-INVENTORY.md) for pins, source URLs and licenses.

## Founder mission: AION Genesis × Project Oracle

**Operating objective:** Improve the EXISTING AION Genesis × Oracle system through measurable engineering and independent scientific evaluation. Research whether +5% NET portfolio return is achievable on the original frozen three-day / 864-completed-5m-bar, $1,000 paper study. This is a falsifiable target, **not a guaranteed live return**. Preserve other historical/forward horizons as separate experiments. Never inflate returns by increasing leverage or silently changing risk, costs, data, or time horizon.

**Before a task:** inspect the existing AION-GENESYS PR lineage and interfaces read-only, the lab's current review branches, installed skills, data-rights manifests, past failures and exact tests. Extend existing infrastructure rather than rebuild it. Verify the current implementation source SHA; do not assume the default branch contains all staged application code.

**Required research cycle:** (1) propose hypothesis and null, (2) pre-register one independent change and spending budget, (3) pin code/data provenance/cost model/date split, (4) test on legally permitted inputs, (5) evaluate independently with chronological, untouched evidence, (6) report net profit, drawdown, completed round trips, missed gains, avoided losses, costs, reproducibility and uncertainty, (7) add evidence-backed findings and failure causes to versioned memory, (8) prioritize the next experiment. Failed and inconclusive trials must remain in the ledger.

**Learning is not merely remembering:** benchmark unchanged Genesis against revised reasoning or model/memory versions on fresh unfamiliar cases. Report causal attribution, confidence calibration, regressions and compute cost. Research outputs are provisional until replicated; a language model cannot approve its own evaluation or bypass the deterministic risk engine.

**Economic priorities:** investigate negative expectancy, overtrading, all-in trading costs, opportunity selection and NO_TRADE, volatility/regime changes, execution timing, price-data gaps and risk exposures. Challenge simple rule baselines and cash before claiming an advanced model adds value.

**Available engineering skills:** use `autoresearch`, `eval-driven-dev`, `harness-engineering`, `agent-architecture`, and relevant ML4T validation, memory and risk skills in `.agents/skills/`. Langfuse skills guide design; traces are **not configured** until the actual SDK/credentials and verified trace retrieval are separately implemented.

**Output per bounded milestone:** code branch + draft PR, relevant GitHub Actions run and artifacts, experiment ID/manifest, reproducible commands, metrics versus frozen baseline, failure analysis, actual compute/tool spend, rights status, limitations, rollback and recommended next action. No claims of passing tests, profitability, model learning or deployment without linked evidence.

**Founder approval boundary:** no merging unreviewed code, production modifications, paid infrastructure, restricted ML training, broker credentials, live execution, or publication of private data without explicit authorization. Laboratory integration into AION-GENESYS requires a separate reviewed production-repository change and compatibility checks. Never invent market results, silently reclassify exposed retrospective data as unseen, or auto-promote strategies.

**Work cadence:** make progress only through authorized, bounded executions, such as GitHub Actions runs or a Work session. Do not imply continuous background execution solely because these instructions exist. Each task should end with a useful evidence-based handoff and the next concrete engineering milestone.
