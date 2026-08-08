# Package manifest

## Entry points

- `START.ps1` — one-command begin/resume launcher.
- `PREFLIGHT.ps1` — deterministic validation with no research model call.
- `START_HERE.md` — autonomous orchestration contract.
- `SYSTEM_PROMPT.md` and `CLAUDE.md` — publication scope and safety rules.

## Policy and gates

- `MODEL_PLAN.md`
- `IP_SCOPE.md`
- `SOURCE_POLICY.md`
- `schemas/OUTPUT_GATES.md`

## Inputs

- `inputs/manuscript/submission.pdf`
- `inputs/manuscript/source_original.zip`
- `inputs/manuscript/source/regular_lsens/regular_lsens.tex`
- `inputs/prior_art_seeds.csv`
- `inputs/HASHES.sha256`
- `inputs/context/excluded_archives.csv`

## Native Claude Code configuration

- `.claude/settings.json`
- `.claude/agents/s00-scope.md`
- `.claude/agents/s10-disclosure.md`
- `.claude/agents/s20-prior-art.md`
- `.claude/agents/s30-ip-screen.md`
- `.claude/agents/s40-uhv.md`
- `.claude/agents/s50-arxiv.md`
- `.claude/agents/s60-red-team.md`
- `.claude/agents/s70-final.md`

## State and documentation

- `state/STATE.json`, `state/WORKLOG.md`, `state/MODEL_LOG.csv`
- `state/FALLBACK_LOG.md`, `state/checkpoints`, `state/quarantine`
- `docs/BASELINE_HYPOTHESES.md`, `docs/OTL_QUESTIONS.md`
- `docs/ARXIV_SCRUB.md`, `docs/MODEL_EVIDENCE.md`, `docs/TOOL_SOURCES.md`

Generated research belongs in `outputs`. Runtime diagnostics remain in `state`.
