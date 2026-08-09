# Resume and recovery

Normal interruption, terminal close, network loss, or a deliberate stop:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
```

The command resumes the named session after Claude has marked
`session_started: true`. The parent must read `state/STATE.json`,
`state/WORKLOG.md`, and the newest file in `state/checkpoints` before acting.

If `state/PAUSE.md` exists, read it before retrying. A Fable two-strike pause is
intentional and must not be bypassed by changing models. Correct only the named
evidence, access, or prompt issue, then tell the resumed Fable session to retry
the paused stage.

If Claude Code itself says the named session cannot be found but the state says
it started, make a safety copy of `state` and `outputs`, then change only
`session_started` to `false` in `state/STATE.json` and run the same command. The
new parent will reconstruct progress from checkpoints.

Never copy state from an older package into this folder.
