# PILOT SAMPLE — NOT FINAL

# B00 Inventory — conflicts and unknowns (pilot scope, attempt 2, repair)

Per stage rules, conflicts are recorded here, not silently resolved. No
version was picked on the agent's authority; where a discrepancy exists,
both values are stated. This is a repair of attempt-1 (rejected solely for
a missing `RUN_META.md` banner). Items #1-#5 below are carried forward
from attempt-1 after this agent re-opened and re-read every cited source
file and confirmed the quotes are accurate. Item #6 is newly found during
this attempt's re-verification.

## 1. Same idea ID, different score across old06 and new06

`sources/old06/60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md` ranks idea
`P3R2-D-02` (reel-to-reel contactless REBCO tape quality metrology) as
rank 1 with `Score = 65.6`. `sources/new06/outputs/70_audit/FINAL/
PORTFOLIO/PORTFOLIO.json` lists the same idea ID `P3R2-D-02` also at rank
1, but with `score_total = 81.9`. This is a real numeric conflict for the
same idea ID across the two corpora's canonical artifacts, re-confirmed by
this attempt via direct Grep/read of both files: the executive-portfolio
markdown table row (`| 1 | P3R2-D-02 | ... | 65.6 | evidence-rich |`) and
the PORTFOLIO.json item (`"idea_id": "P3R2-D-02", "rank": 1, ...
"score_total": 81.9`) were both re-opened and both values match attempt-1
exactly.

Context that may explain (but does not resolve) the discrepancy:
`sources/new06/INPUT_PROVENANCE.md` states the historical old06 P4-P8
conclusions "are preserved for provenance and later comparison, but the
new rerun must not use their conclusions as judgment inputs," implying
the two scores come from independently-run scoring passes with possibly
different rubrics/weights (new06's `outputs/70_audit/AUDIT.md` section 2
describes an 11-criterion, weighted 16/15/10/9/9/11/7/10/8/3/2 rubric
re-derived for all 65 ideas — no equivalent rubric text was read for
old06 in pilot scope). Whether the rubrics are the same, different, or
whether one score supersedes the other is a judgment for a later stage,
not this pilot.

## 2. phd corpus: two "06"-numbered/adjacent missions, only one complete

`sources/phd/P/01/06/` is a fully completed mission
(`06/outputs/FINAL_AUDIT.md`: closing line "FINAL STATUS: PASS", re-read
in this attempt). A separate, newer sibling mission,
`sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/`,
explicitly reads folder `06`'s completed work as input (per
`P/01/README_HYBRID_RADIATION_ANALYSIS.md`) but was **not** complete at
pilot time: its own `08_.../state/PROJECT_STATE.md` records
`Status: STAGE_60_COMPLETE`, "Completed stages: 10 / 12," with stage
`70_redteam` still pending. This is not a contradiction so much as an
incompleteness that the pilot records explicitly rather than silently
treating folder 08 as final: the pilot selected folder 06's
`FINAL_EXECUTIVE_STRATEGY.md` as the phd corpus's one canonical artifact
precisely because folder 08 is unfinished. A full run should confirm
whether folder 08 has since completed and, if so, how its conclusions
relate to (supersede, extend, or coexist with) folder 06's.

## 3. startup corpus: no single mission-wide "final," multiple sub-project states

The `startup` root does not have one corpus-wide final artifact the way
old06/new06/phd do; it holds several independently-staged sub-projects at
different states, per each sub-project's own `05_STATE/MASTER_STATE.json`:

- `01_Startup_Opportunity_Research_2026-07`: `mission: "COMPLETE"` (all 8
  phases complete).
- `03_C12_C10_Strategy_IP_2026-07`: `mission: "IN_PROGRESS"` (round 3;
  `phase5_strategy: "pending"`, `phase6_audit: "pending"`).
- `04_Cocktail_Dilution_Sensor_2026-07`: `phase_status: "NOT_STARTED"`
  (`budget_spent_usd: 0`).
- `05_CryoFree_HTS_RND_2026-07`: state file not read in pilot scope
  (out of scope — no completion status recorded here; not assumed).
- `99_Archive`: legacy notes predating the staged missions; no
  MASTER_STATE.json-style completion marker was located for it in pilot
  scope.

The pilot selected `01_Startup_Opportunity_Research_2026-07`'s phase-6
synthesis as the startup corpus's one canonical artifact because it is
the only sub-project with a recorded COMPLETE mission state and a PASS
(-with-exceptions) final audit among those inspected. This is a pilot-
scope selection among unequal candidates, not a claim that the other
sub-projects lack value — the full run should inventory each sub-project
individually rather than treat one as representative of the whole root.

## 4. startup 01-project: a dated saturation check outside the phase-numbered structure

`sources/startup/01_Startup_Opportunity_Research_2026-07/99_AUDIT/
FINAL_AUDIT.md` is the mission's Phase 7 audit (mission phases
`phase0_init` through `phase7_audit`, all COMPLETE per MASTER_STATE.json).
A further folder, `70_SATURATION_CHECK/SATURATION_REPORT.md`, states it
was "performed 2026-07-04, external sampler" — a date that precedes some
phase-numbered content's own dating conventions elsewhere in the corpus
and uses a folder number (`70_`) that does not correspond to a phase
already enumerated in MASTER_STATE.json's 8-phase list. The pilot did not
determine whether this saturation check is formally part of the audited
mission or a later, separate addendum; it is flagged as an unresolved
structural/date question rather than folded into the canonical artifact's
description.

## 5. Old06 duplicate relationship: attributed, not independently verified

`evidence/SOURCE_MANIFEST.json`'s `deduplicated` section states the
old06 tree nested in `new06` and `startup` was matched "419/419 files ...
by relative path and SHA-256 before build." This agent has no
hashing/code-execution capability and could not recompute or verify any
SHA-256 value. A Glob spot check, re-run in this attempt with the same
three patterns, again confirmed the omitted trees are absent from the
built filesystem (consistent with the claim), but this is not independent
proof of byte-for-byte identity. Recorded as an attributed claim, not a
verified fact, per stage evidence rules.

## 6. [NEW — found during attempt-2 re-verification] startup corpus: 689 vs 690 unique-source count

`sources/startup/01_Startup_Opportunity_Research_2026-07/05_STATE/
MASTER_STATE.json` records `"unique_sources": 689`. The same sub-project's
own `99_AUDIT/FINAL_AUDIT.md` section 1 ("Bibliography integrity"), states:
"**Unique-URL count:** 690 entries, 690 distinct `"id"` values, 690
`"url"` fields — **PASS**." Both files were re-opened and re-read in full
(MASTER_STATE.json) or in relevant part (FINAL_AUDIT.md section 1) during
this attempt's re-verification pass. The two counts differ by exactly one
record. Attempt-1 quoted only the MASTER_STATE.json figure (689) in
`INPUT_MAP.json`'s startup `basic_facts_as_recorded` and did not surface
this discrepancy. Neither value is asserted here as correct; both are
recorded. Possible explanations not investigated in pilot scope: the
audit's count may include one record added or corrected after
MASTER_STATE.json's counter was last updated, or one of the two counting
methods may include/exclude a boundary record differently. This is a
one-record numeric conflict, not evidence of a broader counting error;
flagged for the full run to reconcile.

## Checks performed that found no conflict

- Archive-level file counters in `evidence/SOURCE_MANIFEST.json`
  (`archives` array) are internally consistent with the `deduplicated`
  claims: old06 `skipped_duplicate_files: 0`; new06
  `skipped_duplicate_files: 419`; startup `skipped_duplicate_files: 420`
  (419 + 1 redundant nested zip member). Re-Grepped in this attempt; no
  arithmetic conflict found, and a fourth archive entry
  (`prev_chat(3).md`, `included_files: 1`, `skipped_duplicate_files: 0`)
  not previously cited by attempt-1 was also checked and is consistent.
- No conflicting canonicity claim was found for the old06, new06, or phd
  canonical artifacts (each corpus's own audit file unambiguously names
  one release as final/PASS) — re-confirmed by re-reading each cited
  audit/state file in this attempt.
- The phd `FINAL_AUDIT.md` "re-run fresh in this stage (2026-07-25, this
  session)" phrase quoted by attempt-1 was re-located verbatim at line 52
  during this attempt's re-verification (an initial 40-line spot-check
  had not reached it); attempt-1's claim stands confirmed, not a
  conflict.
