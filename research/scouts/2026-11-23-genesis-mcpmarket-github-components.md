# Oracle research scout — MCPmarket and GitHub for dual-speed market intelligence
**Survey date:** 2026-11-23. **Status:** discovered and metadata checked, NOT installed, starred, forked, imported, benchmarked or approved for live/training use. This public lab document contains no proprietary code or private data.

## Research question
Which existing tools can strengthen a 1m/5m/1h source-verified market feature engine, small fast-path decision router, cost-constrained paper replay, slow research agent, and iPhone/TV dashboard **without** replacing the current application or changing scientific controls?

Primary rule: A public MCP listing or permissive code license does not authorize data ingestion, AI model training, unattended execution, fund movement or backtest result promotion. Every integration needs a separate source, license, security and exact-sha review.

## A. Ranked GitHub repositories

Repository metadata/declared SPDX and stars below were retrieved directly from GitHub's public repository API on 2026-11-23. Star counts and last-push dates change; license summaries are screening indicators, not legal opinions.

| Rank | GitHub source | GitHub SPDX / stars | Why it helps | Adoption recommendation |
| --- | --- | --- | --- | --- |
| P1 | [nardew/talipp](https://github.com/nardew/talipp) | MIT / 546 | Incremental Python technical indicators; high fit for 1-minute feature updates. Last push 2025-09-09. | **Star; first isolated benchmark/fork candidate** after dependency and numerical audit. |
| P1 | [pola-rs/polars](https://github.com/pola-rs/polars) | MIT / 40,438 | Efficient historic candle aggregation, as-of dataset preparation and reproducible data checks. Pushed 2026-11-22. | **Star; pinned dependency or benchmark reference**, not fork entire dataframe project. |
| P1 | [nkaz001/hftbacktest](https://github.com/nkaz001/hftbacktest) | MIT / 5,127 | Models latency, queue positions and limit-order fills for research with true L2/L3 order-book data. Pushed 2025-12-23. | **Star; future simulator reference**; without authorized L2/L3 input it cannot prove queue fills from OHLC. |
| P1 | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT / 21,340 | Typed bounded System 2 proposal contracts and model tool validation. Pushed 2026-11-22. | **Star; compare** with current Python contracts before adding dependency. |
| P1 | [tradingview/lightweight-charts](https://github.com/tradingview/lightweight-charts) | Apache-2.0 / 17,945 | Optional performant phone/TV chart overlays. Pushed 2026-11-18. | **Star; test an isolated view**; do not replace existing renderer by default. |
| P1 | [ccxt/ccxt](https://github.com/ccxt/ccxt) | MIT / 44,958 | Potential read-only venue public-data adapters and consistency checks. Pushed 2026-11-22. | **Star; restricted read-only adapter study**; does not confer eToro access or data rights. |
| P2 | [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | Apache-2.0 / 22,658 | Independently compare fill, portfolio, risk and cost accounting. | Architectural research; too large/C#-centric to import wholesale. |
| P2 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT / 45,274 | Durable slow research workflow with interrupts and checkpoints. | Evaluate only if existing agent machinery has concrete missing capabilities. |
| P2 | [wickra-lib/wickra](https://github.com/wickra-lib/wickra) | Apache-2.0 / 79 | Rust/WASM/Python/JS streaming indicator possibility. Pushed 2026-11-02. | **Experimental only**, small adoption; source, native binary supply chain and numeric parity audit first. |
| HOLD | [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) | LGPL-3.0 / 31,746 | Event-driven fast/slow trading system architecture reference. | Study, but do not copy into proprietary app without LGPL compliance review. |
| HOLD | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | GPL-3.0 / 57,165 | Independent strategy-control benchmark. | Separate experiments only, no auto-vendoring in private app. |
| HOLD | [kernc/backtesting.py](https://github.com/kernc/backtesting.py) | AGPL-3.0 / 9,281 | Lightweight independent backtester. | Commercial/copyleft implications; reference only. |
| HOLD | [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | NOASSERTION / 9,915 | Fast vectorized model search. | Additional Commons-Clause/commercial license terms need review before any integration. |
| HOLD | [langfuse/langfuse](https://github.com/langfuse/langfuse) | NOASSERTION / 37,728 | Model tracing, experiments, evaluations, prompt versioning. | Prefer official connected SDK/hosted API after project privacy/contract review; do not vendor full platform. |

## B. MCPmarket services worth examining

The source links below are public listings, not server-side authorization, installed status or code audit.

1. **[Backtrader MCP](https://mcpmarket.com/server/backtrader)** — [cloudQuant/backtrader-mcp](https://github.com/cloudQuant/backtrader-mcp), MIT, 1 star (pushed 2026-09-20). Local-first immutable CSV datasets, typed strategy drafts and bounded backtests; listing describes an offline-only mode without broker access. **Best small experimental backtest MCP candidate**, but low adoption means full security and reproducibility audit before invoking it.
2. **[Langfuse MCP](https://mcpmarket.com/server/langfuse-1)** — Trace retrieval, session errors, actual model call evidence and evaluation observability. Consult the [official Langfuse MCP](https://langfuse.com/docs/api-and-data-platform/features/mcp-server); the third-party MCPmarket listing is not necessarily the official server. **Highest-value System 2 research connector** if approved and properly redacted. A Langfuse skill was readable in this session, but a configured trace project was NOT verified.
3. **[Finance Toolkit MCP](https://mcpmarket.com/server/finance-toolkit)** — [JerBouma/FinanceToolkit](https://github.com/JerBouma/FinanceToolkit), MIT, 5,556 stars (pushed 2026-11-22). Published financial ratios and formula methods; useful **independent mathematical reference** but NOT a replacement for cash/fill-backed strategy profit factor or expectancy. Verify definitions and sample-size conventions.
4. **[TraderWAI Charts](https://mcpmarket.com/server/traderwai-charts)** — [leonardo-mazzitelli/traderwai-charts](https://github.com/leonardo-mazzitelli/traderwai-charts), CC-BY-4.0 docs repository, 0 stars. Describes hosted OAuth 2.1 read-only chart/OHLC/backtests. Can aid HUMAN review of ruler patterns, but hosted market-data rights, broker account scopes and fees are unknown. **Do not confuse with WRITE-capable TraderWAI trading MCP server.**
5. **[Repo Radar](https://mcpmarket.com/server/repo-radar)** — [javiermorron/repo-radar-mcp](https://github.com/javiermorron/repo-radar-mcp), MIT, 0 stars. Repo scoring/ranking. Low incremental value when GitHub search/get repository tools are already connected.
6. **[Market Data](https://mcpmarket.com/server/market-data)** — Pluggable FastAPI financial OHLC providers with yfinance default; listing reports 0 stars. Architecture reference only. It does NOT establish reliable BTC 1m venue candles, first-observed provenance, ML training permission or executable bid/ask prices.

The direct MCPmarket catalog connector was NOT available as a tool in this session; these listings were inspected through public webpages. The Langfuse MCPmarket-affiliated skill was accessible, but actual connection to a user's Langfuse project was not proved.

## C. Decision and experiment queue

### Immediate star/bookmark shortlist
- talipp, Polars, hftbacktest, Pydantic AI, Lightweight Charts, CCXT.
- No programmatic GitHub star/fork action was available through the current GitHub toolset; NONE was performed. Star through the upstream repository GitHub UI.

### Pilot 1 — streaming indicators (first fork candidate only after review)
Compare existing simple stdlib incremental features against pinned talipp in a sandbox on **identical 10,000 owned-synthetic 1m events**, predeclared gaps, duplicates, revised tick events and multi-timeframe aggregation. Verify:
- as-of-only 5m/1h, no future or incomplete candle use;
- exact/specified-tolerance indicator parity across increments and batch;
- same source hash, rights and event-time integrity;
- p50/p95/p99 incremental update CPU time and memory;
- import/licensing/transitive dependency audit, deterministic exact-head CI;
- no regression against independently validated paper cash/fee accounting.

A fork creates a **separate GitHub repository**, not a folder inside the existing private app. Use a small pinned dependency, isolated adapter or attribution-compliant import only after the pilot demonstrates measurable improvement.

### Pilot 2 — latency and fill economics
Use hftbacktest ONLY when an authorized historic tick/order-book dataset with L2/L3 depth and reliable timing exists. If only OHLC data is available, use conservative modeled execution and no invented order-queue evidence. Keep model signals and evaluator execution independent.

### Pilot 3 — slow strategist trace and correction
Test a minimal typed PydanticAI or existing plain Python structured contract; optionally instrument genuine LLM calls and evaluation with Langfuse on a redacted dataset after privacy/account authorization. Preserve independent signed research receipts separately from observability logs. Model outputs remain proposals, never source truth or broker order authority.

### Pilot 4 — optional terminal overlay
Add one isolated Lightweight Charts chart panel after existing Canvas/UI baseline benchmark. Preserve TV and iPhone controls, prevent visual chart extrapolations from becoming evaluator/source prices.

## D. Explicit red lines

- Do not fork/copy whole trading bots or use their execution plugins to get around application risk boundaries.
- No new paid infrastructure, GPU, credentials, external telemetry or cloud account sharing without approval.
- No model training on market data solely because the data comes via an MCP.
- No blind install or script execution from MCPmarket listings.
- No promotion of simulated "5%" results from stale prices, screenshot rulers, synthetic data-label leakage or vendor-provided backtest summaries.
- Any GPL/AGPL/LGPL or NOASSERTION upstream project must pass legal/commercial-use review before inclusion in a proprietary application.
- Any new candidate must demonstrate a real end-to-end advantage inside the existing app architecture, not merely its own upstream README benchmark.

## E. References and next action

Repository official GitHub pages above; documented product interfaces above. Verify source commit and lockfile **at implementation time**, not from this discovery note. Design an isolated dependency matrix with baseline and rollback, run exact-SHA CI, record failures and negative trials, and only then propose a narrow import.

Current stage: **RESEARCH SCOUT COMPLETE / CODE INTEGRATION NOT STARTED**.
