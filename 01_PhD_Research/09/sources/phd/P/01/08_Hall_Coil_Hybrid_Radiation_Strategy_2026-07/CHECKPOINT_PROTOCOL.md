# Checkpoint and recovery protocol

The PowerShell runner is the source of truth for execution state.

## Automatic durable files

- `state\attempts\<stage>.json`: latest attempt, model evidence, session,
  retry cycle, stream, prompt, and status.
- `state\sessions\<stage>.session_id`: resumable Claude session.
- `state\markers\<stage>.done.json`: validated output hashes.
- `state\generated_prompts`: exact effective prompts.
- `state\CLAUDE_EVENT_LOG.jsonl`: event index flushed during execution.
- `logs\run_*\...\stream.jsonl`: raw live Claude streams.
- `state\CHATGPT_HANDOFF_STATE.json` and `.md`: legacy filename retained for
  compatibility; content is the provider-neutral manual continuation snapshot.
- `state\handoff_history`: immutable archives before an authorized retry.
- `logs\RUN_HISTORY.jsonl`: workflow event history.

## Stage checkpoint

At each major internal milestone, write
`state\checkpoints\CP_<stage>_<timestamp>.md` with:

- stage and current gate;
- completed outputs and row counts;
- searches/analyses completed;
- exact unresolved questions;
- files safe to reuse;
- next action;
- model/effort and any model notice.

Update `state\PROJECT_STATE.md` atomically and append `state\WORKLOG.md`.

## Ordinary interruption

Run the same root command. The launcher passes `-Resume`; the runner resumes a
saved session when available and otherwise starts from durable files.

## First Fable final-result failure

The runner:

1. records all reported models and classifier/fallback text;
2. moves stage outputs into the rejected-attempt directory;
3. preserves raw streams and prompt;
4. writes the manual snapshot;
5. generates a clarified, scope-equivalent prompt;
6. starts one fresh Fable 5 safe-mode retry.

## Second failure

The runner saves and pauses with status `MANUAL_CONTINUATION_REQUIRED`.
Nothing automatically invokes another provider. Inspect the snapshot, then
choose whether to repair the prompt/environment or explicitly start another
Claude-only retry cycle with `-RetryClaudeAfterHandoff`.

Never delete a failed-attempt archive when resuming.
