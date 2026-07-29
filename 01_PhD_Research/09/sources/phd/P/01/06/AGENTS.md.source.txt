# ChatGPT Windows mission continuation

This file applies when the mission is resumed in the ChatGPT desktop app.

## Recover first

Read:

1. `state/CHATGPT_HANDOFF_STATE.json`
2. `state/CHATGPT_HANDOFF.md`
3. all files in `state/markers` and the current `state/attempts/<stage>.json`
4. `state/OPERATION_LOG.csv`, `state/MODEL_EFFORT_LOG.csv`,
   `state/SESSION_INDEX.csv`, and the tail of
   `state/CLAUDE_EVENT_LOG.jsonl`
5. the raw stream and generated prompt listed by the handoff state
6. current-stage partial outputs, the stage prompt, and relevant evidence

The earliest stage without a valid completion marker is the current stage.
Preserve validated earlier stages and reuse valid partial work.

Ignore `_history/r0` for active progress. It is the preserved pre-restart audit
record and must not supply an active marker or resumable session.

## Model mapping

| Interrupted Claude assignment | ChatGPT Windows selection |
|---|---|
| Sonnet 5 / High | GPT-5.6 Sol / High |
| Sonnet 5 / Extra High | GPT-5.6 Sol / Extra High |
| Fable 5 / Extra High | GPT-5.6 Sol / Max |

If Max is unavailable, use GPT-5.6 Sol / Extra High and log the substitution.
Do not invoke Claude Code, another agent CLI, or an MCP server.

## Operation logging

Before and after every meaningful read, research batch, decision, edit,
validation, or checkpoint:

- append one row to `state/OPERATION_LOG.csv`;
- use route `chatgpt_windows`;
- record timestamp, stage, operation, progress, attempt, status, selected
  model/effort, reported/known model, downgrade/usage/inactivity flags,
  affected files or checkpoint, next action, and notes;
- update `state/CHATGPT_HANDOFF_STATE.json` and
  `state/CHATGPT_HANDOFF.md` atomically enough that an interruption leaves a
  readable last-known state.

Do not claim a model or effort that the app does not expose. Use
`MODEL_NOT_VERIFIED` or `EFFORT_NOT_VERIFIED` when necessary.

## Completion marker

After the stage-specific validator passes, create
`state/markers/<stage>.done.json` with:

```json
{
  "stage": "<stage>",
  "status": "complete",
  "completed_at": "<ISO-8601>",
  "route": "chatgpt_windows",
  "attempt": 1,
  "model": "gpt-5.6-sol",
  "effort": "<High|Extra High|Max>",
  "validation": "<exact checks and result>",
  "outputs": [
    {"path": "<relative path>", "sha256": "<lowercase SHA-256>"}
  ]
}
```

Then update the handoff state to the next incomplete stage. Preserve unresolved
evidence gaps and do not mark a stage complete merely because files exist.
