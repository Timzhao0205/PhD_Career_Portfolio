# FULL RANKING — ALL 40 CANDIDATES (max-effort re-derivation, 2026-07-04)

**This file supersedes the first Phase-6 ranking.** Scores were re-derived at maximum reasoning
depth from the mission's own evidence — no new web research. Changes vs. the prior version are
itemized in `03_MAX_EFFORT_DELTA.md`. Details: `30_PHASE3_SCORING/`, `40_PHASE4_DEEPDIVES/`,
`50_PHASE5_POLICY/POLICY_BRIEF.md`.

## Scoring pipeline (three explicit layers)

1. **Raw** — Phase-3 rubric score, all 40 candidates (11 criteria, weights per
   `01_MISSION/SCORING_RUBRIC.md`).
2. **RT-adj** — post-red-team adjustments (top 15 by raw score only), ±1/criterion with written
   reasons. Unchanged from Phase 3. Mean effect: **−7.0 points**.
3. **Final** — NEW layer this revision: deep-dive + policy-brief adjustments (±1/criterion,
   written reasons in `03_MAX_EFFORT_DELTA.md`), applied only to the 12 deep-dived candidates.
   Deep dives moved scores **both directions** (they overturned two red-team pillars and confirmed
   others). Mean effect: **−4.5 points**; full pipeline raw→final mean for the 15 stress-tested
   candidates: **−11.4 points**.

**Expected scores (marked `e`).** Candidates never red-teamed carry raw scores that are
un-stress-tested. Ranking them against fully-adjusted scores would systematically favor the
untested. For ranking purposes only, they carry `raw − 11.4` (the observed mean full-pipeline
adjustment); the three red-teamed-but-not-deep-dived candidates (C30, C13, C20 — all
premise-level kills) carry `RT-adj − 8.9` (the observed deep-dive adjustment for the four
premise-level-kill cases: C23 −11.6, C21 −10.8, C08 −8.0, C35 −5.2). Expected scores are
*expectations, not measurements* — a real red team + deep dive could land anywhere around them.

**Ties** broken by (1) founder-fit score, (2) standalone-value score, (3) capital-efficiency
score, (4) deep-dive conviction.

## Ranked table

| Rank | ID | Idea (short) | Raw | RT-adj | Final | Evidence | One-line final verdict |
|---|---|---|---|---|---|---|---|
| 1 | C12 | NI-HTS coil winding & jointing cells | 93.2 | 84.0 | **83.6** | DD (Medium) | Best risk-adjusted bet as "winding cell + recipe software + inline QC" family; Tokamak Energy's Sept-2025 Ridgway acquisition reopened the vendor-neutral slot [DD-C12-19]; the naive "no vendor exists" claim [S089] stays retracted; China is supply chain + intel, not a market [DD-C12-08]; gate: 3 paid commitments by mid-2030 |
| 2 | C10 | Precision magnet & scientific power converters | 88.4 | 80.4 | **76.8** | DD (Medium) | Real but narrow fast-dynamics wedge (5 kW–multi-kA) in the US/EU fusion buildout — power systems are the #1 surveyed supply bottleneck [DD-C10-14][S058]; ppm-catalog framing dead (CAENels/Danfysik [DD-C10-01][DD-C10-02]); China tenders captured domestically [DD-C10-23][DD-C10-24] — radar, not market; absorbs C11 electronics + C35 LLRF; kill if buyers won't pay for lead time/dynamics by end-2027 |
| 3 | C06 | 800 VDC protection (pivoted: protection-intelligence layer) | 84.0 | 78.0 | **74.8** | DD (Medium, pivot) | Original SSCB dead (ABB Infinitus/Siemens 3QD2 ship [DD-C06-03][DD-C06-04]); survives as per-rack ground-fault-location + series-arc discrimination via integrators — NVIDIA itself names VDC fault detection the open innovation area [DD-C06-01]; red team's "China slot taken" claim rebutted by TYT/Liangxin's own filings (pilot/pre-research stage [DD-C06-16][DD-C06-18]); kill if OCP/NVIDIA embed it by end-2027 |
| 4 | C11 | HTS quench protection (rescoped: detection-first MPMU) | 86.8 | 78.4 | **71.2** | DD (Med-Low rescoped) | Sub-ms kA dump physics-capped and renounced [DD-C11-01]; survives as detection-first magnet protection & management for the non-fusion 0.5–20 kA HTS wave (ASIPP tender proves hardware is bought [DD-C11-15]; NI coils still need management electronics [DD-C11-03]); category ceiling <$150M/yr → **product line inside C10/C12, not a standalone company** |
| 5 | C33 | Cryogenic coil QC instruments | 76.8 | 70.8 | **71.2** | DD (Low standalone / Med-High module) | Only candidate whose score *rose* under deep-dive scrutiny: Tokamak Energy patent block overturned on claim language [DD-C33-01][DD-C33-02], physics demonstrated (LBNL Hall-array inversion [DD-C33-03]), TRL best-in-portfolio — but 8–15 buyers → $2–4M/yr standalone; carry as **C12's QC module** and the founder's credibility engine |
| 6 | C15 | Compact HTS magnets (reframed: fusion test/background magnets) | 80.4 | 74.0 | **69.6** | DD (Low-Med; Medium reframed) | OEM-magnet framing dead (HTS-110 shipping exactly it [DD-C15-13][DD-C15-14]; benchtop NMR chose Halbach on purpose); Medium as US-built fast-turn test/background magnets ($11–35M/yr SAM); China import door closing (domestic-only tenders [DD-C15-09]); best held as **C12's vertical expansion**; cryogenics co-founder required |
| 7 | C01 | MW SiC PEBB family (merged with C03: USV/fast-craft bricks) | 75.2 | 68.8 | **69.6** | DD (Med-Low pivot) | Catalog-PEBB whitespace occupied (GE Vernova ONR award [DD-C01-01]; Danfoss/ABB [DD-C01-06][DD-C01-25]); survives as aviation-class 50–500 kW marine-ruggedized bricks for uncrewed/fast electric craft ($200M Saronic-class demand signal [DD-C01-12]); red team's $2–5M test-capex objection rebutted for the pivot (250 kW regen rig $150–400K [DD-C01-11]); watch H3X [DD-C01-08]; China zero option value |
| 8 | C27 | 300°C downhole power (rescoped: 250°C multi-market platform) | 76.4 | 68.4 | **68.0** | DD (Low-Med) | Merchant power slot above ~230°C verified empty (Honeywell/Ozark sell chips/loggers, not power [DD-C27-01][DD-C27-05]; Watt&Well stops at 220°C [DD-C27-12]) and 250°C is buildable from catalog+screened parts [DD-C27-06] — but current merchant POs ≈ zero, beachhead $2–9M/yr grant-fed [DD-C27-13], oil capex falling; needs the DOE-superhot bridge plus aero/space adjacents |
| 9 | C35 | Particle-therapy RF cassettes | 78.4 | 71.6 | **66.4** | DD (Low — no-go standalone) | BTESA/R&K/Cryoelectra/RFHIC ship the identical product [DD-C35-18][DD-C35-02]; IBA self-supplies [DD-C35-05→published]; 国产化 closes China [S204][DD-C35-15]; merchant accelerator RF ≈ $40–95M/yr total; regulation is its *least* problem (policy archetype g: ✅✅✅) — fold the LLRF-cassette asset into C10 |
| 10 | C23 | JEDEC WBG characterization appliance | 85.6 | 77.2 | **65.6** | DD (Low; narrow Medium wedge) | Category served at both price ends (Keysight PD1500A above [DD-C23-01], Tek/RIGOL below [DD-C23-03][DD-C23-18], UniSiC everywhere with state capital and a Munich office [DD-C23-14][DD-C23-15]); JEP203/204 [S135] arrives at incumbents as firmware; honest beachhead $3–9M/yr; China leg policy-dead (archetype e); survives only as JEP203 SC-bench + compliance-software wedge — the founder's cheapest-to-validate fallback |
| 11 | C08 | GPU transient buffer (re-specced: facility ride-through) | 82.0 | 73.6 | **65.6** | DD (Low as chartered / Med-Low successor) | Rack product commoditized into the NVIDIA/OCP power-shelf spec before it could exist (65 J/GPU embedded; 20× more native in Rubin [DD-C08-01][DD-C08-02]); conditional facility-level successor (5–20 MW NOGRR282-compliance systems [DD-C08-04][S041]) hinges on an unverifiable attach rate and faces the same commoditization one level up |
| 12 | C02 | High-temp WBG packaging platform | 75.2 | — | 63.8e | raw, un-stress-tested | Strong fit and universal WBG heat-flux pain [S015], but license-revenue-late model and years-long reliability data; **conditional top-12 slot: requires red-team + deep dive before any commitment** |
| 13 | C37 | Low-field MRI gradient amplifiers | 75.2 | — | 63.8e | raw, un-stress-tested | Fast, cheap, real gap below Prodrive [S198][S210]; small ceiling, thin frontier story; solid fallback business |
| 14 | C26 | Rad-characterized space WBG modules | 74.8 | — | 63.4e | raw, un-stress-tested | Excellent fit [S161][S151]; ITAR/EAR walls + beam-time capital confirmed by policy brief (archetype h: US-only, parallel ⛔ [P-19]) |
| 15 | C03 | MW marine/off-highway inverters | 74.8 | — | 63.4e | raw; folded into C01 | The surviving content of C01/C03 is one thesis: extreme-density bricks for electric marine/UxV [S022] — ranked at C01 (#7) |
| 16 | C38 | GFM PCS for compute microgrids | 73.6 | — | 62.2e | raw, un-stress-tested | Mandate-driven demand real [S220][S221] but thin moat vs Sungrow/SMA/GE; capital-heavy certification |
| 17 | C19 | SSB isostatic-press cells | 73.2 | — | 61.8e | raw, un-stress-tested | Plausible pilot-scale gap [S097]; domain-new founder; Chinese majors will follow fast |
| 18 | C09 | MV-to-800 VDC power blocks | 72.0 | — | 60.6e | raw, un-stress-tested | Real transformer-crisis pull [S029]; hardest technical lift; funded SSTs likely to down-scope into it |
| 19 | C30 | Fast+accurate current sensors | 77.6 | 69.2 | 60.3e | RT (premise-level kill) | Allegro shipped the 10 MHz TMR part in Oct 2025 [RT-C30-01]; LEM+TDK converging [RT-C30-03]; premise expired before founding — expected score reflects un-run deep-dive discount |
| 20 | C14 | HTS cryostats & QC dewars | 71.6 | — | 60.2e | raw, un-stress-tested | Sensible bundle item for the C12 cluster; not a lead product |
| 21 | C36 | GaN ablation OEM platform | 71.6 | — | 60.2e | raw, un-stress-tested | Decent OEM-subsystem logic [S202]; medical design-in cycles slow; policy archetype (g) is favorable — revisit if C10/C35 lane opens medical RF |
| 22 | C21 | WBG wafer-level burn-in cells | 76.4 | 70.4 | **59.6** | DD (Low — no-go) | All four red-team pillars survived verification: bracketed by Aehr above (FOX-CP/NP, GaN production wins [DD-C21-09][DD-C21-15]) and four funded Chinese vendors below (Semight 43.6% share [DD-C21-18]); market $24–60M/yr with ±2.5× cyclicality [DD-C21-14]; GaN-startup beachhead falsified [DD-C21-27]; §744.6 makes the demand center legally radioactive for a US person [P-42] — **ejected from the top 12** |
| 23 | C13 | HTS current leads & joints | 77.6 | 68.4 | 59.5e | RT (structural kill) | Joints are made in situ from the customer's conductor — cannot ship as a component [RT-C13-05]; leads market $123M/4.2% CAGR owned by HTS-110/CAN/Furukawa [RT-C13-03]; coherent only as a C12 attach line |
| 24 | C29 | Smallsat PPU/PCDU line | 70.8 | — | 59.4e | raw, un-stress-tested | Shortage-validated demand [S151] but flight-heritage chicken-and-egg; policy brief confirms archetype (h): China variant untenable, FOCI/CFIUS exposure [P-19][P-20] |
| 25 | C40 | Second-life battery grading systems | 70.4 | — | 59.0e | raw, un-stress-tested | Regulatory-driven demand in China/US [S218][S226]; moderate fit; instrument-capped category |
| 26 | C16 | HTS induction heaters | 70.0 | — | 58.6e | raw, un-stress-tested | Proven-then-stalled category [S079]; capital-heavy sales; REBCO cost curve may reopen it post-2030 — a natural C12-cluster customer segment, not a first product |
| 27 | C20 | Formation systems for new chemistries | 78.4 | 67.2 | 58.3e | RT (premise-level kill) | "Energy-recycling precision formation" is Chroma's literal shipping product name [RT-C20-01]; Digatron/Neware/Hangke at pilot scale; buyer cohort liquidating [RT-C20-07] |
| 28 | C17 | Compact SMES modules | 69.6 | — | 58.2e | raw, un-stress-tested | Physics real [S092], economics lose to supercaps (C08 evidence confirms the buyer side); chronically stalled category [S081] |
| 29 | C28 | COTS-plus rad-tolerant DC-DC | 69.2 | — | 57.8e | raw, un-stress-tested | Lead-time arbitrage without a physics moat [S152]; crowded shops; ITAR |
| 30 | C39 | Electrolyzer power modules | 69.2 | — | 57.8e | raw, un-stress-tested | Post-45V logic sound [S216][S219] but EPC channel diffuse; Chinese PCS majors adjacent |
| 31 | C22 | PD/insulation EOL rigs | 68.0 | — | 56.6e | raw, un-stress-tested | Served-adjacent by HV-test incumbents [S104]; modest edge; instrument-capped |
| 32 | C07 | 800 V busbar connectors | 68.0 | — | 56.6e | raw — **gate-fail G2** | No meaningful software content; Amphenol wall [S035]; ineligible regardless of score |
| 33 | C18 | HTS MCZ retrofit magnets | 67.2 | — | 55.8e | raw, un-stress-tested | Proven category, unserved geography [S082] — but needs furnace-OEM co-development a solo founder can't force; semicap sensitivities |
| 34 | C34 | Ultra-low-noise SMU line | 67.2 | — | 55.8e | raw, un-stress-tested | Keysight shadow too large [S171]; value-engineering, not extreme-performance |
| 35 | C04 | 2nd-gen MCS charging modules | 66.4 | — | 55.0e | raw, un-stress-tested | OEM in-housing (BYD/Huawei [S004]) squeezes the integrator channel it depends on |
| 36 | C05 | Pulsed-power modules | 65.6 | — | 54.2e | raw, un-stress-tested | Real DoD demand [S014]; primes internalize; US-only; ITAR-heavy for a solo start |
| 37 | C31 | Triaxial OPM magnetometers | 63.6 | — | 52.2e | raw, un-stress-tested | One-vendor market real [S180] but atomic-physics team gap; export-sensitive [S176]; policy brief confirms quantum-sensing OISP tripwire [P-01] |
| 38 | C24 | HV probe cards | 62.0 | — | 50.6e | raw — **gate-fail G2** | No meaningful software content; consumables niche; ineligible |
| 39 | C32 | Rydberg RF probes | 56.4 | — | 45.0e | raw, un-stress-tested | Frontier physics outside the founder's stack [S186]; long runway |
| 40 | C25 | D2W overlay inspection | 55.6 | — | 44.2e | raw, un-stress-tested | Optics-centric, off-stack [S121]; EVG/KLA shadow |

## Re-selected top 12 (deep-dive-slate succession)

The Phase-3 slate (C12, C10, C11, C06, C23, C15, C08, C35, C33, C21, C01, C27) was re-examined
against the full evidence. **Outcome: 11 of 12 retained; C21 ejected** (deep dive confirmed
NO-GO on every red-team pillar; final score 59.6 falls below several un-stress-tested
candidates). Slot 12 passes to **C02 (63.8e), conditionally** — it is the highest-ranked
never-stress-tested candidate, and the condition is explicit: it must survive a red team + deep
dive before any resource commitment. No other change: under expected-score discounting, no
un-stress-tested candidate displaces any retained slate member.

**Diversity check (new top 12 = C12, C10, C06, C11, C33, C15, C01, C27, C35, C23, C08, C02):**
standalone 10/12 = 83% (≥50% ✓) · instruments 2/12 = 17% (C33, C23; ≤33% ✓) · PhD-lane 1/12 =
8.3% (C33; ≥50% outside ✓) · all pass gates G1–G5 (C07/C24 remain reserve) · none conflicts with
transformer condition monitoring ✓.

## Reading notes

1. **Rank = evidence-adjusted rubric score, not a pursuit ordering.** Read the verdict column.
   C35/C23/C08 hold ranks 9–11 on *score* while being NO-GO or fallback as standalone companies —
   their scores are real, fully-stress-tested measurements of ideas whose best assets fold into
   higher-ranked theses. Conversely, nothing below rank 8 is recommended for standalone pursuit.
2. **Scores are comparable only within an evidence class.** A raw 75.2 (C02) is *not* better than
   a deep-dived 74.8 (C06): the observed cost of full stress-testing averaged −11.4 points, which
   is exactly what the `e` column corrects for.
3. **C30/C13/C20 rank above C21 despite structural kills** because their expected scores start
   from RT-adjusted bases; their verdicts, not their ranks, carry the kill. All three kills are
   premise-level (product already shipped / product cannot physically ship as a component /
   customer cohort liquidating) and none is a candidate for revival without new evidence.
4. The two G2 gate failures (C07, C24) are ranked for completeness but ineligible for selection
   at any score.
