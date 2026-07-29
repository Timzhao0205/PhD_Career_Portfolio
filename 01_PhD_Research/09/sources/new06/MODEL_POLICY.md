# Model and effort policy

## Main accepted work

The persistent interactive session is launched with:

```text
model: fable
required observed family: Fable 5
effort: xhigh
permission mode: bypassPermissions
```

The main session performs or personally reconciles every accepted stage. This
removes automatic model switching between stages and avoids the previous
stream-parser ambiguity. It also gives Fable/xhigh oversight to the two
evidence-heavy stages that previously used Sonnet as the stage-level final
model.

## Auxiliary work

Sonnet/high may be used only through the project `source-retriever` and
`mechanical-auditor` subagents:

| Work | Model | Effort | Authority |
|---|---|---|---|
| Current-source retrieval and extraction | Sonnet | high | Auxiliary only |
| Schema, count, arithmetic, and ID checks | Sonnet | high | Auxiliary only |
| Scoring, ranking, selection, synthesis, audit | Fable 5 | xhigh | Main final |

The main Fable agent must inspect and reconcile auxiliary findings. A subagent
response cannot establish an accepted score, selection, or verdict.

## Evidence and logging

- `SessionStart` records the actual main model identifier and session ID.
- The status-line input records current model, exposed effort, token totals, context
  use, duration, cost telemetry, rate-limit telemetry when exposed, and Claude
  Code version.
- Hook events record tool failures, subagent boundaries, compaction, stop
  failures, and session end.
- Stage checkpoints record the latest observed model/effort plus every output
  hash.

Prompt text is never model evidence. An observed non-Fable model or an
explicitly observed non-xhigh effort triggers the two-strike policy. When the
CLI does not expose effort, records say `NOT_EXPOSED` while separately
preserving the command-line request `xhigh`; absence is never converted into a
false verification or a false downgrade.

## Two-strike downgrade handling

Because the main session is pinned once, a verified Fable 5 session normally
cannot silently change per stage. If SessionStart or a status snapshot observes
another model or effort:

1. First unique session event: preserve and quarantine its evidence, reject any
   uncheckpointed work, and automatically start one fresh Fable retry.
2. Second unique session event: preserve all work, create
   `state/MODEL_PAUSE.json`, and require explicit review before another fresh
   session.

After review, the authorized command is:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1 -RetryFableAfterReview
```

The event history remains in `state\FABLE_EVENTS.json`; it is never silently
reset.

Source errors, schema failures, network errors, and missing fields are ordinary
repairable errors, not model downgrades.
