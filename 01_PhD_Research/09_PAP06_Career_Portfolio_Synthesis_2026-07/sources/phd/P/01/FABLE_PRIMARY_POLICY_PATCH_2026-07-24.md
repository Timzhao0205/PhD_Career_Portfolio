# Fable final-result policy and full restart — 2026-07-24

## Outcome

The Claude-only PowerShell workflow now applies downgrade enforcement only to
stages whose requested main model is Fable 5. Auxiliary model selection is
allowed for every stage, including Fable stages.

For every Fable-assigned critical stage, Fable 5 must be the final main model
that reviews, reconciles, validates, and produces the accepted stage result.
Temporary auxiliary use of Opus, Sonnet, Haiku, or another model is logged but
does not itself cause a pause.

The executable workflow is reset to the beginning:

- completed mission stages: 0 of 12;
- first stage: `00_inventory`;
- first run attempt: 1;
- no saved mission session is resumable;
- prior mission outputs, logs, state, and quarantines are retained under
  `_history\r0` for audit only.

## Evidence behind the policy

Claude Code's official model-configuration documentation says:

- Fable 5 is its most capable model for hard and long-running work;
- Fable 5 safety-classifier fallback sends biology-flagged requests to Opus 5
  and cybersecurity-flagged requests to Opus 4.8;
- after content fallback, the session continues on the fallback model;
- workspace context can trigger fallback on the first request;
- `claude --safe-mode` disables project customizations for diagnosis;
- category-specific fallback requires Claude Code 2.1.219 or newer.

Source: https://code.claude.com/docs/en/model-config

The engineering prompts in this package are benign. Nevertheless, the runner
records a security/content-fallback flag because workspace context can affect
the classifier independently of the immediate prompt.

## Exact acceptance policy

1. Record all model names emitted during every operation.
2. Treat the session initialization and non-subagent assistant messages as
   main-session evidence.
3. Treat subagent messages carrying `parent_tool_use_id` and names found only
   in aggregate `modelUsage` as auxiliary evidence.
4. Allow auxiliary model adjustments without pausing.
5. Do not apply downgrade enforcement to Sonnet-assigned stages.
6. For a Fable-assigned stage, evaluate model integrity only after the attempt
   finishes, so temporary auxiliary changes can return to Fable.
7. Accept the stage only when the final main assistant/result model is Fable 5.
   Auxiliary work is draft/evidence until Fable re-reads and validates it.
8. If the final main model is Opus or another non-Fable model, or final Fable
   identity cannot be verified, quarantine the attempt.
9. On the first such event, regenerate a narrowly scoped engineering prompt
   and retry Fable 5 in a fresh `--safe-mode` session.
10. On the second event, save all progress and prepare the mapped GPT-5.6 Sol
    continuation in ChatGPT Windows.

No Claude-to-Codex call, MCP runtime, or automatic alternate-provider route is
enabled.

## Historical correction

The previous broad detector interpreted Sonnet-plus-Haiku aggregate usage in
stage `10a_literature_gan` as a Sonnet downgrade. The raw streams show Sonnet 5
as the session initialization and direct assistant model, while Haiku appeared
as auxiliary usage. Those records are preserved under `_history\r0`; they are
not active completion evidence and do not affect the clean restart.

## Run

Extract the package to a short path such as `D:\PHD`, open PowerShell in
`D:\PHD\01`, and run:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1
```

The same command resumes from the new durable state after interruption.
