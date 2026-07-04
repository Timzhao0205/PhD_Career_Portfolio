# PHASE 3 — TOP-12 SELECTION

## Method

1. All 40 candidates scored (SCORING_MATRIX.md/.csv). C07, C24 gate-failed (G2: no meaningful
   software content) → reserve, ineligible.
2. Top 15 by raw score red-teamed (REDTEAM_C*.md). **Every critique landed material hits** —
   the dominant failure mode was stale whitespace claims (products the Phase-1 scouts missed
   already shipping). Scores adjusted ±1/criterion with written reasons (see SCORING_MATRIX.md
   adjusted table). Mean adjustment: **−7.0 points**.
3. Selection is made from the red-teamed 15 using adjusted scores. Non-red-teamed candidates
   (best: C02 75.2, C37 75.2, C03/C26 74.8 raw) are **not** promoted above red-teamed ones:
   their raw scores are un-stress-tested, and the observed mean −7.0 adjustment would place all
   of them at or below the selection floor. This asymmetry is recorded rather than hidden.
4. Diversity rules applied to the top 12 (below).

## Adjusted ranking of the red-teamed 15

| Rank | ID | Adjusted | Category |
|---|---|---|---|
| 1 | C12 | 84.0 | standalone (capital equipment) |
| 2 | C10 | 80.4 | standalone |
| 3 | C11 | 78.4 | standalone |
| 4 | C06 | 78.0 | standalone |
| 5 | C23 | 77.2 | instrument |
| 6 | C15 | 74.0 | standalone |
| 7 | C08 | 73.6 | standalone |
| 8 | C35 | 71.6 | standalone |
| 9 | C33 | 70.8 | instrument (PhD-lane) |
| 10 | C21 | 70.4 | instrument |
| 11 | C30 | 69.2 | instrument (PhD-lane) |
| 12 | C01 | 68.8 | standalone |
| 13 | C13 | 68.4 | standalone (component) |
| 13 | C27 | 68.4 | standalone |
| 15 | C20 | 67.2 | standalone (mfg equipment) |

## Diversity enforcement

A naive top-12 cut (C12…C01) contains 4 instruments (C23, C33, C21, C30) = 33.3% — **violates
the ≤33% instrument cap**. Per the brief, the lowest-ranked instrument (C30, 69.2) is demoted and
the next-best compliant candidate promoted. C13 and C27 tie at 68.4; **C27 is promoted** over C13
because C13's red-team finding is structural (joints physically cannot ship as a component;
standalone-value collapsed), while C27's risks are market-timing ones a deep dive can bound, and
C27 adds sector diversification (geothermal/harsh-environment energy).

## SELECTED TOP 12 (deep-dive slate)

| # | ID | Title (short) | Adjusted | Deep-dive must resolve (from red team) |
|---|---|---|---|---|
| 1 | C12 | Automated NI-HTS coil winding & jointing machines | 84.0 | Broomfield/Ridgway/BOW positioning; venture-scale vs job-shop; buyer count reality |
| 2 | C10 | Precision magnet/scientific power converters | 80.4 | Differentiation vs CAENels/Danfysik/Jema; is the CAS/China channel actually addressable |
| 3 | C11 | HTS quench-protection modules | 78.4 | Detection-vs-dump value split; in-house-IP objection; NI self-protection trend |
| 4 | C06 | 800 VDC solid-state protection modules | 78.0 | Post-ABB/Siemens niche (retrofit? rack-level? China draft-code angle); certification path |
| 5 | C23 | JEDEC WBG characterization appliance | 77.2 | Position vs Keysight PD1500A + 忱芯科技; is the sub-$150K tier real and defensible |
| 6 | C15 | Compact HTS magnet modules for OEMs | 74.0 | Position vs HTS-110; which OEM segment is genuinely unserved |
| 7 | C08 | GPU transient power buffer | 73.6 | Survive commoditization into OCP shelf spec? utility-side/retrofit niches |
| 8 | C35 | Solid-state RF for particle therapy | 71.6 | OEM concentration; adjacent accelerator markets to widen buyer pool |
| 9 | C33 | Cryogenic quench-onset QC instruments | 70.8 | FTO around Tokamak Energy patents; fiber-optic vs Hall positioning; TAM floor |
| 10 | C21 | WBG wafer-level burn-in cells | 70.4 | Market size floor ($25–55M/yr claim); Semight/Aehr-patent positioning |
| 11 | C01 | MW-class SiC PEBB family | 68.8 | Which niche escapes Danfoss/ABB catalogs + GE Vernova ONR lock |
| 12 | C27 | 300°C EGS downhole power modules | 68.4 | Passives wall (does a buildable BOM exist); real buyer list; DOE-funded qualification path |

**Diversity check (selected 12):** standalone 9/12 = 75% (≥50% ✓) · instruments 3/12 = 25%
(≤33% ✓) · PhD-lane 1/12 = 8.3% (≤50% ✓, i.e., ≥50% outside lane) · every candidate has named
beachhead + expansion + dual-market assessment ✓ · none conflicts with transformer condition
monitoring (G5 ✓).

**Excluded from top 15:** C30 (instrument cap; premise already shipped by Allegro),
C13 (structural component-viability failure), C20 (whitespace fictional; customer cohort
liquidating). These remain in the full ranking for Phase 6.
