# Package validation

`VALIDATE_PACKAGE.ps1` checks:

- required Claude-only runtime and ChatGPT handoff files;
- absence of the former alternate-agent/MCP runtime files;
- Windows PowerShell parser validity for every active script;
- JSON and CSV state-file validity;
- SHA-256 identity of supplied originals;
- extracted manuscript source and HSX results;
- exact 12-stage model/effort allocation;
- seven Fable/Extra High, three Sonnet/Extra High, and two Sonnet/High stages;
- only Fable-assigned final-result failures enforce downgrade transitions;
- temporary and auxiliary/subagent model adjustment is logged and allowed;
- a Fable completion marker requires a Fable final result model;
- first Fable final-result failure → regenerated safe-mode Fable retry;
- second Fable final-result failure → saved ChatGPT Windows handoff;
- explicit post-handoff retry switch forwarding and history preservation;
- globally increasing attempts plus retry-cycle/cycle-attempt state;
- no usage polling or inactivity timeout in the research runner;
- per-event flush logging and handoff-state files;
- stage-specific output gates when `-RequireComplete` is requested.

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\VALIDATE_PACKAGE.ps1
```

The parent `RUN_EVERYTHING.ps1 -DryRun` performs validation and prints the full
Claude/ChatGPT mapping without invoking a research stage.
