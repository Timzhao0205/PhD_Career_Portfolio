# Hall + coil hybrid / radiation analysis

This is a new sibling mission. It reads the completed work in folder `06` and
the HSX context in folder `07`, but writes only to
`08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07`.

## One command

Open PowerShell in this `01` folder and run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1
```

That command uses full permission (`bypassPermissions`) inside the isolated
folder `08` and resumes automatically after an ordinary interruption.

Safer approval mode:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -Mode guarded
```

Preflight without invoking a model:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -DryRun
```

If a Fable-assigned stage finishes without a verifiable Fable 5 final result,
the first event is saved, quarantined, clarified, and retried once in a fresh
safe-mode session. A second event pauses the workflow at a durable checkpoint.
It will not silently substitute another provider. Only after reviewing that
checkpoint, explicitly authorize another Claude-only cycle with:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -RetryClaudeAfterHandoff
```

Start with
`08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07\README_START.md` for the
stage map, evidence gates, logs, and expected deliverables.

Model routing is summarized in `MODEL_ROUTING_HYBRID_RADIATION.md`; package
checks are recorded in
`HYBRID_RADIATION_PACKAGE_TEST_REPORT_2026-07-27.md`.
