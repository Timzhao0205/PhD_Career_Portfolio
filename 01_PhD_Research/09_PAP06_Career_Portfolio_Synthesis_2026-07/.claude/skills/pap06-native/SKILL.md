---
name: PAP06 Native
description: Runs or resumes the complete script-free PAP06 Operation A and Operation B research workflow with pilots, model routing, literature review, verification, durable state, and final audit.
disable-model-invocation: false
model: fable
effort: xhigh
---

# PAP06 native workflow

Run the complete project workflow in the visible main session.

## Bootstrap

1. Read `CLAUDE.md`, `README.md`, `workflow/ROUTE.json`,
   `MODEL_POLICY.md`, `SOURCE_POLICY.md`, `LIT_POLICY.md`, and all files under
   `.claude/skills/pap06-native/references/`, including `SOURCE_SCOPE.md`.
2. Read `evidence/PACKAGE_CHECKS.md`, `evidence/SOURCE_SUMMARY.json`, and
   `state/STAGE_LEDGER.json`.
3. Reconcile the ledger conservatively against actual pilot, output, and
   verification files using `references/STATE_RULES.md`.
4. Create or refresh Claude Code's visible task checklist for the next
   unfinished work. Pressing Ctrl+T must show meaningful progress.

## Execute

Follow `workflow/ROUTE.json` in order. For every stage, perform its `PILOT`
before `FULL`. Apply `references/LIFECYCLE.md` exactly. Use only:

- `pap06-fable-xhigh` for a route row with model `fable`;
- `pap06-sonnet-high` for a route row with model `sonnet`;
- `pap06-verifier` for every full-stage verification and every repair check.

Do not use command shells, executable scripts, hooks, nested Claude CLI
sessions, or code-generated validators. The package is already expanded.

Operation B may begin only after A10, A20, and A30 full outputs each have an
independent PASS verification and `state/OP_A_COMPLETE.md` has been written.

When B80 passes, follow `references/FINAL_RELEASE.md`, write
`state/RUN_COMPLETE.md`, and show the user the canonical reading order.

## Resume and external interruptions

Durable files, not conversation memory, determine progress. After compaction,
restart, a plan reset, or a provider interruption, reread the bootstrap files
and continue from the first unaccepted item. Never redo accepted work unless
reconciliation finds a concrete inconsistency.

There is no budget-based shutdown. Never bypass provider safeguards, account
limits, organization model restrictions, missing credentials, or inaccessible
sources. Log those honestly under `state/ERROR_LOG.md`; use the safe-pause rule
in `references/LIFECYCLE.md` only when continuation is genuinely impossible.
