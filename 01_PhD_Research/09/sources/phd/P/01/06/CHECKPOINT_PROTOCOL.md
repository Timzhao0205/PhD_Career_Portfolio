# Checkpoint protocol

The package uses independent durable layers so a manually closed PowerShell
window does not erase the recovery state.

| Layer | Path | Update frequency |
|---|---|---|
| Raw Claude events | `logs/run_*/<stage>/*/stream.jsonl` | every emitted event, flushed immediately |
| Compact event index | `state/CLAUDE_EVENT_LOG.jsonl` | every emitted event, flushed immediately |
| Lifecycle operations | `state/OPERATION_LOG.csv` | preflight, attempt, Fable final-result failure, quarantine, validation, completion, handoff |
| Model/effort ledger | `state/MODEL_EFFORT_LOG.csv` | after every attempt/probe |
| Session index | `state/SESSION_INDEX.csv` | after every attempt |
| Attempt state | `state/attempts/<stage>.json` | before and after each attempt/transition |
| Completion marker | `state/markers/<stage>.done.json` | only after validation |
| Handoff snapshot | `state/CHATGPT_HANDOFF_STATE.json` and `.md` | attempt start, every stream change, and every transition |
| Effective prompts | `state/generated_prompts/<stage>_attempt_<n>_cycle_<n>_<run>.md` | before every attempt |
| Prior handoff archives | `state/handoff_history/retry_*` | before every explicitly authorized post-handoff Claude cycle |

Claude also updates `state/PROJECT_STATE.md`, `state/WORKLOG.md`, partial
outputs, and `state/checkpoints/CP_<stage>_<timestamp>.md` during substantive
work.

## Manual interruption

If the user closes PowerShell after a long period without output, the last
flushed stream event and handoff JSON remain authoritative. The ChatGPT Windows
continuation must treat `CLAUDE_IN_PROGRESS` as an interrupted attempt, inspect
partial files, and resume without repeating valid work.

## Rejected Fable results

Files produced by a Fable-assigned attempt whose final main result is non-Fable
or unverifiable are moved under the corresponding
`logs/run_*/<stage>/rejected_attempt_*_outputs` directory with
`QUARANTINE_MANIFEST.json`. They remain available for audit but are not
accepted as stage outputs.

Auxiliary model changes, aggregate `modelUsage` entries, and model adjustments
that return to Fable before final result production are recorded without
quarantine or pause. Model adjustments inside a non-Fable stage are also
nonblocking.
Historical `10a_literature_gan` Sonnet-plus-Haiku records remain intact for
audit, but are explicitly reclassified as auxiliary-model use under the
corrected policy.

The original mission state, logs, outputs, and evidence from before the clean
restart are under `_history\r0`. They are audit-only and do not count as
current partial or completed work.

## Explicit retry after handoff

When `-RetryClaudeAfterHandoff` is supplied, the runner copies the prior
attempt state, handoff JSON/Markdown, session ID, generated prompt, and latest
checkpoint to a new handoff-history folder. It also writes
`USER_RETRY_AUTHORIZATION.json` before starting a fresh Claude session.
Completed stage markers are not moved or regenerated.
