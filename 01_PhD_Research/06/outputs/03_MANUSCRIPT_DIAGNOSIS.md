# 03 — Manuscript diagnosis (Stage 30)

Prepared by: Claude Code, stage `30_manuscript`, requested model Fable 5 /
Extra High. Audited artifact: the submitted IEEE Sensors Letters manuscript
`SENSL-26-07-RL-1061` ("AlGaN/GaN Hall-Effect Sensor for In-Situ Magnetic
Field Monitoring of the HSX Stellarator"), read from its LaTeX source
[`../../01_Publications/submitted/regular_lsens/regular_lsens.tex`](../../01_Publications/submitted/regular_lsens/regular_lsens.tex)
(line numbers below refer to that file; per
[`00_INPUT_INVENTORY.md`](00_INPUT_INVENTORY.md) Group B the source compiles
to the identical PDF contained in
[`../inputs/IEEE_submission_bundle_2026-07-02.pdf`](../inputs/IEEE_submission_bundle_2026-07-02.pdf),
whose embedded viewer restrictions prevented direct PDF re-extraction in this
stage). Reviewer wording is from
[`../inputs/Decision_Letter_IEEE_2026-07-23.pdf`](../inputs/Decision_Letter_IEEE_2026-07-23.pdf)
(read in full this stage). Claim IDs `C###` refer to
[`00_CLAIM_BASELINE.csv`](00_CLAIM_BASELINE.csv); conflict IDs to
[`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md); source IDs `S####` to
[`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv). Reviewer-comment IDs
(`AE-##`, `R1-##`, `R2-##`) refer to
[`03_REVIEWER_RESPONSE_MATRIX.csv`](03_REVIEWER_RESPONSE_MATRIX.csv).

Evidence-category legend used throughout: **[SF]** supplied fact,
**[EE]** external evidence (verified ledger source or official policy),
**[INF]** inference, **[REC]** recommendation, **[PX]** proposed experiment
(handed to stage 40), **[GATE]** unresolved gate.

This stage diagnoses only. **No manuscript file was edited.**

---

## 1. Claim-by-claim audit

### 1.1 Title (line 370)

| Claim | Status | Basis |
|---|---|---|
| "AlGaN/GaN Hall-Effect Sensor" | **Supported now** | Device identity is a supplied fact (C001) [SF] |
| "for In-Situ … Monitoring of the HSX Stellarator" | **Supported now** (deployment happened; C001) | [SF] |
| "Magnetic Field Monitoring" | **Requires qualification today; fully supported only after calibration** | The delivered output is voltage-domain only; no tesla value exists anywhere in the study or data (C005; `00_INPUT_INVENTORY.md` Group C). The AE's core objection (AE-01) is precisely this gap between the title's measurand and the reported quantity. [SF]/[INF] |

**[REC]** Keep the title only if the revision delivers field-unit output
(WP-C); otherwise it over-promises the measurand.

### 1.2 Abstract (active 150-word version, lines 426–429)

| # | Claim (abridged) | Status | Basis |
|---|---|---|---|
| A1 | Direct sensors address integration drift in inductive fusion diagnostics | **Supported now** | Field-standard motivation; manuscript refs ref3/ref4; independently corroborated by [S0068](https://doi.org/10.1088/1741-4326/ac8aad), [S0114](https://doi.org/10.1063/1.5038871) [EE] |
| A2 | HSX is "the first quasi-helically symmetric stellarator" | **Requires qualification (wording)** | Peer-reviewed support exists but with more precise wording: [S0128](https://doi.org/10.1088/1361-6587/adb179) calls HSX the "first and only stellarator experiment optimized for quasi-helical symmetry"; exact quasi-helical symmetry is impossible in principle [S0124](https://doi.org/10.1063/1.859916). Stage-10B/10D gate: match S0128's wording, do not paraphrase loosely. [EE] |
| A3 | 1 T on-axis field; up to 200 kW launched ECRH | **Supported now** (cited facility parameters, refs 13/14) | [SF]/[EE]; not re-derived here |
| A4 | Sensor fabricated, packaged, deployed in-vessel near plasma edge | **Supported now** (C001) | [SF] |
| A5 | "During 68 consecutive plasma discharge shots, the sensor remained functional" | **Requires qualification** | C002: the supplied archive documents shots 9–68 (60 distinct documented shots, including non-plasma coil-only shots such as shot 68 itself); the literal count "68 consecutive **plasma** discharge shots" was not reproduced from `test_note.docx` in any stage. A recount is a supplied-data analysis (§4.1). [SF]/[INF] |
| A6 | Clear transient responses associated with ignition and discharge dynamics | **Supported now** (raw traces in archive) | [SF] |
| A7 | Biased/unbiased and plasma/coil-only comparisons confirm Hall origin | **Supported now** (Fig. 4 logic; data present) | [SF] |
| A8 | Temporal correlation with diamagnetic-loop stored energy across three discharge classes | **Supported now, qualitatively** — currently uncorroborated by any correlation statistic; quantifiable from supplied data (§4.1) | [SF]/[INF] |

### 1.3 Introduction (lines 448–453)

| # | Claim | Status | Basis |
|---|---|---|---|
| I1 | Fusion/ML motivation (refs Ongena2016, Degrave2022, Anirudh2023) | Supported now (citations) | [EE] |
| I2 | Integrator drift mechanism in Mirnov-type diagnostics (refs 3–4) | Supported now | [EE]; note R1-03: the Mirnov sentence should re-cite ref2 (Endler W7-X = [S0131](https://doi.org/10.1016/j.fusengdes.2015.07.020)) |
| I3 | "conventional Hall-effect devices based on silicon, GaAs, InAs, InSb **cannot be deployed near the plasma edge**" | **Requires qualification** | Over-general as written: non-GaN Hall systems are deployed long-term in fusion devices — JET's InSb probe system operated 11+ years [S0068], ITER's steady-state set uses bismuth Hall sensors [S0113](https://doi.org/10.1063/1.4732077)–[S0115](https://doi.org/10.1063/1.5038812), plus CASTOR [S0070](https://doi.org/10.1007/s10582-006-0185-4)/[S0117](https://doi.org/10.1063/1.2971209), EAST [S0069](https://doi.org/10.1016/j.fusengdes.2008.07.045). The defensible statement is about *temperature/radiation headroom limits* of narrow-gap III-V near the plasma edge, cited as prior art, not a blanket impossibility. This rewrite is also the correct answer to R2-01. [EE]/[REC] |
| I4 | 2DEG physics and high mobility (refs 9–10) | Supported now | [EE] |
| I5 | AlGaN/GaN sensitivity stable to 576 °C (ref11 = [S0006](https://doi.org/10.1063/1.5139911)) | Supported now (as citation of prior group work) | [EE] |
| I6 | "we demonstrate … in-situ magnetic field monitoring … with a 1 MHz readout bandwidth across 68 consecutive shots" | **Requires qualification + new evidence** | Bundles three exposures: the measurand gap (AE-01), the underived 1 MHz figure (C003, R1-04/AE-07), and the shot-count wording (A5). [SF]/[INF] |
| I7 | Novelty framing (implicit: first such demonstration) | **Requires reframing** | The manuscript never states its "first" precisely, which let R2 attack device-granularity novelty. Defensible granularity (Stage 20 §5): first GaN/WBG 2DEG Hall sensor operated in-vessel in any magnetic-confinement device; first Hall sensor of any kind in a QHS stellarator — both bounded absence findings from the 231-source ledger, with the non-GaN fusion Hall lineage cited as prior art. "First fusion Hall diagnostic" is false and must never appear. [EE]/[REC] |

### 1.4 Methods (Section II, lines 455–487)

| # | Claim | Status | Basis |
|---|---|---|---|
| M1 | Wafer stack, fabrication process, octagonal plate (200 µm), 5×5 mm die (lines 457, Fig. 1) | Supported now (supplied facts; process consistent with cited group lineage ref10/ref11) | [SF] |
| M2 | Packaging: LCC, Al wire bonds, EPO-TEK 353ND, 150 °C vacuum bake, zirconia holder, graphite shield (line 465) | Supported now | [SF] |
| M3 | Bias from oscilloscope waveform generator (Keysight DSOX1204G); INA849 + 2×OPA814 chain (line 483) | Supported now | [SF]; consistent with project 02 `SPECS.md` (C004) |
| M4 | Total gain 200 V/V (line 483) | Supported now (C004, cross-consistent with SPECS.md) — not independently re-measured | [SF] |
| M5 | Bandwidth 1 MHz (line 483) | **Requires new evidence** | C003 `disputed_by_reviewer`; no derivation exists in the manuscript, its references, or `SPECS.md` (AE-07/R1-04). [SF] |
| M6 | Equations (1)–(2): V_H = S_v·V_bias·B; V_out = A_v·V_H + V_off (C023) | Supported now | [SF] |
| M7 | V_off bias-independent, temperature-dependent (ref15 Dowling dissertation) | Supported now as cited claim | [EE] (dissertation — not a peer-reviewed ledger source; acceptable as a citation, not counted toward the ledger) |
| M8 | Biased-vs-unbiased comparison isolates Hall response from offset/EMI/charge artifacts | Supported now (methodologically sound; Fig. 4 data exists) — strengthenable via the bias-scaling analysis in §4.1 | [SF]/[INF] |
| M9 | "Absolute calibration of V_off … remain future work" (line 487) | Supported now — the manuscript's own honest limitation (C005) | [SF] |

### 1.5 Results (Section III, lines 494–504)

| # | Claim | Status | Basis |
|---|---|---|---|
| R-1 | Shot sequence description (motor generators, 48 coils, ~800 ms ramp, 50 ms flat-top, 28 GHz ECRH) | Supported now (facility description, refs 13/14/16) | [SF]/[EE] |
| R-2 | Fig. 4(a) unbiased (63) vs biased (65); Fig. 4(b) plasma (65) vs coil-only (68) behavior | Supported now — shots 63/65/68 have corresponding raw files in the archive (`00_CONFLICT_LEDGER.md` non-conflict list) | [SF] |
| R-3 | "Across the 68 discharge shots, the shape and timing of this transient repeated reliably under comparable conditions, indicating stable sensor operation" (line 496) | **Requires qualification as written; upgradeable by analysis** | Currently a qualitative assertion with no statistic. A per-shot transient amplitude/timing distribution is computable from the 73 supplied scope files (§4.1) and would convert this into a defensible operational-repeatability claim (distinct from AE-03's *fabrication* repeatability, which needs new bench data). [SF]/[INF] |
| R-4 | Diamagnetic-loop comparison across three discharge classes; ~30 ms DAQ offset (line 504) | Supported now qualitatively; correlation statistic recoverable (§4.1) | [SF] |
| R-5 | "establishes that the … sensor can track plasma-dependent magnetic-field dynamics in real time" (line 504) | **Requires qualification** | True in the voltage/temporal domain only; "magnetic-field dynamics" in field units is exactly what is not yet delivered (AE-01). [INF] |

### 1.6 Figures

| Figure | Audit result |
|---|---|
| Fig. 1 (die schematic/optical) | No issues raised; supported. |
| Fig. 2 (packaging/in-vessel) | Supported; becomes more valuable if AE-08's system framing is adopted. |
| Fig. 3 (readout chain) | Supported; a revision should annotate the bandwidth-limiting element once AE-07/R1-04 is answered. |
| Fig. 4 (functional verification) | Supported by archive data (shots 63/65/68). |
| Fig. 5 (stored energy vs sensor output; shots 21/18/19) | Data supported ([SF]; shots 18–21 `.dat` files and the 73 scope CSVs re-verified present this stage; the per-shot scope-file mapping rests on Stage 00's `test_note.docx` audit); **presentation fails AE-05** (volts, not field units) and R1-05 suggests an overlay format. Conversion requires WP-C. |

### 1.7 Conclusion (line 506)

Restates A4–A8 (same statuses apply). Two additional findings:

1. **Future-work sentence partially conflicts with the mission scope rule
   [SF vs SF conflict]:** it promises "radiation and neutron irradiation
   characterization at a dedicated facility." The parent scope rule and
   MISSION.md state **no neutron/gamma experiments are planned** in Tim's
   experimental work; radiation belongs to the co-authored simulation-only
   TCAD paper (C024). **[REC]** In any revision, replace with: radiation
   response addressed via complementary TCAD modeling (co-authored, in
   preparation) and literature ([S0002](https://doi.org/10.1109/TMAG.2012.2196986),
   [S0054](https://doi.org/10.1149/2.0251602jss)), cited as outlook only. Promising an experiment that is not
   planned misleads reviewers and creates a future-work debt the next
   paper cannot pay.
2. The in-situ cross-reference plan (ref17 =
   [S0132](https://doi.org/10.1088/0029-5515/55/11/113012)) is the correct
   future-work anchor and aligns with WP-C/campaign plans — keep.

### 1.8 References (lines 551–613)

- 20 entries; DOIs present except ref14 (Almagri 1998, no DOI recorded) and
  ref15 (PhD dissertation). Spot-verified against the ledger: ref2=S0131,
  ref6=[S0066](https://doi.org/10.1088/1741-4326/aa7867),
  ref10=[S0004](https://doi.org/10.1109/JSEN.2019.2895546), ref11=S0006,
  ref12=[S0017](https://doi.org/10.1063/1.2201339), ref16/ref17 = HSX
  magnetics papers (ref17=S0132). No fabricated citation found. [EE]
- **Gap driving R2-03:** only four GaN-Hall-specific entries
  (ref10/11/12/15). The group's own most on-point GaN result — micro-tesla
  offset via current spinning, [S0005](https://doi.org/10.1109/LSENS.2019.2898157),
  published in *IEEE Sensors Letters itself* — is not cited. Also absent:
  recent GaN Hall work ([S0009](https://doi.org/10.1109/ises54909.2022.00071),
  [S0010](https://doi.org/10.1109/ACCESS.2025.3539435),
  [S0016](https://doi.org/10.1088/1361-6501/ac12fe),
  [S0012](https://doi.org/10.1063/5.0305414)) and most of the fusion Hall
  deployment lineage (S0069/S0070/S0113–S0115/S0117/[S0143](https://doi.org/10.1063/1.4894209)/[S0153](https://doi.org/10.3390/s21030721)).

---

## 2. Summary lists

**Claims exactly supported now (keep as-is in any revision):** A1, A3, A4,
A6, A7, M1–M4, M6–M9, R-1, R-2, R-4 (qualitative form), Fig. 1–4 content.

**Claims requiring qualification or rewording (no new data needed):**

1. A2 — QHS wording → match S0128 exactly.
2. A5 / I6 / R-3 — shot-count and repeatability wording → recount +
   quantify from supplied data (§4.1).
3. I3 — "cannot be deployed" → temperature/radiation-headroom framing with
   the non-GaN fusion Hall lineage cited as prior art.
4. I7 — novelty claim → re-centered "first GaN/WBG in-vessel; first Hall in
   a QHS stellarator" with named bounding prior art.
5. R-5 — "track magnetic-field dynamics" → voltage-domain/temporal wording
   until calibration lands.
6. Conclusion radiation sentence → TCAD/literature outlook only.

**Claims requiring new data before they can be made:**

1. Any tesla-denominated output, Fig. 5 in field units, absolute-field
   bounds (AE-01/AE-04/AE-05/R1-01 → WP-C bench calibration; blocked by the
   open ~109× anomaly C017). [PX → stage 40]
2. Fabrication-iteration repeatability statistics (AE-03/R2-02 → WP-B ≥3
   dies; die availability = advisor gate). [PX → stage 40]
3. A derived/measured bandwidth figure replacing the 1 MHz assertion
   (AE-07/R1-04 → chain analysis + bench sweep). [PX → stage 40]
4. Direct 1:1 field comparison against a conventional probe (R1-02 → UW
   data request first [GATE], else next campaign). [PX → stage 40]

---

## 3. Novelty-comparison dimensions for the GaN-sensor table (WP-A)

The AE asked for a performance comparison table (AE-02); R2's novelty
objection (R2-01) is answered at the same stroke if the table shows where
this work sits. No published review contains a unified GaN-Hall comparison
row set ([S0065](https://doi.org/10.1088/2631-8695/ac0838) has no GaN row) —
the table is itself a small novelty contribution. [EE]

**Recommended dimensions (columns):**

1. Material system / channel (2DEG vs bulk vs metal film)
2. Voltage- or current-scaled sensitivity (state which; normalize units)
3. Demonstrated field range
4. Bandwidth **with its evidentiary basis** (measured/derived/asserted)
5. Raw offset and offset after cancellation (µT-equivalent where given)
6. Noise floor / minimum detectable field (T/√Hz at stated frequency)
7. Demonstrated temperature range
8. Radiation-tolerance evidence (literature citation only — no new
   radiation experiments, per scope rule)
9. Active area / die size
10. Packaging / environment compatibility (UHV, bakeout, GDC survival)
11. Deployment context (bench / accelerator / fusion device; in-vessel vs
    ex-vessel)
12. Calibration status (uncalibrated / bench / traceable per
    [S0051](https://doi.org/10.5194/jsss-9-391-2020))

**Candidate rows:** GaN/WBG: this work; S0004; S0005; S0006; S0016; S0017;
S0009; S0010; S0012. Non-GaN high-performance III-V for contrast:
[S0011](https://doi.org/10.1109/JSEN.2024.3507799),
[S0014](https://doi.org/10.1109/JSEN.2014.2368074). Fusion-deployed non-GaN
Hall anchors: S0068 (JET InSb), S0113–S0115 (ITER bismuth), S0153
(ceramic-Cr), S0066 (gold-film/metal), S0070/S0117 (CASTOR), S0069 (EAST),
S0143 (CTH array).

**[GATE] carried from Stage 10D:** several candidate rows are
`metadata_only`/`abstract_metadata` in the ledger; every specific number
entering the table must first be re-confirmed against the primary PDF.

---

## 4. Recoverable from supplied data vs. data that does not exist

### 4.1 Recoverable by analysis alone (no hardware, no campaign)

From `../../07_HSX_august2025_results/hsx_20250821/` (73 `scope_N.csv`
voltage traces, `test_note.docx` shot manifest, shots 18–21 density/
stored-energy `.dat`, coil-current logs for shots 65/68 — spot-verified
this stage):

1. **Exact shot accounting** — recount plasma vs coil-only vs unbiased
   shots from `test_note.docx`; fix the "68 consecutive plasma discharge
   shots" wording (A5) with the true auditable numbers.
2. **Operational repeatability statistics** — per-shot ignition-transient
   amplitude/timing/shape-correlation distribution across all comparable
   biased plasma shots; converts R-3 from assertion to statistic. (Does
   **not** substitute for AE-03's fabrication-iteration statistics.)
3. **Quantified temporal correlation** — cross-correlation coefficient and
   lag between sensor output and diamagnetic-loop stored energy for shots
   21/18/19, including direct measurement of the stated ~30 ms DAQ offset.
4. **Bias-scaling check** — `test_note.docx` records 0.2–0.4 V bias
   settings; verifying response ∝ V_bias in-situ would materially harden
   the Hall-origin argument (M8) against EMI/charge-artifact alternatives.
5. **In-situ voltage-noise floor** — V/√Hz spectra in the HSX EMI
   environment from existing FFT pipelines (`.m` scripts present).
6. **Figure regeneration** — Fig. 4/5 reproduction and the R1-05 overlay
   re-plot (in volts today; in field units only after WP-C).

### 4.2 Does not exist in supplied data and cannot be recovered from it

| Missing item | Why unrecoverable | Path |
|---|---|---|
| Any tesla value; S_v; calibration factor | No sensitivity/gain-to-field chain anywhere in the archive (Group C inventory) | WP-C bench calibration [PX] |
| V_off of the real GaN die | Never measured; emulator result (C016) does not transfer | WP-C [PX] |
| Verified chain gain / transfer function / bandwidth | Asserted only (C003/C004) | bench sweep [PX] |
| In-vessel sensor temperature during shots | No temperature log in archive | future campaign instrumentation [PX] |
| Multi-die statistics | One module ever deployed (C007) | WP-B [PX] |
| Co-located B-dot/pickup field data for 2025 shots | Not in archive; UW may hold it | [GATE] UW data request |
| Parasitic characterization (bonds, LCC, cabling) | Never measured | bench [PX] |

---

## 5. Statistical/repeatability and calibration gaps (consolidated)

1. **Calibration** — the single blocking gap. No calibration attempt exists
   (C005); project 02's Helmholtz procedure is specified, not run (C013,
   conflict C6); the ~109× magnitude anomaly (C017) is an explicit
   do-not-calibrate-yet blocker that must close first. Norms to meet:
   traceable Hall calibration [S0051], GUM/Monte-Carlo uncertainty
   budget [S0220](https://doi.org/10.3390/s25051633), drift/Allan
   characterization [S0168](https://doi.org/10.1109/TIM.2007.908635).
2. **Fabrication repeatability** — n=1 module deployed; zero die-to-die
   data. Bench-satisfiable per the AE's own concession (AE-03). Templates:
   on-chip Hall-cell statistics [S0218](https://doi.org/10.3390/jsan2010085);
   JET's 18-sensor stability record [S0068] as the field's bar.
3. **Operational repeatability** — claimed qualitatively (R-3), quantifiable
   now from supplied data (§4.1.2) — the cheapest credibility win available.
4. **Offset** — the emulator spinning-current result (≥130× suppression,
   C016) is real bench evidence but is **not** sensor evidence; in the
   revision it may be described only as readout-architecture validation,
   clearly labeled emulator-based, if mentioned at all.

## 6. Bandwidth and parasitic evidence gap (consolidated)

The 1 MHz claim appears twice (lines 453, 483) with no derivation in the
manuscript, its references, or `SPECS.md` (C003). R1-04 asks how it was
established; AE-07 generalizes to bandwidth/parasitics as the quantities
that determine tracking fidelity and class comparison; AE-08 offers
packaging-parasitics novelty if quantified. What exists today: component
identities (INA849, OPA814) and an underived "1 MHz raw BW" note. What is
needed: a measured chain transfer function with the limiting element
identified (device vs amplifier configuration vs cabling/feedthrough vs
acquisition), a bandwidth column in the WP-A table, and — opportunistically
— a packaging-parasitic characterization supporting AE-08's system framing.
Until then, the revision must not restate 1 MHz. [PX → stage 40]

## 7. Concise revision map (diagnosis only — no edits performed)

| Manuscript location | Action in revision | Answers | Evidence prerequisite |
|---|---|---|---|
| Title (370) | Keep only with field-unit results delivered | AE-01 | WP-C |
| Abstract (428) | Recount shots; S0128 QHS wording; add calibrated headline number (S_v ± u, field-unit result); drop/qualify "68 consecutive plasma" | AE-01, A2, A5 | WP-C + §4.1.1 |
| Intro ¶1 (449) | Re-cite ref2 at Mirnov mention | R1-03 | none |
| Intro ¶2 (451) | Rewrite I3 as headroom argument; cite fusion Hall lineage as prior art | R2-01, I3 | none |
| Intro ¶3 (453) | Precise two-part first-claim; remove unsupported 1 MHz | I7, R1-04 | bench sweep for any stated BW |
| Methods II.C (483–487) | State measured gain/BW with basis; add calibration summary sentence(s) per R1's page-limit concession | AE-04, AE-07, R1-01 | WP-C + sweep |
| Results III.A (496) | Replace qualitative repeatability with §4.1.2 statistics; add bias-scaling check | R-3, M8 | analysis only |
| Results III.B (504) | Field-unit Fig. 5 with uncertainty bands; overlay format; quantified correlation + lag | AE-05, R1-05, R-4 | WP-C for units; analysis otherwise |
| NEW: comparison table | Insert WP-A table (§3) | AE-02, R2-01, R2-03 | analysis + primary-PDF re-confirmation |
| NEW: repeatability | WP-B multi-die bench statistics + single-module explanation | AE-03, R2-02 | WP-B + team input |
| Conclusion (506) | Remove neutron-facility promise → TCAD/literature outlook; keep S0132 cross-reference plan | §1.7 | none |
| References | Add S0005 + GaN set + fusion-deployment set within the 4-page/reference-column budget | R2-03 | none |

**Fit check [INF]:** SENSL's 4-page limit (confirmed policy, see
[`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md) §4)
is feasible because R1 explicitly allows calibration as text discussion,
the table replaces prose, and Fig. 5's overlay consolidates panels; the
likeliest cut is shortening III.B's discharge narratives (also AE-06's
request).

## 8. Flags for later stages

1. **Never describe the manuscript as published (2023 or otherwise)** in
   any revision, preprint, cover letter, or response letter — conflict C1
   controls; it is a declined 2026 submission with an invitation to
   resubmit under a new ID.
2. Stage 40 owns the experiment specifications for WP-B/WP-C, the anomaly
   closure, the bench sweep, and the UW co-located-data request (R1-02).
3. Stage 50 owns the pre-disclosure IP screen the advisor required before
   any arXiv posting (user request, `../inputs/ORIGINAL_REQUEST.txt`).
4. The radiation future-work sentence (§1.7.1) must also be reconciled in
   project-03 planning documents when those are next revised (outside this
   mission's write scope).
5. 75/231 ledger rows are metadata-only: any number quoted into the WP-A
   table needs primary-source re-confirmation first (Stage 10D gate).
