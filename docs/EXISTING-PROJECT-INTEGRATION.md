# Existing Genesis × Oracle research integration contract

## Purpose
Keep the EXISTING Genesis and Oracle application as the implementation target. The lab's role is an independent, one-way evidence consumer. This connector intentionally cannot initiate market orders, update model weights, rewrite Genesis memory, or approve a deployment.

## Data flow
Existing application -> **aggregate export** -> local rights review & redaction -> \`FounderMetricSummary/1\` JSON -> \`oracle_lab.evidence_bridge\` -> \`OracleEvidenceIntake/1\` diagnostic receipt -> separate human-reviewed experiment registry.

This is a structural compatibility boundary, **not yet wired into the private application**. Do not move its private code, raw market-data archives, credentials, or private evaluation labels into the public lab.

## Import shape
The bridge accepts one \`FounderMetricSummary/1\` record or a JSON array of at most 50 records (up to 32 KiB), mirroring the documented aggregate export from the existing project. It checks field shape, provider/scope pair, simulated state, chronology, economic return identity and report hash format. The hash is a *claimed pointer*; it is NOT independently authenticated just because its syntax is correct.

For a licensed historical source, a user/human must review source rights outside this adapter. The imported research data is expressly **not automatically authorized for machine-learning training or redistribution**.

## Anti-overclaim policy
Even an apparent +5% net result remains diagnostic until the independent evaluator verifies full source provenance, costs, trade counts, no leakage, unexposed forward evaluation, risk compliance and reproducibility. The bridge does not silently rewrite historical classifications into clean holdouts, turn an aggregate metric into a new training label, or assume Langfuse tracing is active.

## Dry-run
Use Python 3.12 standard library only:

\`\`\`sh
python -m unittest discover -s tests -v
python -m oracle_lab.ingest_summary local-aggregate.json --output local-intake.json
\`\`\`

This branch contains only synthetic test data. No local-aggregate.json has been uploaded.

## Next promotion steps
1. Independently sign source + dataset rights and provenance evidence on a private runner.
2. Validate full trade ledger in the existing project, not from this summary alone.
3. Compare immutable variants under frozen shared costs and a fresh evaluator.
4. Record causal hypotheses and negative results; use an immutable memory evidence log.
5. Introduce a narrow adapter to the existing application in a *separate reviewed production-repo PR* only after its current staged feature branches have a clear authoritative base.
6. Enable optional Langfuse traces with explicit reviewed secrets and redaction. No direct model-to-broker connection.
