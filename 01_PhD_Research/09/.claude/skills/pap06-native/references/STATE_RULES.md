# Durable state rules

`state/STAGE_LEDGER.json` is an index, not sole proof. On every start:

1. For each claimed accepted pilot, confirm the recorded candidate directory,
   all required stage files, `RUN_META.md`, and `SELF_CHECK.md exist.
2. For each claimed accepted full run, confirm the above plus the recorded
   verification report exists and ends with `VERDICT: PASS`.
3. Confirm route prerequisites and order.
4. If proof is incomplete, change status to `NEEDS_REVIEW`, explain the reason
   in `state/ERROR_LOG.md`, and reverify or rerun conservatively.
5. Never infer acceptance from a directory name, a partial file, conversation
   memory, or a previous package's completion marker.

After each accepted item:

- update the one matching ledger entry;
- update `state/PROGRESS.md` with timestamp if available, accepted paths,
  verdict, next action, and limitations;
- append requested and observed model/effort evidence to
  `state/MODEL_LEDGER.md`;
- preserve earlier attempts and reports.

State writes should be small and immediate. If the session ends between stage
completion and acceptance, the next session must verify the candidate before
marking it accepted.
