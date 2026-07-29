# P3R2 Batch C — Dual US+China seeds (22)

Generated 2026-07-13 by the batch-C idea architect (Fable 5 / xhigh). Rules applied: repaired
atlas + lane briefs only; every cited ID verified `accepted: true` and
`india_origin_audit.status = verified_non_india_origin` in `90_BIBLIOGRAPHY/sources.json`;
none of the 42 excluded IDs cited; no claim resurrected from a P2A-removed passage. Each seed
carries independent US and China demand logic such that either market alone could sustain the
beachhead; export-control separability is addressed per seed. India/Singapore excluded
throughout; JP/TW/KR appear only as optional side markets. Substitute vendors named without
atlas IDs are explicitly flagged "uncited — P4 to source." All 2026 prices, policies,
schedules, and competitor facts are treated as baseline evidence to be refreshed in P4/P6, not
as 2030 constants.


> **Adjudication applied 2026-07-13:** the independent elegance/novelty verdicts (`P3R2_ELEGANCE_ADJUDICATION.md`) have been applied to every seed below - PROMOTE/FIX_APPLIED/MERGED/REJECT annotations appear at the end of each seed section and in the batch JSON (`elegance_verdict` fields). See `P3R2_FIX_APPLICATION_LOG.md`.

---

## P3R2-C-01 — 800-VDC rack power-path protection and hot-swap unit

- **Product:** Shelf-format 800V/250–500A hybrid solid-state breaker + managed precharge/inrush
  + insulation monitoring + blind-mate hot-swap sequencing, pre-certified to IEC 62477-1
  (L02-112). The "circuit-breaker layer" every 800VDC rack and sidecar needs and nobody sells.
- **US buyer + pain:** NVIDIA-ecosystem shelf vendors (Eaton, Vertiv, Schneider) and OCP
  hyperscalers; 800VDC is specified for 2027 Kyber/Rubin-Ultra racks (L02-043, L02-044) while
  datacenter electrification capital runs at $2.4B/quarter at one vendor alone (L08-033) and DC
  fault interruption remains research-stage (L08-017, L08-001/003/004).
- **China buyer + pain:** Huawei-class integrators and Alibaba-lineage HVDC operators; Chinese
  trade engineering names 800V protection, grounding, hot-plug, and inlet oscillation as
  unresolved (L02-054); HVDC penetration was only ~12% vs 78% UPS, so the conversion wave is
  ahead (L02-048); the sole mainland NVIDIA-list chip supplier is still in testing (L02-050).
- **Mechanism:** Hybrid interruption (SiC static path + mechanical isolator), <100 µs clearing,
  arc-signature discrimination adapted from the DC arc-fault literature (L08-018–021),
  coordinated precharge state machine.
- **Why incumbents miss it:** Shelf incumbents sell whole power shelves and treat protection as
  an internal cost; breaker incumbents (ABB/Hitachi-lineage, L08-052) build utility-scale
  hardware, not shelf-format hot-swappable units.
- **Decisive experiment:** Q2 2027, $350k — brassboard clearing <100 µs into inductive fault;
  10,000 hot-swap cycles; nuisance-trip immunity at 1MW-rack transient levels.
- **TRL:** 4.
- **2026–2029 plan (pre-company):** topology benchmark publications; OCP power-workstream
  membership; 2–3 provisional patents; 2028 integrator-lab test via MOU; 2029 design-in LOIs +
  evidence refresh.
- **2030–2034 triggers:** US — post-2027 NVIDIA 800VDC production scaling into gigawatt campus
  builds (L02-043) and OCP Mount Diablo spec revisions (L02-044). CN — implementation of the
  April 2026 national AI-energy action plan, Guo-Neng-Fa-Ke-Ji [2026] No.34 (L14-036), plus
  conversion of the low-penetration HVDC base (L02-048).
- **2030 competition:** US — Eaton/Vertiv/Schneider shelves, ABB/Siemens DC breakers, SSCB
  startups. CN — Huawei in-house, Delta, Autrans (L02-049), Innoscience-based designs (L02-050).
- **Window/export risk:** Window stays open because DC protection has not converged after years
  of research (L08-001/003/004/017) and certification is slow for newcomers-at-scale. Export
  separability good: conventional industrial power electronics; dual-entity with local GaN/SiC
  sourcing per market. Risks: hyperscaler verticalization; possible future power-semiconductor
  controls.
- **Kill:** end-2034 if no integrator design win; earlier if OCP standardizes a competing
  in-shelf protection unit with entrenched suppliers by 2032.
- **Big vision:** protection layer for all DC infrastructure — racks, MVDC campuses, EV
  megawatt charging, DC industrial parks.
- **Nearest substitutes:** fuses + contactors (status quo), utility hybrid breakers (L08-052),
  shelf-integrated protection from PSU vendors.
- **Key uncertainty:** whether hyperscalers demand a merchant certified unit vs. accepting
  integrator-internal solutions.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical 800V protection. Genuine independent US/CN demand legs; absorb A-01 fleet analytics, B-03 damping, E-01 ROC dataset + TW/JP wedges. Spec-absorption by NVIDIA/OCP is the standing kill trigger. 2026-07-13: absorbed A-01 (fleet arc-signature analytics, UL/IEC listing path), B-03 (virtual-impedance damping, capacitor ESR/ripple telemetry), B-04 (CN protection-stack variant; unique damping/telemetry content already covered), E-01 (arc-ROC dataset moat; TW Delta/COMPUTEX and JP ROHM supply wedges - best secondary-market logic in the cluster). China leg unchanged: already independently evidenced (L02-048/050/054, L14-036). Standing kill trigger: spec absorption by NVIDIA/OCP.

## P3R2-C-02 — Rack-level pulsed-load energy buffer and DC-link module

- **Product:** 30–100 kW electrolytic-free 800V buffer shelf (film caps + GaN partial-power
  converter): 10:1 transient smoothing, active bus damping, ride-through, capacitor prognostics.
- **US buyer + pain:** power-shelf vendors and hyperscalers; DC-link capacitors are a leading
  converter failure mechanism exactly as density rises (L02-010) and 800V racks concentrate
  pulsed GPU load (L02-043/044; TDP/flow ambiguity itself documented at L14-044).
- **China buyer + pain:** Huawei-ecosystem integrators; inlet-node voltage oscillation and
  hot-plug transients at 800V are named unresolved pains in Chinese trade engineering
  (L02-054); Alibaba-lineage HVDC fleets face the same physics (L02-048).
- **Mechanism:** partial-power conversion lets a small converter manage a large film-cap energy
  bank, hitting electrolytic-bank cost while removing the wear-out mechanism; active damping
  kills bus resonance.
- **Why incumbents miss it:** PSU vendors solve transients by oversizing capacitance
  (cheapest BOM line today); facility vendors solve it at MW scale (flywheels, L16-052);
  nobody owns the rack-level buffer as a product category.
- **Decisive experiment:** 2027, $300k — 30kW brassboard reproducing published 800V oscillation
  profiles; 10:1 smoothing; 1,000h film-vs-electrolytic accelerated reliability.
- **TRL:** 4.
- **2026–2029 plan:** pulse-spectrum characterization from OCP/NVIDIA public material; buffer
  sizing models; patents; 2028 100kW lab prototype; 2029 integrator LOIs.
- **2030–2034 triggers:** US — OCP shelf-spec iterations for 600kW–1MW racks defining a
  ride-through/buffer function (L02-043/044). CN — AI-energy action plan efficiency push
  (L14-036) + HVDC retrofit cycle (L02-048).
- **2030 competition:** Vicor-class modules (L02-113), SiC BBU vendors (L02-051), Delta
  (L02-037); CN — Huawei/Delta in-house.
- **Window/export risk:** commoditization is the main risk — if NVIDIA specs an in-rack buffer
  and Delta/Vicor ship it by 2029 the wedge closes (kill trigger). Export separability good;
  dual-entity manufacturable.
- **Kill:** end-2033 without a design-in.
- **Big vision:** the "power shock absorber" for every pulsed-load system (racks, MW chargers,
  pulsed industrial tools).
- **Nearest substitutes:** oversized electrolytic banks; facility flywheels/rotary UPS
  (L16-052); BBUs.
- **Key uncertainty:** whether buffering lands at rack, shelf, or facility level in the winning
  architecture.
- **[FIX applied 2026-07-13]:** end-2029 fold-into-C-01 kill trigger codified; electrolytic-bank/BBU cost-parity quantification and 2028 integrator-eval gate added.

## P3R2-C-03 — Medium-voltage SST power block for AI campuses (2.4 MW class)

- **Product:** Modular MV-to-800VDC solid-state transformer brick with HF insulation designed
  against the documented IEC 60076 certification mismatch (L02-036, L02-001); multiport-ready
  (L02-107); sold as a certified block to shelf/skid OEMs.
- **US buyer + pain:** OCP hyperscalers — Mount Diablo explicitly standardizes SST power units
  (L02-044) — yet a decade of ARPA-E funding (CIRCUITS→DC-GRIDS, L02-033/034; DOE FITT/SiC
  packaging, L02-111) has produced no certified deployable MV SST.
- **China buyer + pain:** Chinese campuses under the AI-energy action plan (L14-036) with rack
  HVDC lineage (L02-048) lack the MV-to-800VDC stage; Huawei-side integration pains documented
  (L02-054).
- **Mechanism:** SiC cell-stack + medium-frequency transformer; the innovation focus is
  insulation coordination/partial-discharge management engineered to pass (and shape) the
  coming standards revision — attacking the certification blocker, not just the topology.
- **Why incumbents miss it:** incumbents profit from line-frequency transformers + rectifier
  chains; SST startups chase grid/EV first; nobody targets the OCP datacenter socket where a
  spec channel already exists.
- **Decisive experiment:** 2028, $1.2M (consortium/university funded) — 100kW MV cell-string,
  partial-discharge + thermal-cycling dataset vs IEC 60076-24-relevant regimes; publish the
  certification-gap analysis.
- **TRL:** 4.
- **2026–2029 plan:** DC-GRIDS-adjacent university research; IEC/IEEE working-group seats;
  patents on insulation/cell-bypass; 2029 hyperscaler pilot LOI + CN licensing conversation.
- **2030–2034 triggers:** US — OCP SST track maturing into procurement specs 2030–2032
  (L02-044) amid sustained electrification capex (L08-033). CN — action-plan implementation and
  green-power direct-connection framework (L14-036).
- **2030 competition:** Eaton/Schneider/Vertiv, GE Vernova (L02-115), SST startups; CN —
  Huawei, Delta (L02-037), State-Grid-adjacent suppliers.
- **Window/export risk:** capital-heaviest seed; standards timing can slip (the very lag that
  blocked incumbents, L02-036). Export separability moderate — MV SiC stacks to CN may face
  controls; CN entity builds on domestic SiC. Refresh all program facts in 2029.
- **Kill:** 2034; interim kill if no certified MW-class field pilot by end-2033.
- **Big vision:** replace transformer+rectifier chains across datacenters, EV hubs, DC
  industrial parks, then distribution grid.
- **Nearest substitutes:** conventional MV transformer + 800V rectifier shelves (works today);
  GE Vernova-class packaged substations.
- **Key uncertainty:** whether OCP-era buyers will certify a startup's MV product without a
  giant's balance sheet behind it.
- **[FIX applied 2026-07-13]:** hard 2028 gate on IEC 60076-24-class standards progress plus an OCP SST procurement signal; pre-company scope restricted to HF-insulation/PD dataset and standards seats; re-batch-to-wildcard rule if the gate fails; confidence lowered medium->low (schedule-fragile category).

## P3R2-C-04 — PFAS-free pumped two-phase direct-to-chip cooling loop

- **Product:** Sealed fluid-agnostic pumped two-phase loop (cold plate, micro-pump, condenser,
  charge management) qualified on a menu of non-PFAS low-GWP fluids; drop-in >2kW/chip module
  for ODM/CDU vendors, with fluid-lifetime warranty data.
- **US buyer + pain:** CDU/thermal vendors (Vertiv's liquid-cooling orders +50%, $15B backlog,
  L14-048) and OCP hyperscalers (Deschutes ecosystem, L14-043); 3M's PFAS exit removed the
  qualified two-phase fluid family while the AIM Act steps HFCs down to 30% of baseline in
  2029–2033 (L14-033; EU parallel, L14-034); recent literature still validates on discontinued
  Novec (L14-022); chips head to 3–5kW/800–1,000 W/cm² (L14-010).
- **China buyer + pain:** Chinese liquid-cooling vendors and operators facing GB 40879 PUE
  ≤1.25/1.2 (L14-035) and the T/CIEP 0263-2025 liquid-cooling specification (L14-039); Chinese
  reviews call phase-change cooling the trajectory (L14-029). (The rumored "100% liquid-cooling
  mandate" is NOT in the primary action-plan text (L14-036) and is not relied on.)
- **Mechanism:** wide-envelope evaporator + charge management designed around fluid-property
  ranges instead of one chemistry; every future fluid shock becomes an upgrade, not a redesign.
- **Why incumbents miss it:** two-phase startups are locked to proprietary fluids (ZutaCore,
  L14-046); CDU majors defend single-phase water; chemical majors sell fluids, not loops.
- **Decisive experiment:** 2027, $400k — 2kW loop on two candidate non-PFAS fluids; heat-flux/
  stability envelope vs Novec-era baselines; 1,000h sealed-loop degradation.
- **TRL:** 4.
- **2026–2029 plan:** fluid-screening matrix with a chemical partner; charge-management and
  evaporator patents; 2028 reliability run + hyperscaler lab evaluation; 2029 ODM LOI +
  regulatory refresh.
- **2030–2034 triggers:** US — AIM Act 2029 step-down (L14-033) colliding with >4kW chips
  (L14-046 context). CN — GB 40879 enforcement and T/CIEP adoption as acceptance criteria
  (L14-035/039).
- **2030 competition:** US — ZutaCore (L14-046), LiquidStack/Trane (L14-051), JetCool/Flex
  (L14-045), Motivair/Schneider; CN — Envicool (L14-043), Huawei in-house; TW — ITRI-fed ODM
  supply chain (L14-053).
- **Window/export risk:** binding risk is fluid qualification pace — if no non-PFAS two-phase
  fluid reaches datacenter scale by 2031, single-phase wins another cycle (kill trigger).
  Export separability good (uncontrolled thermal hardware; CN localization).
- **Kill:** 2034.
- **Big vision:** own the two-phase layer for the 5kW-chip era across computing, power
  electronics, EV charging, radar.
- **Nearest substitutes:** single-phase water cold plates (incumbent), proprietary-fluid
  two-phase systems, immersion tanks.
- **Key uncertainty:** fluid-chemistry availability and its toxicology/flammability trade
  space by 2030.
- **[FIX applied 2026-07-13]:** adopted B-01's negative-pressure architecture as the primary loop mechanism (defensible-by-physics wedge) with the fluid-menu qualification dataset as second moat; 2031 fluid-availability kill trigger retained; confidence high->medium pending the mechanism demo. B-01 remains the CN-primary canonical; C-04 carries the US+CN dual variant.

## P3R2-C-05 — Standards-grade thermal emulation and conformance metrology

- **Product:** Calibrated programmable thermal test vehicles (0.2–5kW, hotspot maps), rack/
  manifold emulators to 2MW class, and traceable acceptance protocols for liquid/two-phase
  cooling — the industry's thermal dynamometer.
- **US buyer + pain:** the 7+ vendors building CDUs to Google's open Deschutes spec (Boyd,
  CoolerMaster, Delta, Envicool, Nidec, nVent, Vertiv — L14-043) design against inconsistent
  thermal figures; even GB200-class TDP/flow numbers conflict across sources with no
  authoritative public spec (L14-044); COOLERCHIPS ecosystem needs common metrology (L14-030).
- **China buyer + pain:** Chinese cooling vendors must demonstrate conformance to T/CIEP
  0263-2025 (L14-039) and operators must prove GB 40879 PUE compliance (L14-035); domestic
  two-phase push documented (L14-029).
- **Mechanism:** silicon/vapor-chamber vehicles with 16+ zone hotspot control and traceable
  calorimetry; protocol library replaces ad hoc dummy loads.
- **Why incumbents miss it:** every vendor builds internal rigs (sunk-cost inertia); test
  majors haven't noticed the category; institutional analogs (NTT hub L14-050, ITRI L14-053)
  validate the need but don't productize.
- **Decisive experiment:** Q4 2026–2027, $150k — 1.2kW programmable vehicle; blind round-robin
  of 3 commercial cold plates; publish method + variance.
- **TRL:** 5.
- **2026–2029 plan:** university-built first vehicle; open cross-vendor comparison to establish
  method authority; OCP + Chinese-standards engagement via academic partner; 2028 rack-emulator
  pilot; 2029 LOIs.
- **2030–2034 triggers:** US — multi-vendor CDU proliferation and M&A integration waves
  (L14-043/045/051) forcing third-party-grade qualification. CN — T/CIEP conformance adoption
  and PUE acceptance testing for national-hub datacenters (L14-039/035).
- **2030 competition:** in-house rigs, thermal test houses; no dominant merchant vendor;
  institutional labs (L14-050/053).
- **Window/export risk:** TAM ceiling (instrumentation) mitigated by protocols/consumables;
  export separability excellent. If OCP/JEDEC ships full method + reference hardware without us
  by 2030, differentiation collapses — mitigated by standards participation.
- **Kill:** 2034.
- **Big vision:** the defining metrology vendor of liquid-cooled computing; reference datasets
  feeding US/CN/OCP standards.
- **Nearest substitutes:** homemade dummy heaters; chip-vendor thermal test vehicles (scarce,
  restricted); commissioning consultants.
- **Key uncertainty:** willingness to pay for third-party metrology vs. continued in-house
  improvisation.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical thermal metrology. Documented spec chaos as demand driver; independent US/CN legs; tiny capex; TAM ceiling honestly flagged. Absorb A-15 and B-02. 2026-07-13: absorbed A-15 (post-PFAS fluid-qualification rigs; <=1%-closure calorimetry spec; AIM Act/EU F-gas demand ids L14-033/034) and B-02 (T/CIEP 0263-2025 clause-scripted reporting; certification-lab channel; corrosion/biofouling protocol source L14-028). CN leg unchanged - already US+CN with T/CIEP-0263/GB-40879 evidence.

## P3R2-C-06 — Tailored-voltage-waveform RF bias platform for plasma tools

- **Product:** Waveform-programmable bias generator (kHz–MHz synthesis, sub-ns edges) with
  co-designed fast adaptive match and ion-energy-distribution closed loop; bolt-on subsystem
  for etch/deposition OEMs. CN line restricted to ≥28nm-class applications.
- **US buyer + pain:** leading-edge fabs/tool OEM programs; TVW biasing is a live 2024–2026
  frontier with industry co-authorship (L06-009/010/011/027) but no off-the-shelf subsystem;
  Advanced Energy's next-gen platforms are still "early pilot/early production" (L06-039) —
  demand is ahead of supply.
- **China buyer + pain:** AMEC/NAURA/Piotech growing 40–55%/yr (L06-048) on an RF-component
  base <12% localized (L06-054) supplied by two fragile domestic entrants (Hengyunchang
  customer concentration 45–63%, L06-042/043; Injet, L06-044).
- **Mechanism:** direct digital synthesis of bias waveforms + µs-class re-match (L06-001/002/
  003) turns ion energy distribution into a programmable set-point.
- **Why incumbents miss it:** incumbents monetize installed sinusoidal-generator bases and
  retrofit slowly; Chinese entrants copy legacy architectures to displace imports, not to leap
  a generation.
- **Decisive experiment:** 2027, $450k — TVW bias + adaptive match on a 300mm university ICP
  testbed; programmable IEDF narrowing vs sinusoidal; <10 µs re-match under waveform switching.
- **TRL:** 4.
- **2026–2029 plan:** plasma-lab collaboration, publications, match/waveform co-optimization
  patents; 2028 alpha in one OEM process lab; 2029 two design-in LOIs (US leading-edge; CN
  ≥28nm) + completed export-control legal review.
- **2030–2034 triggers:** US — waveform bias entering HVM specs for next logic/memory
  generations 2030–2033 (trajectory: L06-039 ramp + L06-009 industry co-authorship). CN —
  localization push from <12% base (L06-054) across AMEC/NAURA capex cycles (L06-048).
- **2030 competition:** US — Advanced Energy, MKS, Comet Synertia (L06-049), TRUMPF Hüttinger
  (L01-049); CN — Hengyunchang, Injet, IPO-funded entrants; JP — Kyosan (L06-050).
- **Window/export risk:** defining constraint. US rules restrict advanced-node equipment to CN:
  two-entity structure (US leading-edge / CN ≥28nm variants) with clean IP partition; if
  controls broaden to all RF subsystems by 2030, the CN leg dies and the seed re-batches
  US-only. Refresh control scope + localization data in 2029.
- **Kill:** 2034.
- **Big vision:** "the waveform is the process" — programmable-energy plasma control across
  etch, deposition, and industrial plasma chemistry.
- **Nearest substitutes:** multi-frequency sinusoidal bias stacks; OEM-internal pulsed-bias
  development; incumbent next-gen generators.
- **Key uncertainty:** speed at which AE/MKS productize TVW internally; CN control-regime
  trajectory.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-10]:** Import the US/CN two-entity export partition into A-10 as company structure. Record retained as audit trail; not independently promotable.

## P3R2-C-07 — Low-ripple active-front-end rectification retrofits for electrochemistry

- **Product:** Containerized AFE/MMC rectifier retrofit skids (5–50MW) with
  electrochemistry-tuned ripple control and measured performance contracts; stack-vendor
  neutral. Electrowinning beachhead de-risks hydrogen volatility.
- **US buyer + pain:** H2Hubs projects (up to $2.2B committed to Gulf Coast/Midwest hubs,
  L11-032) and Plug-class deployments (L11-046) carry 15–20yr opex exposure to thyristor
  rectification: documented up to ~14% specific-energy and ~13% loss penalties
  (L11-016/017/019/020/021); electrowinning shows the identical lever (L11-045, L11-026/027).
- **China buyer + pain:** flagship plants underperform (Kuqa reported at fractions of
  nameplate, L11-049) while GW-scale alkaline tenders (LONGi/Peric/Sungrow ~70% share,
  L11-050/051) install cost-optimized thyristor supplies — an efficiency retrofit base being
  built right now.
- **Mechanism:** IGBT/MMC active front end with per-string ripple shaping matched to catalyst
  degradation physics (L11-001/003) — electricity is ~the whole LCOH, so single-digit-% energy
  recovery pays capex.
- **Why incumbents miss it:** rectifier majors sell capex-optimized commodity units;
  stack OEMs bundle whatever is cheapest; nobody sells measured-savings contracts against an
  installed base.
- **Decisive experiment:** 2027, $250k — side-by-side SEC measurement on a pilot stack under
  thyristor vs AFE supply across load profiles; publish verified %-savings band.
- **TRL:** 5.
- **2026–2029 plan:** instrumented ripple-vs-degradation study (university/RTO); retrofit
  economics model; 2028 MW-scale retrofit pilot MOUs (US developer, CN EPC via consortium);
  2029 policy/tender refresh.
- **2030–2034 triggers:** US — H2Hubs Phase-2 construction/commissioning 2027–2032 (L11-032)
  plus electrowinning energy programs. CN — second-wave green-H2 bases and first-wave retrofits
  (L11-049/050/051).
- **2030 competition:** ABB/Siemens/Ingeteam rectifier lines (uncited — P4 to source);
  OEM-bundled power (L11-040/041); CN — Sungrow, simultaneously buyer and formidable
  competitor (L11-051).
- **Window/export risk:** US hydrogen policy fragility (Western order books already shrinking,
  L11-047/048) hedged by electrowinning; Sungrow verticalization is the CN risk. Export
  separability good (uncontrolled industrial rectifiers; CN entity localizes).
- **Kill:** 2034; interim kill if no paid MW-scale retrofit in either market by end-2033.
- **Big vision:** precision DC as the power-quality layer for all electrochemistry (H2,
  electrowinning, chlor-alkali, formation).
- **Nearest substitutes:** 12/24-pulse thyristor upgrades, passive filters, OEM-bundled
  rectifiers.
- **Key uncertainty:** field-verified savings landing at the top vs bottom of the 5–14%
  literature band.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical rectification retrofit; the one L11 play the atlas licenses. Electrowinning beachhead hedges hydrogen policy fragility; Sungrow verticalization is CN kill condition; incumbent rectifier names to source in P4. 2026-07-13: absorbed A-19 (US tankhouse-first/H2Hub-second beachhead sequencing; financier M&V protocol; per-cell telemetry) and B-13 (Kuqa retrofit evidence already cited at L11-049; degradation-weighted current-scheduling mechanism with sources L11-004/012/013/031). Flags unchanged (already US+CN); Sungrow verticalization remains the CN kill condition; incumbent rectifier names still to be sourced in P4.

## P3R2-C-08 — Thermal-shock-tolerant printed-circuit heat exchangers (PCHE)

- **Product:** Merchant diffusion-bonded microchannel recuperators engineered for >20 °C/min
  transients (the CAS-IET-documented gap, L04-029), creep-qualified per ASTM E139 (L04-112)
  with Sandia-documented materials logic (L04-113); certified cores for cycle OEMs.
- **US buyer + pain:** STEP-lineage sCO2 integrators build recuperators bespoke in-house
  (L04-039, L04-004/005/006); advanced-reactor BOP has a tiny qualified-vendor pool
  (TerraPower's named awards, L04-045); DOE LPO-backed storage builds add demand (L04-114).
- **China buyer + pain:** China runs the world's first commercial waste-heat sCO2 unit
  (Chaotan One 30MW, L04-048/051) with a state-media-estimated ~300-unit steel-sintering
  retrofit fleet (single-source figure — flagged, P4 to triangulate) and CAS-IET researching
  exactly this cycling-durability gap (L04-029).
- **Mechanism:** channel-geometry + bonding-process design against thermal-shock fatigue;
  qualification data as the product's core moat.
- **Why incumbents miss it:** incumbent PCHE makers (Heatric/VPE-class — uncited, P4 to
  source) serve oil-and-gas specs; rapid-transient sCO2 duty is a different qualification
  regime nobody has certified.
- **Decisive experiment:** 2028, $600k — subscale bonded core; 1,000 cycles at ≥20 °C/min with
  550 °C peaks; sectioning + creep data; publish.
- **TRL:** 5.
- **2026–2029 plan:** materials/bonding research via university + national-lab facility; ASME
  code-case groundwork; 2029 supply LOIs (US cycle developer; CN licensee for retrofit market)
  + refreshed China retrofit economics from eligible sources.
- **2030–2034 triggers:** US — advanced-reactor BOP procurement post-NRC Part 53 (effective
  2026-04, L04-031) and post-STEP commercial units (L04-039). CN — Xinjiang molten-salt+sCO2
  completion ~2028 triggering "first-set" follow-on procurement and the retrofit wave
  (L04-051).
- **2030 competition:** incumbent PCHE makers (uncited — P4), OEM in-house shops (L04-039),
  Chinese institute-affiliated fabricators (L04-029, L04-102/106).
- **Window/export risk:** HXs for CN steel retrofits are low-sensitivity; nuclear-qualified US
  line stays domestic (no CN transfer) — clean two-line separation. Risks: sCO2 slips
  (kill if no ≥10MW-class merchant order by end-2033); institutes verticalize; heavier capex.
- **Kill:** 2034.
- **Big vision:** standard high-temperature compact cores across sCO2, industrial heat pumps,
  thermal storage, H2 liquefaction precooling.
- **Nearest substitutes:** shell-and-tube (bulky), incumbent PCHEs (wrong qualification),
  in-house builds.
- **Key uncertainty:** true size/timing of the Chinese retrofit fleet (single-source today) and
  US sCO2 commercialization pace.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical PCHE. Independent demand legs (STEP/Part 53 vs Chaotan One/Xinjiang); cycling qualification + code documentation wedge; CN TAM single-source-flagged pending P4; absorb A-12, B-07, E-08. 2026-07-13: absorbed A-12 (catalog-frames/lead-time framing, STEP/TerraPower buyer detail, creep-test source L04-101), B-07 (graded-channel/compliant-header mechanism, CNNC first-set logic; RMB100bn TAM stays single-source-flagged), E-08 (KR KAERI/Jinsol/Hanwha consortium channel, MHI-Turboden adjacency, CN-TAM triangulation task). Flags unchanged (already US+CN).

## P3R2-C-09 — Standardized solid-state pulsed-power modulator platform

- **Product:** Stackable Marx/modulator family (10–100kV, kA-class, µs–ms pulses) with digital
  droop correction and standard interfaces — the merchant drive chain for e-beam/X-ray OEMs
  and accelerator systems.
- **US buyer + pain:** cargo/NDT linac demand growing (+25% YoY segment, >$55M new orders,
  L05-033); EtO-replacement e-beam capacity duopoly-backlogged (L05-028); five documented
  non-interoperable modulator designs (L05-003/005/006/007/008) and no dedicated acceptance
  standard beyond IEC 60060 (L05-043); DOE ARDAP funds 29 companies in this ecosystem
  (L05-031) and SLAC's GREEN-RF pushes commercialization (L05-032).
- **China buyer + pain:** CGN Dasheng signed RMB340M in H1-2025 accelerator orders, +21%
  (L05-035); national isotope-center cyclotron tenders live (L05-036) — same fragmented drive
  chains at higher unit volume.
- **Mechanism:** module-level droop-sharing control makes stacks behave as one clean source;
  standard mechanical/control interfaces enable OEM catalog integration.
- **Why incumbents miss it:** ScandiNova/Jema (L05-047/030) sell engineered systems per
  project; OEMs guard in-house designs; nobody sells the interoperable module layer.
- **Decisive experiment:** 2027, $500k — two-module 50kV/500A stack, 100µs pulses at 1% droop
  with active correction; mid-campaign module swap; acceptance protocol per IEC 60060-1:2025.
- **TRL:** 5.
- **2026–2029 plan:** reference designs + published interoperability spec (extends L05-009);
  droop-control patents; 2028 OEM evaluation units via lab partnership; 2029 two OEM LOIs +
  backlog/tender refresh.
- **2030–2034 triggers:** US — EtO-replacement sterilization capacity buildout (L05-028 —
  re-verify 2029) and customs/port scanning recapitalization (L05-033). CN — CGN Dasheng
  multi-site expansion cadence (L05-035) and isotope-center procurement (L05-036).
- **2030 competition:** ScandiNova (L05-047), Jema (L05-030), CPI (L05-050), OEM in-house; CN —
  institute-lineage suppliers (L05-014 context) and CGN internal.
- **Window/export risk:** dual-use adjacency (radiography/EMP) — high-energy variants US-only;
  CN entity ships industrial-class modules to civilian sterilization/NDT buyers; legal review
  by 2028. OEM in-house culture is the demand risk.
- **Kill:** 2034; interim kill if no OEM design-in by end-2033.
- **Big vision:** pulsed power as catalog engineering across sterilization, scanning, medical
  linacs, food processing, compact accelerators.
- **Nearest substitutes:** engineered one-off modulators; legacy PFN/thyratron chains; OEM
  internal builds.
- **Key uncertainty:** whether beam OEMs will externalize their drive chain.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical modulator platform. Absorb D-05 open-interface standard (the differentiating move), E-05 hot-swap serviceability, A-07 acceptance protocol, C-20 SSPA line, B-09 brick detail. 2026-07-13: absorbed D-05 (open-interface standard - the differentiating move), E-05 (hot-swap <30min serviceability + KR Vitzro/PAL channel), A-07 (IEC 60060-1:2025 acceptance-protocol emphasis, Varex-class buyer detail), C-20 (SSPA RF-drive product family + its 20kW/>=68% decisive experiment), B-09 (3kV brick with per-stage droop correction; CGN/CIRC tender evidence already cited). China leg unchanged (already evidenced via L05-035/036); high-energy variants remain US-only per the export partition.

## P3R2-C-10 — Charge-buildup-immune beam-current/dose metrology (FLASH + industrial e-beam)

- **Product:** Hybrid compensated BCT + fast-Faraday beam monitor with drift-corrected
  integration and metrology-grade traceability for ultra-high-dose-rate and industrial
  beamlines; sold with calibration service.
- **US buyer + pain:** FLASH-radiotherapy developers and sterilization contractors — two
  independent 2024–25 groups showed BCTs corrupted by charge buildup at FLASH dose rates
  (L05-023/024) while ISO 11137-1:2025 tightens radiation-sterilization validation (L05-042);
  cargo/NDT linac base grows (L05-033).
- **China buyer + pain:** CGN Dasheng's expanding sterilization/NDT fleet (L05-035) and
  isotope-center accelerators (L05-036) need traceable dosimetry for export-certified
  processing.
- **Mechanism:** field-compensated magnetics + sampled Faraday cross-calibration; error budget
  engineered against induced-charge physics rather than calibrated around it.
- **Why incumbents miss it:** the catalog incumbent (Bergoz, L05-049) serves accelerator labs
  with conventional BCTs; UHDR immunity is a new requirement without an owner.
- **Decisive experiment:** 2027, $200k — prototype benchmarked on a university FLASH-capable
  linac vs Faraday-cup ground truth across 3 orders of magnitude of dose rate.
- **TRL:** 4.
- **2026–2029 plan:** compensation physics with a medical-physics department; publications;
  2028 beta units at one clinical + one industrial beamline; 2029 OEM/calibration LOIs.
- **2030–2034 triggers:** US — FLASH regulatory submissions requiring traceable UHDR dosimetry
  (trajectory from L05-023/024) + ISO 11137-1:2025 revalidation cycles (L05-042). CN — CGN
  line-commissioning cadence (L05-035) and isotope-center buildout (L05-036).
- **2030 competition:** Bergoz (L05-049), OEM in-house monitors, metrology institutes.
- **Window/export risk:** small TAM — honest niche wedge, pairs with C-09; export separability
  good (civilian metrology; CN distributor/entity).
- **Kill:** 2033 if FLASH stalls and industrial buyers accept legacy dosimetry.
- **Big vision:** dose truth for the ultra-high-dose-rate era across therapy, sterilization,
  and e-beam processing.
- **Nearest substitutes:** conventional BCTs + correction factors; calorimetric spot checks.
- **Key uncertainty:** FLASH clinical translation pace.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-09]:** Fake dual: CN leg is a mirrored assertion (no CN procurement/regulatory evidence). US leg already canonical in D-09. Record retained as audit trail.

## P3R2-C-11 — HTS conductor and cable acceptance-test systems

- **Product:** Automated 20–77K test benches: reel-to-reel tape Ic + strain/delamination
  screening, and 10kA-class cable/CICC acceptance stations, with round-robin-compatible
  protocols and financier-grade data packages.
- **US buyer + pain:** fusion magnet makers buying hundreds of km of REBCO (L03-003, L03-044)
  from <10 concentrated vendors (L03-019) must certify against strain/delamination/
  screening-current degradation (L03-018/020/021); QA throughput gates the magnet factories
  funded under the DOE milestone program (L03-032) and CFS's magnet-as-product sales
  (L03-035). (The absence of a finished-cable Ic standard is treated as labeled inference from
  the measurement literature; the prior standards-gap citation was verifier-rejected — P4 to
  re-source IEC/TC90 status.)
- **China buyer + pain:** the operating commercial Shanghai 35kV cable and follow-ons
  (L03-041/052), ASIPP's 35.1T program (L03-029/037), and China's ITER strand QA lineage
  (WST ~65% of NbTi, L03-031) all need bankable acceptance data at cable scale.
- **Mechanism:** automated cryogenic high-current measurement with controlled strain state —
  productized measurement physics currently living in one-off lab rigs.
- **Why incumbents miss it:** magnet builders treat QA as internal overhead; tape vendors
  can't self-certify credibly; no merchant test vendor exists.
- **Decisive experiment:** 2027, $300k — reel-to-reel 77K Ic + delamination screening
  prototype; blind cross-check of two vendors' tape vs lab-standard measurements; publish
  repeatability study.
- **TRL:** 5.
- **2026–2029 plan:** university magnet-lab prototype on loaned tape; inter-lab variance
  publication; 2028 10kA cable-station design + pilot acceptance campaign; 2029 service LOIs
  (US fusion company; CN cable/institute program).
- **2030–2034 triggers:** US — DOE milestone follow-ons post-2027 reauthorization decision
  (L03-032) and third-party certification demand from magnet sales (L03-035). CN — State Grid
  HTS deployments beyond Shanghai (L03-041/052) and CFETR-lineage magnet procurement
  (L03-024).
- **2030 competition:** in-house rigs (CFS/labs), national-lab test services, CN institute
  labs; tape vendors bundling QA (partnership targets: L03-044/052).
- **Window/export risk:** cable-QA equipment is low-sensitivity; fusion-magnet test data may
  become sensitive — separate US-fusion and CN-cable service entities. Kill if REBCO volumes
  stagnate (no fusion follow-on orders and no repeat CN cable projects by end-2033).
- **Kill:** 2034.
- **Big vision:** the SGS/UL of the superconducting economy — every reel, cable, and coil
  ships with our certificate.
- **Nearest substitutes:** in-house rigs; national-lab beam time; vendor self-certification.
- **Key uncertainty:** HTS volume growth rate; institutional willingness to outsource QA.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-D-02]:** Import 10kA cable/CICC acceptance station and financier/insurer data packages into D-02. Record retained as audit trail; not independently promotable.

## P3R2-C-12 — kW-class 20–80 K turbo-Brayton cryocoolers

- **Product:** Sealed turbo-Brayton cryocooler family (200W–2kW at 20–80K), gas-bearing
  turboalternators, >5-year maintenance-free target — the missing class between GM lab coolers
  (mW–W, L03-050) and bespoke helium plants (kW-class, JT-60SA-scale context L03-025-lineage).
- **US buyer + pain:** fusion magnet factories and HTS systems scaling under the DOE milestone
  program (L03-032/035); quantum facilities scale cryo plant (dilution-refrigerator cooling
  power is a documented constraint, L07-014–017; Bluefors localizing US production, L13-041).
- **China buyer + pain:** the operating Shanghai HTS cable's cryogenic plant burden and
  follow-on city cables (L03-041/052); ASIPP's high-field magnet infrastructure (L03-029);
  CFETR-lineage needs (L03-024).
- **Mechanism:** high-speed gas-bearing turboalternator with sealed neon/helium cycle — the
  machine class Nexans' SupraMarine demonstrator uses (L03-034), productized at mid-scale.
- **Why incumbents miss it:** big-plant EPCs (Air Liquide/Linde-class — uncited, P4 to source)
  don't productize small; GM-cooler vendors lack turbomachinery DNA; the mid-band is an
  orphan.
- **Decisive experiment:** 2028, $900k — single-stage cold head ≥200W at 50K-equivalent with
  gas-bearing turboalternator; 1,000h endurance; loss budget vs GM baseline.
- **TRL:** 4.
- **2026–2029 plan:** university turbomachinery-lab research; bearing/alternator integration
  patents; 2029 pilot LOI (US fusion/HTS) + CN path study with export counsel; refresh
  quantum-control scope.
- **2030–2034 triggers:** US — magnet-factory expansion and quantum-facility scaling
  (L03-032/035, L13-041). CN — HTS cable follow-on deployments (L03-041/052) and
  ASIPP/CFETR infrastructure (L03-029, L03-024).
- **2030 competition:** large-plant EPC turbo-Brayton (uncited — P4), Cryomech/Sumitomo GM
  class (L03-050), Stirling vendors; CN domestic cryocooler makers.
- **Window/export risk:** weakest export separability in this batch — cryogenics is entangled
  with quantum controls (2024 US rule; reported 2025 Entity-List additions unconfirmed). Plan:
  US/allied beachhead; CN grid/science sales only via licensed local entity if counsel clears;
  otherwise the CN leg lapses and the seed re-batches. Kill if cold-stage efficiency targets
  unmet by 2033.
- **Kill:** 2034.
- **Big vision:** plug-in cold as infrastructure for HTS grids, fusion, H2 nodes, quantum
  datacenters.
- **Nearest substitutes:** banks of GM coolers; custom helium refrigerators; LN2 logistics.
- **Key uncertainty:** achievable maintenance-free life of gas-bearing machines at this scale.
- **[FIX applied 2026-07-13]:** P4 competitor-map requirement (Air Liquide/Linde turbo-Brayton, Stirling vendors, Chinese makers) added before promotion; CN leg set to license-only and flags lowered honestly (primary_market US+CN->US, china_beachhead->false; CN chapter documented in text); staged-capex rule (no full skid before named buyer LOI). Merged in B-11 (CN mid-scale buyers, HEPS tender context) and D-03 (catalog-price/6-month-lead-time product definition, KR side market).

## P3R2-C-13 — Precision GaN laser pump-driver and power modules

- **Product:** Qualified multi-channel GaN pump drivers (kA-aggregate, ns edge control,
  safety interlocks) + TMI-aware pump-modulation firmware hooks; modules/reference designs for
  laser OEMs; strictly separated US-only line for directed-energy primes.
- **US buyer + pain:** nLIGHT's A&D revenue is now its largest segment ($175.3M, L12-033) and
  driver electronics remain an active research area every OEM re-solves (L12-025/026/027);
  Coherent targets a $4B datacenter-interconnect opportunity needing laser sources (L12-036);
  JLWS structure ($86M/$847M ceiling, L12-031/032) defines the 2030s defense pull (US-entity
  line only).
- **China buyer + pain:** the fiber-laser price war (Han's high-power revenue −6.6% on +30%
  units, L12-037) forces cost-down/outsourcing of non-core electronics while exports boom
  (Raycus handheld +66%, 220kW launch, L12-038).
- **Mechanism:** GaN switching + ns-resolution programmable current shaping; pump modulation as
  a TMI mitigation lever (L12-016/017/018).
- **Why incumbents miss it:** drivers are buried NRE inside laser OEMs; analog-semi vendors
  sell chips, not qualified laser-safety-integrated modules.
- **Decisive experiment:** 2027, $180k — 8-channel 1kA-aggregate GaN driver; closed-loop pump
  modulation on a university 1kW fiber amplifier; publish stability gain.
- **TRL:** 4.
- **2026–2029 plan:** fiber-laser-lab collaboration; patents; 2028 evaluation units with one US
  OEM + CN cost/performance benchmark via academic partner; 2029 design-in LOIs + entity
  partition review.
- **2030–2034 triggers:** US — JLWS-generation DEW fielding 2030–2034 (L12-031/032; US line)
  plus industrial/CPO source growth (L12-036). CN — consolidation-driven outsourcing amid
  export-led volume growth (L12-037/038).
- **2030 competition:** in-house driver teams (IPG L12-034/051, Raycus/Han's L12-037/038),
  analog-semi reference ecosystems, 1–2 module startups.
- **Window/export risk:** sharp-edged but manageable: two entities from day one; any
  DEW-affiliated line free of CN ownership links; a forced divestment choice may drop one
  market (then re-batch). Chinese NIH culture is the demand risk — test in 2028 discovery.
- **Kill:** 2034.
- **Big vision:** the power-electronics backbone of photonics — pump drive, pulse shaping,
  energy recovery across industrial, medical, DEW, and CPO lasers.
- **Nearest substitutes:** in-house drivers; evaluation-board-derived designs.
- **Key uncertainty:** OEM willingness to externalize a core-adjacent subsystem in both
  cultures.
- **[FIX applied 2026-07-13]:** 2028 two-paid-evals buy-vs-build gate added; two-entity US(DEW)/commercial partition made a day-one requirement; fold-into-D-10 fallback codified. Merged in A-18 (diode-health telemetry differentiator) and B-19 (CN price-war up-market OEM pivot as the CN demand chapter).

## P3R2-C-14 — Modular MW-class industrial plasma power supplies

- **Product:** 250kW torch-agnostic building-block supplies (arc + RF assist, millisecond
  arc-restrike control) with fleet-level numbering-up orchestration; sold to torch OEMs,
  remediation operators, and institutes.
- **US buyer + pain:** DoD-linked demand is paid and delivered — CAD$4.1M + $27M torch
  contracts and $2.25M PFAS destruction >300t (L01-034/035/036); plasma-chemistry scale-ups
  hit the numbering-up wall where every reactor needs its own supply/match (L01-014/015/016;
  Nitricity sold out through 2028, L01-031/032).
- **China buyer + pain:** ASIPP is tendering plasma power electronics now (ITER PF converter
  modules; RMP system expansion — L01-037/038) and defense-industrial buyers procure plasma
  deposition equipment (AVIC award, L01-039).
- **Mechanism:** fast arc-stabilization control loops + multi-module current sharing turn many
  small supplies into one orchestrated fleet — matching how non-thermal plasma actually scales.
- **Why incumbents miss it:** RF majors stop below ~100kW (L01-040/049/050); torch vendors
  build supplies internally per project; the 100kW–2MW merchant band is thin.
- **Decisive experiment:** 2027, $350k — 250kW modular supply on a partner torch; restrike-rate
  reduction vs baseline; 4-module numbering-up orchestration on a reactor-bank emulation.
- **TRL:** 5.
- **2026–2029 plan:** university torch-stand research; arc-sharing patents; 2028 field trial
  with a remediation/torch partner + CN institute requirements scoping via academic channels;
  2029 OEM LOI + export review.
- **2030–2034 triggers:** US — PFAS destruction procurement expanding beyond the delivered
  pilot base (L01-036 lineage; regulatory scope re-verified 2029) and 20MW-class torch program
  completions (L01-035). CN — ASIPP tender cadence (L01-037/038) and defense-industrial plasma
  equipment procurement (L01-039).
- **2030 competition:** AE/MKS/Comet/TRUMPF at sub-100kW (L01-040/049/050); torch OEMs
  in-house; CN institute-affiliated suppliers; KR — KIMM lineage (L01-047).
- **Window/export risk:** supplies to Chinese state/fusion institutes may need licenses —
  route CN sales through a local licensee limited to civilian industrial specs; US
  defense-adjacent variants stay domestic. Demand risk: plasma chemistry may stay
  pre-industrial (atlas enthusiasm-zone warning) — anchored instead on already-paid
  remediation/defense demand.
- **Kill:** 2034; interim kill if no OEM/operator contract by end-2033.
- **Big vision:** the power layer of electrified chemistry — PFAS, N2 fixation, methane
  pyrolysis, vitrification, plasma metallurgy.
- **Nearest substitutes:** engineered one-off supplies; rectifier + PFN legacy stacks; RF
  generator arrays.
- **Key uncertainty:** how fast PFAS-destruction procurement broadens beyond the current
  single-vendor pilot base.
- **[Adjudication 2026-07-13 - REJECT]:** US leg = tiny in-house-building torch-OEM universe; CN leg cites big-science bespoke converter tenders (category error) - fake dual; core plasma-chemistry demand is an enthusiasm zone. A-22 is the better vehicle. Record retained as audit trail.

## P3R2-C-15 — Megawatt charge/swap DC power infrastructure for mines and ports

- **Product:** Modular 1.5–3.75MW liquid-cooled charger cabinets + station DC backbones,
  protocol-flexible across IEC MCS (L10-050) and Chinese swap-station interfaces (L10-046),
  with pulsed-load grid buffering.
- **US buyer + pain:** ~$3B of EPA Clean Ports zero-emission equipment grants must be executed
  (L10-048); battery locomotives (UP's 10-unit FLXdrive order, L10-032) and Cat 793 XE trials
  (L10-030) all lack standardized megawatt charging — the IEC MCS spec only landed Feb 2026
  (L10-050).
- **China buyer + pain:** SOE mines tender fleet-scale equipment (China Gold 60+ trucks,
  Baogang retrofit — L10-034/035); China runs multi-class battery-swap deployments with a
  national standard (L10-031/046) and canal e-shipping benchmarks (L10-040) — infrastructure
  supply is the choke point in both ecosystems, which are mutually incompatible (L10-031 vs
  L10-050).
- **Mechanism:** one modular DC power stage reconfigurable across charge/swap profiles; grid
  buffer absorbs duty-cycle pulses.
- **Why incumbents miss it:** OEMs verticalize their own architecture bet (Fortescue in-house
  6MW, L10-029; Cat MEC500, L10-053; XCMG/CATL stacks, L10-028/036); nobody sells the neutral
  power layer across standards.
- **Decisive experiment:** 2028, $500k — 1.5MW dual-interface cabinet at a test yard; MCS
  profile per IEC TS 63379 and swap-station DC profile on one power stage; grid-side pulse
  measurement.
- **TRL:** 5.
- **2026–2029 plan:** MCS-vs-swap architecture study; site load modeling with a mining
  program; CharIN/IEC participation; 2029 pilot LOIs (US port grantee; CN OEM/EPC) + policy
  refresh (CARB repeal aftermath, L10-044).
- **2030–2034 triggers:** US — Clean Ports equipment delivery/installation waves into the
  early 2030s (L10-048) and Class-I battery-locomotive expansion (L10-032 lineage). CN — SOE
  mine electrification tenders (L10-034/035) and swap-standard rollouts across trucks/
  excavators/vessels (L10-046, L10-040, L10-031).
- **2030 competition:** US — OEM chargers (L10-053), charger firms (ABB/Heliox-class —
  uncited, P4), in-house builds (L10-029); CN — XCMG/CATL/SPIC verticals (L10-028/031/036).
- **Window/export risk:** US policy risk real (CARB repeal, L10-044) but EPA money is
  appropriated (L10-048); CN risk is CATL/SPIC vertical integration. Export separability good
  (industrial charging hardware; dual-entity). Architecture non-convergence (L10-002) is the
  window: a standard-agnostic vendor monetizes the confusion.
- **Kill:** 2034; interim kill if no paid site deployment in either market by end-2033.
- **Big vision:** the neutral power layer of off-highway electrification worldwide.
- **Nearest substitutes:** OEM-bundled chargers; genset bridging; trolley-assist
  infrastructure (L10-014/024).
- **Key uncertainty:** post-2026 US port/drayage policy trajectory.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-A-21]:** CN leg is demand-without-access vs vertically integrated domestic stacks. Import dual-standard cabinet option and station-DC-backbone concept into A-21. Record retained as audit trail.

## P3R2-C-16 — Real-time HIL compliance-test systems for DC protection and IBR ride-through

- **Product:** FPGA-based real-time DC-grid emulator + amplifier chain reproducing
  traveling-wave fault physics, breaker interaction, and ride-through events, with scripted
  compliance suites (US PRC-029 pack; Chinese-standard pack via local partner).
- **US buyer + pain:** NERC PRC-029-1 (approved via FERC Order 909, 2025) forces ride-through
  compliance across the inverter-based-resource fleet (L08-043); interregional HVDC is being
  built (Southern Spirit, L08-041) while DC protection algorithms remain unstandardized
  research (L08-004/005/006/007) — no certification-grade DC-fault test environment exists.
- **China buyer + pain:** State Grid's UHV tender machine ships RMB-billion-scale converter
  valves and DC control/protection each round (XJ Electric RMB1.275bn in one 2026 batch,
  L08-034) — all requiring factory/site acceptance testing at growing cadence.
- **Mechanism:** microsecond-fidelity real-time models of DC faults (no zero crossing,
  traveling waves) + power-amplified interfaces to devices under test.
- **Why incumbents miss it:** general-purpose HIL incumbents (RTDS/OPAL-RT-class — uncited,
  P4) underserve DC-fault-specific physics and compliance scripting; state test institutes
  serve themselves.
- **Decisive experiment:** 2027, $250k — real-time emulator reproducing published
  multi-terminal fault records; blind test of two published protection algorithms; fidelity
  benchmark.
- **TRL:** 5.
- **2026–2029 plan:** university power-lab research; validation vs published algorithms; 2028
  pilot bench at a US compliance lab + CN test-institute partnership scoping; 2029 purchase
  LOIs; re-source current IEEE 2800-series test-spec status (prior citation was
  verifier-rejected — P4 note).
- **2030–2034 triggers:** US — PRC-029-1 fleet compliance/re-certification waves and HVDC
  commissioning (L08-043, L08-041). CN — State Grid UHV/VSC tender cadence requiring
  valve+protection acceptance testing (L08-034).
- **2030 competition:** HIL incumbents adding DC packs (watch 2027–2029); in-house rigs at
  XJ/NARI and OEM labs (L08-034, L08-052).
- **Window/export risk:** test equipment — export separability good; CN market realistically
  requires a JV/license given procurement nationalism. Kill if incumbents close the DC-fault
  gap before first sales (decision 2033).
- **Kill:** 2034.
- **Big vision:** the reference certification environment for the DC-dominated grid, extending
  to datacenter MVDC and megawatt charging protection.
- **Nearest substitutes:** generic real-time simulators; field trials; analytic studies.
- **Key uncertainty:** speed of incumbent simulator vendors closing the niche.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-E-14]:** Import CN factory-acceptance-test license market and State Grid test-institute channel into E-14. Record retained as audit trail; not independently promotable.

## P3R2-C-17 — HTS magnet quench detection and protection electronics

- **Product:** Multi-modal quench sensing (fiber/RF/acoustic) + ms-class detection firmware +
  coordinated energy-extraction electronics, qualified per coil family and sold with
  characterization service.
- **US buyer + pain:** HTS quench detection is unsolved at multi-tesla/multi-MJ scale — high
  minimum quench energy defeats voltage taps, forcing conservative no-insulation designs with
  degraded ramp/control (L03-004–008, L03-018); magnet-as-product sales make protection a
  warranty item (L03-035; program funding L03-032).
- **China buyer + pain:** ASIPP's 35.1T record magnets (L03-029/037) and CFETR's 14.5T TF
  engineering (L03-024) carry the identical unresolved protection burden.
- **Mechanism:** detect normal-zone birth via modalities faster than resistive voltage growth;
  act within milliseconds through segmented extraction.
- **Why incumbents miss it:** each magnet team hand-rolls protection; no merchant subsystem
  vendor; CERN-lineage tech never productized.
- **Decisive experiment:** 2027, $300k — fiber+RF detection on an instrumented NI REBCO test
  coil; ≥5x faster detection than voltage taps across 20 induced quenches.
- **TRL:** 4.
- **2026–2029 plan:** university test-coil physics; latency-benchmark publications; 2028
  characterization pilot with a US magnet program; 2029 subsystem LOI + CN export-control
  review.
- **2030–2034 triggers:** US — post-SPARC magnet-factory scaling and DOE milestone follow-ons
  (L03-032/035). CN — CFETR-lineage magnet procurement decisions and ASIPP expansion
  (L03-024, L03-029/037).
- **2030 competition:** in-house teams at CFS/Tokamak Energy (L03-035/033); national-lab
  instrumentation groups.
- **Window/export risk:** weakest dual-market separability alongside C-12: fusion-magnet
  technology to China may be license-blocked by 2030; plan is US/allied beachhead with CN
  participation only if counsel clears a civilian-science channel — otherwise re-batch
  US-primary (flagged for the orchestrator; this is the honest reading, not forced).
- **Kill:** 2034; interim kill if latency targets unmet on representative coils by 2033.
- **Big vision:** the trust layer that lets HTS magnets be insured, financed, and
  mass-produced across fusion, NMR, accelerators, medical.
- **Nearest substitutes:** voltage taps + heaters/CLIQ; conservative NI design as
  pseudo-protection.
- **Key uncertainty:** whether detection modalities generalize across coil families without
  per-coil re-engineering.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-01]:** Seed concedes CN leg may be export-blocked and invites re-batching; D-01 is the cleaner canonical. Record retained as audit trail.

## P3R2-C-18 — 800V-to-point-of-load vertical power delivery modules

- **Product:** Qualified 2–5kW bricks: regulated 800V→48V LLC stage + vertical 48V→sub-1V core
  stage, GaN-based, with published derating/reliability data (benchmark class: Navitas' 97.5%
  800V-to-6V demo, L02-046).
- **US buyer + pain:** NVIDIA's roadmap explicitly targets eliminating conversion stages from
  grid to die (L02-043); 48V-to-sub-1V at kA remains an open density problem
  (L02-022/023, L02-110).
- **China buyer + pain:** the domestic 800V ecosystem is thin — Innoscience is the sole
  mainland supplier on NVIDIA's list and still without confirmed orders (L02-050) — so Chinese
  integrators need merchant conversion built on local devices (L02-054, L02-048).
- **Mechanism:** two-stage architecture with HF planar magnetics co-design
  (L02-019/020) and vertical-power delivery to the core.
- **Why incumbents miss it:** (honestly, they don't entirely — this is the batch's aggressive
  discardable bet) incumbents chase today's sockets; the wedge is winning the 2030–2033
  1MW-rack architecture churn with a 2029-vintage clean-sheet design.
- **Decisive experiment:** 2027, $400k — 2kW 800V→48V→0.8V brick; efficiency/density benchmark
  vs published boards; thermal-cycling screen.
- **TRL:** 4.
- **2026–2029 plan:** university power-electronics-center topology/magnetics work; benchmark
  publications; 2028 ODM evaluation; 2029 LOIs + full landscape refresh.
- **2030–2034 triggers:** US — 1MW-rack OCP shelf refresh cycles 2030–2033 (L02-043/044
  trajectory). CN — domestic accelerator buildouts under the action plan (L14-036) on local
  GaN (L02-050).
- **2030 competition:** Vicor (L02-113), Delta (L02-037), Navitas/Infineon/TI ecosystems
  (L02-046, L02-043); CN — Innoscience-based designs.
- **Window/export risk:** highest commoditization risk in batch C — kill early (2033) if 2030
  shows multi-vendor parity. Export separability good with dual-entity + local device
  sourcing; watch US GaN/SiC export policy.
- **Kill:** 2033.
- **Big vision:** own busbar-to-die conversion, then carry the bricks into EV, aerospace,
  industrial DC.
- **Nearest substitutes:** Vicor NBM/PRM-class modules, Delta shelves, silicon-vendor
  reference designs.
- **Key uncertainty:** whether any merchant module vendor can hold sockets against
  silicon-vendor reference designs by 2033.
- **[Adjudication 2026-07-13 - REJECT]:** Self-declared highest commoditization risk is accurate: parity race vs Vicor/Delta/Infineon/Navitas + Innoscience CN designs by 2030. Record retained as audit trail.

## P3R2-C-19 — Gas-foil bearing and shaft-seal cartridges for sCO2/ORC turbomachinery

- **Product:** Qualified cartridge modules — engineered foil-bearing sets and face-seal
  assemblies for 10–150mm shafts at sCO2/ORC conditions with life-test documentation; sold
  like turbocharger CHRA cartridges.
- **US buyer + pain:** Sandia's assessment names bearings/seals/degradation among five core
  sCO2 machine challenges (L04-113); pilots hand-build rotor support per machine (L04-039);
  sealing research is active, unresolved (L04-101).
- **China buyer + pain:** three national compressor programs (SMDERI, CAS-IET —
  L04-102/106/109) each re-solve the same problems while the commercial waste-heat fleet
  scales (L04-048/051).
- **Mechanism:** foil-bearing + face-seal co-engineering for a supercritical fluid that
  dissolves lubricants; qualification data is the product.
- **Why incumbents miss it:** seal majors (John Crane/EagleBurgmann-class — uncited, P4)
  serve conventional duties; OEM rotor groups are project-bound; no merchant sCO2-qualified
  cartridge vendor is visible in the atlas.
- **Decisive experiment:** 2028, $700k — cartridge on a heated high-pressure N2/CO2 spin rig;
  leakage + lift-off/life map vs labyrinth/oil baselines.
- **TRL:** 4.
- **2026–2029 plan:** university test-cell research; leakage/life-map publications; 2029 OEM
  development LOI + refreshed sCO2 pipeline check.
- **2030–2034 triggers:** US — post-STEP commercial machine builds and DOE-backed storage/
  heat-pump turbomachinery (L04-039, L04-114). CN — Xinjiang first-set completion (~2028)
  unlocking serial machine production (L04-051, L04-102/106).
- **2030 competition:** OEM in-house; seal majors (uncited — P4); CN institute shops.
- **Window/export risk:** fully levered to sCO2 pace — kill 2033 if no OEM development
  contract. Export separability good for non-nuclear machines; nuclear-cycle variants US-only.
- **Kill:** 2033.
- **Big vision:** the rotor-support standard for high-density power cycles — sCO2, ORC, heat
  pumps, fuel-cell air machines, H2 turboexpanders.
- **Nearest substitutes:** oil bearings + dry-gas seals adapted; magnetic bearings; in-house
  foil programs.
- **Key uncertainty:** sCO2 commercialization timing in both markets.
- **[FIX applied 2026-07-13]:** 2028 machine-build-signal gate (STEP Phase 2 hardware orders / CNNC follow-ons); paired with C-08 as one high-temperature-components company; P4 seal-major incumbent mapping required. Absorbed B-08 (CN dry-gas-seal/foil-bearing variant; its CN institute buyers and mechanism detail were already present here).

## P3R2-C-20 — High-efficiency modular SSPA systems for accelerator RF

- **Product:** Standardized 20–100kW GaN SSPA blocks (352/500/650 MHz) with envelope-tracking
  supplies (~70% chain-efficiency evidence base, L05-007), hot-swap modules and combiner
  architecture — catalog RF power for mid-scale accelerators and industrial cavities.
- **US buyer + pain:** accelerator RF historically runs below 50% wall-plug efficiency and DOE
  explicitly funds efficiency commercialization (GREEN-RF, L05-032; ARDAP base of 70
  institutions, L05-031); SSPA adoption is proven but bespoke per facility (L05-007/008/010).
- **China buyer + pain:** IHEP's CEPC program chases efficiency points at ~RMB130M/yr stakes
  by its own framing (78.5% klystron prototypes, L05-012/013); Chinese synchrotron buildouts
  keep tendering facility hardware (HEPS tender culture, L07-045); coupler reliability remains
  a named weak point of the tube incumbency (L05-014).
- **Mechanism:** GaN pallets + envelope tracking + graceful-degradation combining — efficiency
  and availability tubes can't match below ~1MW.
- **Why incumbents miss it:** tube houses (CPI L05-050, Thales L05-029) defend tube economics;
  facility labs build one-off SSPAs without productizing.
- **Decisive experiment:** 2027, $300k — 20kW 500MHz block with envelope tracking; ≥68% chain
  efficiency into cavity-equivalent load across 6dB backoff.
- **TRL:** 5.
- **2026–2029 plan:** accelerator-lab partnership; efficiency benchmarks; 2028 field-trial
  slot at a US facility (CRADA-style); 2029 procurement LOIs + CN institute-procurement path
  check.
- **2030–2034 triggers:** US — DOE facility upgrade/replacement procurements under the
  stewardship/GREEN-RF lineage (L05-031/032). CN — CEPC decision window and continuing
  facility RF procurement (L05-012/013, L07-045).
- **2030 competition:** CPI (L05-050), Thales (L05-029), European SSPA integrators; CN
  institute in-house; KR localization lineage (Vitzro, L05-037).
- **Window/export risk:** gov-lab market is lumpy and CN big-science buys domestic —
  license/JV path; RF amplifier export sensitivity moderate (review). Discardable if the
  orchestrator prefers commercial-market seeds.
- **Kill:** 2034; interim kill if no facility purchase order by end-2033.
- **Big vision:** catalog-ize accelerator RF the way server PSUs were catalog-ized.
- **Nearest substitutes:** klystrons/IOTs with better collectors; facility-built SSPAs.
- **Key uncertainty:** facility procurement conservatism and cadence.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-09]:** Legitimate product line, weak standalone. 2026-07-13 FIX applied via merge: folded into P3R2-C-09 as its RF-drive (SSPA) product family; the 20kW / >=68% chain-efficiency envelope-tracking demo becomes that line's decisive experiment; no standalone company (gov-lumpy demand, self-labeled discardable). Record retained as audit trail. Record retained as audit trail; not independently promotable.

## P3R2-C-21 — Direct-DC renewable-to-datacenter coupling converters

- **Product:** Multiport 1–10MW DC-DC blocks: PV-string/BESS MVDC input straight to 800VDC
  campus bus with protection coordination and islanding — the "DC substation in a container"
  (topology base: multiport SST research, L02-107).
- **US buyer + pain:** hyperscalers buying firmed clean power (Google–Fervo precedent,
  L04-050) pay for PV-DC→AC→rectifier→800VDC chains; ARPA-E DC-GRIDS exists because grid
  DC-DC conversion hardware is missing (L02-034); datacenter electrification capital runs at
  multi-billion-dollar quarterly rates (L08-033).
- **China buyer + pain:** the April 2026 action plan's green-power direct-connection (绿电直连)
  framework (L14-036, fetched primary) is a named policy lane for exactly this architecture,
  on top of China's rack-HVDC lineage (L02-048).
- **Mechanism:** multiport medium-frequency conversion with sub-ms inter-port fault isolation
  (protection logic built on the DC-breaker literature, L08-001/003/004).
- **Why incumbents miss it:** inverter majors are AC-coupled by installed-base economics;
  grid OEMs sell substations, not campus DC blocks.
- **Decisive experiment:** 2028, $600k — 250kW three-port prototype (PV emulator + battery +
  800V load) on a microgrid testbed; <1ms port fault isolation; efficiency vs AC-coupled
  baseline.
- **TRL:** 4.
- **2026–2029 plan:** architecture/protection studies (DC-GRIDS-adjacent); campus economics
  modeling; 2029 developer/EPC LOIs + re-verified CN implementation detail and US
  interconnection rules.
- **2030–2034 triggers:** US — 24/7 clean-power procurement scaling with gigawatt campuses
  (L04-050 precedent, L08-033 capital flow). CN — green-power direct-connection implementation
  projects under the 2026 action plan (L14-036).
- **2030 competition:** GE Vernova/Eaton/Delta AC packages (L02-115, L02-037); CN —
  Huawei/Sungrow-class giants (power-electronics base evidenced at L11-051) — hardest
  competitor set in the batch; wedge is multiport protection-first design + OCP alignment.
- **Window/export risk:** protection/standards immaturity is both moat and schedule risk; CN
  competitor strength may force license-out. Export separability good (grid power
  electronics; dual-entity).
- **Kill:** 2034; interim kill if no MW-class pilot commitment by end-2033.
- **Big vision:** delete AC from the energy-to-compute chain — generation-to-GPU as one DC
  system, then industrial parks and charging hubs.
- **Nearest substitutes:** AC-coupled PV+BESS with 800V rectification (works today); DC-coupled
  storage inverters extended.
- **Key uncertainty:** interconnection/permitting treatment of direct-DC private wires in both
  jurisdictions.
- **[FIX applied 2026-07-13]:** wedge repositioned to protection coordination (A-02/E-14 lineage), not efficiency; 2028 named US campus/IPP pilot-commitment gate added; CN participation set to license-out only with flags lowered honestly (US+CN->US, china_beachhead->false); v1 capex capped $12-30M -> $10-25M.

## P3R2-C-22 — Electrolyzer stack degradation-emulation and bankability test systems

- **Product:** Turnkey 50–500kW benches: programmable rectifier-ripple synthesis,
  renewable-profile playback, OCV-cycling protocols, impedance diagnostics — plus a licensed
  accelerated-vs-field degradation dataset for financiers. The Chroma-of-electrolysis play
  (battery-test analogy: L11-043/044).
- **US buyer + pain:** stack warranties are written before the industry knows which stress
  drives which degradation mode (L11-001/003/004/021/031) — a bankability problem for
  H2Hubs-financed projects (L11-032) and for OEMs whose order books are shrinking
  (L11-047/048); Plug-class deployments need warranty engineering (L11-046).
- **China buyer + pain:** 100+-unit multi-vendor tenders (L11-050/051) and flagship
  underperformance (Kuqa, L11-049) create buyer-side acceptance-testing demand with no
  standard test hardware.
- **Mechanism:** power-electronics stress synthesis + per-mechanism attribution (catalyst vs
  membrane vs contact resistance) compresses 20-year renewable-coupled histories into 90-day
  campaigns.
- **Why incumbents miss it:** battery-test majors (Chroma/Hioki, L11-043/044) track EV cell
  volumes; stack OEMs can't credibly self-certify; test-stand vendors (Greenlight-class —
  uncited, P4) sell hardware without the degradation-science dataset.
- **Decisive experiment:** 2027, $250k — 50kW programmable bench; 90-day accelerated campaign
  on two commercial short stacks; publish induced-vs-literature degradation correlation.
- **TRL:** 5.
- **2026–2029 plan:** 10kW replication of published stressors (university electrochemistry
  lab); the field's missing correlation dataset published; 2028 paid pilot campaigns via lab
  (OEM + lender consortium); 2029 purchase LOIs + demand refresh.
- **2030–2034 triggers:** US — H2Hubs Phase-2 construction/commissioning with lender-mandated
  performance validation (L11-032). CN — second-wave green-H2 base tenders and acceptance/
  retrofit programs after first-wave underperformance (L11-049/050/051).
- **2030 competition:** test-stand vendors (uncited — P4), battery-test majors extending
  sideways (L11-043/044), OEM in-house labs (L11-040/041).
- **Window/export risk:** hydrogen volatility caps growth but the seed monetizes uncertainty
  itself — anti-fragile to the atlas's L11 demand contradiction; worst case is a slow niche,
  not a zero. Export separability excellent (test equipment).
- **Kill:** 2034; interim kill if neither bench sales nor paid campaigns by end-2033.
- **Big vision:** the qualification authority for electrochemical assets — electrolyzers, flow
  batteries, CO2 electrolyzers, formation lines; owning degradation truth lowers the
  industry's cost of capital.
- **Nearest substitutes:** OEM internal test labs; national-lab campaigns; extrapolated field
  data.
- **Key uncertainty:** whether financiers will pay for independent qualification before a
  major warranty blow-up forces them to.

---

**Generic EE/CE transfer note:** every seed in this batch reduces to power conversion, control,
measurement, or qualification of an extreme electrical system, so a founder with deep power
electronics/electrical engineering craft transfers across all 22 without any seed depending on
that background for its selection.
- **[Adjudication 2026-07-13 - PROMOTE]:** Anti-fragile response to the L11 contradiction: demand survives boom and consolidation branches; Chroma-sideways threat named; P4 to re-source the standards-gap citation (self-flagged inference).

