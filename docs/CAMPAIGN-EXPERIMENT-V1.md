# Synthetic campaign experiment — scope and exclusions

This is the **first runnable milestone** in the full program. It is a bounded research loop, NOT a continuously autonomous AI researcher, market strategy optimizer or trading system.

- Registered hypothesis: increased execution costs reduce net simulated passive position value.
- Independent null: costs do not change that value.
- Three trials change exactly one input factor: execution costs at 1×, 2× and 5×, with all positions sized from the same $100 entry budget.
- Shared synthetic fixture: 864 consecutive 5-minute bars using frozen seed 421; prices are entirely fictional.
- Controls: 10%-capped passive holding (open position remains zero completed round trips), no-trade cash (0%).
- Result: separate reviewer recomputes liquidation arithmetic with Decimal, verifies event hashes and forces `can_promote=false`.
- Evidence ledger: deterministic within a single run, hash-linked; artifacts persist for 7 days in GitHub Actions. **Cross-run evidence database and truly persistent memory are NOT yet implemented.**
- Automatic conclusion: future research *proposal* only. No model inference, adaptation, trade entry signals, memory writes or autonomous promotion.
- Production integration and real datasets must pass separate founder and licensing review.

Reproduce (Python 3.12 standard library, no package installs):

    python -m unittest discover -s tests -v
    python -m campaign.run --output artifacts/campaign-synthetic.json
    python -m campaign.verify --input artifacts/campaign-synthetic.json

The GitHub workflow runs on pull requests and can be dispatched manually. A daily **synthetic-only** schedule is declared but GitHub will only execute schedules from the default branch after this change has been reviewed and merged. It does not perform background model improvement or live trading.

## Follow-on authorized milestones
1. Reconcile exact private application baseline and research source dates, without copying private data.
2. Implement append-only *cross-run* evidence storage with restrictive rights and retention.
3. Implement independent market simulator and prospective no-trade/abstention comparison on authorized data only.
4. Add opt-in Langfuse traces, real Genesis hypothesis proposals and reasoned credit memory with explicit approval gates.
5. Integrate verified research summary into the existing Oracle terminal via a separately approved application PR.
