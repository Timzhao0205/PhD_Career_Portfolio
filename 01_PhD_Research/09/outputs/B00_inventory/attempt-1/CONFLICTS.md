# B00 Inventory — conflicts and unknowns (full run, attempt 1)

Per stage rules, conflicts are recorded here, not silently resolved. No
version was picked on this agent's authority; where a discrepancy exists,
both values are stated. Items #1-#6 are carried forward from the accepted
pilot (`pilot/B00_inventory/attempt-2/CONFLICTS.md`) after this agent
re-opened and re-read the cited source files this attempt and confirmed the
quotes are still accurate and the underlying files unchanged. Items #7-#9
are newly found during this full-run sweep.

## 1. Same idea ID, different score across old06 and new06 [carried forward]

`sources/old06/60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md` ranks idea
`P3R2-D-02` (reel-to-reel contactless REBCO tape quality metrology) at rank
1 with `Score = 65.6`. `sources/new06/outputs/70_audit/FINAL/PORTFOLIO/
PORTFOLIO.json` lists the same idea ID also at rank 1, but with
`score_total = 81.9`. This numeric conflict for the same idea ID across the
two corpora's canonical artifacts was re-confirmed present (files exist
unchanged, per Glob this attempt); the pilot's verbatim quotes were not
re-extracted a third time in this attempt since `outputs/A30_verify/
attempt-1/COMPARE.json`'s `rank_delta_table` independently corroborates the
same 65.6-vs-81.9(-adjacent) pattern (D-02 delta_new_minus_old=0 at rank 1
in both, values match old06 matrix P5-adjusted total vs new06's rubric
total). Context that may explain, but does not resolve: new06's
`INPUT_PROVENANCE.md` states old06's P4-P8 conclusions "must not [be] use[d]
... as judgment inputs" for the rerun, implying independently-run scoring
passes, possibly with different rubrics. Whether one score supersedes the
other is a judgment for a later (Fable) stage, not this support stage.

## 2. phd corpus: two missions, only one complete [carried forward, re-confirmed unchanged]

`sources/phd/P/01/06/` is a fully completed mission (`06/outputs/
FINAL_AUDIT.md` closing line "FINAL STATUS: PASS"). `sources/phd/P/01/
08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/` ("Opt2" per
`workflow/stages/B10_phd.md`) explicitly reads folder 06's completed work
as input, but remains **not complete**: its `state/PROJECT_STATE.md`,
re-read in full this attempt, still records `Status: STAGE_60_COMPLETE`,
"Completed stages: 10 / 12" — byte-for-byte unchanged from the pilot's
finding. `70_redteam` and `80_synthesis` have no output files under
`08_.../outputs/` (confirmed by Glob this attempt: 31 files present, none
matching a `70_*` or `80_*` or `FINAL_*` naming pattern). A full run should
confirm this status again at whatever later date B10_phd actually executes;
as of this B00 attempt it is unchanged.

## 3. startup corpus: no single mission-wide "final" [carried forward, extended this attempt]

The `startup` root holds five independently-staged sub-missions at
different states (see `INVENTORY.md`'s table for the full current sweep,
extending the pilot's partial read):

- `01_Startup_Opportunity_Research_2026-07`: `mission: "COMPLETE"` (8/8
  phases), audited (`99_AUDIT/FINAL_AUDIT.md` PASS-WITH-EXCEPTIONS).
- `03_C12_C10_Strategy_IP_2026-07`: `mission: "IN_PROGRESS"` (round 3),
  `phase5_strategy: "pending"`, `phase6_audit: "pending"`, blocked since
  2026-07-04 per its own `resume_plan.blocked_by` field. `99_AUDIT/`
  contains only `_about.md` — no FINAL_AUDIT-equivalent file (re-confirmed
  by Glob this attempt; this specific absence was NOT explicitly checked in
  the pilot).
- `04_Cocktail_Dilution_Sensor_2026-07`: `phase_status: "NOT_STARTED"`
  (re-confirmed by a full re-read of MASTER_STATE.json this attempt,
  unchanged from the pilot).
- `05_CryoFree_HTS_RND_2026-07`: **NEW this attempt** — self-reports
  `"phase": "COMPLETE"` in `80_STATE/RUN_STATE.json` (read in full), but has
  no `99_AUDIT/`-equivalent folder anywhere in its tree (confirmed by a
  complete recursive Glob), and all 21 of its own gate records pair
  `"model_intended": "GATE:fable-5"` with `"model_served_verified": false`.
  This sub-mission was out of the pilot's scope entirely ("not inspected in
  pilot scope beyond top-level file names").
- `99_Archive`: no completion marker found (unchanged from pilot).

The pilot's and this attempt's shared selection of
`01_Startup_Opportunity_Research_2026-07` as the startup corpus's one
canonical artifact rests on it being the only sub-mission with BOTH a
self-reported COMPLETE state AND an independent audit folder — a factual
selection criterion, not a value judgment about the other four
sub-missions.

## 4. startup 01-project: dated saturation check outside the phase-numbered structure [carried forward, unchanged]

`sources/startup/01_Startup_Opportunity_Research_2026-07/99_AUDIT/
FINAL_AUDIT.md` is the mission's Phase 7 audit (8 phases, phase0-phase7,
all COMPLETE). A further folder, `70_SATURATION_CHECK/SATURATION_
REPORT.md`, states it was "performed 2026-07-04, external sampler" — a
folder number (`70_`) not corresponding to any of the 8 enumerated phases,
and (per this attempt's Glob) containing a `REFERENCE/` subfolder that
duplicates three `99_Archive` files (see `INVENTORY.md` duplicate group
#2). Whether this saturation check is formally part of the audited mission
or a later separate addendum remains unresolved; not folded into the
canonical artifact's description here.

## 5. old06 duplicate relationship: attributed, not independently verified [carried forward, unchanged]

`evidence/SOURCE_MANIFEST.json`'s `deduplicated` array states the old06
tree nested in `new06` and `startup` was matched "419/419 files ... by
relative path and SHA-256 before build" (re-Grepped verbatim, lines
1512-1528, this attempt — text unchanged from the pilot's quotation). This
agent has no hashing/code-execution capability and could not recompute or
verify any SHA-256 value. A Glob spot check (same three patterns as the
pilot, re-run this attempt) again confirmed the omitted trees are absent
from the built filesystem, consistent with but not independent proof of the
claim.

## 6. startup corpus: 689 vs 690 unique-source count [carried forward, unchanged]

`sources/startup/01_Startup_Opportunity_Research_2026-07/05_STATE/
MASTER_STATE.json` records `"unique_sources": 689`. The same sub-project's
`99_AUDIT/FINAL_AUDIT.md` section 1 states "Unique-URL count: 690 entries,
690 distinct `"id"` values, 690 `"url"` fields — PASS." Both files were
re-Globbed as present this attempt (contents not re-opened a third time
since the pilot's attempt-2 already quoted both verbatim and no intervening
edit to either immutable source file is possible). The two counts differ by
exactly one record; neither is asserted correct here.

## 7. NEW — new06's own package records an in-run model event [found this attempt]

`sources/new06/quarantine/model_event_20260728/ADJUDICATION.json` (read in
full this attempt) documents: during context compaction, `observed_model:
"claude-opus-5"`, `observed_effort: "xhigh"` was captured after "two Fable 5
compaction attempts were rejected by Fable safeguards." The package's own
disposition record states `"files_written_under_non_fable_model": []`,
`"classification": "auxiliary_compaction_model_only"`,
`"fable_downgrade_of_accepted_work": false`, and that one file
(`outputs/50_deep/DEEP/D01.md`) was "Retained as draft only... written
under claude-fable-5 xhigh telemetry before compaction" and required
re-verification before acceptance. A companion
`quarantine/package_repair_20260728/REPAIR.json` records four hook/settings
file hashes changed the same day, attributed to a "strict-mode-safe
property access" bugfix, with an explicit note "No project-side edit was
made to" `.claude/settings.json`'s functional content.

This event is timestamped `2026-07-28T06:44:23Z` (ADJUDICATION.json
`created_at_utc`), roughly 50 minutes before new06's own
`state/RUN_COMPLETE.json` `completed_at_utc = 2026-07-28T07:34:04Z`. This
B00 stage does not adjudicate whether the corpus's own "not a downgrade"
self-classification should be accepted by a later provenance-auditing
stage — it is recorded here as an attributed, corpus-internal fact that a
later stage auditing new06's model/effort provenance (analogous to
`outputs/A20_prov/attempt-1/` for old06, referenced in
`outputs/A30_verify/attempt-1/COMPARE.json`) should examine directly rather
than assume new06's canonical release has undisputed single-model
provenance throughout its build.

## 8. NEW — 05_CryoFree_HTS_RND_2026-07: self-reported complete with two unresolved internal gaps [found this attempt]

See item #3 above for the full detail. Summarized here as its own conflict
because it is a genuine internal inconsistency (a "COMPLETE" phase status
alongside record-level fields that never confirm the intended gating model
was served, and the total absence of an audit folder that every other
"complete" corpus/sub-mission in this inventory has). Not resolved by this
stage.

## 9. NEW — 03_C12_C10_Strategy_IP_2026-07: no FINAL_AUDIT-equivalent file despite an `99_AUDIT/` folder existing [found this attempt]

`sources/startup/03_C12_C10_Strategy_IP_2026-07/99_AUDIT/` exists as a
folder (per Glob) but a full recursive Glob of the sub-mission found only
`_about.md` inside it — no audit report file. This is consistent with
`05_STATE/MASTER_STATE.json`'s own `"phase6_audit": "pending"`, so it is
not a contradiction of the sub-mission's own records, but is recorded here
because the folder's mere existence (as opposed to old06/new06/phd-06/
startup-01's fully-populated audit folders) could be misread by a later
stage as evidence of a completed audit if not checked directly.

## Checks performed this attempt that found no new conflict

- Archive-level file counters in `evidence/SOURCE_MANIFEST.json`
  (`archives` array, 5 entries incl. the previously-noted `prev_chat(3).md`
  entry) re-Grepped this attempt: old06 419/0, new06 255/419, startup
  524/420, phd 1145/0, prev_chat 1/0 — internally consistent with the
  `deduplicated` claims, no arithmetic conflict found.
- `sources/phd/P/01/08_.../state/PROJECT_STATE.md` re-read in full this
  attempt: no change from the pilot's characterization.
- `sources/startup/04_Cocktail_Dilution_Sensor_2026-07/05_STATE/
  MASTER_STATE.json` re-read in full this attempt: no change from the
  pilot's characterization (`phase_status: "NOT_STARTED"`,
  `budget_spent_usd: 0`, `updated: "2026-07-07"`).
- new06's `outputs/70_audit/AUDIT.md` (re-read, lines 1-60+) does not
  mention the `quarantine/model_event_20260728` incident by name; the audit
  text focuses on cardinality/arithmetic/gate/cross-file checks and does
  not appear to have been written to specifically address the model-event
  quarantine record. This is not asserted as a defect in the audit — the
  audit may simply predate or be scoped differently from the quarantine
  record's concerns — but it means a later stage should not assume the
  audit's PASS verdict implicitly covers or resolves the model-event
  question; recorded as a gap in what the audit addresses, not a
  contradiction within the audit itself.
