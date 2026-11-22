# AION-ORACLE-LAB

Isolated scientific engineering lab for **AION Genesis × Project Oracle**.

**Not a live trading system. No verified real returns yet.**

- [Architecture and roadmap](docs/BLUEPRINT.md)
- [Closed-loop evaluation and promotion protocol](docs/EVALUATION_PROTOCOL.md)
- [Agent mission and operating instructions](docs/FOUNDER_AGENT_PROMPT.md)
- [Langfuse integration plan](docs/LANGFUSE_INTEGRATION.md)
- [Experiment manifest](experiments/protocol.json)
- [Skills inventory](SKILLS-INVENTORY.md)

## Current reproducible smoke test
Requires Python 3.12. No packages, API keys or market data downloads are required.

    python -m unittest discover -s tests -v
    python -m oracle_lab.run_smoke --output artifacts/synthetic-smoke.json

The generated 864 five-minute bars are fictional. The passive 10%-capped and 100%-invested comparisons include fee, slippage and full spread assumptions. They are NOT indicators of profitability. A still-open holding counts as zero completed entry-exit round trips.

GitHub Actions workflow on PR/manual invocation: .github/workflows/synthetic-harness.yml. Results are artifacts, not live-trading signals.
