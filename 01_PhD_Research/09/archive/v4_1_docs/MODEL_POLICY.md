# Interactive model and effort policy

## Fixed route

- Main interactive controller: Fable 5/xhigh.
- Critical pilot/full workers: `pap06-fable-xhigh`, Fable 5/xhigh.
- B00, B10, and B12 pilot/full workers: `pap06-sonnet-high`,
  Sonnet 5/high.
- Opus is not requested because it was unavailable in the user's organization.
- There is no automatic model fallback chain in package settings.

The agent files set `model`, `effort`, and `permissionMode` in frontmatter.
`START.ps1` also explicitly launches the main controller with
`--model fable --effort xhigh --permission-mode bypassPermissions`.

## Evidence and acceptance

Project settings allow exactly `fable` and `sonnet`. A SessionStart hook records
the main model, controller name, session ID, and permission mode when the CLI
exposes it. If that field is absent, it records `NOT_EXPOSED` and requires a
match between the sealed launcher request, inherited launch nonce, and
`state\LAUNCH_INTENT.json`. It never relabels requested permission as an
observed hook value.

For each stage, SubagentStart/Stop hooks bind the exact agent ID to the prepared
stage and parse that subagent's independent transcript. The package records:

- requested and observed model;
- requested effort and observed effort when the transcript exposes it;
- named agent and agent ID;
- duration, assistant turns, input/output tokens, tool calls, and native web
  search/fetch counts;
- transcript SHA-256/size, validation result, and output hashes.

`ACCEPT_STAGE.ps1` accepts output only if the named agent matches, the transcript
model is identifiable as the required family/version, exposed effort does not
conflict, schema validation passes, and a checkpoint can hash every output.

If effort is absent, the record says `NOT_EXPOSED`. Fixed frontmatter and launch
arguments prove the request, not necessarily an organization-side effort cap.
The package never relabels a request as observed evidence.

Interactive subagent transcripts do not expose reliable per-run USD cost. The
numeric compatibility field is zero with
`cost_evidence=NOT_EXPOSED_IN_INTERACTIVE_TRANSCRIPT`; it is not a zero-cost
claim. Claude Code's `/cost` display remains available in the interface.

## Model integrity

For an actual model/effort mismatch:

1. The first event quarantines output and telemetry and authorizes one fresh
   retry with the same required named agent.
2. A second event writes `state\MODEL_PAUSE.json` and stops acceptance.
3. After explicit human review only, use the documented
   `-RetryFableAfterReview` start option. The pause and event ledger are
   preserved in quarantine.

Missing transcript evidence, runtime/API failures, and schema failures are
logged as their own statuses, never silently called successful Fable work.
Sonnet is never accepted as a Fable substitute.

## Context and progress

Each stage worker starts with a fresh named-agent context; accepted output is in
durable files. The visible main session receives concise results and may be
closed at any time. Rerunning `START.ps1` opens a new Fable controller and
resumes from checkpoints, avoiding dependence on a failed `/compact`.

## Budget behavior

There is no maximum budget, cost, token, turn, or elapsed-time setting. Accuracy
and expense are balanced only through narrow fresh contexts, three supporting
Sonnet stages, live pilots, checkpoint reuse, and no duplicate accepted work.
