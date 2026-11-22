# ML4T dependency closure (upstream pinned)

Four companion **instruction skills** added alongside the 12 originally imported skills, all from the same pinned ML4T commit `691857537a0c8befc11dc2f2ad7a458b7c7e801c`.

- `ml4t-purging-embargo`: https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/validation/purging-embargo
- `ml4t-agent-tool-contracts`: https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/advanced-ai/agent-tool-contracts
- `ml4t-registry-system`: https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/infrastructure/registry-system
- `ml4t-risk-metrics`: https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/portfolio/risk-metrics

Run `python scripts/check_skill_dependencies.py` to verify all declared ML4T skill dependencies resolve to installed `.agents/skills/<name>/SKILL.md` files. This is a text-level skill discovery audit, **not a runtime dependency installation, AI intelligence upgrade, or verification of external data rights**. The original MIT/Apache and NOTICE files remain under `third_party_licenses`.

The imported upstream `eval-driven-dev` skill mentions an updater script. **Do not run it automatically**; upgrades/dependencies need explicit review and a reproducible pinned version. No third-party scripts were executed for this skill import.
