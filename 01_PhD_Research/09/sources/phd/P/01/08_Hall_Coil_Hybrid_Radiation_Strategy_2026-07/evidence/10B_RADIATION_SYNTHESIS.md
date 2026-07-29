# Stage 10B synthesis — radiation, temperature, and reliability literature

Ledger: `evidence/10B_RADIATION_SOURCES.csv` (79 rows; 76 `verified_peer_reviewed`,
3 `peer_review_uncertain`; 0 duplicate DOIs/source_ids/normalized titles within the
file; 4 rows independently cross-confirmed by, and flagged as duplicates of, this
mission's own `10A_HYBRID_SOURCES.csv` or the `06` baseline — R005/R077 vs 10A
H007/H031, R066/R069 vs 06 S0082/S0151). Source IDs below (`R001`–`R079`) refer to
that ledger.

Claim-status labels follow root `CLAUDE.md`: **Observed** = directly stated in an
inspected source; **Derived** = calculated here from documented inputs; **Inferred**
= reasoned interpretation, assumptions stated; **Proposed** = future
design/test; **Unknown** = evidence insufficient.

## 1. Search method and access limitations

Eight parallel research passes covered the four required evidence layers: direct
Hall-device neutron [domain A], gamma/TID [domain B], proton/electron/heavy-ion
[domain C]; enabling GaN/AlGaN/AlN physics [domain D] and Si/SOI/GaAs/InSb/InAs
physics [domain E]; measurement-chain electronics [domain F] and coil/insulation/
integrator/fiber-optic [domain G]; fusion qualification/dosimetry practice
[domain H]. Every candidate was checked against Crossref/PubMed/publisher metadata
before acceptance; hallucinated or unresolvable DOIs were dropped rather than
guessed (see per-row `verification_basis`/`notes`). A recurring, honestly-recorded
limitation: ScienceDirect, AIP Publishing, IEEE Xplore, ResearchGate, and MDPI
publisher pages returned HTTP 403 to automated fetch for a large fraction of
candidates. Where this happened, bibliographic identity (title/authors/DOI/venue)
is independently Crossref-verified, but quantitative claims are drawn from
secondary aggregation and are explicitly marked "not independently confirmed" in
the ledger rather than asserted as read fact. This is an **access limitation**,
not an evidence gap — treat every such number as needing full-text re-verification
before it is load-bearing in a compensation-strategy calculation.

## 2. Mechanism primer (Derived/Inferred framing for the sections below)

Three physically distinct damage classes recur across the ledger and must not be
merged:

- **Displacement damage** — an incident particle (neutron, proton, electron, heavy
  ion) knocks a lattice atom off-site, creating vacancy-interstitial (Frenkel)
  pairs, clusters, or (for heavy ions/high-fluence neutrons) amorphized regions.
  Governs mobility loss, carrier removal, and deep-level trap formation in the
  *semiconductor bulk*. [R035, R040, R022, R023, R026, R027]
- **Ionization / total ionizing dose (TID)** — energy deposited in oxides,
  insulators, and depletion regions creates trapped charge (interface states,
  fixed oxide charge) without necessarily displacing lattice atoms. Dominates
  gamma, X-ray, and low-LET-particle effects on *oxides, packaging, and analog
  electronics*, and on SOI buried-oxide/STI structures. [R024, R044, R045, R047]
- **Transmutation** — neutron capture converts a lattice atom to a different
  element (e.g., Ga→Ge in GaN [R025]; In/Sb capture products in InSb [R001]).
  This is the mechanism the fission-vs-fast-neutron contrast in §7.1 turns on.

A given particle can trigger more than one class (e.g., 14 MeV neutrons cause both
displacement damage and, via secondary reactions, some ionization); the ledger's
species/spectrum field is the operative unit, not a coarse "radiation level."

## 3. Direct Hall-device irradiation — material × species matrix

**Observed**, with source IDs, magnitude where confirmed, and reversibility:

| Material | Neutron | Gamma/TID | Proton/electron/heavy-ion |
|---|---|---|---|
| **InSb** | Sensitivity drop under fission-spectrum (thermal-inclusive) neutrons at ~1e16 n/cm² but *stable under purely fast-neutron spectrum at comparable fluence* [R001, R002]; mobility down 75–90% (avg 83%) at 6.6–7.0e17 n/cm² fast-neutron fluence, carrier density direction doping-dependent [R003]; no numeric neutron-degradation figure independently confirmed for the JET/ITER-fielded RHP probes beyond the 06-baseline's own operational-stability claim | none found (direct InSb) | R038: 10-MeV protons, 2e16 cm², limiting Fermi level drives material to p-type regardless of starting doping — enabling-physics only, not a packaged-sensor result |
| **GaAs** | Conductivity/Hall mobility decrease with fluence 1e13–3e15 n/cm² at 300–420 K, n/p ratio inversion signature at highest fluence [R043] | Co-60 gamma: stabilizing regime near (8–10)e3 Gy, degrading above it; I-V and noise-spectral-density change, passive/unbiased [R009, R010]; Wang & Yang report GaAs *more* radiation-sensitive than Si/Ge under gamma/beta [R008] | none found (direct device) |
| **Si / SOI** | Hall-effect bulk characterization only (detector-grade Si, not packaged sensor); shallow-donor removal + deep-center creation model [R007]; universal material-independent leakage-current annealing behavior 1e11–1e15 n/cm² [R040] | Wang & Yang: Si/Ge *more* radiation-resistant than InSb/GaAs under gamma/beta, attributed to larger displacement threshold energy [R008]; FD-SOI Hall TID response is **simulation-only** (+29% sensitivity, efficiency −34%, offset −53%, TCAD) [R044] | 6.6 MeV electrons, Hall/magnetoresistivity defect analysis on bulk Si [R020, R021] |
| **GaN/AlGaN/AlN** | Neutron+gamma combined-exposure synergy is *non-additive* and direction-dependent (leakage sub-additive, cascode V_th super-additive) [R028]; no bare-Hall-plate GaN neutron dataset found — all GaN neutron evidence is HEMT/2DEG-structure enabling physics | AlGaN/GaN HEMT V_th shift in two dose regimes: reversible <3 krad(SiO2), persistent oxide-trapping to ≥2 Mrad in MOS-HEMT [R024]; partial recovery of carrier transport after 200°C/25 min anneal, gamma source unconfirmed [R033] | 2 MeV protons: mobility −28.9%, 2DEG density −12.1%, interface broadened 2.2 nm at 6e14 cm⁻² [R022]; 1.8 MeV protons to 3e15 cm⁻² degrade mobility/2DEG density in AlN-interlayer HEMT [R023]; AlGaN/GaN **micro-Hall sensor** proton series (seed papers): slight effect at 1e13 p/cm² rising with fluence, partial recovery via anneal, enhancement of negative-magnetoresistance sensitivity at cryogenic temperature [R012–R016]; Xe heavy-ion DLTS traps at 0.07/0.48 eV, leakage +10 orders of magnitude [R026]; electron DLTS traps at 0.20 and ~0.90 eV [R027]; He-ion at 25 K, persistent (not annealed to 443 K) mobility/carrier loss [R031] |
| **Bismuth / metallic (Cr, Cu)** | Copper-active-layer Hall sensor on Al2O3: **no measurable sensitivity change** to 1e18 n/cm², sensitivity flat 100–250°C [R071] | none found (direct device) | none found |
| **Graphene-on-SiC** (adjacent, not Hall-plate III-V/Si) | Mobility −43%, sheet density −39% at fast-neutron fluence comparable to InSb test [R003]; defect density ~4e10 cm⁻², partial self-healing of H-intercalation above 200°C but lattice damage largely persistent [R004] | none found | none found |
| **Packaged Hall ICs** (switch/angular-position, not bare plate) | none found | TID <100 krad(Si) tolerated by design [R011]; ≤1% supply-current shift, SPI/analog errors reversible via high-T anneal [R018]; 40 krad(Si) parameters-within-limits claim, un-disaggregated species for the companion SEE test [R019] | Heavy-ion SEE to LET 67.7 MeV·cm²/mg: no SEL/SET observed [R018]; SEE campaign of unconfirmed species [R019] |

**Key contradiction, retained per policy, not resolved by merging:** R001/R002 show
InSb Hall sensitivity is *stable* under a purely fast-neutron spectrum but *drops
significantly* under a thermal-inclusive fission-reactor spectrum at a comparable
total fluence, with the authors' own mechanism attribution being **transmutation**
(In/Sb thermal-neutron capture) rather than displacement damage. This means a
"neutron fluence" number alone is not a sufficient predictor for InSb Hall drift —
the thermal/fast spectral split matters, and any qualification campaign that
reports only integrated fluence without spectral shape is not directly comparable
to R001/R002's result. R071's Cu-Hall-on-ceramic null result at higher total
fluence (1e18 n/cm²) is *not* contradictory with the InSb finding — it is a
different active material (metallic, not semiconductor) and is consistent with
Wang & Yang's [R008] mechanistic claim that metals/Si/Ge tolerate displacement
damage better than InSb/GaAs due to displacement-threshold-energy differences —
but note R008's own species (gamma/beta) differs from R071's (neutron), so this is
an **Inferred**, cross-species plausibility argument, not a directly matched
comparison.

## 4. Enabling device/material physics beyond the direct-Hall dataset

**GaN/AlGaN/AlN** (the user's own device family) has by far the deepest enabling
literature of any material in this ledger (12 rows, R022–R033), but *zero* of it
is a bare GaN/AlGaN Hall-plate irradiation measurement — every quantitative
mobility/carrier-density/trap number comes from HEMT or 2DEG test structures
[R022–R024, R026, R027, R031], AlN ceramic coupons [R029, R030], or an MD
simulation [R032, simulation-only]. The proton-irradiated *micro-Hall-sensor*
papers [R012–R016] are the closest direct analog and confirm the same qualitative
direction (mobility/sensitivity degradation, partial thermal recovery) but with
fluence/magnitude values that could only be independently confirmed at the
"slightly affected at ~1e13 cm⁻²" level — precise dose-response curves for a
fabricated GaN Hall sensor remain **Unknown**. Transmutation doping [R025] shows
Ga→Ge conversion is a real, permanent (non-annealable) side channel distinct from
trap-formation, requiring a 950°C anneal merely to activate/uniformize — far
above any realistic in-service anneal temperature, so **Inferred**: transmutation
products in a GaN Hall die are likely permanent under realistic thermal budgets.

**InSb/InAs/GaAs** enabling physics [R034–R039, R041–R043] is materially
important because InSb-on-GaAs is the *actual* material system already fielded at
JET/ITER (06 baseline). The Brudnyi group's proton-irradiation results [R037,
R038] show both InAs and InSb converge to a **material-specific limiting Fermi
level** at high fluence regardless of starting doping polarity — mechanistically
explained by Walukiewicz's Fermi-level-stabilization theory [R036]. This is a
proton (not neutron) result and must not be silently applied to the fielded
probes' neutron environment, but it is a plausible **long-term-limit** mechanism:
if true, a sufficiently irradiated InSb/InAs Hall element's electrical parameters
should asymptote toward a material constant rather than diverge indefinitely — a
testable, falsifiable prediction for a compensation strategy, not yet confirmed
under neutron exposure. Logan et al. [R042] adds a specific, quantified warning
against extrapolating between species even within one material family: for
InAs/InAsSb, gamma damage per unit NIEL is ~14× the proton-scaled prediction,
because proton cascades self-anneal more efficiently than gamma-produced isolated
Frenkel pairs. **This directly contradicts any NIEL-based proton→gamma
extrapolation** a compensation model might be tempted to use for InSb-family
Hall material.

**Si/SOI** enabling physics [R040, R041, R045] is the thinnest of the three
material families relative to its role — Moll et al.'s leakage-current
material-independence result [R040] is detector-physics (not Hall), and the two
SOI-specific TID papers are either simulation-only [R044] or address a mechanism
(STI-oxide-corner trapping [R045]) explicitly *not* the buried-oxide/BOX
mechanism most often invoked for SOI Hall-sensor radiation tolerance claims.

## 5. Measurement-chain failure pathways (electronics vs coil, kept separate)

### 5.1 Bias/AFE/ADC/cabling/packaging electronics [R046–R055]

- **Bias/instrumentation op-amps**: mixed neutron+gamma damage in a bipolar OP07
  is *synergistic*, not additive, with the input bipolar stage most sensitive
  [R046] — the same non-additivity pattern seen for GaN HEMTs [R028], suggesting
  synergy effects are a general risk for any mixed-field (fusion) qualification,
  not a GaN-specific artifact. BiCMOS input bias current is reported as the most
  dose-rate/temperature-sensitive parameter in ELDRS-type testing, though this
  paper's own numbers are unconfirmed [R047].
- **ADCs**: a 17-part commercial-ADC TID/SEU evaluation exists as a methodology
  reference [R051] but its numeric thresholds were not independently retrievable
  — **Unknown** what specific TID margin a COTS 12–14-bit ADC offers.
  Radiation-hardened instrumentation-amplifier *designs* targeting 1 MGy exist
  but are simulation-only [R050] — no fabricated-and-irradiated confirmation.
- **SET risk**: a single ionizing-particle strike in an op-amp's bias/startup
  circuitry can produce a millisecond-scale output corruption [R052] — a
  transient-fault mode distinct from TID drift, relevant to any DC Hall-bias
  measurement that assumes slowly-varying error only.
- **Cabling**: two distinct, non-overlapping failure mechanisms are documented for
  mineral-insulated (MI) cable — radiation-induced EMF (RIEMF, §5.2) and a
  *separate*, combined radiation+thermal-gradient core-to-sheath current
  asymmetry that Vermeeren & Wéber [R048] found to be *uncorrelated* with
  core-to-core RIEMF voltage; Vermeeren [R049] additionally identifies induced
  current in copper-core (but not steel-core) MI cable as driven by a *named,
  distinct* mechanism — beta decay of the neutron-activation product ⁶⁶Cu — which
  is a materials-selection lever (steel core avoids this specific pathway).
  Organic-insulation (PET/polyimide) radiation-induced conductivity is governed by
  a two-exponential deep-trap model [R053], a different physical mechanism again
  from MI-cable RIEMF. Connector/feedthrough-level qualification evidence is thin
  — only one programmatic ITER in-vessel electrical-integration reference was
  found [R054], with no independently-confirmed numeric qualification limits.
- **Current-sense amplifiers** (the closest published analog to a Hall
  bias/excitation front end) have TID test literature [R055] but content beyond
  bibliographic identity could not be verified — flagged as a real evidence gap,
  not a negative result.

### 5.2 Coil / insulation / integrator / fiber-optic [R056–R070]

- **RIEMF** (radiation-induced electromotive force in MI-cable coil leads) is the
  best-documented coil-adjacent failure mode, with a five-paper cluster spanning
  1997–2004 [R056–R060] establishing it as a real constraint (ITER target: keep
  non-inductive voltage well below 1 µV for 3000 s long-pulse operation, per
  secondary-sourced figures in R056) and separating MgO from Al2O3 insulation
  chemistry [R057] and a theoretical model [R059] from its hardware validation
  [R060].
  - **Contradiction/precision gap**: none of R056–R060's quantitative dose,
    fluence, or temperature conditions could be independently confirmed from
    primary text in this pass (all publisher pages blocked) — the *existence* and
    *qualitative severity* of RIEMF is well-established, but a specific
    dose-to-RIEMF-magnitude curve is **Unknown** pending full-text retrieval.
- **Insulation material class**: a matched cryogenic-temperature pair directly
  compares organic (Kapton/polyimide [R061]) against ceramic (alumina [R062])
  insulation under combined fast-neutron+gamma exposure — the qualitative
  organic-vs-ceramic hierarchy assumed elsewhere in fusion diagnostics literature
  has at least this one matched-condition experimental basis, though both are
  cryogenic (4 K–range) tests and may not transfer directly to room/elevated-T
  coil operation. A separate FRP (fiber-reinforced-plastic) magnet-insulation
  paper [R068] adds a mechanical (interlaminar shear strength) rather than
  electrical failure metric at liquid-helium temperature.
- **Fiber-optic (Faraday) current sensor** — the ITER-baseline coil-adjacent
  alternative — has the single strongest *real-fusion-neutron* dataset in this
  entire ledger: Gusarov et al. [R063] report FOCS performance during actual JET
  D-T (DTE2) operation at ~8.5e20 total D-T neutrons, with Verdet-constant
  shot-to-shot variation of ±4% and no disqualifying degradation, continuously
  cross-validated against the Continuous External Rogowski (CER) coil [R077 is
  the pre-campaign baseline for the same comparison]. A companion paper [R064]
  isolates gamma-only Verdet-constant sensitivity in the same fiber type, and a
  third [R065] reports real-time optical-fiber attenuation monitoring during and
  between individual D-T pulses. This is the only material system in the ledger
  with (a) real 14 MeV D-T fusion-neutron exposure, (b) a magnetic reference
  channel for cross-validation, and (c) multiple independent papers from an
  active, ongoing research program — a strong template for what a Hall+coil
  qualification campaign would need to produce to reach comparable evidentiary
  strength.
- **Coil mechanical/failure evidence**: JET's in-vessel Mirnov coils suffered
  documented "severe faults" attributed to combined radiation+electromagnetic
  (disruption) stress, driving a Ti-wire-to-Cu-alloy-wire redesign [R066] — the
  two stressors are not disaggregated in available text, so radiation's specific
  causal share is **Unknown**, but this is real evidence that coil failure in a
  fusion environment is observed, not merely hypothesized.
- **Effective-area calibration practice**: the ITER Continuous External Rogowski
  program [R069, R070] documents a dedicated calibration rig (effective axis to
  ~0.1 mrad) and an installation/qualification procedure, but no radiation-induced
  effective-area *drift* measurement was found — the calibration method is
  documented, the radiation sensitivity of that calibrated quantity is
  **Unknown**.
- **Timing/reference electronics**: only one source was found and verified —
  quartz-crystal-oscillator radiation-induced frequency shift [R067], general
  space-electronics context, not fusion-specific, with no quantitative content
  independently confirmed. This is the thinnest-covered sub-topic in the entire
  ledger (topic tag `measurement_chain_integrator` appears on only 1 of 79 rows) —
  **flagged as an explicit evidence gap**, not resolved by this search.

## 6. Fusion qualification and calibration practice [R071–R079, plus R063/R077 above]

Dosimetry practice in this ledger is activation-foil-based almost without
exception: VERDI multi-foil detectors were benchmarked at a 14 MeV D-T reference
generator (ENEA FNG) [R076] before real deployment at JET D-D, where they agreed
with an independently determined flux to within 8% [R075]; a parallel TU Dresden
program built and qualified a foil-activation spectrometer specifically as an
ITER-TBM neutron-environment surrogate, explicitly noting its irradiation-position
flux is 3–5 orders of magnitude below full-power ITER-TBM flux [R073, R074] — a
concrete, quantified example of the surrogate-facility-to-target-environment gap
that any Hall-sensor irradiation test campaign would also face. KSTAR's activation
system [R078] and the copper-Hall-sensor paper's LVR-15 reactor test [R071]
extend fusion-qualification practice beyond the ITER/JET/DEMO/W7-X set already
saturating the `06` baseline. No source in this ledger describes an **in-situ,
in-irradiation** (as opposed to pre/post) electrical calibration of a Hall sensor
specifically — the closest analog is FOCS's continuous cross-validation against
the CER coil during actual D-T operation [R063], which is a coil-adjacent, not
Hall, precedent.

## 7. What can be modeled, monitored, calibrated, or only bounded

Framed against the `DECISION_FRAMEWORK.md` state model
`y_H = S_H(t) B(t) + b_H(t) + n_H(t)`, `y_C = K_C(t) dB/dt + b_C(t) + n_C(t)`:

- **Modelable (Derived/Inferred mechanism exists, needs device-specific
  calibration)**: TID-driven threshold/offset shift with a documented reversible
  low-dose / persistent high-dose split for AlGaN/GaN-family electronics [R024];
  the Fermi-level-stabilization limit for InSb/InAs under proton exposure
  [R036–R038] as a bounding asymptote (Inferred, not confirmed under neutrons);
  RIEMF as a coil-signal-chain additive error term with an established but
  imprecisely quantified magnitude [R056–R060].
- **Monitorable (a proxy or witness channel exists in the literature)**:
  activation-foil dosimetry is a mature, cross-validated fluence monitor
  [R072, R075, R076, R078]; temperature is explicitly tracked alongside radiation
  in several enabling-physics papers [R003, R022, R037, R038] and would need to
  be a first-class monitored state per `DECISION_FRAMEWORK.md`'s calibration
  table.
- **Calibratable in principle, unconfirmed in practice for Hall gain**: no source
  in this ledger (or, per the 10A hybrid-lane synthesis, in that lane either)
  demonstrates an in-situ, in-irradiation recalibration of Hall *sensitivity*
  (S_H) using an independent reference while under active neutron/gamma exposure.
  JET's InSb RHP self-recalibration (06-baseline evidence) uses a same-die
  microsolenoid, i.e. same-technology self-test, not a material-diverse
  reference, and is a pre-existing 06 finding, not new here.
- **Only boundable, not currently modelable from this ledger**: exact
  dose-to-RIEMF-magnitude and dose-to-Hall-sensitivity-drift curves under a
  *combined* real fusion neutron+gamma+thermal environment — every quantitative
  curve found is either single-species (proton-only, neutron-only, or
  gamma-only) or, where combined [R028, R046], demonstrates non-additive synergy
  whose sign is structure-dependent and therefore not extrapolatable from
  single-species data without an explicit, tested combined-field model.
  Connector/feedthrough radiation qualification and integrator/timing-reference
  radiation sensitivity are bounded only by general programmatic statements
  [R054, R067], not quantitative curves.

## 8. Evidence gaps for fusion-relevant neutron/gamma conditions

1. **No bare GaN/AlGaN Hall-plate device has been irradiated and reported in the
   peer-reviewed literature under any neutron spectrum** (fission, fast, or 14 MeV
   D-T). All GaN neutron evidence in this ledger is HEMT/2DEG-structure or bulk
   AlN-ceramic enabling physics [R022–R031]. This is the single largest gap
   relative to the user's own device family.
2. **14 MeV D-T-specific direct Hall-device data is essentially absent.** Only
   R028 (GaN HEMT, not a Hall plate) uses real 14 MeV neutrons; every direct
   Hall-sensor neutron result [R001–R007, R071] uses fission-reactor or unspecified
   fast-spectrum sources. The FOCS papers [R063–R065] are the only true 14 MeV
   D-T *in-machine* radiation-effects dataset in the entire ledger, and they are
   not a Hall device.
3. **Combined-field (neutron+gamma+temperature, simultaneously) direct Hall-device
   data does not exist in this ledger.** The only combined-exposure electrical
   dataset found is for GaN HEMTs [R028] and a bipolar op-amp [R046], both
   showing non-additive synergy — a warning that single-species Hall data cannot
   be safely summed to predict mixed-field behavior, but not itself a Hall-device
   answer.
4. **In-situ (during-irradiation, not pre/post) Hall-sensitivity calibration
   against a material-diverse reference is unreported anywhere found**, for any
   material.
5. **Integrator/timing-reference electronics radiation sensitivity is
   single-source and space- (not fusion-) contextualized** [R067].
6. **Connector and feedthrough (as opposed to cable-material) radiation
   qualification data is programmatic, not quantitative** [R054].
7. **Metallic/ceramic Hall (Bi, Cr, Cu) neutron data is single-source** [R071] and
   reports a null result at a single fluence/temperature combination — too thin to
   confirm or bound a general metallic-Hall radiation-tolerance claim.

## 9. Acceptance-gate status

- 79 unique rows in `evidence/10B_RADIATION_SOURCES.csv`; 76 `verified_peer_reviewed`
  (≥45 gate met with margin), 3 `peer_review_uncertain` (R015, R016, R033 — IOP/AIP
  conference-proceedings items, individually flagged, not counted toward the gate).
- 22 direct Hall-device or Hall-system rows (20 `verified_peer_reviewed`), exceeding
  the ≥15 target: 8 neutron [R001–R007, R071], 6 gamma/TID [R008–R011, plus R018/R019
  dual-tagged], 10 proton/electron/heavy-ion [R012–R021, plus R018/R019 dual-tagged].
- Radiation species/spectrum, dose/fluence, temperature, and access level are kept
  in dedicated `claims_supported` sub-fields per row, never silently merged across
  species (see explicit species-separation notes on R018, R019, R028, R042, R046).
- Sensor-material evidence (§3–4) and electronics evidence (§5) are reported in
  separate ledger topic-tag families (`direct_hall_*`/`enabling_physics_*` vs
  `measurement_chain_*`) and separate synthesis sections.
- Contradictory results are retained, not resolved by omission: §3's InSb
  fission-vs-fast-spectrum contrast, §4's proton-vs-gamma NIEL-scaling
  contradiction [R042], and §5.1/§4's cross-domain non-additivity finding
  [R028, R046] are all flagged with their plausible causes rather than merged.
- 4 rows are flagged as cross-lane/baseline duplicates (R005/R077 vs this
  mission's 10A ledger; R066/R069 vs the `06` baseline) — retained per SOURCE_POLICY
  (a source may support multiple topic quotas / appear relevant to multiple
  lanes) but explicitly marked so stage 10D's final-ledger merge does not
  double-count them.
