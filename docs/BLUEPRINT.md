# AION GENESIS × PROJECT ORACLE — RESEARCH SYSTEM BLUEPRINT
Status: proposed architecture, not deployed performance evidence.

## Mission
Build a founder-governed research and decision infrastructure capable of discovering, testing, falsifying, remembering, and deploying useful market hypotheses. Oracle is the terminal and paper/live execution boundary; Genesis is the reasoning and research engine. Their evaluations must remain independently auditable.

## Hard truth about the goal
The founder's +5% NET goal on the fixed three-day / 864 completed 5-minute-bar paper horizon is a research hypothesis, not a guaranteed outcome or entitlement to live returns. Also measure monthly and longer-horizon performance, loss severity, recovery time, exposure, turnover and stability. Never infer repeated success from one successful historical window.

## Distinct system services
1. **Mission controller**: schedules bounded research jobs; records objective, owner, compute and tool budget.
2. **Knowledge/memory layer**: immutable observations and experiment results; versioned summaries, causal hypotheses, confidence, provenance and staleness flags. Avoid self-certifying memories.
3. **Research planner**: hypothesis and counterhypothesis, expected failure modes, measurable predictions and preregistered test criteria.
4. **Data rights and feature gateway**: licensed source manifest; time-available observations only; hash and freeze permitted datasets.
5. **Market simulator**: spot-only accounting, explicit spread/slippage/fees, order timing, incomplete orders, illiquidity, outages and cash conservation.
6. **Benchmark control lab**: passive 10%-capped and separate 100%-exposure reference, Freqtrade EMA/RSI, FreqAI LightGBM, FinRL PPO. Only run ML training on training-authorized datasets.
7. **Adversarial evaluator**: independent chronological holdouts, lookahead detection, placebo tests, bootstrap/confidence intervals, multiple-testing discipline, and single-variable environment challenges.
8. **Observability service**: Langfuse-compatible traces of hypothesis, tool use, decision, evidence, errors and costs; redact sensitive data.
9. **Risk governor**: separate deterministic exposure checks, stop/kill switch, alerts, operator review, no leverage in the approved research protocol.
10. **Oracle terminal**: multi-timeframe charting, research cards, benchmark scorecards, consented paper execution, confidence and provenance displays.
11. **Promotion service**: signed release manifest, reproducible evaluation, model version, risk review, rollback, and human approval before changing production.
12. **Founder dashboard**: money/attention spent, returns and drawdowns by regime, verified completed trials, blocked hypotheses, recovered opportunities, failures and progress.

## The closed loop
Propose -> preregister -> freeze code/data/assumptions -> test -> independent review -> measure costs, drawdown, missed gains and avoided losses -> create an outcome/credit record -> update hypothesis and evidence memory -> propose next change -> promote only if blind validations improve.
Use bounded jobs and explicit stop conditions; automated learning must not change a live execution policy directly.

## Scientific controls
- Never silently change markets, dates, data permissions, capital, maximum position or costs between controls.
- Synthetic technical verification is not historical performance.
- A strategy optimized against a repeatedly consulted holdout is no longer out-of-sample; rotate to fresh held-out periods and separately record selection bias.
- Register every attempted variant and failed evaluation, along with compute usage and time.
- Challenge volatility, regime duration, liquidity/slippage and shock timing separately; change one environment factor per comparison round and record both gains missed and losses avoided.
- Rank by expected risk-adjusted economic value and evidence robustness, not solely by highest observed return.
- No live orders or broker authorization without a separate explicit founder authorization, independent risk certification and rollback process.

## Six-stage engineering roadmap
**Stage 0 — integrity:** pinned skills, reproducible synthetic harness, protected production repo, explicit accounting and evidence schema.
**Stage 1 — comparable historical controls:** authorized dataset/usage rights; fixed Oct 1–31, 2026 BTC/USDT 5-minute window for A/B/C/D when legal; distinct fixed 3-day horizon.
**Stage 2 — intelligence assessment:** Genesis memory, reasoning, calibration, causal credit, novel-scenario, recovery, compute cost and regression tests; Langfuse trace integration.
**Stage 3 — research autonomy:** hypothesis search, correction, champion/challenger, pre-registration and immutable audit history with human-readable review.
**Stage 4 — paper operations:** forward-only paper trading, slippage checks, terminal dashboard, broker-demo compatibility, incidents and kill switches.
**Stage 5 — conditional limited live:** ONLY after demonstrated evidence across sufficiently long independent regimes, regulatory/broker checks and an explicit new founder decision. No guaranteed performance.

## Current status (2026-11-22)
The repo already contains 12 skills. This branch adds only a synthetic harness and research documentation. We have NOT trained Genesis or FreqAI/PPO, connected Langfuse credentials, certified any real-market returns, or authorized live orders.
