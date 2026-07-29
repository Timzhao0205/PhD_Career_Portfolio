# Hall + coil hybrid/radiation package test report

Date: 2026-07-27

## Passed before packaging

- All files from the supplied ZIP were byte-for-byte unchanged.
- New work is isolated to three parent-level entry/reference files and
  `08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07`.
- Required file and prompt inventory passed.
- JSON settings parsed and matched Sonnet/high with connectors disabled.
- Twelve stages and their dependency chain were detected.
- Model routing contained exactly seven Fable 5/xhigh and five Sonnet stages.
- Stale folder-06 stage names were absent from the new runner.
- Full mode, guarded mode, safe-mode retry, model-integrity check, manual
  pause, raw event stream, session resume, and performance telemetry tokens
  were present.
- All initial CSV headers parsed and matched their schemas.
- PowerShell files passed a lexical delimiter, quoted-string, here-string,
  comment, and line-continuation balance check.
- Folder `06` final source ledger and folder `07` HSX context were present.

## Windows-authoritative preflight

The build environment does not include PowerShell, so the Windows PowerShell
AST parser was not executed here. `VALIDATE_PACKAGE.ps1` performs that parse
for all five PowerShell files before Claude is invoked. The parent command
with `-DryRun` is the authoritative no-model preflight:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -DryRun
```

The normal one-command launcher runs the same validator automatically.
