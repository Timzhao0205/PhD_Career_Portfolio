# Package validation

Run from this mission folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\VALIDATE_PACKAGE.ps1
```

Or run the parent launcher with `-DryRun` to validate without invoking Claude:

```powershell
powershell -ExecutionPolicy Bypass -File ..\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -DryRun
```

The validator checks:

- required launchers, contracts, policies, prompts, and state files;
- PowerShell parse errors;
- JSON validity;
- exact twelve-stage routing and seven Fable/xhigh assignments;
- no automatic alternate-provider command;
- performance-log schema;
- folder `06` source ledger and folder `07` context availability;
- final deliverables and terminal audit line when `-RequireComplete` is used.

Live model probes are separate because validation must also work offline.
