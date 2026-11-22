# Langfuse integration — not configured yet

Langfuse MCPmarket skill != Langfuse runtime trace collection. The runtime must explicitly emit observations. The current Langfuse Python SDK is on its v5 line (Nov 2026); verify compatibility with the actual Langfuse Cloud or self-hosted version before pinning a dependency. Official docs: https://langfuse.com/docs/observability/get-started

Do not put API keys in Git, plain logs, experiment artifacts or in ChatGPT prompts. Store LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY in a protected repo or deployment secret store. Set LANGFUSE_BASE_URL if appropriate.

First opt-in spans: experiment_start, hypothesis, decision, tool_call, retrieved_evidence, cost_model, evaluation, independent_review, memory_credit_update, and promotion_gate. Link trace IDs to manifest hashes; redact prompts, account IDs, order credentials and customer information. Do not send public market data when use terms prohibit redistribution.

Default research harness has no dependencies and does not make any Langfuse requests. Enable and test tracing only after authenticated connection and consent.
