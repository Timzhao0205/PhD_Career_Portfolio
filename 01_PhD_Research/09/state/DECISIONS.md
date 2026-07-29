# Controller decisions

- 2026-07-28 — SHUTDOWN CHECKPOINT decision. On user request, prepared for
  immediate computer shutdown: no new stage or agent started; the running
  B00 FULL attempt-2 repair worker could not be signaled (no
  SendMessage/interrupt tool exposed in this session; launching a signaling
  agent was forbidden) and was left to be terminated by app close — judged
  safe because its writes are per-file atomic and confined to
  outputs/B00_inventory/attempt-2. All durable state updated
  (SHUTDOWN_CHECKPOINT.md, STAGE_LEDGER B00 full → NEEDS_REVIEW with
  reconciliation instructions, PROGRESS, ERROR_LOG, MODEL_LEDGER,
  CURRENT_TASK, CURRENT_VERIFY). Nothing partial or unverified was marked
  accepted. Internal harness task ID intentionally not transcribed into
  package state (harness confidentiality constraint); descriptive worker
  identity recorded instead.

Append any conservative reconciliation, retry, dependency invalidation,
source limitation, or downstream rerun decision with its evidence.
