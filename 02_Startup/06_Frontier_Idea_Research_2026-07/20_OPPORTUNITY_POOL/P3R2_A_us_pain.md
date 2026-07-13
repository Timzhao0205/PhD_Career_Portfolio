# P3R2 Batch A — US-pain evidence-first seeds (22 seeds, 15 primary lanes)

Generated 2026-07-13 by idea-architect (claude-fable-5 / xhigh). Primary market: United States for
every seed. All cited IDs verified against `90_BIBLIOGRAPHY/sources.json` as accepted AND
`india_origin_audit`-eligible (rejected/quarantined IDs from the lane briefs were swapped for
eligible co-supporting IDs; notable swaps: L08-016→L08-001/003/004, L09-036→L09-112/113,
L14-040/041/042→L14-043, L15-044→L15-043, L06-040→L06-039, L02-045→L02-046, L10-049→dropped).
Company launch year: 2030. 2026 evidence is baseline pain evidence, not an assumption that 2026
prices/competitors/policies persist. Uncertainty is labeled inline; "inference" flags mean P4 must
re-source before scoring.


> **Adjudication applied 2026-07-13:** the independent elegance/novelty verdicts (`P3R2_ELEGANCE_ADJUDICATION.md`) have been applied to every seed below - PROMOTE/FIX_APPLIED/MERGED/REJECT annotations appear at the end of each seed section and in the batch JSON (`elegance_verdict` fields). See `P3R2_FIX_APPLICATION_LOG.md`.

---

## P3R2-A-01 — 800VDC rack-inlet protection and hot-swap module

- **Product:** UL/IEC-certifiable solid-state 800VDC rack-inlet protection shelf: SiC bidirectional
  disconnect, active precharge/hot-swap management, microsecond fault interruption, DC ground-fault
  and arc-signature detection with fleet telemetry. OCP-form-factor.
- **Buyer + pain evidence:** Rack power OEMs (Vertiv, Eaton, Delta US) and hyperscalers deploying
  NVIDIA/OCP 800VDC architectures (L02-043, L02-044). Rack-inlet grounding, hot-swap, inrush and
  oscillation behavior is documented as unresolved systems engineering (L02-054); DC arc-fault
  detection is still research even at LV (L08-018/019/020/021); datacenter electrification orders
  are at $2.4B/quarter for one vendor alone (L08-033).
- **Technical mechanism:** Series SiC module with sub-10 us current-limiting turn-off, staged
  precharge to suppress inlet oscillation, and high-bandwidth current-signature analytics for
  series/parallel arc discrimination at 800-1500VDC; designed against IEC 62477-1 (L02-112).
- **Why incumbents miss it:** Grid breaker vendors productize at feeder scale; board vendors stop
  at 48V eFuses; rack PSU makers treat protection as someone else's listing problem. There is no
  listed rack-inlet 800VDC protection category yet — a standards-lag wedge, not a physics wedge.
- **Decisive experiment + budget:** 800V/200A interrupter clearing bolted + arcing faults <10 us
  with hot-swap precharge, validated against a recorded transient library. ~$400k, 2027-2028.
- **TRL:** 4.
- **2026–2029 plan (pre-company):** University power-lab characterization of 800V rack fault/arc
  signatures and publication (2026-27); topology + arc-classifier IP; OCP participation; benchtop
  interrupter (2028); third-party interruption-life testing and one rack-OEM pilot LOI (2029).
- **2030–2034 trigger (named):** Second-generation OCP Mount Diablo 800VDC deployment wave and
  1MW-rack retrofits, 2030-2033, following the 2027 Kyber/Rubin ramp (L02-043/044).
- **2030 competition:** Eaton/Schneider/Vertiv shelves, ABB/Hitachi feeder devices (L08-052),
  semiconductor eFuse vendors, 2-3 startups.
- **Window/timing risk:** NVIDIA/OCP reference designs could absorb protection by 2029, reducing
  this to licensing; UL listing pathway timing uncertain.
- **Kill date:** End-2033 if no OEM design-win or hyperscaler pilot by then.
- **Big vision:** Default protection + fault-intelligence layer of the DC datacenter from rack to
  MVDC campus.
- **Nearest substitutes:** Fuses + contactors + upstream AC breakers (today's ad hoc practice);
  PSU-integrated protection.
- **Key uncertainty:** Whether hyperscalers will pay for protection as a separate shelf vs
  demanding integration into PSUs (price-point ownership).
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-01]:** 4x cross-batch convergence proves obviousness. Import into C-01: fleet arc-signature analytics and UL/IEC listing-path emphasis. Record retained as audit trail; not independently promotable.

## P3R2-A-02 — Modular MVDC (1-35kV) hybrid solid-state circuit breaker

- **Product:** Catalogued modular hybrid SSCB frames (mechanical ultrafast disconnect + SiC branch
  + absorber), 1-35kV/1-4kA, with coordinated non-unit DC relaying — sold as products, not
  per-project HVDC engineering.
- **Buyer + pain evidence:** Datacenter campus power teams, DC-GRIDS-seeded utility pilots, MVDC
  collection developers. DC breakers are the documented "showstopper": topology unconverged across
  2023-25 literature (L08-001, L08-003, L08-004, L08-006, L08-013/014/015), datacenter SSCB work
  still academic (L08-017) while datacenter electrification orders boom (L08-033); ARPA-E funded
  a dedicated DC-GRIDS program in 2026 (L02-034); ORNL prototyping (L08-051).
- **Technical mechanism:** Staged commutation — ultra-fast mechanical isolation (<1 ms), SiC
  interruption branch, metal-oxide absorber — packaged as identical series-stackable modules; the
  relay coordination stack handles no-zero-crossing selectivity.
- **Why incumbents miss it:** Hitachi/GE/Siemens engineer breakers per transmission project;
  1-35kV productization has no owner because the MVDC market was too small — until AI campuses.
- **Decisive experiment + budget:** 10kV/2kA module clearing pole-to-pole fault <2 ms, 100+
  operations without refurbishment, at a national-lab facility. ~$1.5M, 2028.
- **TRL:** 3.
- **2026–2029 plan:** Topology benchmarking + scaled prototypes in a university high-power lab
  (2026-27); DC-GRIDS cohort tracking; national-lab 10kV demo (2028); requirements co-development
  with one hyperscaler and one DC-GRIDS performer, test-bed MOU (2029).
- **2030–2034 trigger (named):** First US MVDC campus-distribution and DC-GRIDS-derived utility
  pilots reaching procurement 2030-2033 (L02-034, L08-033); Southern Spirit-class HVDC
  construction from 2029 normalizing DC procurement (L08-041).
- **2030 competition:** Hitachi Energy heritage breakers (L08-052), per-project offerings from
  Siemens/GE (L08-036/037 adjacency), 1-2 ARPA-E spinouts.
- **Window/timing risk:** MVDC may stay point-to-point (breaker-avoiding) into the 2030s;
  converter-integrated fault blocking is a partial substitute.
- **Kill date:** End-2034 if no paid MVDC pilot deployment by then.
- **Big vision:** Enable meshed DC campuses/industrial parks; extend to HVDC tap protection.
- **Nearest substitutes:** Full-bridge MMC fault blocking, AC-side breakers + DC disconnects,
  fuses.
- **Key uncertainty:** Timing of true multi-terminal MVDC adoption in the US.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical MVDC hybrid breaker. Documented showstopper niche; MVDC adoption pace and $1.5M pre-company experiment are the honest risks; lean on DC-GRIDS/ORNL facilities.
- **[Merge-import 2026-07-13 R2]:** absorbed P3R2-F-08 (wave-F REJECT) as the device-strategy workstream: 2027 SiC interruption-duty die-characterization study (di/dt, avalanche energy, series sharing vs press-pack IGBT baselines) and fail-short press-pack qualification concept - cheap, publishable, useful regardless of breaker-market timing; cited to already-present eligible sources (L08-001/003/004/017); F-08's L08-016 is not accepted in the ledger and was not imported.

## P3R2-A-03 — MW-class containerized grid emulator for IBR ride-through compliance (PRC-029-1)

- **Product:** Trailerized 1-5 MW back-to-back converter grid emulator with disturbance playback
  (voltage/frequency/phase-jump, weak grid), automated PRC-029-style test sequences, and
  evidence-grade reporting for plant-level verification.
- **Buyer + pain evidence:** US IBR owner-operators and inverter OEMs facing NERC PRC-029-1
  ride-through obligations approved via FERC Order 909, July 2025 (L08-043); grid-forming
  specification momentum (AEMO framework, 74% of pipeline — L08-048) versus procurement skepticism
  (NESO awarded zero GFM contracts — L08-035) means capability claims need hardware attestation.
- **Technical mechanism:** Bidirectional converter pair synthesizes programmable grid impedance
  and replays recorded disturbance waveforms at MW scale; measurement chain produces
  standard-format compliance artifacts.
- **Why incumbents miss it:** PHIL vendors (OPAL-RT/Typhoon class) stop at lab power; test houses
  lack MW hardware; national-lab facilities are non-commercial and oversubscribed. The compliance
  wave is newer than any product roadmap.
- **Decisive experiment + budget:** 250kW emulator reproducing a recorded multi-phase-jump event
  within 2% envelope error vs PHIL reference, auto-reporting. ~$600k, 2028.
- **TRL:** 5.
- **2026–2029 plan:** Track PRC-029 audits/guidance; converter event-playback control in academic
  PHIL lab (2026-27); 250kW prototype (2028); MW design freeze + two owner-operator LOIs (2029).
- **2030–2034 trigger (named):** NERC PRC-029-1 enforcement/re-verification wave across the US IBR
  fleet 2030-2034 (L08-043), plus GFM capability-attestation demand as US operators formalize
  specifications (AEMO precedent, L08-048).
- **2030 competition:** NREL/Sandia facilities, lab-scale PHIL vendors, consultancies with EMT
  models; syncons as substitute stability provision (L08-036/037).
- **Window/timing risk:** If model-based (EMT) evidence satisfies NERC broadly, field hardware
  demand shrinks; regulatory softening possible.
- **Kill date:** End-2033 if compliance testing remains satisfied by simulation evidence.
- **Big vision:** The verification network for an inverter-dominated grid (ride-through, GFM
  attestation, interconnection model validation).
- **Nearest substitutes:** EMT simulation studies; OEM factory type tests; mobile load banks
  (no disturbance capability).
- **Key uncertainty:** NERC/regional-entity acceptance criteria for hardware vs model evidence —
  inference; P4 must confirm from compliance guidance documents.
- **[FIX applied 2026-07-13]:** demand mechanism hedged (field-MW-hardware requirement unproven vs EMT-model compliance; 2027 documentation gate added); GFM-attestation leg dropped on the NESO negative finding (AEMO kept as watch-item only); repositioned as the field-hardware complement to E-14 with a fold-in path if the gate fails.

## P3R2-A-04 — Merchant HTS quench detection and magnet protection subsystem

- **Product:** Qualified protection stack for REBCO magnets: distributed fiber-optic + RF/acoustic
  quench sensing, sub-ms detection electronics, coordinated energy-extraction control, sold with
  an acceptance-test protocol.
- **Buyer + pain evidence:** CFS (selling magnets to Realta, WHAM — L03-035), Tokamak Energy/TE
  Magnetics (L03-033/044), DOE milestone-program awardees (L03-032), ORNL/US-ITER (L03-030).
  Quench detection at HTS scale is the lane's #1 documented unsolved pain (L03-004…008, L03-018);
  strain/screening-current degradation raises the stakes (L03-020/021).
- **Technical mechanism:** Sensor fusion (Rayleigh-backscatter fiber for mm-scale hot-spot
  localization + RF/acoustic precursors + fast voltage taps) feeding a deterministic sub-5 ms
  protection decision and staged energy extraction.
- **Why incumbents miss it:** Magnet builders treat protection as in-house IP but their core
  business is magnets, not instrumentation; test-and-measurement majors see too-small a market
  today; national labs improvise one-offs.
- **Decisive experiment + budget:** Driven-quench campaign on instrumented sub-scale REBCO
  pancakes: <5 ms reliable detection, <1 false trip per 1,000 ramps. ~$350k, 2027.
- **TRL:** 3.
- **2026–2029 plan:** Instrument sub-scale coils in a university/lab magnet program; publish +
  patent sensor fusion (2026-27); retrofit demo on mid-scale DOE-lab coil, define acceptance
  metrics with two builders (2028); customer test-coil pilot + reliability dossier (2029).
- **2030–2034 trigger (named):** DOE Milestone-Based Fusion Development Program follow-on awards
  (post-FY2027 renewal decision) and fusion pilot-plant magnet procurements 2030-2034 (L03-032,
  L03-035).
- **2030 competition:** In-house teams at CFS/TE; lab instrumentation groups; possible entry by
  fiber-sensing firms (Luna-class) if market proves.
- **Window/timing risk:** Fusion schedule slip; builders may hold protection in-house as IP.
- **Kill date:** End-2034 if fusion magnet merchant market has not produced repeat third-party
  subsystem orders.
- **Big vision:** Protection + health monitoring for the HTS era (fusion, NMR/accelerator magnets,
  superconducting grid hardware).
- **Nearest substitutes:** No-insulation windings (protection-by-design, with ramp-rate penalty);
  conventional voltage-tap protection.
- **Key uncertainty:** Whether merchant subsystems can win against in-house pride at the two US
  anchor customers.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-D-01]:** Import into D-01: acceptance-test protocol / warranty framing for merchant magnet sales. Record retained as audit trail; not independently promotable.

## P3R2-A-05 — US merchant NEG-coating and low-outgassing surface-engineering line

- **Product:** Domestic coating service + component line: TiZrV-class NEG sputter coating of beam
  pipes/chambers, vacuum-firing low-hydrogen treatment, certified outgassing metrology per part.
- **Buyer + pain evidence:** DOE accelerator labs and US-ITER (ITER vacuum tenders live 2025-26 —
  L07-041/042/043/044), NASA space-simulation facilities (L07-035), quantum/EUV chamber builders
  (DOE $625M QIS demand context — L13-028). NEG pumping is effectively single-vendor (SAES —
  L07-037); hydrogen outgassing control requires 30h/250C bakeouts (>70,000x reduction —
  L07-008/009; NEG physics L07-001).
- **Technical mechanism:** Magnetron-sputtered getter films turn chamber walls into pumps;
  combined with vacuum-fired low-H substrates, cutting installed pumping cost and schedule.
- **Why incumbents miss it:** SAES has no US line and no competitor emerged because accelerators
  coated in-house at CERN-affiliated labs; US labs and commercial UHV OEMs lack a merchant option;
  general vacuum job shops don't own the getter metallurgy.
- **Decisive experiment + budget:** NEG-coated 1 m test pipes activating at ≤200C with sticking
  coefficients within 20% of published SAES-class values, independently verified. ~$250k, 2027.
- **TRL:** 5.
- **2026–2029 plan:** Recipe replication on university sputter rig + spec survey (2026-27); pilot
  coating for one DOE lab under cooperative agreement + certified outgassing bench (2028);
  production-line design, two lab LOIs + one chamber-OEM LOI (2029).
- **2030–2034 trigger (named):** DOE accelerator-upgrade and QIS-facility construction
  procurements 2030-2034 (L13-028) plus continuing ITER-class vacuum tenders (L07-041…044).
- **2030 competition:** SAES (sole merchant incumbent), lab in-house coating, ULVAC-class majors
  if niche grows (L07-052).
- **Window/timing risk:** Niche stays small if accelerator budgets stall; SAES could add US
  capacity.
- **Kill date:** End-2034 without a recurring lab/OEM coating book.
- **Big vision:** Engineered vacuum surfaces as a product across accelerators, quantum, EUV, and
  space chambers; integrated getter-pump products.
- **Nearest substitutes:** More ion/turbo pumps; longer bakeouts; buying from SAES with lead-time
  and sovereignty risk.
- **Key uncertainty:** True annual US demand volume (part count) — P4 must build a bottom-up count
  from lab upgrade schedules.
- **[Adjudication 2026-07-13 - PROMOTE]:** Single-source (SAES) supply gap + US sovereignty preference; process know-how moat; modest vision ceiling accepted; SAES adding US capacity is the kill risk. 2026-07-13: absorbed B-12 (CN NEG line). No content imported: the license-into-China model was rejected by the adjudicator as IP leakage in a process-know-how business with CEPC-dependent lumpy demand; A-05 remains US-primary with no CN chapter.

## P3R2-A-06 — Cryogenic I/O scaling stack (high-density flex + integrated 4K LNA/mux)

- **Product:** US-manufactured cryo interconnect looms (superconducting/thin-film flex, engineered
  thermal anchoring) plus integrated 4K modules (LNA + multiplexing) sold as qualified
  channels-per-watt.
- **Buyer + pain evidence:** DOE QIS centers (Fermilab SQMS, Brookhaven C2QA, Argonne Q-NEXT, LBNL
  QSA, ORNL QSC — $625M program, L13-028), US superconducting-qubit builders, Bluefors Syracuse
  ecosystem (L13-041). Wiring density is ~10x short of thousand-qubit needs and the only roadmap
  is a single vendor's unvalidated projection (L13-042); LNA/cryo-CMOS power budgets collide with
  fridge cooling limits (L13-013, L13-021, L13-004/005; fridge cooling-power frontier
  L07-014…017).
- **Technical mechanism:** Photolithographic flex looms cut conductor cross-section and heat leak
  per channel; cold multiplexing amortizes LNA power; the product is a qualified thermal/noise
  budget, not a cable.
- **Why incumbents miss it:** Fridge vendors sell fridges; control vendors sell room-temperature
  racks; the in-between I/O chain is a Dutch boutique (Delft Circuits) with no US line, while DOE
  is actively onshoring quantum supply (Fermilab-Qblox CRADA — L13-032).
- **Decisive experiment + budget:** 64-channel loom + 4K mux/LNA at ≤2 mW/channel with qubit-grade
  noise temperature in a host fridge at a DOE lab. ~$500k, 2027-28.
- **TRL:** 4.
- **2026–2029 plan:** Thermal/microwave modeling + prototype looms in university cryo lab
  (2026-27); 4-8x cold mux module within power budget, DOE-center evaluations (2028); working
  in-fridge pilot + cycling reliability + manufacturing plan (2029).
- **2030–2034 trigger (named):** DOE QIS center renewals and 1,000+ qubit-class machine builds
  2030-2033 (L13-028; 1,000+ qubit control-system delivery signal L13-037, vendor-claim caution).
- **2030 competition:** Delft Circuits, Bluefors integrated offerings, in-house wiring at
  IBM/Google-class builders; cryo-CMOS partially substitutes if it matures (L13-004/005).
- **Window/timing risk:** Cryo-CMOS/optical-link breakthroughs reduce channel counts; federal
  quantum funding continuity.
- **Kill date:** End-2034 if quantum builders still consume <$10M/yr of merchant cryo I/O.
- **Big vision:** Interconnect backbone for cryogenic computing/sensing (quantum, detectors,
  cryo-CMOS test).
- **Nearest substitutes:** Semi-rigid coax looms; vendor-bundled wiring from fridge makers.
- **Key uncertainty:** Qubit-count trajectory of paying customers (superconducting modality risk).
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-E-04]:** Import channels-per-watt sales framing into E-04. Record retained as audit trail.

## P3R2-A-07 — Standardized solid-state pulsed-modulator platform

- **Product:** Catalogued Marx/solid-state modulator family (50-150kV, 10-500A) built from one
  qualified switch module + one control/diagnostics backbone; klystron, magnetron, and e-beam
  drive from identical building blocks; published acceptance protocol per IEC 60060-1:2025.
- **Buyer + pain evidence:** Varex (cargo linacs; industrial segment +25% YoY, >$55M new cargo
  orders — L05-033), DOE ARDAP ecosystem (70 institutions — L05-031), SLAC GREEN-RF
  commercialization (L05-032), gyrotron/RF programs (Thales/F4E EUR20M — L05-029), ESS-class
  modulator procurement precedent (L05-030). Five+ incompatible solid-state designs and no
  module/interconnect standard is the documented pain (L05-003, L05-005, L05-009); no
  accelerator-specific HV test standard beyond IEC 60060 (L05-043).
- **Technical mechanism:** Identical IGBT/SiC switch modules with droop-correction, arbitrary
  series/parallel scaling, integrated diagnostics; one qualified module amortizes reliability
  data across the whole family (klystron coupler-failure pain L05-014 raises value of clean
  drive; L05-015 drive-circuit lineage; LTD heritage L05-044).
- **Why incumbents miss it:** ScandiNova/Jema are European project shops; CPI bundles with tubes
  (L05-050); US labs custom-build. Nobody sells standardized modules with catalog delivery in the
  US.
- **Decisive experiment + budget:** 100kV/100A/5us modulator from 12 identical modules, <1%
  flat-top droop, module hot-swap, witnessed per IEC 60060-1. ~$800k, 2028.
- **TRL:** 5.
- **2026–2029 plan:** Standard-module design + 30kV university testbed (2026-27); 100kV stack
  driving surplus klystron at lab partner, ARDAP/SBIR-track qualification (2028); pilot units at
  one linac OEM + one DOE lab, MTBF collection (2029).
- **2030–2034 trigger (named):** US cargo-scanning fleet expansion and DOE accelerator-stewardship
  procurement 2030-2034 (L05-033, L05-031), riding thyratron obsolescence replacement.
- **2030 competition:** ScandiNova (L05-047), Jema (L05-030), CPI in-house (L05-050), lab builds.
- **Window/timing risk:** OEM vertical integration; slow certification cycles in
  security/medical.
- **Kill date:** End-2034 without an OEM design-win or multi-unit lab orders.
- **Big vision:** US pulsed-power standard from cargo scanners to fusion RF and flash radiography.
- **Nearest substitutes:** Legacy PFN/thyratron refurbishment; European project modulators.
- **Key uncertainty:** Whether buyers value standardization enough to switch from incumbent
  project relationships.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-09]:** 5x convergence. Import IEC 60060-1:2025 acceptance-protocol emphasis into C-09. Record retained as audit trail.

## P3R2-A-08 — Traceable ultra-high-dose-rate (FLASH) beam metrology instrument

- **Product:** UHDR-hardened beam monitor (compensated toroid + fast electro-optic/Faraday
  channel) with a traceability-grade calibration method; per-unit certificates for FLASH R&D and
  e-beam/X-ray sterilization QA.
- **Buyer + pain evidence:** US clinical linac OEMs developing FLASH; contract e-beam/X-ray
  sterilization operators under ISO 11137-1:2025 (L05-042) with capacity backlogs (L05-028);
  accelerator metrology groups (ARDAP base L05-031). Two independent 2024-25 groups documented
  BCT failures under FLASH transients — unresolved (L05-023, L05-024).
- **Technical mechanism:** Charge-buildup-compensated toroidal sensing plus an independent fast
  optical channel; cross-calibrated against calorimetry to build a traceability chain that
  ionization chambers cannot provide at UHDR.
- **Why incumbents miss it:** Bergoz-class vendors (L05-049) sell catalog BCTs not validated in
  this regime; the market is currently research-scale so majors ignore it; the physics failure
  mode is documented but unproductized.
- **Decisive experiment + budget:** Side-by-side UHDR test: <2% current error where standard BCTs
  show published transient errors, calorimetry-validated. ~$200k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** Replicate error mechanisms on a university linac; prototype compensated
  sensor; NIST-adjacent calibration engagement (2026-27); cross-validation at two facilities +
  method publication (2028); pilots in one FLASH program and one sterilization QA lab (2029).
- **2030–2034 trigger (named):** First FLASH radiotherapy regulatory submissions/clearances
  expected early 2030s (inference from trial stage — flagged for P4) plus ISO 11137-1:2025-driven
  revalidation across the growing e-beam base (L05-042, L05-028).
- **2030 competition:** Bergoz catalog BCTs, OEM in-house physics, ionization-chamber vendors
  (physically limited at UHDR).
- **Window/timing risk:** FLASH slips past 2034; instrument-scale market ceiling.
- **Kill date:** End-2033 if FLASH regulatory pathway has not materialized and sterilization QA
  does not adopt.
- **Big vision:** Dosimetry backbone for ultra-fast beams (therapy, industrial UHDR, accelerator
  pulses).
- **Nearest substitutes:** Faraday cups (destructive), radiochromic film (offline), current BCTs
  (inaccurate at UHDR).
- **Key uncertainty:** FLASH clinical timeline; market size below venture scale (may be a
  bootstrap/instrument business).
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-09]:** Import ISO 11137-1:2025 sterilization-QA channel into D-09. Record retained as audit trail.

## P3R2-A-09 — Compact self-shielded solid-state e-beam/X-ray sterilization cell

- **Product:** Factory-floor sterilization cell: 3-10 MeV solid-state-modulator-driven
  accelerator, integrated shielding + conveyor, ISO 11137 dosimetry/records — sized for one device
  plant, serviced like a machine tool.
- **Buyer + pain evidence:** US medical-device OEMs and contract sterilizers exiting EtO. The two
  pure-play e-beam vendors (IBA, L3) are reported backlogged into 2026-27 with a named new line
  (SteriLab — L05-028, trade-press caveat); ISO 11137-1:2025 drives revalidation (L05-042); Varex
  shows accelerator-source industrial demand growth (L05-033).
- **Technical mechanism:** Solid-state modulator reliability (L05-003/005/009, drive-circuit
  lineage L05-015/016) enables uptime economics a thyratron-era in-house machine could not offer;
  compact shielding via beam-energy and geometry choices.
- **Why incumbents miss it:** Incumbents sell central, building-scale plants and are
  capacity-constrained; their business model is throughput hubs, not distributed cells; device
  OEMs increasingly want supply-chain control of sterilization.
- **Decisive experiment + budget:** Dose-uniformity mapping (DUR <1.5) on representative device
  loads using a rented 10 MeV beamline + certified techno-economics vs contract sterilization.
  ~$300k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** Architecture + state radiation-licensing pathfinding (2026-27); dose-mapping
  campaign + two OEM LOI discussions (2028); full engineering design + certification plan + anchor
  term sheet (2029).
- **2030–2034 trigger (named):** Continuing EtO-replacement capacity procurement (IBA/L3 backlog
  evidence L05-028) and ISO 11137-1:2025 revalidation; strength depends on US EtO regulatory
  tightening — EPA rule NOT in accepted ledger; P4 must source before scoring (flagged).
- **2030 competition:** IBA, L3 Applied Technologies (central systems), Varex (sources), possible
  new entrants; Chinese vendors excluded from US medical procurement in practice (L05-035 China
  context only).
- **Window/timing risk:** If incumbents scale capacity or EtO pressure stalls, in-house economics
  weaken; per-site licensing friction.
- **Kill date:** End-2034 without an anchor purchase order.
- **Big vision:** Distributed sterilization; then food-safety and bioprocess beams on the same
  platform.
- **Nearest substitutes:** Contract EtO/gamma/X-ray services; central e-beam plants.
- **Key uncertainty:** Capex tolerance of device OEMs for in-house radiation facilities
  (~$15-35M v1); EtO regulatory trajectory.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-08]:** In-house model fights contract-sterilization industry structure and per-site licensing friction; EtO driver not in accepted ledger. D-08 absorbs as deployment option. Record retained as audit trail.

## P3R2-A-10 — Ion-energy-distribution metrology + tailored-waveform bias control retrofit

- **Product:** Chamber-mounted IEDF sensing (RF-immune retarding analyzer / derived-signal
  estimation) + waveform-synthesis bias controller closing the loop on ion energy, retrofittable
  onto existing RF generators.
- **Buyer + pain evidence:** US leading-edge fabs (CHIPS-era expansions) and etch tool OEMs;
  Advanced Energy's new waveform-capable platforms are ramping ("double-digit millions", early
  production — L06-039) while tailored-voltage-waveform control remains an unsettled 2024-26
  research frontier (L06-009/010/011, L06-027; matching-network frontier L06-001/003); China etch
  growth as secondary mirror (L06-048); arc/abnormal-discharge detection thinly published
  (L06-018).
- **Technical mechanism:** Fast sheath-voltage reconstruction + energy-resolved ion flux
  estimation feeding model-predictive synthesis of multi-harmonic bias waveforms; holds programmed
  IEDF shape against drift.
- **Why incumbents miss it:** Generator vendors sell sources, not vendor-neutral metrology; tool
  OEMs guard chamber data; fabs lack independent measurement to arbitrate — the control loop's
  sensor half has no owner.
- **Decisive experiment + budget:** Closed-loop hold of a programmed bimodal IEDF within +/-2 eV
  across induced pressure/chemistry drift on a lab reactor, correlated to etch profiles. ~$450k,
  2027-28.
- **TRL:** 4.
- **2026–2029 plan:** IEDF estimation on university ICP/CCP reactor benchmarked to gridded
  analyzers, publications + patents (2026-27); alpha retrofit on OEM lab chamber under JDA (2028);
  SEMI-standards engagement + US fab process-development pilot (2029).
- **2030–2034 trigger (named):** Sub-2nm/backside-power etch capacity ramps at CHIPS-funded US
  fabs 2030-2033 and second-generation waveform-bias adoption (L06-039).
- **2030 competition:** AE/MKS/Comet embedding partial capability (L06-039, L06-049; RF incumbents
  L01-049/050); Impedans-class diagnostics; OEM internal sensors.
- **Window/timing risk:** Proprietary chamber-data lockout; good-enough integrated inference by
  2030 narrows the retrofit market to process development.
- **Kill date:** End-2033 without an OEM JDA or fab pilot.
- **Big vision:** Ion-energy-defined processing as the cross-industry control standard.
- **Nearest substitutes:** OES endpointing, generator-side V/I sensing, occasional gridded-probe
  campaigns.
- **Key uncertainty:** Access to development chambers without OEM sponsorship.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical TVW/IEDF control. Merge in C-06 dual-entity export partition, E-03 KR validation channel, B-21 event-detection layer. Export-control counsel is a 2027 gate. 2026-07-13: absorbed C-06 (US/CN two-entity export partition as company structure), B-05 (CN mature-node RF-delivery chapter with localization evidence), E-03 (Samsung co-authorship pull + KR validation channel), B-21 (event-detection/forensics layer, FTO-gated). primary_market US->US+CN and china_beachhead->true because the CN demand leg is independent and cited to eligible CN evidence (L06-042/043/044/048/054); honesty conditions documented - mature-node (>=28nm) scope only, 2027 export-control counsel gate, leading-edge line stays in the US entity.

## P3R2-A-11 — Sub-100ms no-overshoot fast MFC with inline transient metrology

- **Product:** Pressure-insensitive fast MFC (model-predictive valve control + fast sensing)
  delivering settled steps <100 ms without overshoot, plus an inline transient-verification
  module producing SEMI E17-style evidence per channel.
- **Buyer + pain evidence:** Tool OEMs and gas-panel integrators (customer concentration evidence:
  Lam+AMAT = 76% of Ichor's $947.7M — L07-049); SEMI E17 codifies transient response as the
  constraint (L06-035) and 2025 control literature is still attacking MFC transients (L06-026);
  US subfab onshoring signal (CHIPS Edwards award — L06-033); leading-edge platform ramp context
  (L06-039); power-quality-era standards vintage (SEMI F47 2007 — L06-034) shows the standards
  lag pattern.
- **Technical mechanism:** Pressure-based flow sensing (fast, drift-tolerant) + MPC valve
  actuation compensating upstream pressure changes; verification module = calibrated fast
  rate-of-rise measurement.
- **Why incumbents miss it:** Incumbent thermal-MFC architectures are sensing-limited on
  transients; their roadmaps optimize steady-state accuracy and cost; a sensing-modality change is
  a startup-shaped move.
- **Decisive experiment + budget:** 0-90% steps settling <100 ms, zero overshoot, across 2x
  upstream-pressure variation, independently verified. ~$300k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** Control/sensor bench work (2026-27); third-party SEMI E17-protocol
  characterization vs incumbents + integrator JDA discussions (2028); alpha units on an OEM
  development tool (2029).
- **2030–2034 trigger (named):** Next-generation US fab tool builds 2030-2033 (CHIPS-funded
  capacity; L06-033) and an expected SEMI E17 revision tightening transient specs (L06-035
  vintage evidence — revision timing is inference, flagged).
- **2030 competition:** Horiba/Brooks/MKS/Fujikin incumbent lines (structure via L07-049);
  pressure-based products maturing.
- **Window/timing risk:** Incumbent catch-up; long OEM qualification cycles.
- **Kill date:** End-2033 without an OEM design-in.
- **Big vision:** Gas-delivery timing layer for atomic-layer processing across industries.
- **Nearest substitutes:** Faster valve sequencing around existing MFCs; charge-volume dosing.
- **Key uncertainty:** Whether measured throughput delta on real ALD/ALE recipes is large enough
  to force a supplier switch.
- **[FIX applied 2026-07-13]:** 2028 paid-eval/LOI dual-sourcing gate added; $/tool/year throughput-value-vs-switching-cost quantification added; P4 task to broaden the technical base beyond L06-026/034.

## P3R2-A-12 — Cycling-tolerant printed-circuit heat exchangers as a catalog product

- **Product:** Standardized PCHE family qualified to defined thermal-ramp classes with published
  creep/fatigue data (ASTM E139-class methods) and a standing acceptance protocol — catalog
  frames, quoted lead times.
- **Buyer + pain evidence:** STEP Phase 2 integrators (GTI/SwRI/GE Vernova — L04-039),
  advanced-reactor BOP chains (TerraPower's thin named-vendor pool — L04-045), sCO2 and
  heat-to-power developers financed at scale (Fervo-Turboden 1.75 GW — L04-044; $421M project
  debt — L04-115; DOE LPO $1.76B — L04-114). PCHE thermal-cycling durability is the most-cited
  sCO2 bottleneck (L04-029, L04-004/005/006); no sCO2 acceptance-test standard exists (standards
  gap; materials challenges L04-113; seal frontier L04-101; creep-test standard L04-112).
- **Technical mechanism:** Diffusion-bonded microchannel cores with channel geometries and bonding
  schedules engineered for rapid transients (target >=20 C/min classes), qualified via
  accelerated cycling + metallography; acceptance protocol substitutes for the missing PTC.
- **Why incumbents miss it:** Oil/gas PCHE suppliers qualify for steady-state duty; national labs
  hand-build one-offs; nobody owns cycling-class qualification as a catalog promise because the
  sCO2 market was all demos until now.
- **Decisive experiment + budget:** Subscale core surviving 10,000 transients (200-600C at
  >=20 C/min) with <5% effectiveness loss, independent inspection. ~$900k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** Bonding/channel R&D + cycling rig + ASTM E139-24 qualification plan
  (2026-27); 10,000-cycle campaign + spec engagement with STEP-2 and a reactor developer (2028);
  pilot-scale unit order from a lab program + manufacturing partner (2029).
- **2030–2034 trigger (named):** Advanced-reactor BOP procurement (Natrium follow-on units under
  the NRC Part 53 regime effective 2026 — L04-031, L04-045) and STEP-class sCO2 scale-up plus
  EGS/ORC power-block expansion 2030-2034 (L04-039, L04-044, L04-114/115).
- **2030 competition:** Heatric-class suppliers, Vacuum Process Engineering, in-house lab
  fabrication (L04-029/039 pattern), Korean ecosystem (L04-047).
- **Window/timing risk:** Advanced-energy schedule slip; incumbents extending into cycling-rated
  designs if signaled early.
- **Kill date:** End-2034 without repeat (non-demo) orders.
- **Big vision:** The compact heat-exchanger standard for high-temperature power conversion.
- **Nearest substitutes:** Shell-and-tube (bulky), bespoke lab-built PCHEs, plate-fin exchangers.
- **Key uncertainty:** Which end-market (nuclear vs sCO2 vs geothermal) produces the first repeat
  order; nuclear QA burden.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-08]:** Import catalog-frames/lead-time framing and STEP/TerraPower buyer detail into C-08. Record retained as audit trail.

## P3R2-A-13 — Modular rad-tolerant GaN PPUs (2-20kW) with standardized interfaces

- **Product:** Qualified modular PPU family: rad-tolerant GaN stages, standardized
  anode/keeper/mag supplies, common telemetry, AIAA S-122 / ECSS-E-ST-20-20C-aligned interfaces
  (L09-115, L09-111), scaling by module count, sold with a public radiation dossier.
- **Buyer + pain evidence:** NASA EP lineage ($67M AEPS — L09-034; $18.4M NEXT-C — L09-012),
  Gateway PPE chain (L09-043), SDA-scale proliferated procurement ($3.5B Tranche 3 — L09-039; EP
  content unconfirmed, flagged), NASA SBIR component demand (L09-112/113). PPU topology
  non-convergence and supplier concentration are documented pains (L09-041: Aerojet inside
  missile-focused L3Harris).
- **Technical mechanism:** GaN converter stages with SEE-aware derating and topology-level SET
  mitigation (L09-108), validated against heavy-ion GaN/SiC failure physics (L09-103/104,
  L09-014, L09-020); modularity converts qualification cost into a reusable asset.
- **Why incumbents miss it:** The incumbent's parent optimizes for missiles; primes rebuild PPUs
  per program; component vendors (EPC Space, VPT — L09-054/055/053) stop below the
  subsystem level; small-sat EP is priced out (JAXA/Furukawa signal — L09-042).
- **Decisive experiment + budget:** 5kW GaN discharge supply passing heavy-ion test at full
  operating voltage (no destructive SEE at mission-representative LET), >96% efficiency,
  published. ~$700k, 2027-28.
- **TRL:** 4.
- **2026–2029 plan:** University heavy-ion campaigns + breadboard 5kW supply (2026-27);
  SBIR-track qualification module + thermal-vac + interface whitepaper to primes (2028); EM unit
  hot-fire with partner thruster in vacuum facility (2029).
- **2030–2034 trigger (named):** NASA Gateway/Mars-logistics EP sustainment and SDA Tranche 4/5
  procurement 2030-2034 (L09-034/012/043; L09-039 scale signal with EP-content caveat).
- **2030 competition:** L3Harris/Aerojet, Busek/Moog in-house, EPC Space components, JAXA/Furukawa
  (Japan), Rocket Lab vertical integration (L09-114).
- **Window/timing risk:** Prime vertical integration; GaN SEE derating eroding the advantage;
  NASA budget cycles.
- **Kill date:** End-2034 without a flight-qualification contract.
- **Big vision:** Merchant power electronics for the electric spacecraft, up to fission-surface-
  power conversion electronics.
- **Nearest substitutes:** Silicon rad-hard PPUs (mass penalty), program-specific prime builds.
- **Key uncertainty:** Whether proliferated-constellation primes buy merchant PPUs or clone
  in-house; SDA EP content must be confirmed in P4.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical GaN PPU. SDA EP content unconfirmed - P4 must close. Merge in E-10 ECSS/AIAA framing + JAXA-Furukawa pattern; D-15 SEE-map-first sequencing. Prime vertical integration is standing risk. 2026-07-13: absorbed E-10 (ECSS/AIAA qualification framing, JAXA-Furukawa J-SPARC partner pattern, KARI emergent-buyer note) and D-15 (SEE-map-first sequencing, qualified-once qualification-file framing, Space Force Maneuverable-GEO trigger L09-037). Prime vertical integration remains the standing risk.

## P3R2-A-14 — 300C-class mixed-signal electronics platform for superhot geothermal and downhole

- **Product:** Qualified 300C instrumentation platform: SiC/SOI front-ends (ADC, mux, drivers),
  high-temp passives/packaging stack, and a reference logging/telemetry module sold to tool OEMs.
- **Buyer + pain evidence:** Baker Hughes ($2.0B New Energy orders incl. 300MW geothermal ORC —
  L15-040), SLB-Ormat EGS pilot (L15-041), FORGE awardees (Welltec, PetroQuip — L15-027/028),
  ARPA-E SUPERHOT performers (>375C target — L15-029), DARPA THERMAL (800C ICs — L15-026).
  Commercial HT ICs stop at 225C and the incumbent line is obsolete/last-time-buy (CISSOID CHT —
  L15-043); no converged platform above 250C after two decades of programs (L15-031, L15-001,
  L15-004).
- **Technical mechanism:** SiC JFET/SOI mixed-signal circuits (NASA Glenn 500C/1-yr lineage —
  L15-009, HOTTech — L15-030) plus the real bottleneck: die-attach/packaging engineered and
  cycled as part of the platform (L15-005, L15-025).
- **Why incumbents miss it:** Oilfield service majors build in-house at 175-200C for their own
  tools only; CISSOID/Honeywell exited/obsoleted; DARPA still funding 800C basics proves no
  commercial platform exists — the 250-350C product band is orphaned between silicon and science.
- **Decisive experiment + budget:** 8-channel SiC/SOI acquisition front-end running 1,000 h at
  300C with <1% drift + 500 packaging thermal cycles, independently witnessed. ~$850k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** Building-block circuits via university SiC/SOI fab runs + packaging cycling
  study (2026-27); 1,000-h soak + FORGE/SUPERHOT community engagement + 10 OEM discovery
  interviews (2028); field-representative module in heated test well/autoclave + service-company
  LOI (2029).
- **2030–2034 trigger (named):** Superhot-rock EGS drilling campaigns 2030-2034 seeded by ARPA-E
  SUPERHOT (awards from Nov 2025 — L15-029) and FORGE cohorts (L15-027/028); Baker Hughes-scale
  geothermal order flow (L15-040); DARPA THERMAL Phase II completion ~2029 de-risks hotter
  follow-ons (L15-026).
- **2030 competition:** TI HT silicon (to ~210C), CISSOID remnants, in-house SLB/Halliburton
  electronics, niche design houses; no 300C qualified platform seller.
- **Window/timing risk:** Superhot drilling slips → market stays program-funded; oilfield
  in-house capture.
- **Kill date:** End-2034 without a paying tool-OEM qualification program.
- **Big vision:** Native electronics for hot places: geothermal, aero-engine/hypersonic
  instrumentation, Venus-class missions, hot gate-drive.
- **Nearest substitutes:** Active cooling (dewars/thermal batteries — L15 competing-strategy
  evidence), derated 225C parts with short mission life.
- **Key uncertainty:** Volume: whether superhot EGS well counts by 2034 support a platform vendor
  (P4 bottom-up from FORGE/SUPERHOT drilling plans).
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical 300C platform. Best demand-timing story in family (SUPERHOT/FORGE vs CISSOID/Honeywell exit). Merge in E-09 packaging-first strategy + JP side market; D-14 400C tier. 2026-07-13: absorbed E-09 (packaging-first strategy, 1,000h powered-soak artifact, JP decommissioning side market), D-14 (400C SiC-JFET tier, FORGE field-trial step), B-17 (rejected CN chapter - kept out of demand base for lack of named CN procurement).

## P3R2-A-15 — Precision thermal qualification instrumentation for liquid/two-phase cooling

- **Product:** Reference thermal test vehicles (to 5kW/chip, mapped local flux), 1%-closure
  calorimetry benches for cold plates/CDUs (Deschutes-class protocols), and accelerated post-PFAS
  fluid qualification rigs, with a published methods library.
- **Buyer + pain evidence:** Seven+ vendors building CDUs to Google's open 2MW Deschutes spec
  (L14-043); Vertiv's +50% liquid-cooling orders and $15B backlog (L14-048, secondary-sourced);
  M&A-consolidated integrators needing credible data (Flex/JetCool — L14-045; ZutaCore $100M C —
  L14-046); COOLERCHIPS ecosystem incl. NVIDIA/Raytheon (L14-030/031). Pain: GB200-class
  TDP/flow specs are inconsistent across sources with no authoritative public spec (L14-044);
  3M PFAS exit + AIM Act/EU F-gas collision forces industry-wide fluid requalification
  (L14-033/034, research still using discontinued Novec — L14-022).
- **Technical mechanism:** Emulated-TDP dies with embedded flux mapping; enthalpy-closure
  calorimetry (<=1% electrical-to-fluid balance) on 100+ LPM single/two-phase loops
  (microchannel/flux frontier — L14-009/010; two-phase behavior — L14-001/002/003); standardized
  accelerated fluid-aging protocols.
- **Why incumbents miss it:** Test-equipment majors have no fluid calorimetry; hyperscalers build
  in-house and don't sell; JEDEC-era methodology is air-cooling vintage; every vendor
  self-certifies with incomparable data — a classic missing-metrology market.
- **Decisive experiment + budget:** Test vehicle (2.5kW) + bench showing <=1% enthalpy closure and
  a published 3-vendor cold-plate round-robin exposing measurement spread. ~$350k, 2027.
- **TRL:** 5.
- **2026–2029 plan:** Open reference test-vehicle design + round-robin publication + calorimetry
  prototype (2026-27); alpha benches at two CDU vendors + OCP methods contribution (2028);
  productized bench + fluid-qual rig with paid evaluation backlog (2029).
- **2030–2034 trigger (named):** EPA AIM Act step-down to 30% of baseline in 2029 (L14-033) and
  post-Novec fluid transitions colliding with 4,000W+ chip platforms and 2MW CDU ecosystems
  (L14-044, L14-043) through 2030-2033.
- **2030 competition:** In-house hyperscaler labs, generic thermal test chambers, university labs,
  possible COOLERCHIPS spinout; ITRI as Taiwan-side ecosystem (L14-053).
- **Window/timing risk:** OCP/ASHRAE standardizing on hyperscaler in-house methods; R&D-budget
  cyclicality of equipment sales.
- **Kill date:** End-2033 if hyperscalers/vendors show no willingness to pay for neutral
  metrology.
- **Big vision:** The metrology authority of liquid-cooled computing; extend to CPO optics
  cooling and power-electronics thermal test.
- **Nearest substitutes:** Vendor self-testing; one-off consultant studies; national-lab
  facilities.
- **Key uncertainty:** Vertiv figures are secondary-sourced (L14-048 caveat); P4 must re-derive
  from the primary 10-K.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-05]:** Import fluid-qualification rigs and 1%-closure calorimetry spec into C-05. Record retained as audit trail; not independently promotable.

## P3R2-A-16 — Chiplet-era TIM system (liquid-metal/sintered) with per-package reliability engineering

- **Product:** A TIM *system*: liquid-metal/sintered-metal composite + engineered barrier/wetting
  layers + qualified dispensing/containment process, sold with accelerated reliability data
  (power cycling, pump-out, corrosion) per package family.
- **Buyer + pain evidence:** US advanced packagers and AI-accelerator vendors; defense electronics
  primes (COOLERCHIPS lineage incl. Raytheon/NVIDIA — L14-030). Pain: TIM tradeoffs (bulk
  conductivity vs bond-line vs compliance) are a documented first-order constraint for 2.5D/3D
  chiplet packages (L14-014/015/016/018) as device flux heads to 800-1,000 W/cm2 (L14-010) and
  rack architectures go liquid (L14-044).
- **Technical mechanism:** Metallic interfaces at <=5 mm2K/W with metallurgical barriers that
  survive thousands of power cycles; reliability engineering is the product, formulation is
  table stakes.
- **Why incumbents miss it:** Incumbent TIM suppliers optimize for dispense-line manufacturability
  at volume; extreme-flux engineered-per-package work is service-heavy and initially small — a
  classic overshoot niche.
- **Decisive experiment + budget:** <=5 mm2K/W with <10% degradation over 1,000 cycles at
  500 W/cm2 local flux vs two incumbent TIMs. ~$400k, 2028.
- **TRL:** 3.
- **2026–2029 plan:** University materials program (barriers, pump-out physics) + cycling rig
  (2026-27); test-vehicle reliability demonstration + packager advanced-dev engagement (2028);
  pilot process definition with dispensing partner + anchor qualification plan (2029).
- **2030–2034 trigger (named):** US advanced-packaging ramps and 4-5kW accelerator packages
  2030-2033 (L14-010, L14-044).
- **2030 competition:** Honeywell/Shin-Etsu/Dow, Indium Corp, packager in-house; academic
  liquid-metal commoditization at the formulation level.
- **Window/timing risk:** Direct-liquid/embedded cooling could bypass TIM1; materials giants can
  outspend once the segment is proven.
- **Kill date:** End-2033 without a packager qualification engagement.
- **Big vision:** Own the last 50 microns between die and coolant across AI, power, RF.
- **Nearest substitutes:** Best-in-class silicone/graphite TIMs, solder TIMs, direct-bonded lids.
- **Key uncertainty:** Whether packagers award materials qualification to a startup at all
  (supply-assurance bias) — mitigate via dispensing-equipment partner.
- **[FIX applied 2026-07-13]:** converted consulting-shaped offering into a productized SKU + dispensing-process license model; 2028 anchor-packager LOI added; the two-incumbent head-to-head reliability delta made the explicit kill gate.

## P3R2-A-17 — Ruggedized beam-combining and wavefront-control subsystem for 100kW+ lasers

- **Product:** Merchant combining stack: multi-channel (32→512) phase detection + kHz-class
  locking electronics, environmental-grade deformable-mirror control, turbulence/jitter
  compensation firmware — qualified subsystem for primes and NNSA labs.
- **Buyer + pain evidence:** JLWS awardees nLIGHT Defense and Lockheed Martin Aculight ($86M
  initial/$847M ceiling, July 2026 — L12-031/032), nLIGHT A&D revenue $175.3M and growing
  (L12-033), NNSA EYC CD-1 + $26M FY2026 (L12-042), DARPA MELT laser tiles and POWER relay
  (L12-041, L12-047). Pain: TMI caps single-fiber power (L12-016/017/018) so scaling runs through
  CBC (L12-001/002), and a documented gap exists between astronomy-grade AO and ruggedized
  fieldable control (L12-009/010/011); GAO documents the prototype-to-program transition risk
  (L12-045).
- **Technical mechanism:** Stochastic-parallel-gradient + heterodyne phase sensing hybrid,
  hard-real-time FPGA control, vibration-tolerant optical metrology; delivered as a qualified
  LRU with documented environmental envelope.
- **Why incumbents miss it:** Each prime rebuilds beam control internally per program; component
  vendors sell lab parts; no merchant mid-tier exists — the JLWS production schedule makes
  buying faster than rebuilding.
- **Decisive experiment + budget:** 32-channel combining at >90% efficiency with residual phase
  error <lambda/30 under induced vibration. ~$600k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** University photonics lab phase-lock architectures 8-16 channels +
  benchmarks (2026-27); 32-channel demo, SBIR/STTR entry (2028); environmental testing + prime
  teaming agreement (2029).
- **2030–2034 trigger (named):** JLWS production/scaling decisions within the $847M ceiling
  2030-2033 (L12-031/032) plus NNSA EYC execution beyond CD-1 (L12-042) and MELT/POWER follow-ons
  (L12-041/047).
- **2030 competition:** Prime in-house (nLIGHT, LM, Northrop), Coherent/II-VI components,
  DM vendors without control stacks; IPG industrial combining (L12-034).
- **Window/timing risk:** Primes refusing to outsource core beam control; classification
  friction; DEW budget cyclicality.
- **Kill date:** End-2034 without a prime subcontract or lab production order.
- **Big vision:** The coherence layer for high-power photonics — DEW, power beaming, fusion
  drivers, industrial combining.
- **Nearest substitutes:** In-house prime solutions; spectral beam combining (partial); bigger
  single fibers (TMI-limited).
- **Key uncertainty:** Willingness of primes to buy the crown-jewel subsystem from a merchant.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-10]:** Import ruggedized DM control and NNSA EYC demand leg into D-10. Record retained as audit trail.

## P3R2-A-18 — Precision high-current laser-diode driver modules (GaN, sub-ns, telemetry)

- **Product:** Driver family: multi-hundred-amp CW/QCW GaN stages, <1% ripple, sub-ns pulse
  shaping options, integrated diode-health telemetry, ruggedized formats.
- **Buyer + pain evidence:** nLIGHT/Coherent-class OEMs and DARPA AMPED performers. Driver
  electronics remain an active research frontier (GaN pulsed topologies L12-027; LLC modulation
  L12-025; ps-resolution drivers L12-026); every integrator inherits driver R&D risk (documented
  pain); DEW volume growth via JLWS (L12-031/033); AMPED $53M program (L12-040).
- **Technical mechanism:** GaN stages with active ripple cancellation and per-channel health
  analytics correlating drive quality to diode degradation — telemetry as differentiation.
- **Why incumbents miss it:** Laser OEMs treat drivers as internal plumbing; instrument vendors
  stop at low current; nobody sells qualified high-current precision drive with lifetime data.
- **Decisive experiment + budget:** 500A CW GaN driver, <0.5% ripple, telemetry, driving a diode
  stack; published comparison vs two commercial drivers. ~$250k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** Topology + benchmarking (2026-27); 500A CW + 2ns-edge prototypes, diode
  lifetime-correlation study with a diode vendor (2028); ruggedization/EMI qual + two OEM
  evaluations (2029).
- **2030–2034 trigger (named):** JLWS-driven pump-diode volume growth 2030-2033 (L12-031/033);
  DARPA AMPED Phase 2 completion ~2029 leading to productization (L12-040).
- **2030 competition:** OEM in-house teams (IPG/nLIGHT/Coherent — L12-034/033), defense
  electronics houses, fragmented merchant field.
- **Window/timing risk:** Component-vendor squeeze; must win on telemetry + qualification data.
- **Kill date:** End-2033 without OEM design-ins.
- **Big vision:** The current source behind every high-power photon, including chip-scale laser
  tiles.
- **Nearest substitutes:** In-house drivers; adapted server power modules.
- **Key uncertainty:** Standalone company vs product line of A-17 — orchestrator may merge.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-13]:** Import diode-health telemetry differentiator into C-13. Record retained as audit trail.

## P3R2-A-19 — Switch-mode low-ripple DC power retrofits for electrowinning and electrolysis

- **Product:** Modular IGBT/SiC switch-mode rectifier skids (10-100kA) with active ripple control,
  PFC, per-cell telemetry + health analytics; brownfield retrofits with verified
  energy-per-tonne guarantees.
- **Buyer + pain evidence:** US copper electrowinning tankhouses (archetype — named buyers to be
  sourced in P4), DOE H2Hub projects (up to $2.2B committed — L11-032), electrolyzer deployments
  (Plug $187M revenue — L11-046). Pain: six-pulse thyristor installed base; documented ~13-14%
  specific-energy penalty from ripple/harmonics in electrolysis (L11-016/017/019/020/021) and the
  same lever marketed in electrowinning (L11-045; electrochemistry literature L11-026/027).
  Atlas guidance: rectifier quality is the sanctioned L11 niche; no stack plays against Chinese
  overcapacity (L11-035 context).
- **Technical mechanism:** Interleaved switch-mode stages with active ripple shaping matched to
  cell electrochemistry; per-cell monitoring converts energy savings into a measurable,
  financeable guarantee.
- **Why incumbents miss it:** Legacy rectifier vendors sell capex-optimized thyristor units;
  buyers are conservative and never see the opex telemetry; the efficiency lever sits in
  literature, not products.
- **Decisive experiment + budget:** Side-by-side pilot cells, independently metered, verified
  >=5% specific-energy improvement vs thyristor-emulated drive. ~$350k, 2027-28.
- **TRL:** 5.
- **2026–2029 plan:** Ripple-to-efficiency transfer functions on lab cells + publication + 10kA
  module design (2026-27); pilot-scale side-by-side + financier-grade M&V protocol (2028);
  single-rectifier retrofit LOI at one US site (2029).
- **2030–2034 trigger (named):** DOE H2Hubs Phase 2/3 construction disbursements 2030-2033
  (L11-032) and US copper electrowinning investment driven by electrification demand (archetype —
  inference, P4 to name buyers and budgets).
- **2030 competition:** Legacy thyristor suppliers, Dynapower/Advint-class integrators (L11-045),
  Chinese stack OEMs bundling rectification upstream (L11-048, L11-035 context).
- **Window/timing risk:** Conservative replacement cycles; bundling by stack OEMs limits
  greenfield share — brownfield focus mitigates.
- **Kill date:** End-2034 without a paid tankhouse/plant retrofit.
- **Big vision:** Precision DC across electrochemical industry — one platform, many chemistries.
- **Nearest substitutes:** 12/24-pulse thyristor upgrades + passive filters; doing nothing
  (cheap power eras).
- **Key uncertainty:** US electrowinning buyer set and energy-price sensitivity must be
  evidenced in P4 (currently archetype-level).
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-07]:** Import US tankhouse/H2Hub beachhead sequencing and financier M&V protocol into C-07. Record retained as audit trail.

## P3R2-A-20 — Recuperative battery-formation power electronics for US gigafactories

- **Product:** Bidirectional SiC formation shelves (>=97% channel recuperation), plant-level DC
  bus energy pooling, grid-services-capable control; retrofit shelves for integrators and plants.
- **Buyer + pain evidence:** US cell plants (archetype), formation-line integrators; market
  structure dominated by Chroma ATE (TW) and Hioki (JP) with US-oriented precision niche players
  (NOVONIX/Arbin/BioLogic) (L11-043/044). Formation is a documented energy/capex sink and this
  sub-market is decoupled from the hydrogen cycle (L11-043/044; precision-DC literature
  L11-016/017/020/021).
- **Technical mechanism:** Channel-to-channel energy recirculation on a shared DC bus rather than
  per-channel dissipation/AC round-trips; plant-level orchestration turns formation floors into
  controllable load/storage.
- **Why incumbents miss it:** Incumbents monetize measurement precision and installed
  relationships; system-level energy pooling and US-domestic service is a different product
  concept aimed at plant economics, not test specs.
- **Decisive experiment + budget:** 100-channel rack, >=95% plant-level round-trip recovery on a
  representative protocol, calibration <0.05%. ~$500k, 2028.
- **TRL:** 5.
- **2026–2029 plan:** Architecture study + incumbent benchmark + 10 plant-engineering interviews
  (2026-27); prototype rack + UL pathway (2028); pilot in one US formation development line
  (2029).
- **2030–2034 trigger (named):** Second-wave US gigafactory buildouts/retooling 2030-2034
  (structure evidence L11-043/044; named US plant demand must be sourced in P4 — flagged).
- **2030 competition:** Chroma, Hioki, Digatron/PEC recuperative lines, Arbin/NOVONIX.
- **Window/timing risk:** EV demand volatility; recuperation partially commoditized — wedge must
  be plant-level pooling + grid interactivity, else fails the commoditization screen.
- **Kill date:** End-2033 if recuperative formation is commodity across incumbents with no
  system-level differentiation left.
- **Big vision:** Formation floors as grid assets; platform extends to electrolyzer test and
  burn-in.
- **Nearest substitutes:** Incumbent recuperative cyclers; contract formation.
- **Key uncertainty:** Differentiation durability vs Chroma roadmap — weakest seed of the batch
  by design (extra for discard).
- **[Adjudication 2026-07-13 - REJECT]:** Hidden commodity: incumbents already ship recuperative formation lines; residual wedge is a feature; named US demand absent. Pair seed E-06 rejected for same reason. Record retained as audit trail.

## P3R2-A-21 — Ruggedized multi-megawatt charging systems for ports, rail yards, and mines

- **Product:** 1.5-6MW modular charging systems: SiC stacks, liquid-cooled MCS dispensing per
  IEC TS 63379, fleet-management-integrated sequencing, containerized for harsh duty, optional
  storage buffering.
- **Buyer + pain evidence:** EPA Clean Ports grantees (53 grants, ~$3B, 26 states — L10-048),
  Union Pacific (10 FLXdrive order — L10-032; 7 MWh Heavy-Haul variant — L10-051), US surface
  mines following the BHP/Rio/Cat 793 XE trials (L10-030). Pain: miners build chargers in-house
  for lack of vendors (Fortescue 6MW — L10-029), three charging architectures compete
  unconverged (L10-002), trolley/charging research still active (L10-014); MCS standard published
  Feb 2026 (L10-050); megawatt cable/connector thermal engineering is still a research area
  (L14-019/020/021/022).
- **Technical mechanism:** Interleaved SiC conversion + liquid-cooled 3,000A-class dispensing +
  autonomous-docking-compatible controls integrated with fleet management; storage buffering to
  cap demand charges at weak-grid sites.
- **Why incumbents miss it:** EVSE majors chase highway trucking; mining/rail OEMs bundle
  proprietary chargers with vehicles; the open, harsh-duty, fleet-integrated merchant niche is
  unowned.
- **Decisive experiment + budget:** 1MW stack + liquid-cooled dispenser executing repeated
  10-minute megawatt sessions at 45C ambient with published thermal/efficiency data. ~$1.2M,
  2028.
- **TRL:** 5.
- **2026–2029 plan:** Duty-cycle/interconnection studies with one port and one railroad + MCS
  tracking (2026-27); 350kW-1MW prototype at a utility/university test yard + dispenser thermal
  design (2028); funded pilot commitment with a Clean Ports grantee (2029).
- **2030–2034 trigger (named):** EPA Clean Ports equipment deliveries through 2030 (L10-048),
  Class-I battery-locomotive scaling beyond initial FLXdrive orders (L10-032/051), US mine BEV
  fleet decisions post-Early-Learner trials (L10-030), MCS certification wave post-IEC TS 63379
  (L10-050).
- **2030 competition:** ABB/Siemens/Kempower-class (truck-focused), Wabtec/Cat proprietary
  bundles (L10-051/053), in-house builds (L10-029).
- **Window/timing risk:** US regulatory reversals (CARB repeal — L10-044) can soften port/drayage
  demand; mining capex cycles; OEM bundling.
- **Kill date:** End-2034 without a funded port/rail/mine deployment.
- **Big vision:** The refueling layer of heavy industry; extend to vessel charging hybrids.
- **Nearest substitutes:** Diesel (status quo), battery swap (Chinese ecosystem), trolley-assist
  infrastructure.
- **Key uncertainty:** Pace of US mine/rail fleet conversion absent regulatory compulsion —
  economics-led adoption timing.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical heavy-fleet charging. Top-decile demand evidence (obligated EPA funds, named fleets); elegance mediocre (integration play); OEM-bundled charging and regulatory reversal are the risks. Import C-15 dual-standard option, B-14 interface-personality module. 2026-07-13: absorbed C-15 (dual-standard cabinet option, station-DC-backbone concept; its CN demand leg NOT imported - demand-without-access vs vertically integrated domestic stacks) and registered B-14's fold-in path as the interface-personality module. A-21 remains US-primary.

## P3R2-A-22 — Modular plasma destruction units for concentrated PFAS streams

- **Product:** Containerized plasma destruction units (100-2,000 L/day) for PFAS concentrates
  (spent AFFF, IX regenerant, membrane reject): nanosecond-pulsed plasma reactor, fluoride
  capture, integrated destruction-verification instrumentation producing regulator-grade records.
- **Buyer + pain evidence:** US DoD installation restoration (paid precedent: $2.25M PFAS
  destruction contract, >300 tonnes treated — L01-036; defense torch spending trajectory
  $4.1M→$27M — L01-034/035), remediation primes, water utilities holding PFAS concentrate
  residuals. Supplier base is one thin foreign small-cap; destruction demand is evidenced by
  delivered contracts, not projections.
- **Technical mechanism:** Nanosecond-pulsed non-thermal plasma (power-supply lineage — L01-112,
  L01-105) attacking C-F bonds in concentrate-phase liquids with staged mineralization and
  fluoride mass-balance verification; "numbering-up" reactor economics fit modular skids rather
  than MW torch plants (L01-014/015/016; DBD water-treatment lineage L01-101).
- **Why incumbents miss it:** The incumbent (PyroGenesis) is MW-torch-centric and
  defense-project-driven; SCWO competitors have corrosion/salt handling burdens on brines;
  nobody sells verified on-site modular destruction with auditable records.
- **Decisive experiment + budget:** Skid prototype: >99.99% PFOA/PFOS destruction on real AFFF
  concentrate at <=50 kWh/kg-PFAS with closed fluorine mass balance, independent analytical
  verification. ~$550k, 2027-28.
- **TRL:** 4.
- **2026–2029 plan:** University plasma-chemistry campaign (destruction efficiency vs energy;
  verification chemistry) (2026-27); 10-50 L/day skid with a DoD-lab/SERDP-style collaboration
  (2028); base or utility demonstration + cost dossier vs SCWO (2029).
- **2030–2034 trigger (named):** DoD installation-restoration destruction procurements 2030-2034
  following AFFF transition completion (paid precedent L01-036); utility concentrate-destruction
  demand as treatment residuals accumulate (inference — EPA drivers must be re-sourced in P4;
  flagged).
- **2030 competition:** PyroGenesis, SCWO vendors (374Water/Aquagga-class), electrochemical
  oxidation startups, incineration under regulatory pressure (competitor gasification context
  L01-053).
- **Window/timing risk:** Technology selection could tip to SCWO; destruction-verification
  regulatory acceptance unsettled.
- **Kill date:** End-2034 without a DoD or utility purchase order.
- **Big vision:** Distributed molecular incineration for halogenated and pharma waste.
- **Nearest substitutes:** Hazardous-waste incineration, deep-well injection, storage/deferral.
- **Key uncertainty:** Plasma vs SCWO cost-per-kg-destroyed at concentrate salinity; EPA
  regulatory driver not yet in accepted ledger.

---

Lane coverage (primary): L01, L02, L03, L04, L05 (x3), L06 (x2), L07, L08 (x2), L09, L10, L11
(x2), L12 (x2), L13, L14 (x2), L15 — 15 distinct primary lanes, 22 seeds. Seeds A-08, A-09,
A-11, A-16, A-18, A-20 are deliberate extras with flagged weaknesses for orchestrator discard.

EE/CE transfer note (post-freeze, generic): all 22 seeds are built on power-electronics, RF,
instrumentation-and-control, and mixed-signal/packaging engineering, so validation work on any
one seed builds directly reusable electrical/computer-engineering capability for the others.
- **[Adjudication 2026-07-13 - PROMOTE]:** Paid DoD precedent anchors an enthusiasm-zone lane correctly; verification-chemistry wedge; SCWO competition named; EPA drivers to re-source in P4.

