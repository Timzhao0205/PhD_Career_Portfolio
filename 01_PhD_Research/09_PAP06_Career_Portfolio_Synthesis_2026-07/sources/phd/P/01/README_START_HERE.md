# Claude-only PhD research package

This folder runs the complete research workflow through Claude Code in Windows
PowerShell. It contains no automatic call to another AI provider and no active
MCP server configuration.

## One command

For Windows path-length reliability, extract the ZIP to a short path such as
`D:\PHD`. Open PowerShell in the resulting `D:\PHD\01` folder and
run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1
```

Run the same command again to resume completed or interrupted work.
This release begins from `00_inventory` with 0 of 12 mission stages complete.

If the saved state already says `CHATGPT_HANDOFF_REQUIRED` and you have
explicitly decided to try Claude again because usage remains, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -RetryClaudeAfterHandoff
```

That command preserves the previous handoff in `state\handoff_history`, keeps
completed stages, and starts the current incomplete stage in a fresh Claude
session. See
[RETRY_CLAUDE_AFTER_HANDOFF.md](RETRY_CLAUDE_AFTER_HANDOFF.md).

The launcher:

1. validates the package;
2. performs small live Sonnet 5 and Fable 5 probes;
3. runs all 12 stages through Claude Code only;
4. logs every streamed Claude event immediately;
5. records stage, attempt, requested/reported/primary/auxiliary models, effort,
   Fable-only downgrade and security-fallback flags, files, validation, and
   next action;
6. keeps an always-current ChatGPT Windows handoff snapshot.

The runner does **not** check usage, enforce an inactivity timeout, or stop a
quiet Claude process. You can check usage yourself and close PowerShell
manually. The current stage remains recoverable from:

- `06\state\CHATGPT_HANDOFF_STATE.json`
- `06\state\CHATGPT_HANDOFF.md`
- `06\state\CLAUDE_EVENT_LOG.jsonl`
- the current `logs\run_*\<stage>\...\stream.jsonl`

## Fable final-result policy

- Enforcement applies only to the seven Fable-assigned critical stages.
  Auxiliary and temporary model adjustments are logged and allowed.
- The runner waits for the attempt to finish. Fable 5 must perform the final
  review/validation and produce the accepted main result.
- First non-Fable or unverifiable final result: the attempt is logged and
  quarantined; a clarified engineering prompt is generated and Fable 5 is
  tried once more in a fresh safe-mode session.
- Second such final-result event: Claude stops. All state is saved and the
  package exits with a ready-to-use ChatGPT Windows handoff.
- A later Claude retry is never automatic. If the user explicitly supplies
  `-RetryClaudeAfterHandoff`, the prior handoff is archived and a new
  two-attempt integrity cycle begins with globally increasing attempt numbers.

The prior `10a_literature_gan` Sonnet-plus-Haiku records were auxiliary-model
usage, not a Sonnet primary downgrade. The entire prior mission run is retained
under `_history\r0` for audit only. The active workflow starts again at
`00_inventory`; no old completion marker or session is active.

## Continue in ChatGPT Windows

Read [CHATGPT_WINDOWS_CONTINUE.md](CHATGPT_WINDOWS_CONTINUE.md). Open this
folder as the primary local project, choose the model/effort in the handoff
state, and paste [CHATGPT_WINDOWS_START_PROMPT.md](CHATGPT_WINDOWS_START_PROMPT.md).

## Useful safe checks

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File .\RUN_PHD_RESEARCH.ps1 -SelfTest
```

`-DryRun` validates and prints routing without invoking a research model.
`-SelfTest` checks temporary/auxiliary classification, Fable final-result
acceptance, and the first/second transition policy.

The complete change and validation record is in
[CLAUDE_ONLY_MIGRATION_2026-07-24.md](CLAUDE_ONLY_MIGRATION_2026-07-24.md).
The explicit retry addition is recorded in
[CLAUDE_RETRY_OVERRIDE_PATCH_2026-07-24.md](CLAUDE_RETRY_OVERRIDE_PATCH_2026-07-24.md).
Concrete preservation and validation results are in
[PACKAGE_TEST_REPORT_2026-07-24.md](PACKAGE_TEST_REPORT_2026-07-24.md).
The current policy and restart are recorded in
[FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md](FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md).
The Windows PowerShell 5.1 validator correction is recorded in
[VALIDATOR_PS51_HOTFIX_2026-07-24.md](VALIDATOR_PS51_HOTFIX_2026-07-24.md).
