# Run and resume

## Normal

From `01`:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1
```

The command includes `-Resume`. Repeating it skips hashed, validated stage
markers and resumes an incomplete session when possible.

## Dry run

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -DryRun
```

## Guarded permissions

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -Mode guarded
```

## After a protected pause

Read:

- `state\CHATGPT_HANDOFF.md` (legacy compatible filename);
- `state\CHATGPT_HANDOFF_STATE.json`;
- the current file in `state\attempts`;
- the latest raw stream under `logs\run_*`.

Only when a fresh Claude-only cycle is intended:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -RetryClaudeAfterHandoff
```

The previous pause is archived before the new cycle begins.
