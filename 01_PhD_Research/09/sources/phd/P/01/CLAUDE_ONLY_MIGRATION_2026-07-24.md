# Claude-only migration record — 2026-07-24

> Historical note: the active workflow was later reset to stage 00 under the
> Fable final-result policy in `FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md`.

## Decision implemented

The PowerShell workflow now invokes Claude Code only. It never calls another AI
provider and contains no active MCP server configuration.

Removed runtime files:

- `06\CODEX_MCP_CLIENT.ps1`
- `06\TEST_MCP_CONNECTION.ps1`
- `06\INVOKE_CODEX_EXEC_CHILD.ps1`
- `06\.mcp.codex.json`
- superseded root recovery note

The original user request/setup records under `inputs` remain immutable for
provenance. The earlier build log is retained under
`state\HISTORICAL_BUILD_LOG_BEFORE_CLAUDE_ONLY_2026-07-24.md` and is explicitly
non-active.

## Active behavior

- 12 sequential Claude stages
- 7 Fable 5 / Extra High critical stages
- 3 Sonnet 5 / Extra High literature lanes
- 2 Sonnet 5 / High organization/timeline stages
- no usage polling
- no no-output/inactivity timeout for research stages
- user-controlled manual PowerShell termination
- every Claude stream event flushed to a raw stream and compact event index
- attempt/model/effort/session/downgrade/quarantine/validation logs
- current ChatGPT Windows handoff JSON and Markdown snapshot

## Model-integrity transitions

1. First downgrade or unverifiable requested model: stop; record the reported
   model and flags; quarantine candidate stage outputs; save a handoff
   checkpoint; regenerate the effective prompt; retry the requested Claude
   model once.
2. Second event: stop Claude; save all progress and logs; set
   `CHATGPT_HANDOFF_REQUIRED`; continue manually in the ChatGPT desktop app
   using the stage's documented GPT-5.6 Sol equivalent.

## Validation performed before packaging

- latest wrapper upload passed full ZIP integrity testing;
- all seven PowerShell scripts parsed without syntax errors;
- all JSON files parsed;
- state CSV headers matched their writers;
- exact 12-stage routing counts passed;
- first/second downgrade transition checks passed;
- no active alternate-provider or MCP execution file remained;
- no usage/inactivity watchdog remained in the research runner;
- all six immutable-input SHA-256 checks passed;
- the manuscript, HSX, PDF, and source-archive bytes matched the supplied
  valid attachments;
- per-event auto-flush and progress/model/effort/downgrade fields were wired.

The user’s Windows machine performs the live Claude Sonnet/Fable probes at the
start of `RUN_EVERYTHING.ps1`; no paid live model call was made while rebuilding
the archive.

## Explicit retry patch

After the saved `10a_literature_gan` handoff, the user explicitly requested
another Claude-only run because usage remained. The additive
`-RetryClaudeAfterHandoff` path archives the old handoff, retains completed
markers, starts a fresh session, records retry-cycle metadata, and keeps the
same two-attempt integrity policy. Details are in
`CLAUDE_RETRY_OVERRIDE_PATCH_2026-07-24.md`.
