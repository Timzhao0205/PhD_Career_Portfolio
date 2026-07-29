# Stage lifecycle

For the next route item and mode:

1. Confirm prerequisites are accepted.
2. Determine target:
   - pilot: `pilot/<stage>/`
   - full: `outputs/<stage>/`
3. If a non-accepted target already contains files, move nothing and overwrite
   nothing. Record the attempt in `state/ERROR_LOG.md`, create the next
   `attempt-N` subdirectory under that target, and use it as the candidate.
4. Write `state/CURRENT_TASK.md` from `state/CURRENT_TASK_TEMPLATE.md`. Include
   exact stage, mode, target, named worker, requested model/effort, stage
   specification, allowed inputs, prerequisite outputs, required files, and
   the current repair notes if any.
5. Append a `STARTED` row to `state/MODEL_LEDGER.md`. Requested configuration
   is evidence of intent only.
6. Tell the user what is starting, then invoke the exact named worker in the
   foreground and wait.
7. Immediately append any Claude Code-exposed agent ID, model, effort,
   duration, turns, token counts, tool/web counts, or failure information to
   `state/MODEL_LEDGER.md`. Use `NOT_EXPOSED` rather than estimating.
8. Inspect candidate files and `SELF_CHECK.md`.

## Pilot acceptance

The controller checks the complete pilot rubric in
`references/ACCEPTANCE.md`. A pilot must exercise the whole method on the
specified sample and contain every required filename. If it fails, delegate a
fresh worker with exact repairs. Once it passes, mark the pilot `ACCEPTED` in
the stage ledger and immediately proceed to full.

## Full acceptance

1. Write `state/CURRENT_VERIFY.md` from its template.
2. Invoke `pap06-verifier` in the foreground.
3. The verifier writes only
   `verification/<stage>/FULL_attempt-N.md`.
4. Accept only a report ending in `VERDICT: PASS`.
5. On FAIL, append the defects to `state/ERROR_LOG.md`, create a fresh
   candidate attempt, and invoke the route worker with those repairs. Then use
   a fresh verifier. Do not let the controller silently repair research.
6. After PASS, record accepted candidate and report paths in
   `state/STAGE_LEDGER.json`, append completion/model notes, update
   `state/PROGRESS.md`, and clear the current-task files.

There is no monetary retry cap. To prevent an infinite defect loop, after
three consecutive failures with the same unresolved structural cause, write
`state/BLOCKER.md` with evidence and pause for human review. This is a
correctness gate, not a budget gate.

## Model/provider events

- Never substitute Sonnet for Fable.
- If an explicitly exposed model conflicts with the route, reject the attempt
  and retry once with the same named agent.
- A second explicit mismatch writes `state/MODEL_PAUSE.md` and stops.
- If model or effort is not exposed, record `NOT_EXPOSED`; do not relabel the
  request as observed proof.
- If Fable safeguards reject a safe request, record the request ID if shown and
  retry once in a fresh Fable agent with a concise, neutral task description.
  If it rejects again, write `state/BLOCKER.md`. Do not switch critical work to
  Sonnet.
- If a context compaction fails, durable state remains valid. The user can
  close Claude Code and rerun the same one command.
