# P3R2 Batch E — Seeds with Japan/Taiwan/Korea side-market leverage

Generated 2026-07-13 by idea-architect (claude-fable-5 / xhigh). Rules applied: US and/or CN primary
market mandatory; JP/TW/KR documented only as side markets (accelerant, reference customer, or
supply-chain wedge); India/Singapore excluded; all cited IDs verified `accepted: true` and
`india_origin_audit.status = verified_non_india_origin` in `90_BIBLIOGRAPHY/sources.json`
(rejected/quarantined IDs — including L03-053, L06-040, L06-045, L08-016, L08-047, L09-036,
L13-047, L14-047, L15-044 and the 42 origin-excluded IDs — were checked and deliberately NOT
cited). 14 seeds are provided against a target of 12 so weak concepts can be discarded.
Company launch year: 2030. All 2026–2029 plans assume no operating company (academic/consortium/
consulting vehicles only).


> **Adjudication applied 2026-07-13:** the independent elegance/novelty verdicts (`P3R2_ELEGANCE_ADJUDICATION.md`) have been applied to every seed below - PROMOTE/FIX_APPLIED/MERGED/REJECT annotations appear at the end of each seed section and in the batch JSON (`elegance_verdict` fields). See `P3R2_FIX_APPLICATION_LOG.md`.

---

## P3R2-E-01 — 800 VDC rack power-path protection and hot-swap module

- **Product:** OCP-form-factor solid-state DC breaker/hot-swap sled for 800 VDC AI racks: 1200 V
  SiC switch stage with sub-10 µs clearing, two-tier selectivity, series-arc-signature detection,
  capacitor precharge/inrush control, insulation monitoring; IEC 62477-1-aligned (L02-112).
- **Primary buyer + pain (US):** hyperscalers and rack/power-sidecar OEMs executing the NVIDIA/OCP
  800 VDC transition (L02-043, L02-044; supplier-side ramp caution L02-047). DC faults have no
  zero-crossing; SSCBs for datacenters and DC arc-fault detection are still research-stage
  (L08-017, L08-019–L08-021), and DC-link capacitors remain a leading failure mechanism (L02-010).
  Datacenter electrification demand is evidenced by GE Vernova's $2.4B/quarter orders (L08-033).
- **JP/TW/KR side role:** TW — Delta and the Taipei ODM ecosystem build the racks; design-in and
  manufacturing wedge (L02-037, L02-046). JP — ROHM-class SiC devices already designed into
  AI-server power as component supply/co-qualification (L02-051).
- **Mechanism:** µs-class SiC interruption + coordinated selectivity + high-bandwidth current
  signature acquisition for series-arc classification at 800 V + blind-mate hot-swap sequencing.
- **Why incumbents miss it:** AC-breaker majors productize utility-scale hybrid DC breakers, not
  rack sleds; rack vendors optimize conversion efficiency and ship fuses+contactors; the
  selectivity+arc-analytics+serviceability combination is a controls/data problem nobody owns.
- **Decisive experiment + budget:** 2027, $350k — 800 V/50 kW SSCB + arcing testbed; <10 µs
  clearing, two-tier selectivity, published arc-detection ROC on an OCP busbar mockup.
- **TRL:** 4.
- **2026–2029 plan:** university DC-arc research; OCP Mount Diablo workstream participation;
  patents on selectivity/arc methods; ODM design-study engagements; hyperscaler LOIs — no company
  until 2030.
- **2030–2034 trigger (named):** second-generation OCP Mount Diablo / NVIDIA 800 VDC fleet
  deployments at 600 kW–1 MW racks (L02-043, L02-044) amid the continuing electrification order
  wave (L08-033).
- **2030 competition:** Eaton/Schneider/Vertiv integrated features, down-scaled ABB/Siemens hybrid
  breakers, shelf-level e-fuses, Chinese rack ecosystems (L02-050, L08-052).
- **Window/timing risk:** hyperscalers may accept fuse-based protection; 800 VDC could stall at
  ±400 V.
- **Kill date:** 2033-12 without a hyperscaler/ODM design win by mid-2033.
- **Big vision:** the protection-and-power-path OS of all-DC campuses, scaling to row and MVDC.
- **Nearest substitutes:** fuses + hybrid contactors; e-fuse ICs; PSU-integrated protection.
- **Key uncertainty:** willingness to pay for a third-party safety subsystem vs ODM bundling;
  arc-detection false-positive rate at fleet scale.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-01]:** Import arc-ROC dataset moat and TW (Delta/COMPUTEX) + JP (ROHM) supply wedges - best secondary-market logic in cluster. Record retained as audit trail; not independently promotable.

## P3R2-E-02 — Refrigerant-agnostic two-phase cooling control subsystem

- **Product:** vapor-quality sensor head (capacitive+ultrasonic fusion) + dryout-margin observer +
  MPC pump/expansion controller that makes any CDU/cold-plate two-phase loop safe across post-PFAS
  low-GWP fluids; licensed to thermal OEMs.
- **Primary buyer + pain (US):** CDU/thermal OEMs and hyperscalers (Vertiv 50%+ liquid-cooling
  order growth, $15B backlog L14-048; OCP Deschutes spec L14-043; COOLERCHIPS lineage L14-030).
  Two-phase is the acknowledged path beyond single-phase (L14-001–003, L14-029) but the 3M PFAS
  exit desynchronized fluids from the literature (L14-022) while the AIM Act (L14-033) and EU
  F-gas rules (L14-034) squeeze HFC alternatives — every OEM faces per-fluid requalification.
- **JP/TW/KR side role:** TW — ITRI's 2,400 W low-pressure-refrigerant cold plate and domestic
  supply-chain buildout as co-development/manufacturing wedge (L14-053). KR — GS Caltex DLC/
  immersion fluids with named customers Samsung SDS and LG U+ as fluid partners and pilot sites
  (L14-049). JP — NTT Facilities' 780 kW DC Cooling Hub as neutral verification venue (L14-050).
- **Mechanism:** real-time exit vapor-quality estimation, fluid-property auto-ID, model-predictive
  control holding exit quality ~0.6–0.8 through 10x heat-flux transients with a dryout-margin
  observer.
- **Why incumbents miss it:** single-phase water dominates incumbent CDUs; two-phase startups
  vertically integrate around one proprietary fluid (L14-046); nobody sells the control/metrology
  layer as a component.
- **Decisive experiment + budget:** 2027, $250k — two-channel rig, dryout-margin control across
  three low-GWP fluids under 10x steps, quality-estimation error <5% vs reference.
- **TRL:** 3.
- **2026–2029 plan:** academic rig and sensor publications; OCP cooling workstream; patents;
  validation slots at NTT hub and with a Taiwan cold-plate maker; two OEM development agreements
  as licensor/consultant.
- **2030–2034 trigger (named):** EPA AIM Act step-down to 30% of baseline (2029–2033, L14-033)
  colliding with post-Novec requalification (L14-022) during hyperscaler two-phase procurement;
  ITRI-class 2.4 kW/chip cold plates entering ODM volume (L14-053).
- **2030 competition:** ZutaCore/Accelsius-class integrated systems (L14-046), Trane/LiquidStack
  (L14-051), Flex/JetCool (L14-045), OEM internal controls.
- **Window/timing risk:** single-phase water may stretch to 5 kW/chip; a single winning successor
  fluid would erode the fluid-agnostic premium.
- **Kill date:** 2033-12 if two-phase <5% of liquid-cooling shipments or no OEM license.
- **Big vision:** the ECU of two-phase thermal across DC, power electronics, and megawatt charging.
- **Nearest substitutes:** conservative fixed-superheat control; oversized single-phase loops.
- **Key uncertainty:** sensor robustness/fouling at fleet scale; OEM appetite to outsource a
  safety-critical control layer.
- **[FIX applied 2026-07-13]:** two OEM development agreements made a hard 2028 gate proving buy-vs-build appetite, with a pre-agreed fallback merge into the B-01/C-04 loop stack as its control layer; the two-phase shipment-share kill trigger made binding.

## P3R2-E-03 — Ion-energy-distribution control module (tailored-voltage-waveform bias)

- **Product:** kV-class multi-MHz solid-state arbitrary-waveform bias supply with V-I-probe sheath
  estimation and closed-loop ion-energy setpoints (<5 eV FWHM target), retrofittable to etch/
  deposition chambers.
- **Primary buyer + pain (US+CN):** US — leading-edge etch OEMs/RF integrators; fabs are already
  paying for next-gen RF platforms ("double-digit millions," early ramp: L06-039). CN — AMEC/
  NAURA/Piotech growing 40–55%/yr (L06-048) while RF power components remain <12% localized
  (L06-054), with new domestic entrants proving the budget line (Hengyunchang IPO L06-042/043,
  Injet orders L06-044). TVW biasing is a live 2024–26 research frontier not yet productized
  (L06-009, L06-010, L06-011, L06-027) and matching itself is unsettled (L06-001–003).
- **JP/TW/KR side role:** KR — Samsung's co-authorship on TVW research (L06-009) is leading-edge
  user pull; Korean plasma-diagnostics groups (L06-024, L06-025) as validation/talent channel.
  JP — Kyosan Electric as RF incumbent benchmark and potential manufacturing/licensing partner
  (L06-050).
- **Mechanism:** GaN/SiC HV amplifier with multi-harmonic synthesis; real-time sheath-voltage
  estimator; per-wafer IEDF recipes.
- **Why incumbents miss it:** generator vendors ship incremental pulsing features on platform
  roadmaps (L06-039, L06-049); closed-loop IEDF-as-a-spec requires physics+controls integration
  outside their component pattern; OEM in-house teams are chamber-specific.
- **Decisive experiment + budget:** 2027–28, $400k — 2 kV/5 MHz TVW bias on a university ICP
  chamber; <5 eV FWHM at 100–500 eV; measured ALE selectivity gain vs sinusoidal bias.
- **TRL:** 3.
- **2026–2029 plan:** PhD/postdoc TVW replication and extension; waveform/sheath-estimator
  patents; one US integrator evaluation; exploratory technical exchange with a Chinese tool OEM;
  KR academic collaboration.
- **2030–2034 trigger (named):** US leading-edge fab expansion (Intel/TSMC-AZ/Samsung-TX-class)
  qualifying next-gen etch fleets 2030–2033, plus China's RF-localization procurement wave
  (L06-042–044, L06-054).
- **2030 competition:** Advanced Energy next-gen platforms (L06-039), MKS, Comet (L06-049),
  Kyosan (L06-050), Hengyunchang (CN).
- **Window/timing risk:** AE/MKS could productize closed-loop TVW pre-2030; export controls could
  sever the CN half.
- **Kill date:** 2033-06 without an OEM beta on a production-class chamber.
- **Big vision:** ion energy as a universal closed-loop process variable across plasma processing.
- **Nearest substitutes:** dual-frequency bias + pulsing on incumbent generators; process
  work-arounds via chemistry.
- **Key uncertainty:** OEM qualification-cycle length; whether IEDF control shows yield-visible
  gains outside lab ALE.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-A-10]:** Import Samsung co-authorship pull evidence and KR diagnostics validation channel into A-10. Record retained as audit trail.

## P3R2-E-04 — High-density cryogenic interconnect with integrated 4 K readout front-end

- **Product:** fridge-insert loader delivering 2,000+ channels: superconducting/low-conductance
  flex laminates with co-packaged 4 K 64:1 cryo-CMOS multiplexers and GaAs/SiGe LNAs, engineered
  against stage-by-stage heat budgets.
- **Primary buyer + pain (US):** DOE QIS centers ($625M, L13-028), the Fermilab–Qblox QICK supply
  chain (L13-032), US superconducting-qubit builders; Bluefors Syracuse as OEM channel (L13-041).
  Wiring density is an acknowledged scaling wall — 256 channels/loader today with only one
  vendor's unvalidated roadmap (L13-042) — while cryo-electronics power budgets collide with
  mK-stage cooling limits (L13-004, L13-005, L13-022, L13-023; dilution-fridge cooling-power
  frontier L07-014–017).
- **JP/TW/KR side role:** TW — SEEQC–ITRI superconducting-control-chip manufacturing line as the
  foundry/packaging wedge (L13-038). JP — AIST G-QuAT's 1,000+-qubit control deployment as
  reference market (L13-037). KR — KRISS 1,000-qubit-by-2032 roadmap as emergent buyer (L13-040).
- **Mechanism:** flex-laminate thermal/crosstalk engineering + cold multiplexing (1.08 mW/qubit
  FDM-class ASICs, L13-023) + cryo-LNA integration (L13-021, L13-013) to cut heat load/channel ~10x.
- **Why incumbents miss it:** cable vendors sell cables, control vendors sell room-temperature
  racks, fridge OEMs sell fridges — the harness+cold-electronics integration point is orphaned.
- **Decisive experiment + budget:** 2027, $500k — 256-channel flex segment + 4 K 64:1 mux; <1%
  crosstalk, <20% of coax heat load, readout-fidelity parity on test resonators.
- **TRL:** 3.
- **2026–2029 plan:** cryolab research + MPW tape-outs; publications; co-packaging patents; pilot
  integration with a QIS-center testbed and one fridge OEM; Taiwan manufacturing costing; LOIs.
- **2030–2034 trigger (named):** DOE QIS funding renewals beyond the $625M tranche (L13-028) and
  first >5,000-physical-qubit systems hitting the interconnect wall (L13-042); QICK
  industrialization (L13-032).
- **2030 competition:** Delft Circuits, Bluefors integrated wiring, in-house at IBM/Google-class
  labs, RFSoC-based room-temperature stacks (L13-045).
- **Window/timing risk:** on-chip 1000:1 multiplexing or optical cryo-links could leapfrog;
  government-dependent capex.
- **Kill date:** 2034-06 without an OEM/QIS integration contract by 2033.
- **Big vision:** the backplane of the quantum datacenter; extension to big-science detector
  readout.
- **Nearest substitutes:** bundled coax looms; vendor cabling roadmaps; per-lab custom harnesses.
- **Key uncertainty:** cryo-CMOS yield/reliability at 4 K in volume; qubit-count timelines.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical cryo I/O: flex + 4K mux + LNA against fridge heat budget, TW manufacturing wedge (SEEQC-ITRI), JP/KR reference markets. Keep D-17's substitution risks (SFQ, cryo-CMOS, optical) on record. 2026-07-13: absorbed A-06 (channels-per-watt sales framing) and D-17 (SFQ/cryo-CMOS/optical substitution-risk framing, roadmap-validation angle).

## P3R2-E-05 — Standardized solid-state pulsed-power modulator platform

- **Product:** catalog family of IGBT/SiC Marx cells (50–150 kV blocks, <0.1% droop, per-cell
  health telemetry, <30 min hot-swap) with one control/interconnect standard; qualified to IEC
  60060-1:2025 (L05-043), aligned to ISO 11137-1:2025 (L05-042).
- **Primary buyer + pain (US):** sterilization networks and device OEMs converting off EtO while
  the IBA/L3 e-beam duopoly runs backlogs into 2026–27 (L05-028); cargo-screening linac OEMs
  growing +25% YoY (L05-033); accelerator labs. Today at least five incompatible solid-state
  modulator designs exist across projects (L05-003–006) — every buyer pays bespoke NRE and
  negotiates bespoke acceptance tests.
- **JP/TW/KR side role:** KR — the Vitzro Nextec/PAL klystron-localization ecosystem (~70 units
  at PAL) as manufacturing partner and validation site (L05-037); Korean GaN SSPA synchrotron
  program as adjacent channel (L05-010).
- **Mechanism:** modular Marx cells with active droop correction, PFN-free topology, prognostic
  health monitoring per cell.
- **Why incumbents miss it:** ScandiNova/Jema sell project-engineered units (L05-047, L05-030);
  IBA vertically integrates; no one sells a standardized, hot-swappable cell family with
  published shot-life data in the US.
- **Decisive experiment + budget:** 2027–28, $450k — 4-cell 50 kV/500 A stack: <0.1% droop at
  14 Hz, hot-swap <30 min, 10^7-shot reliability run.
- **TRL:** 4.
- **2026–2029 plan:** benchmark study; 15 integrator interviews; university HV-lab build and
  reliability campaign; patents; KR co-qualification talks; US integrator LOIs.
- **2030–2034 trigger (named):** US EtO regulatory replacement cycle driving new e-beam/X-ray
  sterilization lines into 2030–2034 against the documented duopoly backlog (L05-028), plus ISO
  11137-1:2025 revalidation cycles (L05-042) and customs-screening upgrades (L05-033).
- **2030 competition:** ScandiNova (L05-047), Jema (L05-030), IBA in-house, CGN Dasheng in China
  (L05-035); Comet-class RF/X-ray vendors (L05-034).
- **Window/timing risk:** duopoly backlog could clear and X-ray sterilization overbuild by 2030;
  ScandiNova could standardize first.
- **Kill date:** 2033-12 without a US integrator design win.
- **Big vision:** the standard building block of pulsed power across sterilization, screening,
  medical linacs, and research accelerators.
- **Nearest substitutes:** project-engineered ScandiNova/Jema units; refurbished PFN/thyratron
  chains.
- **Key uncertainty:** whether sterilization integrators buy components vs turnkey lines; shot-life
  economics vs incumbent service models.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-09]:** Import hot-swap-<30min serviceability spec and KR (Vitzro/PAL) channel into C-09. Record retained as audit trail.

## P3R2-E-06 — Grid-interactive recuperative battery-formation power system

- **Product:** SiC bidirectional formation/grading cabinets: >92% round-trip energy recuperation
  to a shared DC bus, ±0.02% current accuracy, per-channel EIS hooks, optional grid-services
  aggregation.
- **Primary buyer + pain (US):** US gigafactories of the CATL/LGES/Samsung SDI/SK On/Panasonic
  wave that formation-equipment vendors already track (L11-043, L11-044). Formation is a dominant
  plant energy consumer, and the rectifier-quality literature documents a 13–14% specific-energy
  lever when replacing thyristor-class conversion with IGBT/switch-mode topologies (L11-016,
  L11-017, L11-019–021) — incumbents optimize metrology, not plant energy economics.
- **JP/TW/KR side role:** TW — Chroma-anchored test-equipment manufacturing base as contract-
  manufacturing/OEM channel (L11-043). KR — Korean cell makers' domestic pilot lines as
  qualification sites feeding their US plants (L11-043). JP — Hioki-class precision ecosystem as
  metrology benchmark/partner (L11-044).
- **Mechanism:** high-frequency SiC bidirectional converters with shared-bus energy recycling and
  metrology-grade sensing; electrowinning analog documented (L11-045).
- **Why incumbents miss it:** test-equipment vendors sell measurement precision; power-electronics
  majors lack µV/mA metrology; nobody couples formation to plant-level energy/grid value.
- **Decisive experiment + budget:** 2027, $300k — 8-channel 6 kW recuperative cabinet, >92%
  verified round-trip return at ±0.02% accuracy, third-party audit.
- **TRL:** 4.
- **2026–2029 plan:** formation-floor energy audits with two plant partners; university prototype;
  Taiwan CM costing; KR pilot-line qualification; one US plant LOI.
- **2030–2034 trigger (named):** the post-2030 US cell-capacity second wave plus first-wave plant
  retrofit cycles (the same expansion the incumbents ride: L11-043/044) under electricity-cost
  pressure that monetizes the documented rectifier lever.
- **2030 competition:** Chroma (TW), Hioki (JP), Digatron/Bitrode-class, large Chinese formation
  vendors — some already ship partial recuperation.
- **Window/timing risk:** highest commoditization risk in this batch; US battery policy
  volatility.
- **Kill date:** 2033-12 if no pilot-line deployment, or earlier if recuperation becomes a
  standard incumbent feature before launch.
- **Big vision:** precision electrochemical power delivery as a category (formation →
  electrowinning → electrolyzer rectification).
- **Nearest substitutes:** incumbent formation lines with partial recovery; resistor-discharge
  cyclers.
- **Key uncertainty:** in-atlas demand evidence is thin (L11-043/044 only) — real formation
  energy-bill data must be validated in 2026–27 before further investment.
- **[Adjudication 2026-07-13 - REJECT]:** Same hidden-commodity finding as A-20; self-diagnosed highest commoditization risk; incumbents already ship recuperation. Record retained as audit trail.

## P3R2-E-07 — HTS quench-precursor detection and conductor-health instrumentation

- **Product:** co-wound Rayleigh/FBG fiber + RF-reflectometry quench-precursor detection with
  physics-based thresholds, cryogenic interrogators, and standardized REBCO conductor/joint QA
  benches.
- **Primary buyer + pain (US):** CFS (selling magnets to Realta/UW-WHAM: L03-035), DOE Milestone
  fusion awardees (L03-032), US-ITER/ORNL operations (L03-030). HTS quench detection is unsolved
  at multi-tesla/multi-MJ scale (L03-004–006, L03-018) and REBCO degrades via strain/delamination/
  screening-current stress (L03-020, L03-021), forcing over-engineering and bespoke acceptance
  testing.
- **JP/TW/KR side role:** JP — Furukawa/SuperPower and Fujikura tape suppliers (Furukawa–Tokamak
  Energy supply deal) as conductor-QA co-development partners (L03-044). KR — KEPCO + LS Cable/LS
  Electric AI-datacenter superconducting-grid MOU as the cable-monitoring side market (L03-042,
  L03-043).
- **Mechanism:** distributed fiber strain/temperature precursors + reflectometry hot-spot
  localization, cross-validated against voltage taps.
- **Why incumbents miss it:** magnet builders keep instrumentation in-house and unshareable; AMSC
  sells systems, not merchant diagnostics (L03-046); fiber-sensing generalists lack HTS physics.
- **Decisive experiment + budget:** 2027, $350k — instrument a partner lab's HTS coil; 10x earlier
  precursor detection than voltage taps, <1 false alarm/100 h.
- **TRL:** 3.
- **2026–2029 plan:** lab collaboration; detection-latency dataset publication; threshold patents;
  paid pilots with one fusion company and one tape supplier; LOIs.
- **2030–2034 trigger (named):** DOE Milestone program renewal after FY2027 (L03-032), CFS's
  external magnet-sales line scaling (L03-035), and the KEPCO/LS datacenter superconducting-grid
  build (L03-042/043).
- **2030 competition:** in-house CFS/Tokamak Energy systems, Luna-class fiber vendors,
  national-lab spinouts.
- **Window/timing risk:** no-insulation windings may reduce urgency for some magnet classes;
  fusion schedule slips.
- **Kill date:** 2034-06 without a fusion-vendor or cable-project contract by 2033.
- **Big vision:** the sensor-and-safety layer of the superconducting economy.
- **Nearest substitutes:** voltage taps + conservative margins; in-house fiber experiments.
- **Key uncertainty:** access to representative coils pre-company; whether builders outsource
  safety-critical instrumentation.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-D-01]:** Straddles D-01 + D-02. Split-import: precursor-dataset moat + KEPCO/LS cable monitoring to D-01; conductor/joint QA benches + Furukawa/Fujikura partnerships to D-02. Record retained as audit trail; not independently promotable.

## P3R2-E-08 — Merchant PCHE recuperator line for sCO2 power blocks

- **Product:** diffusion-bonded printed-circuit heat-exchanger cores rated for 20 °C/min
  transients at 550–700 °C, delivered with ASTM E139 creep data (L04-112) and an open
  acceptance-test protocol substituting for the missing sCO2 test standard.
- **Primary buyer + pain (US+CN):** US — STEP-lineage integrators (GTI/SwRI/GE Vernova, L04-039)
  and pipeline waste-heat adopters (TC Energy–Hanwha MOU, L04-047). CN — CNNC's commercial 30 MW
  Chaotan One and the Xinjiang "first-set" molten-salt+sCO2 pipeline (L04-048, L04-051). PCHE
  recuperators are the most-cited sCO2 bottleneck: thermal-inertia/rapid-cycling durability is an
  open research problem and every integrator builds bespoke cores (L04-029, L04-004–006, L04-113).
- **JP/TW/KR side role:** KR — KAERI/KAIST/Jinsol consortium and Hanwha's commercial sCO2
  turbo-expander line as first-adopter partners (L04-028, L04-047; KIER compressor work L04-103).
  JP — MHI-owned Turboden ORC relationships as adjacent heat-to-power channel (L04-044).
- **Mechanism:** engineered headers/channel geometry for thermal-shock tolerance; elastohydro-
  dynamic sealing advances (L04-101); alloy qualification per Sandia's named materials challenges
  (L04-113).
- **Why incumbents miss it:** integrators treat recuperators as in-house one-offs; established HX
  suppliers have not published cyclic-rated sCO2 lines; the standards vacuum (no sCO2 PTC) keeps
  the market bespoke.
- **Decisive experiment + budget:** 2028, $600k — 200 kW-class core, 1,000 cycles at 20 °C/min
  between 550–700 °C, <2% effectiveness degradation + creep coupons.
- **TRL:** 4.
- **2026–2029 plan:** diffusion-bonding research residency; bottom-up validation of the
  untriangulated China retrofit TAM (L04-051) before commitment; national-lab cyclic campaign;
  KAERI/Hanwha and US integrator co-qualification; LOI + licensed protocol.
- **2030–2034 trigger (named):** CNNC Xinjiang completion (2028) and "first-set" designation
  unlocking Chinese waste-heat retrofit procurement post-2028 (L04-051); DOE STEP Phase 2 scaling
  to its 10 MWe design point with follow-on US pilots (L04-039).
- **2030 competition:** integrator in-house fabrication (GTI/SwRI, CAS-IET: L04-039, L04-029),
  established diffusion-bonded HX suppliers, Korean consortium suppliers (L04-028).
- **Window/timing risk:** sCO2 may stay demo-stage in the West past 2034; Chinese procurement may
  exclude foreign cores; capex-heavy.
- **Kill date:** 2034-12 if no >50 MW-class commercial sCO2 orders outside China; earlier
  deprioritization if 2027 TAM diligence fails.
- **Big vision:** the standard core component of high-temperature Brayton hardware (sCO2, CSP,
  nuclear BOP, thermal batteries).
- **Nearest substitutes:** in-house cores; shell-and-tube compromises at efficiency loss.
- **Key uncertainty:** single-source China market-size claim (L04-051) explicitly untriangulated;
  US commercial sCO2 pace.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-08]:** Import KR consortium channel (KAERI/Jinsol/Hanwha), MHI-Turboden adjacency, and pre-commitment CN TAM triangulation task into C-08. Record retained as audit trail.

## P3R2-E-09 — 300 °C SiC/SOI instrumentation module platform for superhot wells

- **Product:** qualified module family (ADC + telemetry + sensor front-end + gate drive) rated
  300 °C continuous with a 350–500 °C roadmap, built packaging-first (die-attach/ceramics — the
  documented bottleneck: L15-005, L15-025).
- **Primary buyer + pain (US):** Baker Hughes ($2.0B New Energy orders, 300 MW ORC contract:
  L15-040), SLB–Ormat EGS lineage (L15-041), FORGE toolmakers Welltec/PetroQuip (L15-027,
  L15-028), ARPA-E SUPERHOT teams (L15-029). Superhot targets (>375 °C) exceed the 225 °C
  commercial ceiling while the incumbent CISSOID CHT family is obsolete/last-time-buy with no
  successor (L15-043) — a live supply gap with funded buyers; DARPA THERMAL confirms the problem
  is still open at 800 °C (L15-026).
- **JP/TW/KR side role:** JP — Fukushima-decommissioning robotics ecosystem (gamma-qualification
  culture, L15-011) as side market for high-temp/rad-tolerant control modules. KR — rad-tolerant
  FPGA/space-electronics research base as collaboration channel (L15-022).
- **Mechanism:** SiC JFET/SOI mixed-signal ICs (SOI to 300 °C: L15-004; NASA SiC 500 °C/1-yr
  heritage: L15-009, L15-030) in Ag-sintered/ceramic packages qualified by powered soak.
- **Why incumbents miss it:** two decades of federal programs never converged a commercial
  platform (L15-001); Honeywell/CISSOID exited or obsoleted product lines; tool OEMs' in-house
  ASIC teams don't sell merchant.
- **Decisive experiment + budget:** 2027–28, $500k — 1,000 h powered soak at 300 °C with <1%
  drift; evaluation units to one downhole tool OEM under MOU.
- **TRL:** 4.
- **2026–2029 plan:** SiC-IC/packaging research role; socket mapping via toolmaker interviews;
  module build + soak campaign; package-stack patents; two paid prototype evaluations; JP
  decommissioning pilot exploration.
- **2030–2034 trigger (named):** ARPA-E SUPERHOT wells and successors entering drilling/completion
  2030–2033 (L15-029) with Baker Hughes/SLB EGS programs scaling (L15-040/041); DARPA THERMAL
  Phase II device outputs needing productization (L15-026).
- **2030 competition:** CISSOID successor attempts, tool-OEM in-house ASICs, active-cooling
  workarounds, primes absorbing THERMAL performers.
- **Window/timing risk:** drilling programs could stall below 300 °C; long qualification cycles.
- **Kill date:** 2034-06 without a toolmaker design-in by 2033.
- **Big vision:** the standard electronics platform of the >300 °C world (wells, engines, nuclear
  robotics, Venus-class instruments).
- **Nearest substitutes:** 225 °C legacy parts + derating; vacuum-flask active cooling.
- **Key uncertainty:** merchant-market size vs OEM in-house instinct; packaging reliability
  statistics at 300 °C+.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-14]:** Import packaging-first qualification strategy, 1,000h powered-soak artifact, and JP decommissioning side market into A-14. Record retained as audit trail; not independently promotable.

## P3R2-E-10 — Standardized rad-tolerant GaN PPU platform for smallsat electric propulsion

- **Product:** modular GaN PPU family (1–6 kW anode blocks, magnet/keeper/heater cards, flow-
  control drive) with SET-mitigated topologies (L09-108) and a common digital interface, qualified
  to ECSS-E-ST-20-20C / AIAA S-122 (L09-111, L09-115).
- **Primary buyer + pain (US):** thruster makers without deep PPU lines (Busek: L09-009, L09-043),
  constellation primes (SDA tranche cadence: L09-039 — EP content flagged as inferred), NASA EP
  programs (AEPS $67M, NEXT-C $18.4M: L09-034, L09-012; component-level SBIR funding: L09-112,
  L09-113). PPU topology never converged (L09-001, L09-003, L09-006, L09-008), the flagship US
  supplier now sits inside a missile-focused parent (L09-041), and GaN/SiC space qualification is
  unresolved (L09-014, L09-020, L09-103, L09-104) — every program re-pays PPU NRE.
- **JP/TW/KR side role:** JP — JAXA–Furukawa J-SPARC GaN Hall-thruster power-supply
  commercialization as validation-pattern partner and cross-Pacific credibility (L09-042). KR —
  KARI full-EP GEO design studies as an emergent buyer (L09-019).
- **Mechanism:** GaN converters with SET-mitigation-by-topology, derating policy from published
  heavy-ion data, standardized interfaces across thruster vendors.
- **Why incumbents miss it:** primes treat PPUs as program-specific NRE; component vendors (EPC
  Space) sell parts without independent qualification (L09-054, L09-055); nobody sells a merchant,
  standards-qualified PPU family.
- **Decisive experiment + budget:** 2027–28, $400k — 3 kW GaN anode-supply breadboard at 96%+
  efficiency; university-cyclotron heavy-ion campaign; integrated burn with a university Hall
  thruster.
- **TRL:** 4.
- **2026–2029 plan:** graduate SEE-mitigation research; publications and patents; SBIR-track
  collaborations; JAXA/Furukawa-pattern validation study; two thruster-OEM LOIs.
- **2030–2034 trigger (named):** SDA Tranche 4/5-class replenishment cycles and Gateway/Mars-
  logistics SEP buys 2030–2034 (L09-039, L09-043, L09-034).
- **2030 competition:** L3Harris/Aerojet, Moog, EPC Space components, thruster-OEM in-house,
  Furukawa in Japan (L09-042).
- **Window/timing risk:** prime vertical integration; GaN SEE failure at higher bus voltages
  forcing SiC fallback.
- **Kill date:** 2034-06 without a flight-qualification contract by 2033.
- **Big vision:** the standardized power stack of in-space mobility up to 100 kW-class SEP.
- **Nearest substitutes:** program-specific PPU NRE at primes; silicon rad-hard legacy converters
  with mass penalty.
- **Key uncertainty:** EP content of SDA-class buses (not confirmed in sources: L09-039);
  qualification cost vs smallsat price tolerance.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-13]:** Import ECSS/AIAA qualification framing, JAXA-Furukawa J-SPARC pattern, KARI emergent-buyer note into A-13. Record retained as audit trail; not independently promotable.

## P3R2-E-11 — CPO thermal-stabilization module for co-packaged optical switch ASICs

- **Product:** package-level thermal subsystem: lid-integrated two-phase micro-loop + distributed
  micro-TEC islands (±0.5 °C laser-site regulation) + validated TIM/bond-line stack, sold to
  switch vendors and OSATs as a qualified BOM item.
- **Primary buyer + pain (US):** Broadcom-class switch vendors and Coherent (publicly targeting a
  $4B datacenter-interconnect opportunity: L12-035, L12-036), plus hyperscalers via OCP specs
  (L14-043). CPO concentrates optical power on the switch package with no converged thermal
  architecture across four independent 2024–26 approaches (L12-021–024), while TIMs for
  chiplet-scale hotspots remain a live materials bottleneck (L14-014–016, L14-018).
- **JP/TW/KR side role:** TW — OSAT/ODM packaging supply chain plus ITRI's two-phase cold-plate
  ecosystem as co-development and manufacturing wedge; CPO assembly physically happens in Taiwan
  (L14-053).
- **Mechanism:** passive two-phase spreading tuned for low-pressure fluids + local TEC trim only
  where wavelength stability requires it, minimizing cooling-power overhead.
- **Why incumbents miss it:** cold-plate vendors stop at the lid; OSATs ship passive lids; switch
  vendors' thermal teams are ASIC-centric, not photonics-stability-centric.
- **Decisive experiment + budget:** 2027, $300k — CPO-emulating testbed (ASIC + 8 laser sites);
  ±0.5 °C regulation under 30% power transient at <3% cooling overhead.
- **TRL:** 3.
- **2026–2029 plan:** packaging-lab testbed and comparative publication; lid prototype; layout
  patents; one Taiwan OSAT co-development agreement; one US switch-vendor evaluation; LOIs.
- **2030–2034 trigger (named):** CPO volume ramp in the 3.2T/6.4T optics generations into the $4B
  DCI opportunity Coherent has quantified (L12-036), with OCP cooling specs extending to package
  level (L14-043).
- **2030 competition:** OSAT in-house lids, Flex/JetCool downward extension (L14-045),
  ZutaCore-class package-scale two-phase (L14-046), switch-vendor internal teams; Coherent as
  buyer-and-competitor.
- **Window/timing risk:** LPO/linear-drive pluggables could defer CPO volume past 2034; OSAT
  roadmaps may absorb the niche.
- **Kill date:** 2033-12 if CPO volume has not started or no co-development by 2033.
- **Big vision:** the thermal interface layer between photonics and silicon across optical I/O.
- **Nearest substitutes:** oversized cold plates + wavelength-tolerant photonics design; TEC-only
  solutions at high power overhead.
- **Key uncertainty:** CPO adoption timing; whether ±0.5 °C is the binding spec across vendor
  architectures.
- **[FIX applied 2026-07-13]:** 2028 gate on CPO volume-ramp evidence plus one switch-vendor/OSAT co-development agreement; explicit LPO-substitution monitor; defensive IP plan for Coherent as simultaneous buyer and competitor.

## P3R2-E-12 — Low-cost Ka-band metamaterial ESA radar tile

- **Product:** varactor/holographically-tuned metasurface aperture tile (256+ elements, ±45°
  scan) with commodity RF backend and open beam-control software, engineered to the US Army's
  published $300k/unit production target.
- **Primary buyer + pain (US):** the Army SBIR A254-049 sponsor and range-modernization/
  counter-UAS offices (Phase I $250k, explicit unit-cost target: L16-020). Ranges and layered
  counter-UAS need many cheap steerable Ka-band apertures; conventional AESA LRUs are an order of
  magnitude too expensive. China's Guangqi (RMB ~2.6B 2025 orders) proves metamaterial defense
  hardware is a real revenue category (L16-017).
- **JP/TW/KR side role:** KR — the KRISS-to-KER stealth-metamaterial transfer (~KRW 500M,
  L16-018) as precedent and teaming model for an allied-market variant with a Korean
  defense-electronics partner.
- **Mechanism:** metasurface phase control replaces per-element T/R modules; calibration and
  beam-control software carry the margin (technical base: L16-010, L16-011).
- **Why incumbents miss it:** primes optimize exquisite AESA performance, not $300k unit
  economics; existing US metamaterial-ESA vendors focus on different bands/missions.
- **Decisive experiment + budget:** 2027, $350k — 256-element Ka-band tile; measured ±45° scan,
  sidelobes, and G/T vs a phased-array baseline at a university range.
- **TRL:** 4.
- **2026–2029 plan:** university RF-lab design and range measurements; tuning/calibration
  patents; SBIR Phase I/II as academic partner to a small prime; KER-class exploratory teaming;
  incorporate 2030 for Phase III.
- **2030–2034 trigger (named):** Army A254-049 Phase II/III transition and follow-on range-
  instrumentation/counter-UAS procurements 2030–2034 (L16-020).
- **2030 competition:** established US metamaterial-ESA vendors, prime in-house AESAs; Guangqi
  defines the cost frontier in a closed market (L16-017).
- **Window/timing risk:** defense cycles; the topic could be won by an established vendor;
  Ka-band component costs may not fall to target.
- **Kill date:** 2033-12 without Phase II/III or a prime partnership.
- **Big vision:** commodity electronically-steered apertures for radar and comms meshes.
- **Nearest substitutes:** used/derated AESA assets; dish-on-positioner instrumentation radars.
- **Key uncertainty:** competitive density in US metamaterial ESA by 2030; achievable scan-loss/
  bandwidth at the cost point.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-18]:** Import KRISS-to-KER transfer precedent as allied-variant model into D-18. Record retained as audit trail.

## P3R2-E-13 — 2-µm high-energy drive-laser modules for next-generation EUV sources

- **Product:** Tm/Ho-based 2-µm pulsed amplifier modules (joule-class, kHz-class, pre-pulse
  shaping options) as qualified building blocks for EUV LPP conversion-efficiency upgrade
  programs, with a coherent-combining growth path.
- **Primary buyer + pain (US):** ASML/Cymer source development in San Diego — each EUV power step
  (250 W→500 W→1,000 W) required re-engineering, cumulative EUV R&D exceeds EUR 6B (L12-034), and
  peer-reviewed work models a 2-µm drive architecture at ~5% conversion efficiency vs CO2
  (L12-003; pre-pulse and droplet modeling L06-016, L06-017). No merchant supplier base exists
  for joule-class high-rep 2-µm amplifiers.
- **JP/TW/KR side role:** JP — Gigaphoton (Komatsu group, ~2,000 excimer lasers shipped, active
  EUV/DUV R&D: L12-053) as second source-developer customer/partner, hedging single-customer risk.
- **Mechanism:** Tm-doped fiber/Ho:YLF amplifier chains; ultrafast coherent-combining heritage
  (260 fs/403 W class: L12-001, L12-002) as the scaling path.
- **Why incumbents miss it:** TRUMPF's business is the CO2 incumbent chain (L12-039); Cymer
  optimizes the current architecture; 2-µm high-energy remains fragmented academic hardware.
- **Decisive experiment + budget:** 2028, $700k (consortium) — joule-class 2-µm chain on an
  existing tin-droplet LPP testbed, measured CE vs 10.6-µm baseline, target >4%.
- **TRL:** 3 (explicitly the highest-physics-risk seed in this batch; the decisive experiment
  resolves the core uncertainty by 2028–29, keeping it inside the 2030-launch contract).
- **2026–2029 plan:** PhD/postdoc in a high-energy-laser group; sub-scale amplifier chain; LPP
  consortium experiment; CE dataset publication; architecture patents; technical dialogues with
  Cymer and Gigaphoton. Incorporate in 2030 only if CE >4% demonstrated.
- **2030–2034 trigger (named):** ASML/Cymer (and Gigaphoton) next-generation source architecture
  decisions during the high-NA EUV power ramp 2030–2033 (L12-034, L12-053).
- **2030 competition:** TRUMPF, IPG, Cymer internal development.
- **Window/timing risk:** ASML may keep scaling CO2; single-customer concentration; physics may
  not transfer from models to industrial rep-rates.
- **Kill date:** 2034-06, with an explicit earlier gate: kill if tin-droplet CE >4% at relevant
  rep-rate is not demonstrated by end-2033.
- **Big vision:** own the 2-µm high-energy component layer (EUV first, then transparent-material
  processing and beam-combining adjacencies).
- **Nearest substitutes:** continued CO2 drive-chain scaling; solid-state 1-µm alternatives.
- **Key uncertainty:** conversion-efficiency physics at scale — modeled, not demonstrated.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-11]:** Import CE->4%-by-2033 kill gate and Gigaphoton second-customer hedge into D-11. Record retained as audit trail.

## P3R2-E-14 — Multi-terminal DC fault-discrimination relay + HIL qualification platform

- **Product:** DC protection relay implementing benchmarked traveling-wave/non-unit
  discrimination (<1 ms decision) plus an open RTDS/HIL suite qualifying any breaker/relay/
  converter combination — the "SEL of DC grids."
- **Primary buyer + pain (US):** US HVDC developers (Southern Spirit: $2.6B private + $360M DOE,
  L08-041), converter vendors riding the ~$10B HVDC backlog and $2.4B/qtr datacenter orders
  (L08-033), and TSOs under NERC PRC-029-1 compliance (L08-043). DC faults must clear in
  single-digit ms without zero-crossings; discrimination algorithms are still re-derived paper by
  paper (L08-004–007), breakers are non-converged (L08-017), and DC arc-fault detection is
  unsolved even at LV (L08-019–021) — meshed DC cannot be built with confidence.
- **JP/TW/KR side role:** KR — KEPCO's 2 GW West Coast HVDC "Energy Expressway" (tenders from
  2026, 2030 completion) plus the 2027 national HVDC-equipment localization target make Korean
  suppliers (LS Electric/Hyosung-class) natural early customers for neutral protection/
  qualification services (L08-038, L08-039).
- **Mechanism:** high-bandwidth traveling-wave acquisition, non-unit discrimination with
  physics-bounded settings, published benchmark suite as the acceptance standard.
- **Why incumbents miss it:** Hitachi/Siemens/GE bundle protection inside their converter
  stations (L08-052); AC relay incumbents lack DC fault physics; no neutral qualification vendor
  exists.
- **Decisive experiment + budget:** 2027, $300k — RTDS/HIL benchmark of three published
  algorithms on a 4-terminal MVDC model + relay prototype with <1 ms trip decisions; released as
  an open benchmark.
- **TRL:** 3.
- **2026–2029 plan:** graduate benchmarking work; open benchmark release; relay prototype and
  patents; paid HIL studies for one converter vendor and one Korean localization supplier; LOIs.
- **2030–2034 trigger (named):** Southern Spirit construction (2029) toward 2032 in-service
  (L08-041); continuing HVDC/datacenter electrification orders (L08-033); KEPCO West Coast HVDC
  procurement cycle (L08-038/039).
- **2030 competition:** converter-vendor integrated protection, SEL-class AC incumbents extending
  to DC, academic toolchains.
- **Window/timing risk:** if US/offshore DC stays point-to-point through 2034, fast
  discrimination demand defers; vendors may exclude third-party relays from their stations.
- **Kill date:** 2034-12 without a multi-terminal project or vendor engagement by 2033.
- **Big vision:** the independent protection-and-qualification authority for the DC century
  (datacenter MVDC, offshore multi-terminal HVDC, DC industrial parks).
- **Nearest substitutes:** point-to-point architectures that avoid fast DC breakers; vendor-locked
  protection.
- **Key uncertainty:** pace of genuinely meshed DC projects in the US; TSO willingness to qualify
  a startup relay in protection chains.

---

Batch E frozen 2026-07-13. EE/CE transfer note: every seed in this batch reduces to the same
generic electrical/computer-engineering competency stack — precision power conversion, fast
protection and fault physics, closed-loop control around a hard physical constraint, and
qualification-grade instrumentation — which transfers across all fourteen products regardless of
which seeds survive scoring.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical DC protection relay + vendor-neutral qualification ('SEL of DC grids'); open-benchmark strategy converts research chaos into an ownable acceptance standard; dated US anchors + KR localization side market. Absorb C-16 CN license angle; coordinate scope with A-02 and A-03. 2026-07-13: absorbed C-16 (CN factory-acceptance-test license market + State Grid test-institute channel, L08-034) as a license-only chapter - E-14 is not on the adjudicator's endorsed licensed-CN-leg list for flag purposes, so primary_market stays US and china_beachhead stays false. Scope coordinated with A-02 and A-03.

