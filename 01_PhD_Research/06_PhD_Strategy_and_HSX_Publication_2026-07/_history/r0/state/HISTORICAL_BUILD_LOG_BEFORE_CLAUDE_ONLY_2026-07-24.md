# Historical build log before the Claude-only decision

This record is retained for patch provenance only. Its earlier runtime design
is superseded and is not active in the current package.

Append new entries below. Do not rewrite prior entries.

- 2026-07-24 — Package baseline created from the supplied project, manuscript,
  decision letter, request, and HSX results.
- 2026-07-24 — Pre-delivery validation passed for script grammar, JSON,
  immutable-input checksums, both source archives, PDF readability, and
  archive-to-extraction byte identity.
- 2026-07-24 — Added a direct PowerShell client for `codex mcp-server`, a live
  read-only GPT-5.6 Sol connection probe, a 30-minute Claude inactivity
  watchdog, immediate usage-limit handoff, and route-specific resume records.
- 2026-07-24 — Changed every Fable stage previously requesting `max` effort to
  `xhigh`; inventory remains `high` and Codex fallback efforts are unchanged.
- 2026-07-24 — Confirmed Codex CLI as the OpenAI MCP fallback, clarified that
  authentication may use ChatGPT browser login or an API key, renamed the
  reference server to `codex_fallback`, and set the one-token connection probe
  to GPT-5.6 Sol at `low` effort without changing substantive stage efforts.
- 2026-07-24 — Smoke-tested `codex-cli 0.145.0` in an isolated unauthenticated
  environment: MCP initialization, `codex`/`codex-reply` discovery, and the
  client-used argument schema passed. The account-facing model probe remains a
  first-run test on the user's Windows computer.
- 2026-07-24 — Rebuilt the package from the newly supplied attachments. Added
  `RUN_EVERYTHING.ps1`, which performs the live connection test and then
  automatically resumes the staged mission with one command.
- 2026-07-24 — Fixed the Windows PowerShell false failure caused when
  `codex login status` prints the successful `Logged in using ChatGPT` message
  on stderr. Native CLI success is now determined by its exit code.
- 2026-07-24 — Reserved `70_redteam` for direct GPT-5.6 Sol `max` as the
  independent cross-model audit, kept all substantive Fable stages at
  `xhigh`, and adjusted broad Codex evidence fallbacks to `xhigh` for budget
  control.
- 2026-07-24 — Rebalanced the primary Claude routes for accuracy per unit of
  budget: Sonnet 5 handles inventory, three bounded evidence batches, and the
  timeline; Fable 5 is reserved for evidence integration, research direction,
  manuscript strategy, experiment design, IP screening, and final synthesis.
  Added stage-specific family verification so either an unintended downgrade
  or an unintended expensive upgrade is quarantined and retried.
- 2026-07-24 — Fixed the offline validator's strict-mode quoting regression:
  the model-integrity regex now preserves `$requestedClaudeModel` literally
  instead of trying to read it as an unset validator variable. Added a static
  guard against backslash-escaped PowerShell variables in expandable strings.
- 2026-07-24 — A Windows PowerShell 5.1 field run confirmed live access to
  GPT-5.6 Sol through Codex MCP, Claude Sonnet 5, and Claude Fable 5.
- 2026-07-24 — Replaced the Claude probe receipt's generic `List[object]`
  array subexpression with a native object array and forced the Codex effort
  sequence to remain a typed string array when it contains one item. Removed
  the same risky generic-list wrapping pattern from active runtime paths and
  added executable compatibility checks to offline validation.
