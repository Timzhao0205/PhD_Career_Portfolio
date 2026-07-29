# Model and effort policy

## Routing rationale

| Work type | Assigned model | Effort | Why |
|---|---|---|---|
| Inventory and traceability | Sonnet 5 | high | Mostly deterministic inspection and structured extraction |
| Hybrid and radiation search | Sonnet 5 | xhigh | Broad retrieval needs care, but evidence reconciliation is deferred |
| Applications search | Sonnet 5 | high | Wide current landscape; final priority is decided later |
| Applications/collaboration scoring | Sonnet 5 | xhigh | Substantial judgment, but bounded by the Fable-reviewed technical analysis |
| Evidence merge and all central technical decisions | Fable 5 | xhigh | Highest cost of error and strongest cross-domain reasoning need |
| Red team and final synthesis | Fable 5 | xhigh | Must challenge and sign off the full argument |

Seven of twelve stages require Fable 5 at xhigh. This satisfies the requirement
that Fable handle the most critical thinking while controlling budget on
search-heavy work.

The aliases passed to Claude Code are `sonnet` and `fable`; the installed
Claude Code version must be at least 2.1.219 so current model-category behavior
and model reporting can be checked.

## Integrity rule

For a Fable-assigned stage, the accepted final main response must report a
Fable model. Temporary main-thread adjustment followed by a Fable final result
is logged and allowed. Auxiliary/subagent use of another model is logged and
allowed. A final non-Fable or unverifiable model triggers:

1. First event: quarantine expected outputs, checkpoint all evidence, generate
   a narrowly clarified benign academic prompt, and retry once in a fresh
   Fable session with `--safe-mode`.
2. Second event: quarantine, checkpoint, stop the workflow, and require manual
   review. No silent provider or model substitution.

The retry prompt may clarify scope and remove ambiguous framing, but it may not
weaken evidence gates or change the scientific question.

## Logs

`MODEL_EFFORT_LOG.csv` records requested model/effort, all reported models,
final-result integrity, session, duration, validation, and notes.

`PERFORMANCE_LOG.csv` records duration, turns, token/cache fields, reported
cost, web-search/fetch counts, final model, integrity, and current verified
source count when those fields are available in Claude's stream.

Missing telemetry is recorded as zero or blank; it is never estimated.
