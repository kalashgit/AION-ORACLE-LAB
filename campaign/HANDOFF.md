# Engineering handoff — last verified state

Campaign created from lab branch `research/research-evidence-bridge-v1`; proposal is stacked on previous draft PRs. All changes to private application remain outside scope.

**First implementation task:** add a bounded, deterministic, offline closed-loop cost-sensitivity experiment with exact input hashes, sequential hash-linked evidence events, independent failure-closed review and no auto-promotion. Include negative tests; execute CI on draft PR; publish only synthetic aggregate artifacts.

**Next after first verified CI:** reconcile the private production PR dependency tree and implement the minimal read-only integration test in the private repo only with explicit authorization; then independently verify rights/holdout custody before any real market A/B/C/D test.

**Known blockers:** original three-day historic date window not frozen in public lab; rights for ML training on existing historical market data unverified; Langfuse runtime credentials/traces not configured; production integration not approved; no forward live validation.

**Completion rule:** the project is NOT COMPLETE until an end-to-end Genesis hypothesis → frozen independent experiment → reviewed evidence memory → existing Oracle terminal explanation is verified, and forward paper/risk controls are separately demonstrated.
