# A30_verify FULL — three-way comparison: A10 blind vs old Folder 06 vs new Folder 06

- Stage: `A30_verify`, mode FULL, attempt 1. Worker: `pap06-fable-xhigh` (requested Fable 5 / xhigh).
- Machine-readable detail: `COMPARE.json`. Calibrated conclusions: `VERDICT.md`. Web provenance: `SOURCES.csv`.
- The accepted A30 pilot's six-ID findings were incorporated only after independently re-checking its file citations (elegance-adjudication lines 95/111, matrix ranks, P4 kill lines, new06 canonical selection) and re-opening its two C-05 web sources. This run extends the pilot to all 24/10, all pairings, and three additional verified disagreements.

## 1. The three sets and exactly which files define them

| Set | Final 24 | Top set | Universe |
|---|---|---|---|
| **BLIND** (A10) | `outputs/A10_blind/attempt-1/SELECTION.json` ranks 1-24 | `TOP10.json` = ranks 1-10 | 126 P3R2 records (`evidence/blind/POOL_1..3`), pre-longlist, clusters unresolved, no web |
| **OLD** (old06) | `sources/old06/60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv` (all 24 ranks verified identical to `30_SCREENING/P5_SELECTION.json` final_24) | `P5_SELECTION.json` top_10_deep_dives = matrix ranks 1-10, order verified | 65-idea frozen longlist (`30_SCREENING/LONGLIST.json`, membership enumerated) + post-longlist P5 supplementals, 3 of which entered the final |
| **NEW** (new06) | `sources/new06/outputs/70_audit/FINAL/SELECTION.json` final_24 (README designates `outputs/70_audit/FINAL` canonical; AUDIT.md PASS) | Two documented variants: NEW10-RANKS = final ranks 1-10; NEW10-DEEP = `top_10_deep_dives` (ranks 1-8 + C-09 at 12 + C-22 at 13; C-13/F-01/A-05 deliberately passed over for lane coverage per `40_select/SELECTION.md`) | The same 65-idea frozen longlist; supplementals never candidates |

Kill-decision context files: old06 `30_SCREENING/SCORECARDS/P4_SCORES_ALL.md` (65 scored, 30 survivors, 35 eliminated with per-idea gate reasons), `30_SCREENING/REDTEAM/P5_RT_G01..G06` and `P5_RT_REVIVALS.md`; new06 `outputs/20_p4/P4_REPORT.md` + `SURVIVORS.json` (65 scored, 30 survivors, cut 62.7), `outputs/40_select/SELECTION.md`.

## 2. Overlap metrics (exact-ID ledger, semantic strictly separate)

### At 24

| Pairing | Exact | Semantic-augmented | Additions in each direction |
|---|---|---|---|
| BLIND vs OLD | **12/24** | **13/24** (SEM-01 only) | 12 BLIND-only; 12 OLD-only |
| BLIND vs NEW | **16/24** | **17/24** (SEM-01 only) | 8 BLIND-only; 8 NEW-only |
| OLD vs NEW | **14/24** | **14/24** (no change) | 10 OLD-only; 10 NEW-only |

Eleven ideas sit in **all three** finals: D-01, D-02, A-14, E-14, C-08, A-10, C-04, C-22, F-01, E-04, C-13. Union across the three finals = 41 unique IDs (inclusion-exclusion checks: 72 − 12 − 16 − 14 + 11 = 41).

### At 10

| Pairing | Exact | Semantic-augmented |
|---|---|---|
| BLIND10 vs OLD10 | **4/10** (D-01, D-02, A-14, E-14) | **5/10** (+E-01↔C-01) |
| BLIND10 vs NEW10-RANKS | **6/10** (C-05, D-01, D-02, A-14, E-14, A-10) | **7/10** (+E-01↔C-01) |
| BLIND10 vs NEW10-DEEP | **7/10** (adds C-09) | **8/10** (+E-01↔C-01) |
| OLD10 vs NEW10-RANKS | **7/10** (D-02, C-01, D-01, E-14, A-14, C-13, F-01) | 7/10 |
| OLD10 vs NEW10-DEEP | **6/10** (D-02, C-01, D-01, E-14, A-14, C-22) | 6/10 |

Reading: the blind rerun agrees far more with the fresh canonical release than with the old final, at both depths, and the gap is driven almost entirely by old06's G7 timing-gate kills (section 4).

## 3. Semantic-match ledger (documented evidence only — never name similarity)

Counted in augmented overlap:

- **SEM-01 — E-01 ↔ C-01** (BLIND 1 ↔ OLD 5 / NEW 2). Documented on both sides: old06's elegance adjudication records E-01 REJECT with `duplicate_of: P3R2-C-01` and the cluster "800VDC rack-inlet protection" with canonical C-01 and member E-01 (`P3R2_ELEGANCE_ADJUDICATION.json` lines 95/111, re-verified); A10's own SELECTION/METHOD record the reverse representative choice ("E-01 over C-01 — same concept, lower capital, cleaner export posture"). The concept is at the very top of all three rankings; only the representative differs.

Documented but NOT counted (no overlap effect, or exact member already matched — rule in COMPARE.json):

- **SEM-02 — B-01 ↔ C-04** (same two-phase-loop thesis per new06's own near-miss note and A10's merge note; old06 carried both as separate finalists, ranks 12 and 16).
- **SEM-03 — E-10 ↔ A-13** (documented cluster "Rad-tolerant GaN PPU"; A-13 in neither final — old P5 KILL, new P4 cut).
- **SEM-04 — C-15 ↔ A-21** (documented cluster "Multi-MW heavy-fleet charging"; A-21 in neither final).
- **NON-MATCH-C14** — deliberately recorded: C-14 (BLIND 13) vs A-22 (NEW 18) is NOT a semantic match; both corpora treat them as different products (elegance verdict has `duplicate_of: null`).

## 4. Why composition and ordering changed — methodological analysis

**(a) Universe construction is the first-order cause of BLIND-only picks.** A10 ranked 126 pre-longlist records and chose its own cluster representatives; four of its 24 (E-01 rank 1, E-10 rank 12, C-14 rank 13, C-15 rank 18) were removed from the shared universe *before* old06's P4 ever ran, by the elegance adjudication's canonicalization. Neither baseline ever scored them. Conversely, old06's final holds three post-longlist supplementals (P5-USSCI2-S01 rank 6, P5R2-CN-01 rank 8, P5R2-CN-03 rank 14) that neither A10 nor new06 could select — new06's rerun consumed the frozen longlist and dropped all three by construction. Any overlap number is meaningful only with these universe statements attached.

**(b) The old G7 timing gate is the single largest decision-layer difference.** Old06's P4 demanded a *dated primary/official 2028-2035 trigger* and killed regardless of score: D-10 died at 73.4 — a score that would have ranked 2nd among its own survivors — and C-05 at 67.4, C-09 at 64.4, C-07 at 60.0, D-09 at 58.2, F-16 at 57.4. Six of new06's ten reinstatements (C-05, D-10, C-09, D-09, F-16, F-19) reverse exactly these gate kills, after new06's stage-10 refresh found the dated triggers the old evidence lacked (Deschutes spec via OCP; JLWS/JBCS awards and budget lines; 2025-2026 cargo-NII orders) or found the old forecast had not materialized. My fresh web verification (section 5 register; three of these plus C-07 opened end-to-end) confirms the pattern is real, not cosmetic: the old gate was strict-by-construction and its evidence was older, and in two of the four verified cases the old kill *premise* was nonetheless factually right in part (EtO direction; 2026-2028 decision concentration).

**(c) Red-team severity vs judgment reconciliation.** Old06's P5 killed 8 of its 30 P4 survivors and held 1 (A-05 at 82% kill probability, A-22 at 90%, A-13 at 92%, plus D-13, A-21, E-02, D-16, A-02; D-19 HOLD), applying a strict product-specific-buyer G1 discipline. New06 red-teamed all 30 survivors but dropped only 6 at selection — as *near-misses*, mostly on lane quotas and thesis overlap — and reinstated four of old06's P5 kills into its final tail (A-05 → 11, A-22 → 18, D-19 → 20, D-16 → 24). So the OLD→NEW membership delta decomposes cleanly: 3 universe drops + 6 G7-kill reversals + 4 P5-kill reversals versus 5 score-cut drops (F-02, F-12, F-06, F-03 + G-01's fresh G1 kill on the CEPC 15th-FYP exclusion) + 2 near-miss drops (B-01, D-12).

**(d) Scoring formalism.** BLIND: coarse 1-5 ordinal components, holistic ranks, no totals, soft sector diversification. OLD: 0-100 P4 totals + literal hard gates, then P5-adjusted totals (the matrix's D-02 65.6 vs P4's 76.6) and exact structural quotas. NEW: 0-100 rescoring with historical analyst gate opinions explicitly non-binding, judgment ranks ("clean-survive outranks equal-scored repair"), lane caps (max 3 per lane forced L14 drops; B-01/C-04 one-slot rule). Consequences visible in the deltas: A-10 rises 19→8 (old06's score had priced an export-blocked CN leg that new06 repaired to US-primary), C-22 falls 2→13 (hydrogen turbulence), F-01 falls 4→10, G-03 rises 20→15, and new06's rank order is deliberately not score-monotonic (C-05 78.3 at rank 3 above D-10 78.7 at rank 4).

**(e) Where each pair uniquely agrees against the third.** BLIND+OLD vs NEW: F-02 (both select mid-tier; new06 score-cut it at 59.4). BLIND+NEW vs OLD: the C-05/C-09/D-10/A-05/D-09 reinstatement block. OLD+NEW vs BLIND: C-01 as cluster representative (BLIND took E-01 — same concept, SEM-01), G-03 and F-23 (both baselines select; A10 called them CONTINGENT near-misses), and C-13 (old 10 / new 9 vs BLIND 24 — A10 priced OEM-insourcing risk far more heavily). BLIND alone: C-07 in the top 10 (see DIS-C07 — the verified facts side with the baselines).

## 5. Verified disagreement register (fresh web, 2026-07-28)

Four disagreements verified — the pilot's C-05 case deepened and re-checked, plus three new ones. Every opened source is at claim level in `SOURCES.csv`; opened vs not-opened is explicit there.

### DIS-C05-OCP-DESCHUTES (BLIND 2 / OLD kill 67.4 / NEW 3)
Both pilot anchor sources re-opened in full and still support the finding: Google's 2025-10-13 blog confirms the Deschutes CDU contribution to OCP, publication of `ocp-specification-deschutes-final-2025-09-05` plus design collateral, and seven named suppliers demoing at OCP Summit/SC25; Nidec's own release confirms a spec-compliant 2 MW-class / 80 PSI prototype with IEEE-519 ULHD VFD at SC25. The OCP spec PDF was re-attempted and still returns 403 — it stays **existence-only**. A fresh search surfaced OCP's "Liquid to Liquid CDU Test Methodology" *white paper* and the CDU sub-project page; both also 403. The "no complete conformance program with reference hardware" negative claim therefore remains **partially verified** (discovery-level, consistent, narrow reading). Adjudication unchanged from the pilot but on firmer ground: new06's revival predicate is substantively correct; the old kill mixed a failed forecast with strict gate construction. Confidence moderate-to-high.

### DIS-D10-JLWS-BEAMCONTROL (BLIND 14 / OLD kill 73.4 / NEW 4) — NEW
Opened: Lockheed Martin's JLWS award release (2026-07-09, 500 kW containerized system) and nLIGHT's JLWS release (2026-07-09; $44M initial, $627M ceiling; ~150 kW prototypes scaling to 300-500 kW; demos "as early as 2028"), plus a Military Times report citing the Navy FY2027 budget request ($31.7M JBCS beam-control development awards as soon as Q4 2026; roadmap through FY2031). Both corpora's facts verify; the inferences split. Old06 was right that decisions concentrate 2026-2028, wrong to treat 2030 as fully closed (funded roadmap through FY2031 with production options). New06's "procured now" is right, but its rank-4 merchant-socket premise is directly weakened by nLIGHT's own statement that it uses **proprietary coherent beam combination** in a **vertically integrated** approach — the internalization risk old06 and A10 both priced. A10's mid-rank select (14) is the best-calibrated disposition on opened evidence. Facts high-confidence; disposition judgment moderate.

### DIS-C09-ETO-SCANDINOVA-CARGO (BLIND 4 / OLD double-kill / NEW 12) — NEW
Opened: EPA's 2026-03-13 release proposing to rescind the 2024 EtO NESHAP's risk-based standards (regulatory pressure clearly relaxing — old06's "wrong direction" premise CONFIRMED, and it undercuts the EtO-replacement demand leg A10's blind rank 4 leaned on); ScandiNova's own acquisition news with the CEO's "integrated power systems" strategy quote (supports new06's proprietary-integration whitespace claim, noting the acquisition itself is 2023 — a trend, not a 2026 event); OSI/Rapiscan's 2026-05-14 ~$15M U.S. government cargo/vehicle-inspection task order (live dated procurement; more 2025-2026 orders at search level). Adjudication: old06's kill premise was partly right but over-absolute; new06's non-EtO-led mid-pack revival is the best-supported disposition; A10's top-5 placement overweights a leg that regulation has since weakened. Facts high; disposition moderate-to-high.

### DIS-C07-45V-INGETEAM (BLIND 10 / OLD kill 60.0 / NEW cut 61.6) — NEW
The only BLIND top-10 member rejected by both baselines. Opened: the current text of 26 USC 45V — construction must now begin **before January 1, 2028** (was 2033), amended by Public Law 119-21 §70511 (2025-07-04); and Ingeteam's own INGECON H2 FSK E12000 release — IGBT electrolyser rectifier, harmonic distortion <3% without extra filters, 12,000-15,860 Adc, commercial deliveries from September 2023 (>600 MW deployed and a 36 kA "Megalyzer" at search level). Both of old06's load-bearing kill facts verify on primary sources; the category A10 top-10'd is already merchant-served and its hydrogen leg is structurally time-boxed. This is the clearest identified BLIND ranking error, attributable to the web-free protocol. Confidence high.

Unverified-this-run reversals (mapped, flagged for Operation B): D-09, F-16, F-19 (+28.0 — the largest old→new score swing), A-05, A-22, D-19, D-16.

## 6. Provenance conditioning (accepted A20)

Everything on the old06 *decision* side of this comparison — P4 scores and G7 kills, P5 red teams and revival kills, the final 24/top 10, deep dives — is **CONTRADICTED** provenance: ChatGPT-continuation work, actual model and effort unknown. Only the idea records and frozen longlist are Fable-5 model-verified, with effort request-only (**PARTIAL_PROVENANCE**). new06 was never audited by this package. Therefore: BLIND-vs-OLD disagreements say nothing about Fable self-consistency; agreement with OLD confers no provenance; and the strong BLIND-NEW convergence is a content-level agreement between two fresh processes that shared an input lineage — agreement evidence, not proof of correctness, and not evidence of historical authorship.
