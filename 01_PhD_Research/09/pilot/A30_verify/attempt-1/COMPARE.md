# PILOT SAMPLE — NOT FINAL

# A30_verify PILOT — six-ID comparison: A10 blind vs old Folder 06 vs new Folder 06

- Stage: `A30_verify`, mode PILOT, attempt 1. Worker: `pap06-fable-xhigh`.
- Scope: exactly the six IDs at ranks 1-6 of the accepted A10 full
  `outputs/A10_blind/attempt-1/SELECTION.json`:
  P3R2-E-01, P3R2-C-05, P3R2-D-01, P3R2-C-09, P3R2-D-02, P3R2-A-14.
- Old baseline: `sources/old06/60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv`
  (final 24, ranks + score_total), cross-checked against
  `sources/old06/30_SCREENING/P5_SELECTION.json` (top-10 deep dives match the
  matrix's ranks 1-10 exactly).
- New baseline: `sources/new06/outputs/70_audit/FINAL/SELECTION.json` — the
  canonical audited package per new06's own `README.md`; `AUDIT.md` records
  zero repairs to the canonical copies.
- Machine-readable detail: `COMPARE.json` in this directory.

## 1. Six-ID disposition table (exact-ID ledger)

| A10 rank | ID | Old06 final | Old06 detail | New06 final | New06 detail |
|---|---|---|---|---|---|
| 1 | P3R2-E-01 | ABSENT | Rejected at elegance adjudication as duplicate of canonical C-01; never on frozen longlist | ABSENT | Never a candidate (rerun consumed the frozen longlist; zero mentions in new06) |
| 2 | P3R2-C-05 | ABSENT (killed) | Longlist PROMOTE; P4 67.4 but G7 FAIL; no revival | RANK 3 | score 78.3; deep dive D03 |
| 3 | P3R2-D-01 | RANK 3 | score 62.8; deep-dived | RANK 7 | score 72.9; deep dive D07 |
| 4 | P3R2-C-09 | ABSENT (killed twice) | P4 64.4 G7 FAIL; P5 revival re-killed 52.2 (stale CEPC schedule) | RANK 12 | score 72.0; deep dive D09 |
| 5 | P3R2-D-02 | RANK 1 | score 65.6; deep-dived | RANK 1 | score 81.9; deep dive D01 |
| 6 | P3R2-A-14 | RANK 9 | score 54.6; deep-dived | RANK 6 | score 74.8; deep dive D06 |

Exact-ID overlap within pilot scope: 3/6 in old06 final 24 (D-01, D-02,
A-14, all deep-dived), 5/6 in new06 final 24 (all five also deep-dived).
Of the six, 3 appear in both old and new finals.

## 2. Semantic-match ledger (kept separate — documented evidence only)

| Ledger | A10 ID | Matches | Old06 | New06 | Documentation |
|---|---|---|---|---|---|
| SEM-01 | P3R2-E-01 | P3R2-C-01 | rank 5, deep-dived | rank 2, deep-dived | Old06's own elegance adjudication: E-01 REJECT with `duplicate_of: P3R2-C-01`, cluster "800VDC rack-inlet protection" canonical C-01 with E-01 a member (`P3R2_ELEGANCE_ADJUDICATION.json` lines 95/111). A10's own records: rank-1 decision "Chosen over near-duplicates A-01/B-03/C-01"; METHOD tie-note "E-01 over C-01 (same concept, lower capital and cleaner export posture)". |

This is a same-concept cluster documented in BOTH corpora's records, not a
name-similarity guess. With SEM-01 counted, concept-level presence rises to
4/6 (old) and 6/6 (new). No other semantic match was needed for the six.

Notable representative flip inside SEM-01: old06 canonicalized C-01 and
rejected E-01 as its duplicate; A10 did the reverse (selected E-01, marked
C-01 DUP-UNSEL, citing lower capital and cleaner export posture). The
concept agrees at the very top of all three rankings (A10 #1, new #2,
old #5); only the cluster representative differs.

## 3. Rank deltas and decision changes

- P3R2-D-02: old 1 -> new 1 (delta 0). A10 places it 5 — the pilot's only
  ordering divergence at the very top; both baselines rank it first.
- P3R2-A-14: old 9 -> new 6 (delta -3). A10 rank 6 exactly matches new06.
- P3R2-D-01: old 3 -> new 7 (delta +4). A10 rank 3 matches old06.
- P3R2-C-05: decision change, old KILL (P4 G7) -> new SELECT rank 3.
- P3R2-C-09: decision change, old KILL (P4 G7 + revival re-kill) -> new
  SELECT rank 12 with deep dive.
- P3R2-E-01/C-01 (semantic): old 5 -> new 2 (delta -3).

## 4. Methodological differences noticed (pilot-scope observations)

1. **Gate construction vs holistic ranking.** Old06 and new06 both use
   numeric 0-100 scores and hard gates G1-G7; A10 used coarse 1-5 ordinal
   components with holistic ranks and no totals. Old06's G7 demanded a
   *dated primary/official 2028-2035 trigger*; several strong ideas died on
   that construction alone.
2. **Fresh evidence reverses G7 kills.** The visible pattern in scope: new06
   re-verified 2025-2026 market facts and reinstated C-05 (kill -> rank 3)
   and C-09 (double kill -> rank 12). (Outside scope but same pattern:
   D-10, old-killed at 73.4, new rank 4 — flagged for the full run.)
3. **Candidate universes differ.** Old06's final 24 contains three
   post-longlist supplemental ideas (P5-USSCI2-S01 rank 6, P5R2-CN-01 rank
   8, P5R2-CN-03 rank 14) that do not exist in A10's 126-ID pool; new06's
   canonical final 24 contains none of them. Any full-run overlap metric
   must state the universe it is computed over.
4. **Deep-dive sets follow each run's own ranking.** All pilot-scope members
   of each final's top tier were deep-dived in that corpus; new06 also
   deep-dived C-09 (rank 12) and C-22 (rank 13) while skipping C-13 (9),
   F-01 (10), A-05 (11) — a deliberate choice recorded in its selection
   policy, noted for the full run.

## 5. Verified material disagreement — DIS-C05-OCP-DESCHUTES

**The disagreement.** P3R2-C-05 (liquid-cooling conformance metrology) is
the sharpest decision divergence in scope: old06 killed it at P4 gate G7
(score 67.4) saying the qualification gap "is already active", lacked a
primary/official 2028-2035 trigger, and that "OCP or vendor labs" would
credibly "standardize it before a 2030 launch"; new06 selected it at rank 3
on the factual predicate that Google published its Project Deschutes 2 MW
CDU specification through OCP with eight named vendors building to it while
OCP standardization "remains partial ... no complete conformance test
method with reference hardware" (`sources/new06/outputs/50_deep/DEEP/D03.md`).
A10, blind and web-free, independently ranked it 2.

**Fresh web verification (2026-07-28), primary sources opened:**

1. *Google Cloud Blog, "Agile data centers and systems to enable AI
   innovations", 2025-10-13* (opened in full). Confirms Google contributed
   Project Deschutes to the Open Compute community and "have since published
   the specification and design collateral", linking the OCP-hosted spec
   document `ocp-specification-deschutes-final-2025-09-05`; names seven
   suppliers — Boyd, CoolerMaster, Delta, Envicool, Nidec, nVent, Vertiv —
   showcasing demos at the OCP Global Summit and SuperComputing 2025.
2. *Nidec Corporation official news release, "Nidec Accelerates
   Liquid-Cooling Adoption for AI Generation Data Centers: Prototypes
   Project Deschutes CDU Based on Google OCP Specification"* (opened in
   full). Confirms a prototype "compliant with Google Open Compute Project
   (OCP) specification", "2 MW class cooling capacity and 80 PSI", IEEE-519
   ultra-low-harmonic VFD, extremely low approach-temperature design,
   exhibited at SC25 (Nov 2025). (Page date displayed ambiguously; see
   limitations.)

**Verification results.**

- Deschutes spec contributed to OCP and published, with a real multi-vendor
  implementation ecosystem: **VERIFIED** by two independent primary/official
  sources opened in full. This is exactly the class of concrete,
  buyer-authored official demand anchor old06's G7 said was missing.
- "Eight named vendors": Google's own blog names **seven**; the eighth
  (Stulz) appears only in trade coverage (DCD headline) that returned HTTP
  403 to fetch. Recorded as verified-for-7, discovery-level for the 8th.
- "OCP publishes only guidelines / no complete conformance method with
  reference hardware": **PARTIALLY VERIFIED.** Search-level listings of
  opencompute.org documents show guideline/requirements/white-paper-class
  titles (including a "Cold Plate Development and Qualification" white paper
  and an "L2L CDU Test Methodology performance rating" white paper), and no
  OCP conformance/certification program with reference hardware surfaced.
  But opencompute.org refused every direct fetch (HTTP 403: blog, wiki,
  spec PDF), so this negative claim rests on discovery-level evidence plus
  the opened Google blog's characterization, not on opened OCP pages. The
  existence of a CDU test-methodology *white paper* narrows, without
  contradicting, the "vacuum" claim.

**Adjudication.** On opened primary evidence, new06's factual predicate for
reviving C-05 is substantively correct, and old06's kill rested partly on a
forecast (OCP/vendor standardization closing the gap before 2030) that had
not materialized by the new06 refresh, and partly on a strict gate
construction that is methodological rather than factual. A10's independent
blind rank 2 aligns directionally with new06. Whether the correct landing
spot is rank 2-3 versus merely "selected" is judgment these facts do not
settle.

## 6. Provenance conditioning (from accepted A20)

Every old06 artifact this pilot compared against on the decision side — the
P4 scores and G7 kills, the P5 red teams and revival kills, the final
24/top 10, and all deep dives — is **CONTRADICTED** provenance:
ChatGPT-continuation work with actual model and effort unknown. Only the
underlying idea records (frozen longlist) are Fable-5-model-verified, and
even there effort is request-only (PARTIAL_PROVENANCE). Consequences:

- Old-vs-A10 disagreements are **not** "Fable disagreeing with Fable".
- Overlap with old06 finals is agreement with an unknown-model selection.
- The more meaningful agreement signal in this pilot is A10 (blind, fresh,
  Fable-run under this package) against new06 (fresh canonical rerun) —
  5/6 exact-ID, 6/6 with the documented semantic match — but high overlap
  is agreement evidence only, never proof of correctness.
