# Agent routing

The main interactive session is the sole final decision-maker and must remain
Fable 5/xhigh. Project subagents are auxiliary:

- `source-retriever`: Sonnet/high retrieval and extraction only.
- `mechanical-auditor`: Sonnet/high read-only schema and consistency checks.

Auxiliary work never establishes an accepted score, rank, selection, synthesis,
or final audit verdict.

