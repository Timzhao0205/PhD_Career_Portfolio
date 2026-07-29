# Mission runner

This mission is executed only by Claude Code when launched from PowerShell.

From the parent `01` folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1
```

The same command resumes from durable state. The runner does not poll account
usage and does not use a no-output timeout. You may close PowerShell manually;
the current prompt, raw stream, event index, model/effort record, attempt state,
and ChatGPT handoff snapshot are saved in this mission folder.

If the current attempt state is already `CHATGPT_HANDOFF_REQUIRED` and the
user explicitly wants another Claude cycle, run from the parent folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -RetryClaudeAfterHandoff
```

The old handoff is archived, completed markers are retained, and the current
stage starts in a fresh Claude session. A normal run without this switch does
not restart a handoff stage.

For a safe validation-only run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_PHD_RESEARCH.ps1 -DryRun
```

For the Fable final-result model-policy test:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_PHD_RESEARCH.ps1 -SelfTest
```

The model-policy test verifies that Sonnet/Haiku and other temporary or
auxiliary adjustments are logged and allowed, while every Fable-assigned stage
requires Fable 5 to produce the final result. Only a non-Fable/unverifiable
Fable-stage final result causes the one-retry/two-event handoff transition.

If Claude cannot continue, open the parent folder in the ChatGPT desktop app
for Windows and follow `..\CHATGPT_WINDOWS_CONTINUE.md`.
