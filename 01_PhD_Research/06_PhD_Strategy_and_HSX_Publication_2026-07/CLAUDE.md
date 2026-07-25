# Claude Code mission contract

Run only the stage named in the effective prompt. The files in this mission,
not prior chat memory, are authoritative.

## Boundaries

- Write only inside this mission folder.
- Treat `inputs`, parent manuscript sources, and HSX raw data as immutable.
- Do not send, submit, publish, purchase, upload, file, or mutate any external
  account.
- Public web research is allowed when required by the stage.
- Never invent a citation, DOI, result, reviewer position, venue rule, or legal
  conclusion.
- Separate supplied fact, external evidence, inference, recommendation,
  proposed experiment, and unresolved gate.
- Do not invoke another AI provider or external agent runtime.

## Model integrity

The launcher explicitly requests the stage's main model and effort. Only the
final result model of a Fable-assigned stage is an integrity gate. Auxiliary
operations, subagents, and temporary adjustments may use another model when
useful; their identity is logged but does not count as a downgrade. Non-Fable
stages are not paused for model adjustment.

For a Fable-assigned stage, Fable 5 must personally re-read auxiliary work,
reconcile it against the evidence, validate all outputs, and produce the final
main response. If the finished attempt's final main model is not Fable, or
cannot be verified, the launcher quarantines it, saves a checkpoint,
regenerates a clearer engineering prompt, and retries Fable once in a fresh
safe-mode session. A second failure ends Claude execution and prepares the
documented ChatGPT Windows continuation.

## Durable progress

The launcher writes every streamed event to both the raw `stream.jsonl` and
`state/CLAUDE_EVENT_LOG.jsonl` with requested model, effort, reported models,
main/transient/auxiliary models, current or final result model, Fable-only
downgrade status, and any security-fallback flag. In addition:

- update `state/PROJECT_STATE.md` before and after each meaningful research
  batch, decision, edit, validation, or checkpoint;
- append a concise entry to `state/WORKLOG.md` for each such operation;
- write partial outputs frequently using stable relative paths;
- create a recovery checkpoint before any broad rewrite and at stage
  completion.

If PowerShell is stopped manually, leave the latest valid partial files in
place. Do not delete evidence needed for continuation.
