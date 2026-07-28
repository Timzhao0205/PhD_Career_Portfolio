# Autonomous interactive runbook

## 1. Bootstrap

1. Read `CLAUDE.md`, `MODEL_POLICY.md`, `SOURCE_POLICY.md`, `ROUTE.json`, and
   this runbook.
2. If `state/MODEL_PAUSE.json` exists, do no substantive work.
3. Read `state/ACTIVE_SESSION.json` and the newest line of
   `logs/status.jsonl`. Confirm observed Fable 5. Confirm effort `xhigh`, or
   record `NOT_EXPOSED` while preserving the launcher request `xhigh`; an
   explicit different effort is a model-integrity event.
4. Run:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\CHECK.ps1
   ```

5. Inspect `state/stages`. A stage is reusable only when its marker exists,
   `CHECKPOINT.ps1 -Stage <name> -Verify` passes, and every upstream marker is
   also valid.

## 2. Stage order

Run exactly:

```text
10_refresh
20_p4
30_redteam
40_select
45_packs
50_deep
60_synth
70_audit
```

For each unfinished stage:

1. Read the corresponding file in `prompts/`.
2. Perform a small representative pilot before the full stage:
   - choose two or three representative records;
   - exercise every planned read/search/write/validation path;
   - do not reuse pilot judgments as full-stage answers;
   - write `pilot\<stage>\PILOT.json` and `PILOT.md`;
   - `PILOT.json` must contain `stage`, `status:"PASS"`, `sample_ids`,
     `paths_tested`, `checks`, `errors`, and `lessons`;
   - `errors` must be an empty JSON array;
   - run:

     ```powershell
     powershell -NoProfile -ExecutionPolicy Bypass -File .\VALIDATE.ps1 -Stage <stage> -Pilot
     powershell -NoProfile -ExecutionPolicy Bypass -File .\CHECKPOINT.ps1 -Stage <stage> -Pilot
     ```

3. Complete the full stage under `outputs\<stage>`. Partial files are allowed
   during work, but no completion marker may exist yet.
4. Run the stage validator. Repair every visible failure and rerun until it
   exits 0:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\VALIDATE.ps1 -Stage <stage>
   ```

5. Run the read-only `mechanical-auditor` when the stage contract calls for
   cross-file checks. Personally decide and make any repairs.
6. Create the durable checkpoint:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\CHECKPOINT.ps1 -Stage <stage>
   ```

7. Continue immediately to the next stage. Do not stop for a progress summary.

## 3. Error recovery

- Schema, count, arithmetic, missing-file, and source-ID failures: repair and
  revalidate in the same session.
- Interrupted session or external usage/network/authentication failure: leave
  partial files unmarked. The same `START.ps1` command resumes.
- Context compaction: reread this runbook and durable stage markers.
- Genuine unrecoverable external blocker: write `state/PAUSE.json` containing
  UTC time, stage, exact blocker, completed files, and the single next action.
- First model/effort mismatch: let the launcher archive the attempt and perform
  its single automatic fresh-session retry. Second mismatch: preserve
  `state/MODEL_PAUSE.json`; do not accept the stage.

## 4. Final release

After Stage 70:

1. Confirm `outputs\70_audit\AUDIT.json` has `verdict:"PASS"`, zero unresolved
   critical issues, and zero unresolved major issues.
2. Run:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\VALIDATE.ps1 -All
   ```

3. If it exits 0, run:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\COMPLETE.ps1
   ```

   This writes `state\RUN_COMPLETE.json`, records completion/session/model/
   effort/audit evidence and all stage-marker hashes, then validates again.
4. Only after `COMPLETE.ps1` exits 0 may the session stop.
