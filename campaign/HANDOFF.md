# Genesis × Oracle Full Campaign — Verified Engineering Handoff

**Current engineering state:** FOUNDATION_IN_PROGRESS; the complete system is NOT yet built.
**Verified date:** 2026-11-22 UTC.

## Current campaign change
- Lab draft PR: https://github.com/kalashgit/AION-ORACLE-LAB/pull/10
- Campaign branch: `campaign/full-system-research-v1`
- Latest verified commit: `5e860829feff0871ef76274c22f46a4a18178f24` (the commit that passed CI).
- Tests: **33 passed**, two independent successful GitHub Actions workflows:
  - https://github.com/kalashgit/AION-ORACLE-LAB/actions/runs/45052850286 (bounded campaign, artifact uploaded)
  - https://github.com/kalashgit/AION-ORACLE-LAB/actions/runs/45052850283 (existing synthetic harness)
- Research artifact: `synthetic-campaign-evidence` in run `45052850286` (7-day retention).
- 3 fixed synthetic-only cost-factor trials (1×, 2×, 5×), a no-trade cash reference and a SHA256 hash-linked audit event ledger. The independent Decimal evaluator checks modeled liquidation.
- Independent review always denies trading promotion. **Real-market performance, live return, model learning and Langfuse traces: NOT MEASURED.**

## Existing research PR dependencies
- PR #2: base synthetic benchmark and documentation; draft.
- PR #7: read-only aggregate metric evidence bridge, stacked on #2; draft.
- PR #9: standing founder `AGENTS.md` directive, separate draft against main.
- PR #10: full-campaign roadmap and executable synthetic controller, stacked on #7; draft.

**Do not merge #10 alone into main without reviewing its stacked prerequisite PRs.** No changes have been written to the private AION-GENESYS application.

## Issue queue
- [#11](https://github.com/kalashgit/AION-ORACLE-LAB/issues/11): canonical existing-application branch/PR lineage; the **next integration gate**.
- [#12](https://github.com/kalashgit/AION-ORACLE-LAB/issues/12): genuinely persistent cross-run evidence and causal-credit review.
- [#13](https://github.com/kalashgit/AION-ORACLE-LAB/issues/13): measured Genesis reasoning + optional Langfuse.
- [#14](https://github.com/kalashgit/AION-ORACLE-LAB/issues/14): fair controls and economic opportunity research, data-rights gate.
- [#15](https://github.com/kalashgit/AION-ORACLE-LAB/issues/15): read-only research integration in existing Oracle terminal.
- [#16](https://github.com/kalashgit/AION-ORACLE-LAB/issues/16): independent forward paper and risk readiness.
- [#17](https://github.com/kalashgit/AION-ORACLE-LAB/issues/17): bounded scheduler and founder reporting.

## Exact next action for an authorized Work/engineering session
1. Read this file, `docs/MASTER-CAMPAIGN.md`, `campaign/plan.json`, and the founder directive in lab PR #9.
2. Review draft PR #10 and its CI/negative results. Preserve all prior test history and synthetic status.
3. Proceed to **issue #11**: in the private existing app, read current PR ancestry and test evidence, identify a canonical review branch and prepare a compatibility matrix. Make no production writes or merges without approval.
4. Separately progress **issue #12** in the lab: ensure independently auditable cross-run records while avoiding treating the repeated identical synthetic fixture as additional market evidence.
5. Don't broaden to historical or training data until the legal purpose/rights and untouched evaluation periods are frozen. No live broker code path.

## Resumption / budget policy
- GitHub synthetic schedule is declared but cannot operate as a default-branch schedule until all relevant changes are approved and merged. When active, it is limited to three synthetic trials, zero market requests, zero LLM calls and 10 minutes per run.
- CI cost and runtime: Actions workflow run is evidenced above; actual infrastructure charges not independently measured.
- This is bounded software research, not a continuously resident autonomous engineer. Each authorized agent session or job must leave another evidence-backed handoff.
- If a candidate claims a profitable 5% live strategy, it MUST be challenged with separate independent forward-market evidence before such a claim can be accepted.
