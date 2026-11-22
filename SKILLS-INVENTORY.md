# Genesis × Oracle — imported agent skills

**12 upstream-pinned skills** copied into `.agents/skills/`. These are instructions and supporting files, not deployed agents, trading models, or validated financial returns. The target repository is currently public.

## Development skills — GitHub awesome-copilot
- `.agents/skills/autoresearch/SKILL.md` — [upstream](https://github.com/github/awesome-copilot/tree/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/skills/autoresearch)
- `.agents/skills/eval-driven-dev/SKILL.md` — [upstream](https://github.com/github/awesome-copilot/tree/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/skills/eval-driven-dev)
- `.agents/skills/harness-engineering/SKILL.md` — [upstream](https://github.com/github/awesome-copilot/tree/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/skills/harness-engineering)
- `.agents/skills/agent-architecture/SKILL.md` — [upstream](https://github.com/github/awesome-copilot/tree/f10fdb8b2660ce85c98f220b2f1ca24653768a5c/skills/agent-architecture)

## Oracle research and trading skills — ML4T
- `.agents/skills/ml4t-walk-forward-cv/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/validation/walk-forward-cv)
- `.agents/skills/ml4t-lookahead-bias/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/concepts/lookahead-bias)
- `.agents/skills/ml4t-transaction-costs/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/concepts/transaction-costs)
- `.agents/skills/ml4t-backtest-overfitting/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/concepts/backtest-overfitting)
- `.agents/skills/ml4t-regime-awareness/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/concepts/regime-awareness)
- `.agents/skills/ml4t-agent-state-memory/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/advanced-ai/agent-state-memory)
- `.agents/skills/ml4t-research-operator/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/advanced-ai/research-operator)
- `.agents/skills/ml4t-kill-switch/SKILL.md` — [upstream](https://github.com/ml4t/skills/tree/691857537a0c8befc11dc2f2ad7a458b7c7e801c/portfolio/kill-switch)

## Provenance, licenses, safety
- Pinned `github/awesome-copilot` commit: `f10fdb8b2660ce85c98f220b2f1ca24653768a5c` (MIT). Includes skill-local MIT license for `agent-architecture`.
- Pinned `ml4t/skills` commit: `691857537a0c8befc11dc2f2ad7a458b7c7e801c` (Apache-2.0). Its NOTICE is preserved.
- Copied all linked references from `eval-driven-dev` and `agent-architecture`, plus their ancillary resources, so skill instructions can resolve their local references.
- The upstream `.agents/skills/eval-driven-dev/resources/setup.sh` installs dependencies, updates packages, and starts a server. **It has not been executed and must not be executed without an explicit review.**
- Other coding agents may need explicit configuration or a different skill discovery directory; this copy does not automatically configure ChatGPT, Langfuse, or MCPmarket.
- Preserve original license and attribution files under `third_party_licenses/`.
- Before experiment use, independently verify every source's license and every dependency; never store secret credentials, private datasets, client information, or production configuration in this public repository.

## Next engineering step
Create an isolated, reproducible synthetic smoke-test and evaluation harness, then audit data licensing and reproducibility before attempting real historical comparisons. Do not make live trades. Production `kalashgit/AION-GENESYS` was not modified.
