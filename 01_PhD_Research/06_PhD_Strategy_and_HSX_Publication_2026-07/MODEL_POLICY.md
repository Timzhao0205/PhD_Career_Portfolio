# Model and effort policy

## Claude-only PowerShell route

- Sonnet 5 / High: inventory and timeline assembly.
- Sonnet 5 / Extra High: three parallel literature-search lanes.
- Fable 5 / Extra High: literature merge, research direction, manuscript
  strategy, experiment planning, IP analysis, red-team audit, and final
  synthesis.

Fable is reserved for the seven judgment-heavy stages to control budget while
retaining the strongest Claude allocation where errors would propagate.

## Fable final-result integrity policy

Downgrade enforcement applies only when the configured main stage model is
Fable 5. The launcher distinguishes:

- **main-session evidence**: the session `system/init.model` plus assistant
  messages that do not have a `parent_tool_use_id`;
- **auxiliary model evidence**: subagent/tool activity and model names that
  appear only in aggregate `modelUsage`.

Sonnet, Haiku, Opus, or another model used for an auxiliary operation is
logged, but is allowed and never triggers a pause. A non-Fable primary stage
is also not subject to downgrade enforcement.

For a Fable-assigned stage:

1. Attempt 1 requests Fable 5 and the configured effort.
2. Temporary non-Fable activity is allowed. The runner waits for the attempt
   to finish and records main, transient, auxiliary, and final-result models.
3. Fable 5 must re-read, reconcile, validate, and produce the accepted result.
   If the final main model is non-Fable, or final Fable identity cannot be
   verified, outputs are quarantined and all model evidence is saved.
4. The effective prompt is regenerated with a narrow, truthful description of
   the benign engineering task. A fresh Fable 5 session retries once with
   `--safe-mode`, which helps determine whether project customizations caused
   a content-classifier fallback.
5. If the retry also lacks a Fable-produced final result, Claude stops and writes
   `CHATGPT_HANDOFF_REQUIRED`.

Claude Code documents that Fable 5 content-classifier fallback can move
biology requests to Opus 5 and cybersecurity requests to Opus 4.8. It also
notes that first-request workspace context can trigger fallback and recommends
`claude --safe-mode` when diagnosing customizations:
https://code.claude.com/docs/en/model-config

No automatic alternate-provider execution is permitted.

## Explicit user-authorized Claude retry after handoff

`CHATGPT_HANDOFF_REQUIRED` remains a stop state by default. If the user later
confirms that Claude should be tried again, the
`-RetryClaudeAfterHandoff` switch:

1. archives the existing handoff evidence;
2. opens a new numbered retry cycle;
3. starts a fresh session on the same stage and requested model/effort;
4. applies the same first/second Fable-final-result policy within that cycle.

The rejected Claude session is not resumed. Attempt numbers increase globally,
while `retry_cycle` and `cycle_attempt` identify the integrity cycle.

For a non-Fable stage, a user-authorized retry is a single normal Claude
attempt unless it ends for a runtime or validation reason. Auxiliary-model
selection remains flexible.

## Manual ChatGPT Windows continuation

- Sonnet/High → GPT-5.6 Sol/High
- Sonnet/Extra High → GPT-5.6 Sol/Extra High
- Fable/Extra High → GPT-5.6 Sol/Max
- If Max is unavailable → GPT-5.6 Sol/Extra High, logged as a substitution

The mapping is a recovery choice, not an automated runtime route.
