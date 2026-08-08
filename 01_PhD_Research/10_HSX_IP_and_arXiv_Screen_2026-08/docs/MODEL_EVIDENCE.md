# Model and telemetry evidence rules

Requested model/effort come from the launch arguments and agent frontmatter.
They do not prove the served model. Accept observed values only when shown by:

- Claude Code `/status` or status line;
- session, task, or API metadata exposed by Claude Code;
- an explicit safety-fallback or availability notice in the transcript; or
- durable debug metadata that unambiguously names the served model.

Do not treat an agent saying "I am Fable" as independent evidence. If no
platform evidence is exposed, record `not_exposed` and preserve the requested
configuration as separate evidence.

Record duration, turns, tokens, web queries, and cost only when observable.
Blank or `not_exposed` is correct; estimates presented as measured values are
not. The final model report must reconcile every Fable stage and every event in
`state/FALLBACK_LOG.md`.
