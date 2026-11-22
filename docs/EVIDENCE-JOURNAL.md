# Persistent synthetic evidence journal — milestone C1

`campaign/journal.py` is a **local same-host** JSONL custody ledger. It only accepts full deterministic, synthetically generated results from the already tested `campaign.controller`, replays them before appending, and records hash-linked receipts across runs. Identical run IDs are idempotent; conflicting IDs, malformed histories, reordered/tampered entries, invalid custody signatures and unsigned production access fail closed.

**Limits:** An HMAC key (at least 32 bytes) is mandatory for normal use; explicitly unsigned mode is permitted **only for synthetic research**. Never store a real custody key in Git or CI logs. The GitHub Actions artifact is ephemeral and **does not provide durable storage across runner invocations**. For protected persistent storage, configure an approved private volume or managed backing store and separate external hash anchors, access control and backup policy. The journal itself is not independently immutable against the host administrator.

No raw market data, third-party archive, personal trade data, live financial claims, model weights or broker APIs are supported.

Run:
```sh
python -m unittest discover -s tests -v
python -m campaign.record --ledger /tmp/oracle-synthetic-evidence.jsonl --run-id local-0001 --allow-unsigned-synthetic
```
Report classification: `SYNTHETIC_ONLY`. A run with a different ID but the **same fixture** is NOT an independent market test or learning validation.
