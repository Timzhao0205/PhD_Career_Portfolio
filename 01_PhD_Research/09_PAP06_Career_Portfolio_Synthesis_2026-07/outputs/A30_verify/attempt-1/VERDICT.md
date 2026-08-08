# A30_verify FULL verdict — calibrated conclusions

Stage `A30_verify`, FULL, attempt 1. Basis: the complete three-way comparison in
`COMPARE.md`/`COMPARE.json`, four web-verified disagreements (`SOURCES.csv`),
and the accepted A20 provenance audit. Numbers below are exact-ID unless
labeled semantic-augmented; the two ledgers were never merged.

## 1. Strength of agreement

**At 24:**
- BLIND vs NEW: 16/24 exact (67%), 17/24 with the single documented semantic
  match (E-01↔C-01). This is the strongest pairing.
- OLD vs NEW: 14/24 exact (58%); semantic augmentation adds nothing.
- BLIND vs OLD: 12/24 exact (50%), 13/24 semantic — the weakest pairing.

**At 10:**
- BLIND vs NEW: 6/10 exact against NEW's rank-order top 10, 7/10 against NEW's
  documented deep-dive ten; 7/10 and 8/10 semantic-augmented.
- OLD vs NEW: 7/10 (rank-order) or 6/10 (deep-dive set).
- BLIND vs OLD: 4/10 exact, 5/10 semantic.

**Calibration of what this means.** Eleven ideas appear in all three finals,
and the same concept (800VDC rack protection, E-01/C-01) tops or nearly tops
all three rankings — that is genuine, non-trivial convergence on a shortlist
drawn from 65-126 candidates. But the three runs are not independent draws:
all consumed one record lineage, and NEW+OLD shared one frozen longlist. The
BLIND-OLD gap is mostly one methodological object (the old G7 timing gate plus
old P5 kill severity), not scattered noise: of the 12 BLIND-only-vs-OLD picks,
four were removed from the universe before old06's scoring ever ran, and six of
the remaining eight died on gates whose reversals new06 later made. High
overlap is agreement evidence, not proof that any ranking is correct, and (per
A20) not evidence about who or what produced the old selections.

## 2. Correctness confidence per verified disagreement

| Disagreement | Direction the verified facts support | Confidence |
|---|---|---|
| DIS-C05 (BLIND 2 / OLD kill / NEW 3) | NEW+BLIND: revival predicate (Deschutes OCP spec, multi-vendor ecosystem) re-verified on two re-opened primaries; OCP-vacuum negative claim still only discovery-level (OCP 403-blocked, and an OCP CDU test-methodology *white paper* exists) | Facts HIGH; "old kill was wrong" MODERATE-TO-HIGH; exact rank 2-3 vs merely-selected: judgment |
| DIS-D10 (BLIND 14 / OLD kill / NEW 4) | Split: procurement is live and funded through FY2031 (OLD's hard kill overstated), but the JLWS awardee's own release claims proprietary in-house coherent beam combining (NEW's rank-4 merchant premise weakened). BLIND's mid-rank select is best calibrated | Facts HIGH; disposition adjudication MODERATE |
| DIS-C09 (BLIND 4 / OLD double-kill / NEW 12) | Split: EtO relaxation confirmed by EPA's own 2026 proposal (OLD's premise right; BLIND's top-5 too high), yet dated cargo-NII procurement and incumbent integration posture support NEW's mid-pack revival | Facts HIGH; disposition MODERATE-TO-HIGH for NEW's mid-rank |
| DIS-C07 (BLIND 10 / OLD kill / NEW cut) | Baselines: 45V construction-start pulled to pre-2028 by PL 119-21 §70511 (statute text opened) and Ingeteam ships <3%-distortion IGBT electrolyser rectifiers since 2023. BLIND's top-10 placement is the clearest identified blind error | HIGH |

Pattern across all four: the old kills were built on strict gate construction
plus 2026-vintage forecasts — sometimes factually right in part (EtO, decision
timing) but too absolute; the new revivals are directionally supported but in
one case (D-10 at rank 4) more aggressive than the primary evidence warrants;
the blind ranking is well calibrated exactly where record-internal reasoning
sufficed (C-05 clusters, D-10 risk pricing) and wrong where 2025-2026 external
facts moved (C-07, C-09's EtO leg). None of the three processes dominates.

## 3. What A20's provenance limits do and do not permit concluding

**Permitted:**
- The old06 idea records and frozen longlist that BLIND ranked are Fable-5
  runtime-model-verified (effort request-only). Agreement at the record level
  is expected — same inputs — and is not independent confirmation.
- Every old06 decision artifact this stage disagreed with (P4/G7 kills, P5
  kills, final 24/10, deep dives) is CONTRADICTED provenance: produced in the
  ChatGPT continuation, actual model and effort unknown. The G7-kill reversals
  therefore say nothing about Fable stability across time, and nothing here
  rehabilitates or further indicts any Fable/xhigh label on those artifacts.

**Not permitted:**
- Treating BLIND-vs-OLD divergence as "the same model changing its mind."
- Treating the 16/24 BLIND-NEW convergence as proof of correctness, or as
  provenance evidence for new06 (whose runtime was never audited here).
- Concluding runtime effort (xhigh) for anything, anywhere: A20 found no
  runtime effort evidence exists in the corpus at all.

**Net provenance-conditioned reading:** the strongest defensible claim is that
two fresh selection processes (one blind/record-internal under this package's
Fable route, one web-refreshed in the new06 rerun) independently reproduce
about two-thirds of each other's portfolio and the same top concept, while the
unknown-authorship old decision layer is the outlier — and where I verified the
outlier's reasons against primary sources, they were partly right on facts but
over-absolute in kill decisions.

## 4. Ideas needing deeper rerun in Operation B, and why

Priority order:

1. **C-05 / C-01+E-01 (datacenter conformance metrology + 800VDC protection).**
   Consensus top-of-portfolio across all three runs, so error costs are
   highest here. Open items: OCP primary documents (403-blocked site — the
   conformance-vacuum claim is still discovery-level), the C-01-vs-E-01
   representative choice (capital/export-posture trade documented on both
   sides but never web-tested), the eighth vendor (Stulz), and replacement of
   new06's weak R10-023 (sector-signals.net) sourcing.
2. **C-07 (AFE rectification).** Verified BLIND top-10 error. Rerun must test
   whether the electrowinning-only thesis survives with the hydrogen leg
   time-boxed by 45V (construction-start before 2028) and Ingeteam/Sungrow
   occupancy — i.e., does a copper-electrowinning-first company clear the bar
   without the hydrogen wave, and is there any merchant gap the >600 MW
   incumbent base does not cover?
3. **D-10 (beam-combining phase control).** Membership flips OLD-kill →
   NEW-rank-4; my verification shows both the live funded window (JBCS Q4-2026,
   roadmap through FY2031) and the awardee's proprietary vertical integration.
   Rerun needs: whether JBCS/JLWS awards contain any subsystem carve-out, the
   actual merchant addressable slice, and the Navy budget justification book
   itself (only trade coverage was opened).
4. **C-09 (pulsed-power platform).** Rerun the demand stack without the EtO
   leg (EPA relaxation verified from the regulator), quantify the cargo-NII and
   isotope legs from procurement primaries, and resolve the CGN
   Entity-List-adjacency counsel question that old06 raised and new06 carried.
5. **F-19, F-16, D-09 and the P5-kill revivals (A-05, A-22, D-19, D-16).**
   Eight OLD→NEW decision reversals were mapped but not web-verified in this
   stage; F-19's +28.0 score swing on a single acquisition fact (Ecolab/CoolIT)
   is the largest unaudited jump and A-05 (82% kill probability reversed to
   rank 11) the sharpest red-team contradiction.
6. **G-03 and F-23.** Selected by both baselines, absent from BLIND's 24; if
   two of three processes are right, BLIND's CONTINGENT calls need testing
   against fresh acceptance-market and lender-behavior evidence.
7. **The out-of-longlist BLIND picks (E-10, C-14, C-15).** No run has ever
   web-verified them (rejected at elegance stage before any P4). If Operation B
   values the blind perspective, these need first-pass verification from
   scratch; otherwise record them as universe artifacts, not losses.
8. **The three old06 supplementals (P5-USSCI2-S01, P5R2-CN-01, P5R2-CN-03).**
   CONTRADICTED-provenance additions that no fresh process has re-derived;
   include in Operation B only after independent regeneration of their demand
   cases.

## 5. Bottom line

Across the full 24/10 comparison, the fresh blind ranking and the fresh
canonical rerun converge strongly (16/24, up to 8/10 semantic-augmented at the
top) and both diverge from the unknown-authorship old final in one dominant,
now-verified way: the old G7 timing gate and P5 kill severity eliminated ideas
whose 2025-2026 factual predicates now check out against opened primary
sources — while in two verified cases (C-07, C-09's EtO leg) the old kills
also captured real facts that the blind run, by protocol, could not see. The
comparison upgrades confidence in the shared core (11 three-way ideas, the
800VDC-protection concept at the top) and produces a concrete, prioritized
rerun list; it does not, and cannot, restore Fable/xhigh provenance to any old
Folder 06 decision artifact.
