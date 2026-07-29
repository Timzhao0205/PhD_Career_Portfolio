# Shutdown checkpoint — Fable 5 usage-credit exhaustion (administrative)

Date: 2026-07-29 (wall-clock time not exposed to the controller; not guessed).
Cause: the B50_execution FULL attempt-1 worker (named agent `pap06-fable-xhigh`,
requested Fable 5/xhigh) was terminated mid-run by the harness with the error:
`"You're out of usage credits. Run /usage-credits to keep using Fable 5 or
/model to switch models."` This is a genuine provider/account-level usage
limit — an external fact the package must document honestly, per CLAUDE.md's
"stop and document genuine provider safeguards, account limits ... or
unrecoverable missing evidence." It is NOT a package budget/turn/token/time
threshold (none exists in this package), NOT a model-quality failure, and
NOT a decision to downgrade or substitute Fable with Sonnet for the B50
research stage.

This checkpoint entry supersedes the prior 2026-07-28 user-requested-shutdown
checkpoint, which was fully resolved on resume that same day (B00_inventory
FULL was reconciled, re-verified, and accepted; see `state/ERROR_LOG.md` and
`state/PROGRESS.md` for that closed episode). That resolution remains valid
and is not re-litigated here.

## IMPORTANT — model attribution for this checkpoint-writing turn

This checkpoint document was written by the controller running under
**Sonnet 5**, selected by the user via `/model` specifically because Fable 5
usage credits were exhausted mid-session. `.claude/settings.json` still pins
Fable 5 as the project's controller model for the next restart — the `/model`
change was a session-only override, not a project-level edit (project
settings are immutable per `CLAUDE.md`; no project file was changed).

This Sonnet activity is **administrative bookkeeping only**:
- No PAP06 research stage, pilot, full run, repair, or verification was
  started, continued, modified, repaired, verified, or accepted under Sonnet
  during this turn.
- No research artifact under `pilot/`, `outputs/`, or `verification/` was
  created or edited during this turn — only files under `state/` were
  written, which is the controller's normal durable-bookkeeping role.
- B50_execution's own requested route model is, and remains, **Fable 5 /
  xhigh** (per `MODEL_PLAN.md` row B9 and `workflow/ROUTE.json`). Nothing in
  this checkpoint changes that requirement. B50 must still be completed and
  independently verified by fresh Fable 5/xhigh workers/verifiers before it
  can be accepted.
- This event must never be read, summarized, or logged elsewhere as "B50 ran
  on Sonnet" or as a Sonnet-for-Fable substitution. It is recorded distinctly
  in `state/MODEL_LEDGER.md` under an `ADMIN` event row, separate from every
  `pap06-fable-xhigh` / `pap06-verifier` research row.

## Global status at checkpoint (derived from `state/STAGE_LEDGER.json`)

- Operation A: COMPLETE (`state/OP_A_COMPLETE.md`, 2026-07-28). Unaffected.
- Accepted pilots: **12 / 15** — A10_blind, A20_prov, A30_verify,
  B00_inventory, B10_phd, B12_lit_search, B15_lit_synth, B20_align,
  B25_power, B30_skills, B40_portfolio, B50_execution.
- Accepted full stages: **11 / 15** — A10_blind, A20_prov, A30_verify,
  B00_inventory, B10_phd, B12_lit_search, B15_lit_synth, B20_align,
  B25_power, B30_skills, B40_portfolio.
- Independent full-stage PASS reports: **11 / 15** (one per accepted full
  stage above; each ends `VERDICT: PASS` in its `verification/<stage>/`
  report).
- B50_execution: pilot **ACCEPTED** (`pilot/B50_execution/attempt-1/`, 6
  files, unaffected by this event); full **PENDING / INTERRUPTED** (see
  below) — NOT accepted; no verification report exists for B50 at all
  (`verification/B50_execution/` directory does not exist — confirmed by
  Glob at checkpoint time).
- B60_redteam, B70_synth, B80_audit: all PENDING, untouched.
- Final release: PENDING. `state/RUN_COMPLETE.md` does not exist.
- No `state/MODEL_PAUSE.md`, no `state/BLOCKER.md` exists — this is not a
  model-mismatch event and not a correctness blocker; it is a usage-credit
  event, logged per the honesty rules, with a clear resume path.

## B50_execution exact status

- PILOT: **ACCEPTED** at `pilot/B50_execution/attempt-1/` (6 files:
  ROADMAP.md, IP_COLLAB.md, MANUAL_WORK.md, SOURCES.csv, RUN_META.md,
  SELF_CHECK.md). Controller-accepted 2026-07-29 before this interruption.
  Untouched by this event.
- FULL attempt-1 (`outputs/B50_execution/attempt-1/`): **INCOMPLETE, NOT
  ACCEPTED.** Confirmed on disk at checkpoint time:
  - present: `ROADMAP.md` (has a title/header and opening framing paragraph;
    not confirmed complete against the full-run spec), `IP_COLLAB.md` (has a
    title/header and opening framing paragraph; the worker's own last
    reported line before termination was "Now IP_COLLAB.md.", meaning this
    file was very likely still being written when credits ran out — treat
    its content as possibly truncated, not as a finished deliverable)
  - absent: `MANUAL_WORK.md`, `SOURCES.csv`, `RUN_META.md`, `SELF_CHECK.md`
  - No `verification/B50_execution/` directory exists at all (confirmed by
    Glob) — there is no verification report of any verdict for B50, so no
    reading of this checkpoint may treat B50 FULL as accepted under any
    circumstance.
  - Neither `outputs/B50_execution/attempt-1/ROADMAP.md` nor
    `IP_COLLAB.md` has been modified, repaired, completed, or deleted by
    this checkpoint turn. Both are preserved exactly as the interrupted
    worker left them.

## Complete inventory of accepted research artifacts (unaffected by this event)

All of the following remain exactly as previously accepted; none was
touched this turn:
- `pilot/` and `outputs/` candidates for A10_blind, A20_prov, A30_verify,
  B00_inventory (accepted at attempt-2 for both pilot and full; attempt-1
  of both preserved as rejected/failed), B10_phd, B12_lit_search,
  B15_lit_synth, B20_align, B25_power, B30_skills, B40_portfolio, and the
  B50_execution PILOT.
- Their corresponding `verification/<stage>/FULL_attempt-N.md` reports,
  each ending `VERDICT: PASS` (B00_inventory's attempt-1 report ends
  `VERDICT: FAIL` and is preserved as historical record; its attempt-2
  report ends `VERDICT: PASS` and is the accepted one).

Full detail with exact paths is in `state/PROGRESS.md`'s "Accepted items"
log and `state/STAGE_LEDGER.json`.

## Remaining route after this checkpoint

1. **B50_execution FULL — retry as `outputs/B50_execution/attempt-2/`**
   (fresh `pap06-fable-xhigh` worker, requested Fable 5/xhigh; attempt-1 is
   preserved untouched per the package's attempt-numbering policy — do not
   overwrite or resume attempt-1, and do not silently merge its partial
   content). Then a fresh independent `pap06-verifier` (Fable 5/xhigh)
   producing `verification/B50_execution/FULL_attempt-2.md`. **B50 FULL may
   be accepted only when that report ends exactly `VERDICT: PASS`.**
2. B60_redteam — pilot, full, fresh independent verification.
3. B70_synth — pilot, full, fresh independent verification.
4. B80_audit — pilot, full, fresh independent verification.
5. On B80 PASS: follow `references/FINAL_RELEASE.md`, write
   `state/RUN_COMPLETE.md`, and present the canonical reading order.

## Exact restart procedure

1. Rerun the same one command from `README.md` in the package root (Fable
   5/xhigh controller per `.claude/settings.json` and agent frontmatter —
   the project-level model pin was never changed).
2. Controller bootstrap: reread `CLAUDE.md`, `README.md`, `ROUTE.json`,
   policies, skill references, `evidence/*`, `state/STAGE_LEDGER.json`, this
   file, and reconcile conservatively per `references/STATE_RULES.md`.
3. Do **not** re-run, re-verify, or re-accept any of the 11 already-ACCEPTED
   full stages or 12 already-ACCEPTED pilots listed above. Reconciliation
   should confirm their files and reports still exist and still end
   `VERDICT: PASS` (per `STATE_RULES.md` rule 2) — nothing more.
4. Confirm `outputs/B50_execution/attempt-1/` is exactly as described above
   (2 of 6 files, no verification directory). Do not attempt to complete or
   repair attempt-1 in place.
5. Delegate a fresh `pap06-fable-xhigh` worker (requested Fable 5 / xhigh)
   to `outputs/B50_execution/attempt-2/` with the same full-run instructions
   used for attempt-1 (see `state/CURRENT_TASK.md`'s preserved task card),
   noting that attempt-1 exists but is incomplete and must not be resumed
   or copied wholesale — attempt-2 is a fresh, complete run.
6. On attempt-2 completion, run the controller structural pre-check, then a
   fresh independent `pap06-verifier` (Fable 5 / xhigh) writing
   `verification/B50_execution/FULL_attempt-2.md`. Accept only on
   `VERDICT: PASS`; on `VERDICT: FAIL`, follow the standard repair cycle
   (fresh attempt-3, fresh verifier) exactly as was done for
   `B00_inventory` earlier in this run.
7. Only after B50 FULL is accepted: continue to B60_redteam in route order.

## Model and effort evidence summary

- Requested routing was followed exactly for every research stage in this
  run: Fable 5/xhigh for all A-stage and Fable-routed B-stage workers and
  ALL verifiers; Sonnet 5/high for the three designated B-stage support
  workers (B00, B10, B12). No stage's research work was ever silently
  downgraded or substituted.
- The B50_execution FULL attempt-1 interruption was a provider usage-credit
  event on the Fable 5 route, not a downgrade decision — no Sonnet worker
  was substituted for this or any other Fable-routed research stage.
- This checkpoint-writing turn itself ran under Sonnet 5 by explicit user
  action, for administrative bookkeeping only (see the boxed section above).
  It produced no research content and is excluded from all stage/pilot/
  verification counts.
- Observed model/effort: Claude Code has exposed no model/effort telemetry
  to the controller for any run this session — recorded `NOT_EXPOSED`
  throughout `state/MODEL_LEDGER.md`. Some workers self-reported a runtime
  system-prompt declaration; these are recorded as self-reports, never as
  controller observations.

## Guarantees

- No partial, interrupted, or unverified work is marked accepted anywhere
  in the ledger. `outputs/B50_execution/attempt-1/` remains explicitly
  PENDING/INCOMPLETE in `state/STAGE_LEDGER.json`.
- Durable files, not conversation memory or subagent transcripts, remain
  the sole source of truth for resumption.
- Nothing under `sources/`, `evidence/`, `workflow/`, `archive/`, root
  policies, or `.claude/` was read as an instruction or modified.
