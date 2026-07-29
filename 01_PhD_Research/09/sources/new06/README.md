# Folder 06 interactive Fable rerun — no budget stop

This is a fresh standalone package for Windows PowerShell 5.1 and Claude Code
interactive mode. It preserves the complete validated Folder 06 corpus but
does not reuse the previous PowerShell stream parser, response sentinel,
per-stage child launchers, or budget/turn-stop machinery.

## One command to start or resume

Extract to a short path, preferably:

```text
C:\AI\F06I
```

Open **Windows PowerShell**, enter the extracted folder, and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
```

The same command:

1. checks the exact PowerShell target and package/source hashes;
2. parses every active PowerShell script using the installed PS 5.1 parser;
3. runs offline fixtures for every stage and every hook;
4. starts a persistent interactive Claude Code session on Fable 5/xhigh;
5. resumes the recorded session on later runs;
6. keeps working through all eight stage pilots and full stages;
7. validates and checkpoints every stage;
8. stops only after the final audited release passes.

There is no package-defined monetary, turn, token, or time shutdown.

## Required setup

1. Use the memorized runtime:

   ```text
   Windows PowerShell 5.1.26100.8875 Desktop
   Build 10.0.26100.8875
   CLR 4.0.30319.42000
   ```

2. Install and sign in to Claude Code. Confirm:

   ```powershell
   claude --version
   claude
   ```

   If Claude opens successfully, exit that test session and return to this
   folder.

3. Keep the package at a short path. Do not run it from inside another Claude
   project.

4. Run the one command above. Claude opens interactively and begins
   automatically. You may observe it, but routine input is not required.

## Model and effort route

| Stage | Main accepted work | Auxiliary work | Pilot |
|---|---|---|---|
| 10_refresh | Fable 5/xhigh reconciliation | Sonnet/high retrieval | Required |
| 20_p4 | Fable 5/xhigh scoring | Sonnet/high mechanical check | Required |
| 30_redteam | Fable 5/xhigh judgment | Sonnet/high retrieval | Required |
| 40_select | Fable 5/xhigh selection | Sonnet/high mechanical check | Required |
| 45_packs | Fable 5/xhigh acceptance | Sonnet/high retrieval/check | Required |
| 50_deep | Fable 5/xhigh deep analysis | Sonnet/high retrieval/check | Required |
| 60_synth | Fable 5/xhigh synthesis | Sonnet/high mechanical check | Required |
| 70_audit | Fable 5/xhigh final audit | Sonnet/high retrieval/check | Required |

The main session remains Fable throughout, so the package no longer has to
switch or parse models between stages.

## Full permissions

The launcher uses:

```text
--permission-mode bypassPermissions
```

This provides unattended read/edit/tool permission. It is powerful. Run only
inside this dedicated folder, preferably in a Windows Sandbox or VM. Project
instructions prohibit writes outside the package and prohibit modification of
`src\06`, but bypass mode itself is not an operating-system sandbox.

## Logging

| File | Contents |
|---|---|
| `logs\status.jsonl` | Model, effort, tokens, context, duration, cost telemetry, limits |
| `logs\events.jsonl` | Session, failure, subagent, compaction, and stop events |
| `state\ACTIVE_SESSION.json` | Resumable session ID and observed model |
| `state\stages\<stage>.json` | Validation result, model/effort, files, hashes |
| `pilot\<stage>` | Required pre-stage pilot |
| `outputs\<stage>` | Accepted full-stage work |
| `outputs\70_audit\FINAL` | Canonical audited package |

Reported dollar values are telemetry; they are not a local spending cutoff.

## Pausing and resuming

- To pause manually, press `Ctrl+C`. The Stop hook does not override a user
  interrupt.
- To resume, rerun the same `START.ps1` command.
- If Claude Code reports an external usage or authentication limit, close it,
  resolve/wait for the external issue, and run the same command.
- Do not delete `state`, `outputs`, `logs`, or `pilot`.

Optional diagnostics:

```powershell
# Offline checks and fixtures only
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1 -CheckOnly

# Verify all completed stages and the final release
powershell -NoProfile -ExecutionPolicy Bypass -File .\VALIDATE.ps1 -All

# Start a fresh interactive session while retaining durable outputs
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1 -NewSession

# Explicitly authorize a fresh attempt after a protected second model event
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1 -RetryFableAfterReview
```

`-AllowCompatiblePS51` accepts another Windows PowerShell 5.1 Desktop patch
level. Use it only when you intentionally changed Windows; the default remains
the exact memorized runtime.
