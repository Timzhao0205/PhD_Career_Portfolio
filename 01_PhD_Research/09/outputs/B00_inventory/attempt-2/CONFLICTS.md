# B00 Inventory — conflicts and unknowns (full run, attempt 2, repair)

Per stage rules, conflicts are recorded here, not silently resolved. No
version was picked on this agent's authority; where a discrepancy exists,
both values are stated. All nine items below were independently reproduced
and verified clean in `verification/B00_inventory/FULL_attempt-1.md`
("all 9 conflicts reproduce verbatim on both sides"). This attempt repairs
one false observed count inside item #2 and one loose phrasing in item #3;
all other content is carried forward unchanged from attempt-1.

## 1. Same idea ID, different score across old06 and new06 [unchanged]

`sources/old06/60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md` ranks idea
`P3R2-D-02` (reel-to-reel contactless REBCO tape quality metrology) at rank
1 with `Score = 65.6`. `sources/new06/outputs/70_audit/FINAL/PORTFOLIO/
PORTFOLIO.json` lists the same idea ID also at rank 1, but with
`score_total = 81.9`. `outputs/A30_verify/attempt-1/COMPARE.json`'s
`rank_delta_table` independently corroborates the same 65.6-vs-81.9(-adjacent)
pattern (D-02 delta_new_minus_old=0 at rank 1 in both, values match old06
matrix P5-adjusted total vs new06's rubric total). Context that may explain,
but does not resolve: new06's `INPUT_PROVENANCE.md` states old06's P4-P8
conclusions "must not [be] use[d] ... as judgment inputs" for the rerun,
implying independently-run scoring passes, possibly with different rubrics.
Whether one score supersedes the other is a judgment for a later (Fable)
stage, not this support stage.

## 2. phd corpus: two missions, only one complete [REPAIRED count]

`sources/phd/P/01/06/` is a fully completed mission (`06/outputs/
FINAL_AUDIT.md` closing line "FINAL STATUS: PASS"). `sources/phd/P/01/
08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/` ("Opt2" per
`workflow/stages/B10_phd.md`) explicitly reads folder 06's completed work
as input, but remains **not complete**: its `state/PROJECT_STATE.md` still
records `Status: STAGE_60_COMPLETE`, "Completed stages: 10 / 12".
`70_redteam` and `80_synthesis` have no output files under
`08_.../outputs/` — **confirmed by a fresh, single, non-truncated Glob this
attempt: 25 files present, none matching a `70_*` or `80_*` or `FINAL_*`
naming pattern.** [REPAIR: attempt-1 asserted "31 files present, confirmed
by Glob" here, which was false against the real tree; the real,
re-Globbed count is 25. This is the sole content change to this conflict
item; the substantive conclusion — no 70_redteam/80_synthesis/FINAL_*
outputs, 10/12 stages complete — is unchanged and correct.] A later Fable
stage should confirm this status again at whatever later date B10_phd
actually executes; as of this B00 attempt it is unchanged from attempt-1's
finding except for the corrected count.

## 3. startup corpus: no single mission-wide "final" [REPAIRED phrasing]

The `startup` root holds five independently-staged sub-missions at
different states (see `INVENTORY.md`'s table for the full current sweep):

- `01_Startup_Opportunity_Research_2026-07`: `mission: "COMPLETE"` (8/8
  phases), audited (`99_AUDIT/FINAL_AUDIT.md` PASS-WITH-EXCEPTIONS).
- `03_C12_C10_Strategy_IP_2026-07`: `mission: "IN_PROGRESS"` (round 3),
  `phase5_strategy: "pending"`, `phase6_audit: "pending"`, blocked since
  2026-07-04 per its own `resume_plan.blocked_by` field. `99_AUDIT/`
  contains only `_about.md` — no FINAL_AUDIT-equivalent file.
- `04_Cocktail_Dilution_Sensor_2026-07`: `phase_status: "NOT_STARTED"`.
- `05_CryoFree_HTS_RND_2026-07`: self-reports `"phase": "COMPLETE"` in
  `80_STATE/RUN_STATE.json` (read in full), but has no
  `99_AUDIT/`-equivalent folder anywhere in its tree (confirmed by a
  complete recursive Glob), and its `gates` object holds **7 records, one
  per candidate (CF-1..CF-7)**, each pairing `"model_intended":
  "GATE:fable-5"` with `"model_served_verified": false` once while covering
  three gate-verdict fields (G-PHYS/G-NOVEL/G-CLAIM) — **7 records, 21 gate
  verdicts total**, re-confirmed by a fresh full read of `RUN_STATE.json`
  this attempt. [REPAIR: attempt-1 said "all 21 of its own gate records",
  overstating the record-level granularity; corrected here. The substantive
  finding — model-service verification is false for every one of the 21
  gate verdicts — is unchanged.]
- `99_Archive`: no completion marker found.

The shared selection of `01_Startup_Opportunity_Research_2026-07` as the
startup corpus's one canonical artifact rests on it being the only
sub-mission with BOTH a self-reported COMPLETE state AND an independent
audit folder — a factual selection criterion, not a value judgment about
the other four sub-missions.

## 4. startup 01-project: dated saturation check outside the phase-numbered structure [unchanged]

`sources/startup/01_Startup_Opportunity_Research_2026-07/99_AUDIT/
FINAL_AUDIT.md` is the mission's Phase 7 audit (8 phases, phase0-phase7,
all COMPLETE). A further folder, `70_SATURATION_CHECK/SATURATION_
REPORT.md`, states it was "performed 2026-07-04, external sampler" — a
folder number (`70_`) not corresponding to any of the 8 enumerated phases,
and containing a `REFERENCE/` subfolder that duplicates three `99_Archive`
files (see `INVENTORY.md` duplicate group #2). Whether this saturation
check is formally part of the audited mission or a later separate addendum
remains unresolved; not folded into the canonical artifact's description
here.

## 5. old06 duplicate relationship: attributed, not independently verified [unchanged]

`evidence/SOURCE_MANIFEST.json`'s `deduplicated` array states the old06
tree nested in `new06` and `startup` was matched "419/419 files ... by
relative path and SHA-256 before build" (lines 1512-1528). This agent has
no hashing/code-execution capability and could not recompute or verify any
SHA-256 value. A Glob spot check (three patterns) again confirmed the
omitted trees are absent from the built filesystem, consistent with but not
independent proof of the claim.

## 6. startup corpus: 689 vs 690 unique-source count [unchanged]

`sources/startup/01_Startup_Opportunity_Research_2026-07/05_STATE/
MASTER_STATE.json` records `"unique_sources": 689`. The same sub-project's
`99_AUDIT/FINAL_AUDIT.md` section 1 states "Unique-URL count: 690 entries,
690 distinct `"id"` values, 690 `"url"` fields — PASS." The two counts
differ by exactly one record; neither is asserted correct here.

## 7. new06's own package records an in-run model event [unchanged]

`sources/new06/quarantine/model_event_20260728/ADJUDICATION.json`
documents: during context compaction, `observed_model: "claude-opus-5"`,
`observed_effort: "xhigh"` was captured after "two Fable 5 compaction
attempts were rejected by Fable safeguards." The package's own disposition
record states `"files_written_under_non_fable_model": []`,
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
later stage auditing new06's model/effort provenance should examine
directly rather than assume new06's canonical release has undisputed
single-model provenance throughout its build.

## 8. 05_CryoFree_HTS_RND_2026-07: self-reported complete with two unresolved internal gaps [phrasing repaired, see #3]

See item #3 above for the full detail, corrected this attempt to "7 records
covering 21 gate verdicts." Summarized here as its own conflict because it
is a genuine internal inconsistency (a "COMPLETE" phase status alongside
record-level fields that never confirm the intended gating model was
served, and the total absence of an audit folder that every other
"complete" corpus/sub-mission in this inventory has). Not resolved by this
stage.

## 9. 03_C12_C10_Strategy_IP_2026-07: no FINAL_AUDIT-equivalent file despite an `99_AUDIT/` folder existing [unchanged]

`sources/startup/03_C12_C10_Strategy_IP_2026-07/99_AUDIT/` exists as a
folder (per Glob) but a full recursive Glob of the sub-mission found only
`_about.md` inside it — no audit report file. This is consistent with
`05_STATE/MASTER_STATE.json`'s own `"phase6_audit": "pending"`, so it is
not a contradiction of the sub-mission's own records, but is recorded here
because the folder's mere existence (as opposed to old06/new06/phd-06/
startup-01's fully-populated audit folders) could be misread by a later
stage as evidence of a completed audit if not checked directly.

## Checks performed this attempt that found no new conflict

- Fresh, non-truncated Globs this attempt confirmed: old06
  `60_FINAL_PORTFOLIO/` = 8 files (7 named + `_about.md`); old06
  `40_DEEP_DIVES/` = 10 `DD_*.md` reports; new06
  `outputs/70_audit/FINAL/DEEP/` = D01-D10 (10 files); startup/01
  `40_PHASE4_DEEPDIVES/` = 12 `DD_C*.md` deep dives; startup/03
  `50_INVENTIONS/` = 14 `ID_*` + 14 `IPRT_*` files; startup/03
  `30_PATENTS/` = 10 `PL_P*` clusters; startup/03 `10_COMPETITORS/` = 8
  `CS_*` profiles; phd/06 `outputs/` = 31 content files + `.gitkeep`;
  phd/08 full subtree = 205 files (truncation notice at 100 confirms
  total); phd/08 `prompts/` = 13 files incl. `_shared_system.md`. None of
  these spot re-checks found a discrepancy from attempt-1's figures.
- Archive-level file counters in `evidence/SOURCE_MANIFEST.json`
  (`archives` array, 5 entries incl. the previously-noted `prev_chat(3).md`
  entry): old06 419/0, new06 255/419, startup 524/420, phd 1145/0,
  prev_chat 1/0 — internally consistent with the `deduplicated` claims, no
  arithmetic conflict found (attributed to the manifest, not independently
  recomputed).
- new06's `outputs/70_audit/AUDIT.md` does not mention the
  `quarantine/model_event_20260728` incident by name; the audit text
  focuses on cardinality/arithmetic/gate/cross-file checks. This is not
  asserted as a defect in the audit — it means a later stage should not
  assume the audit's PASS verdict implicitly covers or resolves the
  model-event question; recorded as a gap in what the audit addresses, not
  a contradiction within the audit itself.

## New count discrepancy found during this repair's fresh-Glob sweep (disclosed, not a source-corpus conflict)

A fresh, single, non-truncated recursive Glob of
`sources/startup/05_CryoFree_HTS_RND_2026-07/**` this attempt returns
exactly **80 files**, cross-validated by four independent sub-Globs summing
to the same total (root 6; `60_PRIOR_ART/**` 22; `20_SIM/**` 16;
`_claude_source/**` 11; plus `40_PROTOTYPE` 1, `30_IDEATION` 1,
`10_MISSION` 3, `80_STATE` 4, `tools` 1, `98_CLAUDE_METRICS` 5,
`70_DISCLOSURES` 7, `90_SOURCES` 3 = 80). This is this agent's own directly
observed figure for the tree AS IT EXISTS NOW, not a conflict between two
corpus source files. It is recorded here for transparency because it
differs from two other prior counts of the SAME static, immutable tree:
attempt-1's own "~90 results" estimate, and the independent verifier's
stated "83 files" in `verification/B00_inventory/FULL_attempt-1.md`'s
Defect 5 discussion. Since `sources/` is immutable and none of the three
counting sessions reported a truncation/cap notice, the most likely
explanation is a counting-methodology difference (e.g., whether a specific
subfolder was included) rather than a change in the underlying files; this
agent cannot determine which of 80/83/~90 the other two sessions actually
computed from, only that its own fresh, cross-validated count this attempt
is 80. Flagged for a future verifier to re-derive independently rather than
silently reconciled toward either prior figure.
