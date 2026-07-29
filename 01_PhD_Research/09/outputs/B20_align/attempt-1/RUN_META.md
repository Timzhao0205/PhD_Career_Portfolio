# RUN_META — B20_align (FULL)

- Stage: `B20_align`
- Mode: `FULL`
- Attempt: `1`
- Target directory: `outputs/B20_align/attempt-1/`
- Named agent: `pap06-fable-xhigh`
- Requested model: Fable 5
- Requested effort: xhigh
- Observed model: the runtime system prompt self-identifies as "Fable 5"
  (model ID string `claude-fable-5`). This is a self-declaration visible to
  the worker, not an independently verifiable runtime observation; recorded
  as such and kept separate from the requested-model line above.
- Observed effort: NOT_EXPOSED
- Start/end times: exact clock times NOT_EXPOSED; run date 2026-07-28
  (single continuous fresh-context session).

## Prerequisite inputs read (in order)

1. `state/CURRENT_TASK.md`
2. `workflow/stages/B20_align.md`
3. `SOURCE_POLICY.md`
4. Accepted pilot `pilot/B20_align/attempt-1/` — all six files (ALIGNMENT.csv,
   ALIGNMENT.md, IMPACT_MAP.md, SOURCES.csv, RUN_META.md, SELF_CHECK.md)
5. `outputs/A30_verify/attempt-1/COMPARE.json` (full)
6. `outputs/B10_phd/attempt-1/PHD_FACTS.json` (full, both pages);
   `OPT2.md` (first ~70 lines); `PHD_CORE.md` NOT read this run — disclosed
   below under limitations
7. `outputs/B15_lit_synth/attempt-1/EVIDENCE_MAP.csv` (full); `GAPS.md`
   (full); `LIT_REVIEW.md` (first ~60 lines — audit header)
8. `outputs/B00_inventory/attempt-2/INVENTORY.md` (full)

## Per-idea record-read list (which file per idea, this run vs carried)

Deep-dive tier:
- P3R2-D-02 — carried from pilot (new06 FINAL/DEEP/D01.md full; old06
  DD_P3R2_D_02.md first ~30 lines)
- P3R2-C-01 — new06 FINAL/DEEP/D02.md (lines 1-100 + §14 at 262-275) read
  this run; consolidated E-01's pool record read this run
  (old06 20_OPPORTUNITY_POOL/P3R2_E_jptwkr_side.md, E-01 entry)
- P3R2-C-05 — new06 FINAL/DEEP/D03.md (lines 1-100) read this run
- P3R2-D-10 — carried from pilot (new06 D04.md first ~120 lines)
- P3R2-E-14 — new06 FINAL/DEEP/D05.md (lines 1-80) read this run
- P3R2-A-14 — carried from pilot (new06 D06.md first ~110 lines) PLUS old06
  40_DEEP_DIVES/DD_P3R2_A_14.md (lines 1-50) read this run — closes the
  pilot's disclosed not-read gap
- P3R2-D-01 — carried from pilot (new06 D07.md full; old06 DD first ~30)
- P3R2-A-10 — new06 FINAL/DEEP/D08.md (lines 1-80, 88-99, §14 at 260-271)
  read this run
- P3R2-C-09 — new06 FINAL/DEEP/D09.md (lines 1-80) read this run
- P3R2-C-22 — new06 FINAL/DEEP/D10.md (lines 1-80) read this run; old06
  DD_P3R2_C_22.md exists, NOT read (disclosed in row)
- P3R2-C-13 — carried from pilot (old06 DD_P3R2_C_13.md full; new06
  SELECTION.json rank-9 entry)
- P3R2-F-01 — old06 40_DEEP_DIVES/DD_P3R2_F_01.md (lines 1-60) read this
  run + new06 SELECTION.json rank-10 entry
- P5-USSCI2-S01 — old06 40_DEEP_DIVES/DD_P5_USSCI2_S01.md (lines 1-70) read
  this run
- P5R2-CN-01 — old06 40_DEEP_DIVES/DD_P5R2_CN_01.md (lines 1-55) read this
  run

Screening-evidence tier (old06 30_SCREENING/EVIDENCE/*.md):
- P3R2-C-08 — full file read this run (+ new06 SELECTION rank-14 entry)
- P3R2-E-04 — full file read this run (+ new06 SELECTION rank-16 entry)
- P3R2-C-04 — header (lines 1-18) this run (+ new06 SELECTION rank-19 entry);
  consolidated B-01's evidence header (lines 1-15) read this run
- P3R2-F-02 — header (lines 1-18) this run
- P3R2-F-12 — header (lines 1-18) this run
- P3R2-G-01 — header (lines 1-18) this run
- P3R2-D-12 — header (lines 1-15) this run
- P3R2-F-06 — header (lines 1-15) this run
- P3R2-F-03 — header (lines 1-15) this run
- P3R2-C-12 — header (lines 1-15) this run
- P3R2-A-02 — lines 1-20 this run
- P3R2-A-05 — lines 1-20 this run (+ new06 SELECTION rank-11 entry)
- P3R2-D-09 — lines 1-30 this run (+ new06 SELECTION rank-17 entry)
- P3R2-C-07 — carried from pilot (full file)

Selection-entry tier (new06 outputs/70_audit/FINAL/SELECTION.json — the
canonical audited package — read in FULL this run, all 24 entries + policy +
near-misses; used as the primary record for NEW24 members without deep
dives):
- P3R2-G-03, P3R2-F-23, P3R2-A-22, P3R2-D-19, P3R2-F-16, P3R2-F-19,
  P3R2-D-16 — SELECTION.json entries; their old06 EVIDENCE files exist and
  were NOT opened (disclosed per row). Rationale: these are far-domain ideas
  where the fresh, audited canonical entry plus A30's rank/decision data
  sufficed for a mechanism-absence determination; the old06 screening layer
  additionally carries A30's CONTRADICTED-provenance caveat.

P5-supplemental/pool tier:
- P5R2-CN-03 — old06 30_SCREENING/P5_SUPPLEMENTAL_CANDIDATES.json entry
  (grep-extracted, 13 lines) — no deeper record exists; thinnest record in
  the universe, disclosed in its row
- P3R2-E-10 — old06 20_OPPORTUNITY_POOL/P3R2_E_jptwkr_side.md entry (grep)
- P3R2-C-14 — old06 20_OPPORTUNITY_POOL/P3R2_C_dual_us_cn.md entry (grep)
- P3R2-C-15 — old06 20_OPPORTUNITY_POOL/P3R2_C_dual_us_cn.md entry (grep)

Founder-fit checks: grep "founder" across new06 D02/D08 plus targeted reads
of D02 §14, D08 §14 and D08 feasibility lines 88-99, D03's founder-stack
sentence (within the lines-1-100 read).

Directory/structure reads: Glob of `pilot/B20_align/attempt-1/*`,
`sources/old06/40_DEEP_DIVES/*`, `sources/old06/30_SCREENING/*` and
`.../EVIDENCE/*`, `sources/old06/20_OPPORTUNITY_POOL/*`,
`sources/new06/outputs/70_audit/FINAL/**`.

## Web activity (honest log)

WebSearch (discovery only, snippets not cited as evidence):
1. "Impedans Semion retarding field energy analyzer ion energy measurement
   product"

WebFetch / opens:
- OPENED OK this run: `https://www.impedans.com/semion-rfea-system/`
  (S-B20-03).
- Carried from pilot without re-opening (same run date, claims reused
  verbatim): S-B20-01 (theva.com/products), S-B20-02 (cfs.energy
  CFS-Realta release).
- FAILED opens this run: none.

All other current-market facts used in the rows are cited to A30's
already-verified opened primaries via `outputs/A30_verify/attempt-1/
COMPARE.json` (rows C05-DIS-01/02, C07-DIS-01/02, C09-DIS-01..03,
D10-DIS-01..03) and were NOT re-opened, or are corpus-dated record claims
explicitly labeled corpus-dated/refresh-sensitive in the relevant cells
(REBCO ramp, SPARC schedule, NVIDIA 800VDC 2027, HVDC project capital,
hydrogen-hub cost share, AFFF deadline, CISSOID last-time-buy, NCI SBIR
topic recurrence, superhot-2030 projects, EIC/PIP-II schedules, F-19's
A30-flagged unverified reversal).

## Files written (all inside the target)

- `outputs/B20_align/attempt-1/ALIGNMENT.csv` (39 rows + legend comment)
- `outputs/B20_align/attempt-1/ALIGNMENT.md`
- `outputs/B20_align/attempt-1/IMPACT_MAP.md`
- `outputs/B20_align/attempt-1/SOURCES.csv`
- `outputs/B20_align/attempt-1/RUN_META.md` (this file)
- `outputs/B20_align/attempt-1/SELF_CHECK.md`

## Limitations

- `outputs/B10_phd/attempt-1/PHD_CORE.md` was not opened this run; its
  content is the narrative counterpart of PHD_FACTS.json (read in full,
  C01-C50) and OPT2.md (partially read); no claim in this stage rests on
  PHD_CORE.md-only material. Disclosed rather than concealed.
- `outputs/B15_lit_synth/attempt-1/LIT_REVIEW.md` was read only through its
  audit header; all literature claims in this stage cite EVIDENCE_MAP.csv
  rows (read in full) and GAPS.md items (read in full).
- Record-depth stratification is by design and disclosed per idea: 7 NEW24
  ideas rest on canonical selection entries rather than their unopened old06
  evidence files; 8 old06 evidence files were read at header depth only;
  CN-03 has only a screening JSON entry anywhere in the corpus. Where a row's
  class could plausibly change on a fuller read, the row's falsifier or
  action cell says so (G-03 explicitly).
- Old06 record provenance is CONTRADICTED at the decision layer per A30;
  old06 deep-dive/evidence content is used as record evidence with primary
  citations, never as scoring authority. New06's own runtime provenance is
  unaudited (A30 note).
- Only one new web source was opened; the stage's alignment classes are
  mechanism judgments over corpus records and B10/B15 evidence, not
  current-market judgments, and every current-market claim is either
  A30-verified, S-B20-sourced, or labeled corpus-dated.
- Alignment/direction classes are this worker's own mechanism judgments
  (made personally, not delegated); falsifiers are recorded per row.
- No startup ranking performed (reserved for B40); no venture-viability
  verdicts beyond quoting the corpora's own kill rules and A30's verified
  adjudications.
