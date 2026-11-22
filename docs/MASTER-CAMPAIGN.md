# AION Genesis × Project Oracle — Full Engineering Campaign

**Campaign ID:** AO-FULL-2026-11 · **Status:** ACTIVE ENGINEERING / INCOMPLETE · **Scope:** existing application + isolated public research lab.

## Mission and boundaries
Build a complete integrated research-and-decision-support system, not a second trading terminal. The existing private application remains the implementation destination; this **public** repository holds generic evaluation infrastructure, reproducible synthetic tests, skills and non-confidential planning artifacts. Do not copy private source, historical licensed raw datasets, credentials or trade-level personal journals into this repository.

**Financial research question:** Can a fixed `$1,000` no-leverage BTC/USDT spot paper portfolio meet **+5.00% NET** over the originally specified 864 fully completed 5-minute bars, after costs and within preregistered risk controls? The original real-data dates are not yet frozen here. Another proposed 30-day horizon is a **separate study**, not interchangeable. This is not a claim of an attainable or guaranteed live return.

## Operating architecture
```
Founder authority / budget / scope
          |
Existing Genesis: observation -> hypothesis -> prior evidence -> proposal
          | (one-way, non-executing)
Research Registry: preregistration -> immutable protocol/data/code hashes
          |
Experiment Controller -> fixed comparators -> environment shocks
          |
Independent Evaluator -> negative/failure/cost audit -> evidence receipt
          |
Evidence Memory (proposed until reviewed) -> champion/challenger review
          | (no automatic promotion)
Existing Oracle: research/dashboard -> forward-only paper -> risk review
          |
Separately approved deployment / live boundary; DENIED by default
```

## Eight complete workstreams and acceptance conditions

| ID | Workstream | What is actually required to mark COMPLETE |
|---|---|---|
| A | Integration | Canonical private-app code lineage, compatibility matrix, reproducible build, reviewable integration PRs, end-to-end source-to-terminal trace |
| B | Genesis intelligence | Measured agent planning, calibrated uncertainty, causal evidence memory and opt-in model improvement vs frozen model on unfamiliar cases |
| C | Scientific experiment factory | Frozen source+data+protocol, immutable trial ledger, independent evaluator, adversarial tests, full replay and reproducibility |
| D | Trading research | A/B/C/D comparable controls only where authorized, no-trade baseline, costs, walk-forward and fresh evidence, negative trials published as aggregates |
| E | Improvement loop | Hypothesis → registry → experiment → independent verification → reviewer-approved memory update → next hypothesis with champion/challenger gate |
| F | Oracle terminal | Existing UI integrates verified experiment status, market provenance, strategy evidence, paper ledger and iPhone/TV acceptance tests |
| G | Observability/operations | Langfuse traces with redaction, bounded scheduled workflows, budgets, incidents, robust status/reporting and restartable handoffs |
| H | Forward readiness | Paper-only forward collection, outage and slip tests, risk kill switches, rollback, broker demo only with explicit approval; live trading separately authorized |

## Dependency graph (do not skip)
A0 authority / branch/revision mapping -> C0 deterministic synthetic validation -> C1 immutable research ledger -> E0 bounded controller -> G0 scheduled CI -> D0 rights review -> D1 historical same-window benchmarks -> B0 trace/causal memory -> E1 independent champion/challenger -> F0 terminal integration -> H0 forward paper validation -> H1 independent live-readiness assessment. Workstreams B/F may proceed in parallel as isolated testable tasks; neither changes the deterministic execution hot path.

## Delivery stages
**P0: consolidate foundations:** protect existing PR lineage; verify CI and aggregate-only evidence contracts; introduce campaign tracker and bounded synthetic loop; maintain explicit protocol hashes.
**P1: build laboratory quality:** standalone immutable ledgers, chronological replay, environment stress, lost opportunity/gain avoided analyses, data-rights review, model eval datasets.
**P2: build intelligence:** agent reasoning/credit memory, offline model experiments on authorized data, Langfuse traces with redaction, calibrated disagreement and true outcome measures.
**P3: system integration:** merge only reviewed work after all dependent checks; integrate research status into existing terminal; forward paper and user-device checks.
**P4: demonstrate operational quality:** independent forward validation across conditions, incident monitoring, rollback and budget caps, external security/compliance review, strictly human-controlled promotions.

## Founder scoreboard contract
At each milestone report: commit/pr/CI links, tests and replay identity; initial and final capital; actual net return %, completed entry-exit round trips (open positions separate); max drawdown; fees/slippage/spread; baseline and delta pp; loss reduction and model calibration where measured; attempts/compute cost; blocked rights; next priority. Missing results are **NOT MEASURED**, never 0 or estimated. Maintain a separate scientific completion status (implemented / tested / independently verified / integrated / forward evidence).

## Data rights / confidentiality / approvals
- The existing app's Binance Vision historical workflow is classified personal non-production *backtesting*, NOT blanket permission for ML model training, public price redistribution or live signals.
- Do not fetch restricted market archives into public CI or transfer private source/metrics without provenance/redaction/review.
- Current licensed historical controls C/D must remain NOT MEASURED until separately training-authorized datasets exist.
- Never infer stable live returns from synthetic runs, exposed retrospective datasets or repeated identical replays.
- **Human approvals required** for any merge, money expenditure, production modification, broker credential use, live execution, or policy activation. The agent cannot self-certify its own economic results.

## Honest current state
Lab skills are on `main`. Research harness (PR #2), evidence bridge (PR #7), and founder directive (PR #9) are staged for review. This campaign branch builds on #7 and does **not** change the private app. The workflow in this PR is synthetic-only and will not be continuously scheduled on the default branch until reviewed and merged; GitHub Actions schedule is not an always-running model agent. Real forward performance and full integration remain NOT DEMONSTRATED.

## First source and test references
- Existing main project: https://github.com/kalashgit/AION-GENESYS (private; access limited)
- Lab: https://github.com/kalashgit/AION-ORACLE-LAB
- Research harness: https://github.com/kalashgit/AION-ORACLE-LAB/pull/2
- Aggregate bridge: https://github.com/kalashgit/AION-ORACLE-LAB/pull/7
- Founder rules: https://github.com/kalashgit/AION-ORACLE-LAB/pull/9

## Task handoff protocol
Each issue supplies owner role, scope, explicit acceptance tests, dependencies and a STOP condition. Coding agent starts by reading `AGENTS.md`, this roadmap, `campaign/plan.json` and the source PRs, writes an isolated branch, retains failed logs, opens a **draft** PR, then ends the run with reproducible evidence and the exact next task. If Work session ends, an authorized next session uses GitHub—not a fabricated background commitment.
