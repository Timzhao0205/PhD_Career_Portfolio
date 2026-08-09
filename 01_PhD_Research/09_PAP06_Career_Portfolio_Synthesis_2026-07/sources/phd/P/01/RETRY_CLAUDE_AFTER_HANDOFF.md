# Retry Claude after a saved handoff

Use this only when the current stage has already been saved as
`CHATGPT_HANDOFF_REQUIRED` and you explicitly want another Claude-only cycle.

From this extracted `01` folder, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -RetryClaudeAfterHandoff
```

## What the switch does

1. Keeps every valid active completion marker. This release initially has none
   because the user requested a full restart from stage `00_inventory`.
2. Copies the existing attempt state, ChatGPT handoff snapshots, session ID,
   generated prompt, and latest stage checkpoint into a timestamped
   `state\handoff_history\retry_*` folder.
3. Appends a `user_authorized_claude_retry` operation and a machine-readable
   authorization record.
4. Starts the earliest incomplete stage in a **fresh Claude session** with the
   configured Claude model and effort. It does not resume the session that
   reported the rejected model.
5. Uses globally increasing attempt numbers plus `retry_cycle` and
   `cycle_attempt` fields so earlier and later evidence cannot be confused.
6. Preserves the same Fable-only integrity rule inside the new cycle:
   temporary and auxiliary models are allowed; a Fable-assigned stage must
   finish with Fable 5 producing the accepted result. First final-result
   failure → quarantine and safe-mode Fable retry; second → save and return to
   ChatGPT Windows handoff.

The switch never invokes ChatGPT, Codex, MCP, or another provider. To inspect
the plan without invoking a research model:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -DryRun
```

Omitting `-RetryClaudeAfterHandoff` preserves the saved handoff and does not
restart Claude.
