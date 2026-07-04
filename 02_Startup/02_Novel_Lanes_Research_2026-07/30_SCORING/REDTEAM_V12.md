# RED TEAM — V12 Heavy-REE magnetic-signature triage sensor (PhD-LANE FLAGGED)

Raw 83.2. Sources: `REDTEAM_V12_sources.json` (RT-V12-01…15).

## 1. Novelty verification (G7-NOVEL)
Three nearest ledger neighbors: **C33** (Hall-array coil QC inversion, cryogenic — C12 cluster): same modality family (field map + inversion QC of a magnetic object) but different buyer (recyclers vs coil/magnet manufacturers) and different product (conveyor routing head vs cryo bench QC) — adjacency is capability-level, not a re-parameterization. **C31** (triaxial OPM): V12 consumes magnetometers as components; it does not sell sensors. **C40/RID-016** (second-life battery grading): no battery packs anywhere in the V12 flow — clean. Disguise check vs PhD work: battery magnetic imaging inverts fields from **injected currents** in live cells; V12 inverts **remanent magnetization** of passive scrap — shared math/toolchain only, no shared buyer or object. **Verdict: NOVEL** (PhD-lane slot 1/2 correctly consumed). Note: novelty ≠ whitespace — see §3.

## 2. Physics reality check — the Dy-coercivity problem (kill-grade)
The headline claim (grade high- vs low-Dy/Tb passively) conflicts with magnetostatics. An external array measures stray field, which is set by the magnetization distribution M(r) (≈Br × geometry × magnetization state). Dy's signature is **intrinsic coercivity HcJ — a hysteresis property with zero external-field observable**. Grade floors: standard ≥955 kA/m vs EH ≥2388 kA/m at overlapping Br bands (N35 and N35EH share the same Br spec; EH carries ~8–10 wt% Dy) [RT-V12-07]. Worse: post-2012 EV traction magnets are grain-boundary-diffusion types explicitly engineered so Br is "comparable to the magnet with no element replacement" [RT-V12-08] — the Br→Dy mapping is many-to-one exactly on the high-value feedstock. Confounds stack: unknown thermal/field knockdown (an overheated motor magnet reads "weak"), flux shunting by stator laminations, superposed multi-magnet fields, moving-steel background. Coercivity is only measurable by applied-field hysteresis — Hirst PFM08-class pulse magnetometry drives samples to 10.5 T in an enclosed fixture [RT-V12-03]; not doable at conveyor standoff. What survives passively: ferrite vs RE (5–10x moment gap), magnetized-vs-dead, coarse NdFeB/SmCo (overlapping Br bands — marginal). That surviving product is a gaussmeter array, not a $80–250K instrument.

## 3. Hidden competition (the one-pager's "no inline REE-triage instrument exists" is false)
- **SUSMAGPRO** (H2020, Pforzheim + RISE, 2019–2023): sensor systems + robotic sorting lines to identify/localize NdFeB in WEEE, pilot line built [RT-V12-01][RT-V12-02]. Direct prior art for the exact concept.
- **Element-specific inline sorting exists commercially**: STEINERT LIBS/XRF chute sorters [RT-V12-10], TOMRA e-scrap spectral/electromagnetic sorting incl. AUTOSORT PULSE dynamic LIBS (2023) [RT-V12-11]. LIBS quantifies Dy in used coated NdFeB to <10% relative uncertainty, even at 1 m standoff — published for sorting-prior-to-recycling (CEA MAGNOLIA) [RT-V12-04]. Handhelds: SciAps XRF/LIBS market REE apps [RT-V12-06]; XRF Dy is degraded by Fe-Kα/Dy-Lα overlap [RT-V12-05], pushing users to LIBS — either way $30–50K spot-check beats a $150K inference head.
- **Magnet-QC instrument incumbents**: Magcam's 128×128 Hall-array field camera + inversion software (incl. rotor inspection) is V12's modality already productized [RT-V12-12]; Hirst owns coercivity QC [RT-V12-03].
- **Buyers self-solve**: HPMS hydrogen decrepitation ingests magnetized scrap and outputs demagnetized powder — HyProMag doesn't need magnetized-state detection [RT-V12-09]; Cyclic markets MagCycle as feedstock-agnostic [RT-V12-15]; Chinese practice is sampling assay of REE/Dy/Tb into 5 scrap classes at dismantler labor cost [RT-V12-14], with 华宏科技/鑫泰科技 as integrated equipment+recycling cloners [RT-V12-13].

## 4. Bear case & WTP
By 2031: Dy claim retracted after first pilot; product descopes to magnet-presence/state gating that Steinert/TOMRA sell as line modules and a $2K fluxgate approximates. TAM honesty: ~15–40 magnet-recycling sites globally by 2030; auto shredders won't pay (magnets <0.1 wt% of feed value). 100 heads × $150K = $15M **cumulative** — sub-venture-scale. No named buyer has stated WTP; the cited pains are yield/purity, which LIBS/XRF address element-directly.

## 5. Founder-fit anti-anchoring (PhD lane)
This is capability-anchored ideation: "own a magnetometer array → point it at scrap." The binding constraints — coercivity/composition discrimination (materials physics), scrap-yard SNR, selling instruments to capital-poor recyclers — are not addressed by inversion skill. Leverage is partial; familiarity inflated C1.

## 6. Score adjustments (±1, reasons)
- C1 5→4: anti-anchoring — skill doesn't touch the binding physics problem.
- C2 4→3: headline edge physically unsupported (GBD Br-decoupling); residual edge commodity.
- C3 4→3: lead buyers demonstrably don't need it (HPMS self-demag, feedstock-agnostic MagCycle, sampling assay).
- C6 5→4: real Dy grading needs applied-field/elemental subsystem — new TRL path, not 12-month v1.
- C7 4→3: SUSMAGPRO prior art + TOMRA/Steinert/Magcam/Hirst/SciAps crowd every practical flank.
- C10 5→4: pilot-gated sales into ~dozen buyers stretch time-to-revenue.
- Unchanged: C4=3, C5=4, C8=4, C9=4, C11=3.
**Adjusted total: 70.8** (−12.4).

## 7. Steelman
If the head fuses passive field maps with a modest applied-field susceptibility/eddy probe and a LIBS spot-checker, a routing station that lifts HPMS feed purity a few points could pay for itself at 10,000 t/yr plants — and the DoW/CRMA build-out is buying equipment now, before workflows ossify. The founder can genuinely build that fused instrument faster than a sorting OEM can hire magnetics inversion talent.

**Verdict: kill-probability 75% · adjusted 70.8 · G7-NOVEL pass (NOVEL) · biggest objection: Dy lives in HcJ, and HcJ does not radiate.**
