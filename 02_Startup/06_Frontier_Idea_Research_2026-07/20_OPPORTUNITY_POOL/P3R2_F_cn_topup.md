# P3R2 top-up wave F — China-credible distinct concepts

Generator: idea-architect, claude-fable-5 / xhigh (configured route). Date: 2026-07-13.
Inputs read in order: `P3R2_ELEGANCE_ADJUDICATION.md` (Section 5 survivors respected),
repaired `ATLAS.md`, lane briefs L01/L03/L04/L05/L06/L07/L08/L10/L11/L14/L16 (post-P2A
repair sections respected; L12/L03 consulted by targeted extraction),
`INDIA_SOURCE_ORIGIN_AUDIT.md`, `IDEA_RECORD_TEMPLATE.json`. Founder profile NOT read.
Prior `SEEDS_A–D` NOT read. All cited IDs checked against the 42 quarantined IDs and the
per-lane P2A removal lists; load-bearing demand anchors spot-verified in
`90_BIBLIOGRAPHY/sources.json` as `accepted: true` + `verified_non_india_origin`.

Composition: 23 seeds — 15 dual US+CN (F-01..F-10, F-19..F-23), 8 CN-primary
(F-11..F-18). Datacenter-capex-dependent: 1 (F-19), within the 4-seed cap. Lanes covered:
L01, L03, L04, L05, L06, L07, L08, L10, L11, L12, L14, L16. Extras beyond 22 are provided
so weak concepts can be discarded; F-18 and F-21 are explicitly flagged as merge/option
candidates. India/Singapore excluded everywhere; JP/TW/KR appear only as optional
secondary markets.

> **Adjudication R2 applied 2026-07-13:** the second-pass verdicts
> (`P3R2_ELEGANCE_ADJUDICATION_R2.md`) have been applied to all 23 seeds - 3 PROMOTE
> (F-01, F-02, F-12), 15 FIX_APPLIED, 5 REJECT/MERGED (F-08 REJECT with import to A-02;
> F-13 REJECT; F-14 REJECT with import to F-01; F-18 merged into F-03; F-21 merged into
> F-02). F-06 downgraded to US-primary (china_beachhead false) per the honesty ruling.
> Post-merge distinct wave-F concepts: 18. Annotations at the end of each seed section
> match the JSON `elegance_verdict`/`fix_applied_notes` fields. See
> `P3R2_FIX_APPLICATION_LOG.md` (round-2 section).

---

## P3R2-F-01 — Solid-state microsecond matching engines for RF plasma tools (dual US+CN)

- **Product:** Drop-in solid-state impedance-matching networks (switched SiC/PIN
  capacitor arrays, 400 kHz–60 MHz, 1–10 kW first), sub-10 µs re-match, pulse-synchronous
  tuning tables, health telemetry. Sold to RF-generator vendors and tool OEMs; CN line
  scoped to >=28 nm / panel / display.
- **Buyer + pain per market:** US — generator vendors/tool OEMs racing to productize
  pulsed/TVW processes; matching is still research, not commodity (L06-001/002/003,
  L01-012/013; AE platform ramp L06-039/040). CN — AMEC/NAURA/Piotech growing 40–55%/yr
  (L06-048, L01-044) on an RF supply chain with <12% component localization (L06-054) and
  fragile domestic entrants (Hengyunchang concentration, L06-042/043; Injet L06-044).
- **Mechanism:** Replace motorized vacuum capacitors with binary-weighted switched
  reactance arrays + predictive tuning tables synchronized to pulse recipes; arc-aware
  fast detune as a protection feature.
- **Why incumbents miss it:** AE/MKS/Comet monetize the generator+matchbox bundle;
  cannibalizing electromechanical match lines with a merchant module is against their
  bundle economics; CN entrants lack the high-frequency pulsed engineering depth.
- **Not a duplicate:** Nearest survivor A-10 (closed-loop IEDF bias control). A-10 sells
  the *process-control* layer (IEDF sensing + servo); F-01 sells the *impedance-delivery
  hardware* any generator or tool must contain. Complementary, and A-10's product does
  not include a matching network. Also distinct from B-06 (ESC electronics) and B-21
  (arc/event detection).
- **Decisive experiment + budget:** 13.56 MHz/5 kW matcher showing <10 µs re-match on a
  pulsed plasma load vs >100 ms motorized baseline, with 1e9-event switch-life data —
  $250k, 2027.
- **TRL:** 4. **2026–2029 plan:** university-lab prototype → 2027 export-control gate →
  2028 two paid OEM evaluations → 2029 reliability design-freeze.
- **Named triggers 2030–2034:** US — next tool-platform qualification cycles (AE
  Everest/EVOS-class ramps, L06-039/040). CN — 15th/16th Five-Year-Plan
  semiconductor-equipment localization programs; SMIC/YMTC mature-node expansions
  (L06-051/052/054).
- **2030 competition:** Comet Synertia, AE/MKS in-house, DAIHEN; CN: Hengyunchang/Injet
  moving up-stack (fast at generator level, slow at high-end match components).
- **Window/access risk:** incumbent absorption pre-2030 is the main risk; CN access via
  component sales/licensing into mature-node OEM chains is export-clean if scoped.
- **Kill date:** 2034; kill trigger — no design-in/converted evaluation by end-2033.
- **Big vision:** the impedance-delivery layer for all fast plasma processing.
- **Nearest substitutes:** motorized vacuum-cap matchboxes; frequency-tuning-only
  generators; OEM in-house solid-state matches.
- **Key uncertainty:** whether solid-state elements meet vacuum-cap voltage/Q ratings at
  acceptable cost at 60 MHz.
- **[Adjudication 2026-07-13 R2 - PROMOTE]:** strongest new dual seed (N6/E7/C7/V7/T7); non-obvious by the convergence test; clean A-10 complement. Absorbed F-14's licensing-with-golden-reference mechanics (milestone-based contracts via an HK-structured IP entity; founder retains golden references, calibration methodology, and factory test benches) as the CN chapter's IP structure; Hengyunchang/Injet buyer evidence already cited (L06-042/043/044). Comet-Synertia absorption risk covered by the kill trigger.

## P3R2-F-02 — Superconducting-magnet drive-and-dump electrical BOP platform (dual US+CN)

- **Product:** Standardized skids: 1–50 kA ppm-class precision DC converters, integrated
  energy-extraction/dump units with magnet-aware sequencing, HTS/binary current leads,
  water-cooled bus; published acceptance protocol; clean interface to third-party quench
  detection. Entry SKU (absorbed from F-21): catalog binary current leads (0.5–20 kA)
  and vacuum-tight instrumented feedthroughs with certified heat-load datasheets.
- **Buyer + pain per market:** US — merchant magnet commerce now exists (CFS→Realta,
  UW-WHAM, L03-035) atop the DOE milestone program (L03-032); every magnet sale drags a
  bespoke electrical island behind it. CN — ASIPP runs real, dated tenders for exactly
  this hardware class (ITER PF converter control modules L01-037; RMP power-supply
  expansion L01-038); WST/ITER lineage shows the procurement channel (L03-031).
- **Mechanism:** high-stability (10 ppm) converter modules + fail-safe extraction with
  sequenced dump resistors, engineered as one certified unit rather than per-project
  engineering.
- **Why incumbents miss it:** magnet PSU work is trapped between national-lab in-house
  builds and one-off vendor projects; precision converters themselves are catalog items
  (OCEM/Danfysik-class), so the unproductized white space is the integrated
  extraction/dump + leads + acceptance-protocol island — not converter novelty (P4
  incumbency map required pre-promotion).
- **Not a duplicate:** Nearest survivor D-01 (quench detection + protection electronics).
  D-01 detects and triggers; F-02 *drives and dumps* — the power island D-01's trigger
  commands. Also distinct from C-09 (pulsed modulators; this is precision steady-state
  DC). Designed to integrate with D-01, mirroring the A-02/E-14 hardware/intelligence
  split the judge endorsed.
- **Decisive experiment + budget:** scaled 5 kA converter + integrated dump on a
  university HTS coil, 10 ppm stability, clean extraction on simulated quench — $400k,
  2027–28.
- **TRL:** 6 (converter engineering mature; novelty is standardization + magnet-aware
  integration). **2026–2029 plan:** acceptance-protocol drafting with a magnet lab;
  prototype; 2028 merchant-magnet-buyer LOI; 2029 lead/busbar supply chain; 2027
  export/CN-access counsel gate.
- **Named triggers 2030–2034:** US — DOE Milestone Program reauthorization at FY2027
  boundary (L03-032) and post-SPARC pilot-plant magnet procurement. CN — ASIPP/CAS
  big-science power-supply tender cadence under the 15th FYP large-facility program
  (L01-037/038), reached via international big-science procurement routes.
- **2030 competition:** OCEM/Danfysik-class PSU specialists (judgment; P4 map), lab
  in-house groups, CN institute self-supply; CFS vertical integration caps the US share.
- **Window/access risk:** fusion schedule slip; CN access is big-science-channel only.
  Hedge: research/industrial magnets and accelerator PSUs exist regardless of fusion.
- **Kill date:** 2034; kill trigger — no paid order from magnet buyer or lab by end-2033.
- **Big vision:** the "power island in a box" for the commercial-magnet fleet.
- **Nearest substitutes:** lab-built converters; converter-vendor one-off projects.
- **Key uncertainty:** how much of the drive-and-dump stack CFS-class vendors bundle with
  the magnets they sell.
- **[Adjudication 2026-07-13 R2 - PROMOTE]:** (N5/E7/C7/V7/T7). Promote-conditions applied: white space restated as the integrated extraction/dump + leads + acceptance-protocol island (precision converters are catalog items - P4 OCEM/Danfysik incumbency map required pre-promotion); CFS bundling stays the named US ceiling. Absorbed F-21 as entry SKU: catalog binary leads/instrumented feedthroughs, certified heat-load datasheets, end-2031 <$1M entry-SKU gate (source imports +L03-052, +L07-009).

## P3R2-F-03 — High-speed PM turbo-generator + converter "electrical cartridge" for waste-heat/geothermal power blocks (dual US+CN)

- **Product:** Catalog electrical cartridge for 0.3–20 MW turbomachinery: high-speed PM
  generator classes, active front-end converter with grid-code package, bearing-drive
  electronics, defined shaft interfaces; sold to machine integrators.
- **Buyer + pain per market:** US — EGS is turbine-supply-constrained even with a 1.75 GW
  Turboden order and $421M project debt behind it (L04-044/115); STEP-class sCO2
  machines hand-build their electrical systems (L04-039); TC Energy–Hanwha shows
  pipeline-compressor WHR demand (L04-047). CN — Chaotan One is the world's first
  commercial sCO2 waste-heat unit (30 MW, steel sintering; L04-048/051) with a state-media
  retrofit pipeline (RMB ~100B, single-source, flagged) and institute compressor programs
  (CAS-IET/SMDERI, L04-102/106) but no standardized electrical island.
- **Mechanism:** co-designed PM rotor + converter + bearing drive as one rotordynamic
  unit; grid-code compliance engineered once, reused across cycles (sCO2/ORC/air).
- **Why incumbents miss it:** turbine OEMs treat generators as project engineering;
  high-speed machine specialists sell components, not certified cartridges with grid
  interface.
- **Not a duplicate:** Nearest survivors C-08 (PCHE recuperators) and C-19 (seals/foil
  bearings) — both are *thermal-mechanical* components for the same machines; F-03 is the
  *electromagnetic conversion + power electronics* subsystem. No survivor owns the
  electrical side of heat-to-power machines.
- **Decisive experiment + budget:** 250 kW/30 krpm generator + AFE on a drive stand with
  sCO2/ORC load transients, grid-code ride-through, hot restart — $900k, 2028.
- **TRL:** 5. **2026–2029 plan:** machine-builder requirements interviews → prototype →
  2029 co-development agreement; CN licensing structure scoped 2028.
- **Named triggers 2030–2034:** US — post-2029 EGS expansion procurement beyond Cape
  Station (debt-financed precedent L04-115); NRC Part 53-era advanced-reactor BOP awards
  (L04-045 pattern). CN — post-Xinjiang "first-set" serial sintering retrofits
  (designation-unlocked procurement, L04-051), via licensed manufacturing.
- **2030 competition:** Calnetix-class specialists (judgment), Turboden/Hanwha in-house
  (L04-047/055), CAS-IET-affiliated CN suppliers.
- **Window/access risk:** if retrofits stay CNNC-internal and ORC OEMs keep generators
  in-house, the merchant socket shrinks; multi-cycle applicability is the hedge. EGS leg
  is partially datacenter-correlated (Google offtake) but primary engines are industrial
  waste heat and turbine capacity shortage.
- **Kill date:** 2034; kill trigger — no machine-builder design win by end-2033.
- **Big vision:** commoditize the electrical half of small turbomachinery.
- **Nearest substitutes:** gearbox + standard generator packages; OEM in-house PM designs.
- **Key uncertainty:** the CN retrofit TAM is single-source (L04-051) — P4 must
  triangulate before any scale assumption.
- **[FIX applied 2026-07-13 R2]:** P4 Calnetix-class/turbine-OEM in-house incumbent map made a pre-promotion requirement; 2029 machine-builder co-development agreement made a binding gate; single-source CN TAM (L04-051) now carries a pre-scale triangulation gate; $900k experiment staged behind the requirements interviews; absorbed F-18 as the CN plant-integration/licensing chapter (EPC co-bidding memorandum, Xinjiang first-set alignment, rollout-industrialization framing).

## P3R2-F-04 — Merchant active-magnetic-bearing drive electronics + rotor-health platform (dual US+CN)

- **Product:** Standardized 5-axis AMB controller family: sensing, adaptive
  unbalance/shock control, touchdown-bearing life management, fleet telemetry;
  semiconductor-grade qualification dossier; entry via turbomolecular pumps, expansion to
  sCO2 compressors, blowers, flywheels.
- **Buyer + pain per market:** US — turbopump bearing/vibration reliability is unsolved
  after 30+ years (L07-010..013, incl. 2023 shock-instability work); MKS-scale vacuum
  businesses ride fab capex (L07-050); Sandia lists bearings among sCO2 unknowns
  (L04-113); flywheel power buffering is procurable (Piller selection, L16-052). CN —
  semiconductor vacuum demand re-accelerating (INFICON APAC +19.2% attributed to China,
  L07-053), tool-OEM expansion (L06-048), CAS-IET turbomachinery programs (L04-106/109),
  HEPS-class big-science vacuum (L07-045). CN leg graded moderate and flagged.
- **Mechanism:** modern control (self-identifying rotor models, adaptive notch,
  shock-event recovery) + telemetry on a certified electronics platform, sold merchant.
- **Why incumbents miss it:** machine OEMs treat AMB controllers as in-house craft;
  merchant AMB vendors serve oil&gas-scale machines, not semiconductor-grade duty with
  fleet analytics.
- **Not a duplicate:** Nearest survivors C-19 (mechanical foil-bearing/seal cartridges —
  different physics, no electronics) and D-19 (flywheel *system* vendor — a customer, not
  a competitor). No survivor sells bearing electronics.
- **Decisive experiment + budget:** retrofit controller on a commercial turbopump; shock
  ride-through per L07-012 scenario + validated touchdown-life prediction — $350k, 2027.
- **TRL:** 5. **2026–2029 plan:** retrofit demo → incumbent teardown positioning study →
  2028 OEM paid evaluation → 2029 second-vertical demo (sCO2 rig or flywheel).
- **Named triggers 2030–2034:** US — STEP-lineage sCO2 hardware scale-up; flywheel
  deployments for AI-power stabilization (L16-052 precedent). CN — fab-tool localization
  waves pulling domestic pump content (L06-048); CAS turbo programs (L04-106/109).
- **2030 competition:** SKF S2M, Calnetix, Waukesha (judgment; P4 to source); CN maglev
  blower/pump makers scaling — CN domestic substitution is fast.
- **Window/access risk:** incumbents are real; wedge (semiconductor-grade shock recovery
  + cross-fleet telemetry) must prove decisive early, hence the tighter kill.
- **Kill date:** 2034 hard stop; internal kill 2032 if no OEM design win.
- **Big vision:** bearing electronics as a platform across the high-speed machine fleet.
- **Nearest substitutes:** in-house controllers; incumbent merchant AMB electronics; hybrid
  ceramic bearings avoiding AMB entirely.
- **Key uncertainty:** whether pump OEMs will externalize a component this close to their
  core differentiation.
- **[FIX applied 2026-07-13 R2]:** 2028 paid OEM evaluation made the binding externalization proof; 2027/P4 teardown of SKF S2M/Calnetix/Waukesha vs the semiconductor-duty claim; CN leg conditional - a named CN pump/tool-OEM design-in channel must be evidenced in P4 or primary_market downgrades to US (INFICON APAC attribution is not buyer evidence); 2032 internal kill retained. Counted dual-conditional in the judge's quota.

## P3R2-F-05 — Certified battery-electric traction repower kits for port/mining equipment (dual US+CN)

- **Product:** Repower kit family: 650–1000 V pack power conversion, harsh-duty traction
  inverters, VCU, dual-personality charge interface (CCS/MCS and GB/T-swap variants);
  certified once, reused across vehicle classes; sold to repower integrators and OEM
  export programs.
- **Buyer + pain per market:** US — ~$3B EPA Clean Ports awards must become zero-emission
  equipment within 3–4-year windows (L10-048); repowering existing diesel fleets is the
  affordable path but off-highway repower electrics remain per-project engineering ('no
  standardized kit' downgraded to judgment pending the P4 teardown); E-hybrid RTG procurement shows the
  equipment class (L10-041). CN — Chinese OEMs exporting electric heavy equipment into
  Western fleets (XCMG–Fortescue, phased 2028–2030, L10-028) need IEC/UL/MCS-certified
  power electronics their domestic chain wasn't built for; swap-standard equipment lines
  are codified (L10-046) and SOE fleet scale is documented (L10-034).
- **Mechanism:** one certified electrics stack + interface personalities; certification
  matrix (UL/IEC/GB) engineered as the product core.
- **Why incumbents miss it:** vehicle-OEM electrics are model-specific; Tier-1 traction
  suppliers chase on-highway volume; nobody serves heterogeneous off-highway retrofits
  with a certified kit.
- **Not a duplicate:** Nearest survivors A-21 (multi-MW *charging infrastructure*) and
  B-14 (dual-standard *interface module*). F-05 is the *vehicle-side powertrain kit* —
  the other end of the plug; B-14's interface concept appears here only as one purchased
  personality module.
- **Decisive experiment + budget:** one yard-tractor/RTG-class repower under a port
  pilot; duty-cycle equivalence, 45 C thermal margins, certification-gap audit — $600k,
  2028.
- **TRL:** 6. **2026–2029 plan:** EPA-fleet mapping → 2028 grant-funded pilot + one CN
  OEM export-certification engagement → 2029 UL/IEC certification of kit v1; monitor
  CARB-repeal-style regression (L10-044) as a demand-quality gate.
- **Named triggers 2030–2034:** US — post-grant equipment mid-life repower cycles; MCS
  charger arrival at scale (IEC TS 63379, L10-050). CN — XCMG/CATL-ecosystem export
  deliveries 2028–2030 (L10-028) requiring Western-cert electronics; GB/T swap equipment
  programs (L10-046).
- **2030 competition:** Dana TM4, BAE, Danfoss Editron, ZF (judgment); CN OEM in-house
  electrics — certification-led positioning is the only defense against cost-led
  substitution.
- **Window/access risk:** regulatory reversal risk documented (L10-044); OEM-integrated
  electrics may close the socket mid-2030s.
- **Kill date:** 2034; kill trigger — <2 paid repower programs or no CN OEM engagement by
  end-2032.
- **Big vision:** the certified-electrics standard for off-highway electrification.
- **Nearest substitutes:** OEM new-equipment sales; bespoke one-off conversions.
- **Key uncertainty:** post-grant (unsubsidized) repower economics.
- **[FIX applied 2026-07-13 R2]:** defensible core restated as the UL/IEC/GB certification matrix + dual-personality interface (kit-existence claim downgraded to judgment pending P4 teardown vs Danfoss Editron/Dana TM4/BAE); 2028 CN OEM export-certification LOI made binding; unsubsidized repower economics model due 2028; B-14 interface personality bought as a module, not rebuilt.

## P3R2-F-06 — Precision wideband DC sensing platform for HVDC, electrolysis, magnets (US-primary; CN license chapter only — downgraded 2026-07-13)

- **Product:** Fiber-optic DC CTs + zero-flux hybrid transducers (kA–100 kA, DC–1 MHz)
  with a published accuracy/bandwidth acceptance protocol; sold to converter/protection
  OEMs and plant EPCs; CN via license-out manufacturing only.
- **Buyer + pain per market:** US — Southern Spirit-class VSC-HVDC (construction 2029,
  L08-041), GEV's ~$10B HVDC backlog (L08-033), and the PRC-029/IEEE-2800.2 compliance
  wave (L08-043/047) all need protection-grade DC measurement; protection algorithms are
  re-derived per project partly because sensing varies (L08-005/006/007). CN — State
  Grid's precisely disclosed UHV tender cadence (XJ RMB1.275B including DC
  control/protection, L08-034) defines a licensed-manufacture channel; electrolysis
  plants lack ripple-visibility instrumentation (L11-016..021, L11-045).
- **Mechanism:** interferometric fiber sensing fused with zero-flux reference channels
  for absolute accuracy + wideband transient fidelity in one head.
- **Why incumbents miss it:** sensing is bundled inside converter OEM scope; merchant
  vendors optimize either accuracy (metering) or bandwidth (protection), not both with an
  open qualification protocol.
- **Not a duplicate:** Nearest survivor E-14 (DC protection relay + qualification). E-14
  is the *protection intelligence*; F-06 is the *measurement layer* that feeds it — an
  explicit complement, structured like the A-02/E-14 split.
- **Decisive experiment + budget:** 10 kA optical+zero-flux hybrid, published round-robin
  vs commercial references, DC–100 kHz fidelity for traveling-wave protection — $300k,
  2027–28.
- **TRL:** 5. **2026–2029 plan:** prototype → national-lab round-robin → 2029 OEM/EPC
  evaluation agreement; CN license term sheet 2029.
- **Named triggers 2030–2034:** US — Southern Spirit and successor interregional HVDC
  procurements 2029–2032 (L08-041); IBR ride-through retrofit testing (L08-043/047).
  CN — annual State Grid UHV equipment tender batches (L08-034), licensed channel.
- **2030 competition:** Hitachi/ABB optical CTs, LEM/Hitec, NR/XJ in-house.
- **Window/access risk:** component margins + entrenched bundling; State Grid is
  domestic-only, so CN revenue is license royalties at best.
- **Kill date:** 2034; kill trigger — no project order via OEM/EPC by end-2033.
- **Big vision:** the interoperable measurement backbone of the DC century.
- **Nearest substitutes:** converter-OEM bundled sensing; conventional shunts/DCCTs.
- **Key uncertainty:** whether third-party protection (E-14-class) wins enough sockets to
  pull an independent sensing layer with it.
- **[FIX applied 2026-07-13 R2 - flags downgraded]:** primary_market US+CN -> US, china_beachhead -> false (honesty ruling: State Grid domestic-only, CN revenue 'license royalties at best' - the C-12/C-21 condition; CN license chapter retained in text, not counted toward CN quota). 2029 OEM/EPC evaluation agreement made binding and paired with E-14-class third-party protection traction; P4 Hitachi/ABB optical-CT incumbency map required - the wedge is the demonstrated round-robin result, not an assertion.

## P3R2-F-07 — High-cycle charging-interface thermal subsystems: MCS cables (US) + swap couplers (CN) (dual US+CN)

- **Product:** Liquid-cooled (water-glycol/low-GWP, explicitly non-PFAS) megawatt
  cable-connector assemblies for MCS charging with contact-health sensing; high-cycle
  swap-coupler thermal/contact modules and buffer-charging cold plates for swap stations;
  sold to charger and swap-equipment OEMs.
- **Buyer + pain per market:** US — MCS standard published (IEC TS 63379, 3.75 MW/3,000 A,
  L10-050), NREL building a 20 MW emulator (L10-049), EPA-funded port equipment entering
  service (L10-048); connector/cable thermal engineering is still active research
  (L14-019..022) with its reference coolant family discontinued. CN — swap architecture is
  the strategic bet: sub-7-minute swaps cycling 13×800 kWh packs (SPIC Oyu Tolgoi,
  L10-031), a national excavator-swap standard (L10-046), canal swap ships as national
  benchmarks (L10-040, CCS rules L10-045) — all high-cycle contact+thermal duty with no
  specialist supplier.
- **Mechanism:** conductor-integrated cooling channels + contact-resistance
  micro-signature monitoring; thermal design validated at duty cycles, not steady state.
- **Why incumbents miss it:** connector majors sell geometry and amp ratings; the
  duty-cycle thermal+health engineering between EVSE OEM and connector vendor is
  no-man's-land.
- **Not a duplicate:** Nearest survivors B-14 (standards-personality interface module —
  electrical/standards arbitrage, not thermal engineering) and A-21 (charging systems —
  a customer). B-01 is chip-cooling loops in racks, different market and product.
- **Decisive experiment + budget:** 3,000 A/1,250 V cooled cable-connector on a thermal
  bench: 10-minute-cycle duty on water-glycol, <10% contact-resistance drift over 10,000
  mate cycles — $450k, 2027–28.
- **TRL:** 5. **2026–2029 plan:** duty-cycle bench → 2028 charger-OEM co-development +
  CN swap-equipment licensed design-in → 2029 endurance dataset.
- **Named triggers 2030–2034:** US — MCS charger rollouts for ports/heavy trucking as
  EPA-funded fleets mature (L10-048/050) and NREL-qualified hardware ships (L10-049).
  CN — swap-network expansion under national standards and SOE mining/marine programs
  (L10-031/040/046).
- **2030 competition:** Staubli/Phoenix/Huber+Suhner-class (judgment; P4 map); CATL/SPIC
  in-house for swap; CN connector majors.
- **Window/access risk:** MCS volume slip and swap vertical integration are the twin
  risks; coordinate with B-14 rather than compete.
- **Kill date:** 2034; kill trigger — no OEM design-in by end-2032.
- **Big vision:** own the amp-meters-per-minute bottleneck of heavy electrification.
- **Nearest substitutes:** oversized air-cooled cables; OEM-integrated cooling.
- **Key uncertainty:** no eligible atlas source yet documents CN *conductive* MW-charging
  demand — the CN leg rides swap evidence; P4 must confirm swap-side component
  procurement is open to licensed outsiders.
- **[FIX applied 2026-07-13 R2]:** CN-leg binding gate added (P4 confirmation that CN swap-equipment component procurement is open to licensed outsiders); 2028 charger-OEM co-development made binding; P4 connector-major incumbent map (Staubli/Phoenix Contact/Huber+Suhner) with the 10,000-mate-cycle duty dataset as wedge proof; sequencing fixed: port/mining (funded) before trucking (MCS volume risk).

## P3R2-F-08 — Press-pack SiC switching modules for DC fault interruption (dual US+CN)

- **Product:** Press-pack, double-side-cooled, fail-short, series-stackable SiC module
  family with characterized interruption duty (di/dt, avalanche, sharing), integrated
  grading and gate-drive interface — the switching heart for SSCBs/hybrid breakers and
  fault-blocking MMC submodules.
- **Buyer + pain per market:** US — DC breakers are the documented "showstopper"
  (L08-016) and topology research continues without converged devices (L08-001/003/017;
  ORNL prototyping L08-051); datacenter electrification orders surging (GEV $2.4B/quarter,
  L08-033) pull MVDC protection qualification. CN — State Grid buys converter valves and
  DC control/protection at RMB-precision (XJ RMB1.275B, L08-034); fault-blocking
  submodules trade device count against loss — a device-level gap (license-out packaging
  only for CN).
- **Mechanism:** SiC's fast, high-temperature interruption capability packaged in
  press-pack format (fail-short, stackable) that breaker/valve OEMs already know how to
  integrate.
- **Why incumbents miss it:** device majors optimize traction/inverter volume;
  interruption duty is a specialty qualification they under-prioritize; breaker startups
  improvise with repurposed IGBTs.
- **Not a duplicate:** Nearest survivor A-02 (MVDC hybrid breaker — the *system*). F-08 is
  a *component supplier to* A-02-class OEMs; no survivor sells switching devices.
- **Decisive experiment + budget:** interruption-duty characterization of commercial SiC
  die vs press-pack IGBT baselines, published gap analysis — $350k, 2027 (university
  power-packaging lab).
- **TRL:** 4. **2026–2029 plan:** die characterization → 2028 first press-pack prototype
  with fail-short qualification → 2029 two breaker-developer evaluations; packaging-partner
  route to cap capex.
- **Named triggers 2030–2034:** US — MVDC pilot deployments and datacenter MVDC
  protection qualification cycles (L08-033/051). CN — State Grid VSC/flexible-DC tender
  batches needing fault-blocking submodules (L08-034), licensed packaging only.
- **2030 competition:** Infineon/Hitachi/Fuji press-pack lines extending to SiC;
  StarPower/BYD Semi (judgment; P4 to source).
- **Window/access risk:** gated on meshed-DC adoption (open contradiction in L08-016 vs
  awarded point-to-point projects); capital-intensive packaging.
- **Kill date:** 2034; kill trigger — no breaker-OEM design-in by end-2033 or absent
  meshed-DC procurement signals by 2032.
- **Big vision:** the switch foundry of the meshed-DC era.
- **Nearest substitutes:** press-pack IGBTs/IGCTs; paralleled discrete SiC.
- **Key uncertainty:** whether SiC's interruption ruggedness (avalanche/short-circuit
  withstand) can be engineered to breaker-grade at acceptable die cost.
- **[Adjudication 2026-07-13 R2 - REJECT]:** double contingency - component supplier into the atlas's documented unconverged meshed-MVDC showstopper, one level below A-02 without its productization wedge; the offered demand anchors do not hold (GEV orders are not MVDC-protection procurement; State Grid valves license-out only); press-pack incumbents absorb the socket if meshed DC arrives. Die-characterization workstream imported into P3R2-A-02 (see the A batch). Record retained as audit trail.

## P3R2-F-09 — Merchant high-power RF vacuum windows and output couplers (dual US+CN)

- **Product:** Qualified coaxial/waveguide windows and couplers (brazed ceramic,
  multipactor-suppressed) with integrated arc/temperature diagnostics and a published
  acceptance protocol (IEC 60060-1:2025-referenced HV practice, L05-043); OEM components
  and lifetime-extension spares.
- **Buyer + pain per market:** US — coupler/window failure is named the most common
  vacuum-electronics failure mode at high CW power with fixes still research-stage
  (L05-014); DOE ARDAP funds accelerator industrialization (L05-031/032); gyrotron
  deliveries run to ~2029 (Thales/F4E EUR20M, L05-029). CN — IHEP's CEPC klystron program
  (78.5% at 803 kW, L05-012/013) and CGN Dasheng's expanding industrial-accelerator
  business (L05-035/038) consume the same components; access via big-science procurement.
- **Mechanism:** ceramic-metal joining + anti-multipactor coatings + integrated
  diagnostics, produced under a repeatable qualification protocol instead of tube-shop
  craft.
- **Why incumbents miss it:** tube primes treat windows as internal art and don't sell
  qualified spares; labs hand-build; no one has productized the interface with health
  telemetry.
- **Not a duplicate:** Nearest survivor C-09 (modulator platform — drives the tube; F-09
  is the RF-vacuum interface component). D-07 (MSDC retrofit) touches collectors, not
  windows/couplers.
- **Decisive experiment + budget:** 1 MW-class pillbox window prototype, thermal-cycling
  life + multipactor margin vs reference, integrated diagnostics — $500k, 2028.
- **TRL:** 4. **2026–2029 plan:** joining + multipactor test capability with a lab
  partner → 2028 evaluation windows into one rebuild program (ARDAP channel) → 2029
  published lifetime dataset; CN channel via international procurement counsel.
- **Named triggers 2030–2034:** US — fusion-heating RF procurement and ARDAP-lineage
  accelerator industrialization post-2030 (L05-031/032). CN — CEPC construction decision
  window and CGN Dasheng capacity additions (L05-012/013, L05-035/038).
- **2030 competition:** CPI/Thales/Canon in-house (L05-050/029), Kyocera-class ceramics
  (judgment); KR localization channel (Vitzro/PAL, L05-037) as optional side market.
- **Window/access risk:** small TAM, conservative buyers — honestly a component-niche
  business unless the diagnostics layer creates a standard.
- **Kill date:** 2034; kill trigger — fewer than two paying lab/OEM customers by
  end-2032.
- **Big vision:** the standard RF-vacuum interface company for the beam economy.
- **Nearest substitutes:** OEM internal window shops; lab spares fabrication.
- **Key uncertainty:** whether tube primes will buy a critical reliability component from
  a startup rather than fix it internally.
- **[FIX applied 2026-07-13 R2]:** 2028 evaluation windows inside one NAMED rebuild program (ARDAP channel) made the binding gate; P4 evidence on prime merchant-buy behavior (negative -> re-scope to lab spares/aftermarket and re-size); two-paying-customers-by-2032 kill retained; P4 evaluates a beam-components portfolio company with C-09/D-07 adjacency.

## P3R2-F-10 — Laser-ultrasonic inline weld inspection: battery welds (CN) + pipelines (US) (dual US+CN)

- **Product:** Non-contact inline inspection head — fiber-laser ultrasound generation,
  interferometric/EMAT detection, real-time phased-array reconstruction — packaged as a
  bolt-on QC subsystem for battery-welding equipment OEMs and pipeline scanner
  integrators, with standards-mapped reporting.
- **Buyer + pain per market:** US — PAUT is the standards-governed workhorse of pipeline
  weld inspection (ISO 13588 / ASTM E2700, L16-026/027) but is couplant-based and slow;
  code editions revise on ~7-year cycles. CN — battery makers weld millions of Al–Cu
  joints on equipment bought at documented, buyer-concentrated scale (CATL/BYD >50% of a
  major supplier's comparable purchases, L16-028) with no non-contact volumetric QC at
  line rate; laser-PAUT exists as research only (L16-029).
- **Mechanism:** laser-generated broadband ultrasound + synthetic-aperture phased-array
  processing = volumetric weld interrogation with zero contact/couplant at production
  speed.
- **Why incumbents miss it:** NDT majors monetize handheld/scanner PAUT and have no
  production-line OEM channel; battery equipment makers monetize welders, not inspection.
- **Not a duplicate:** No NDT survivor exists in the pool. Nearest survivor in *style* is
  D-02 (reel-to-reel Ic metrology) — different physics, market, and buyers. Instrument
  wedge honestly flagged; expansion path is OEM-embedded subsystem, per wave guidance.
- **Decisive experiment + budget:** laser-UT scan of production Al–Cu tab welds at >=1
  weld/s equivalent with teardown-correlated POD vs offline PAUT — $400k, 2027.
- **TRL:** 4. **2026–2029 plan:** lab demo + destructive correlation → 2028
  co-development with one CN battery-equipment maker (design-in/license) and one US NDT
  service firm → 2029 ISO 13588-revision engagement + POD-at-speed dataset.
- **Named triggers 2030–2034:** US — hydrogen/CO2 pipeline construction waves inspected
  under updated ISO/ASTM editions (L16-026/027 cycle). CN — next battery-capacity and
  equipment-replacement cycles at CATL/BYD-class lines (L16-028).
- **2030 competition:** Evident/Olympus, Zetec, Baker Hughes NDT (judgment); CN NDT
  makers; cheap substitutes: vision + electrical weld monitoring.
- **Window/access risk:** POD-at-speed is the make-or-break metric; if it underperforms,
  this remains a lab curiosity.
- **Kill date:** 2034; kill trigger — POD/speed target unmet by end-2029 or no OEM
  design-in by end-2032.
- **Big vision:** non-contact volumetric weld QC wherever gel cannot go.
- **Nearest substitutes:** offline PAUT, X-ray/CT sampling, electrical weld monitors.
- **Key uncertainty:** signal quality on thin, highly reflective Al–Cu stacks at line
  rate.
- **[FIX applied 2026-07-13 R2]:** CN demand bridge made binding (battery-equipment OEM co-development/design-in LOI by 2028); US pipeline leg de-weighted until a named operator/NDT-service evaluation exists by 2028; POD-at-speed end-2029 kill made binding; L16-028 (2022) refresh required before final scoring; P4 incumbent check extended to Tecnar-class laser-UT and Evident/Baker Hughes production NDT.

## P3R2-F-11 — Magnetic-pulse welding machines for Al–Cu battery interconnects (CN-primary)

- **Product:** Production MPW cell: long-life field-shaper coils (the consumable moat),
  solid-state capacitor bank with per-shot energy control and coil-health monitoring,
  weld-window recipes for Al–Cu busbar/tab stacks.
- **Buyer + pain (CN):** battery-equipment integrators serving CATL/BYD — the documented,
  buyer-concentrated equipment channel (L16-028). Ultrasonic struggles with thick busbars
  and particle generation; MPW research shows sound dissimilar joints inside mapped
  weldability windows (L16-030/031) but a 15-year "renaissance" has never productized it
  (L16-032/033).
- **Mechanism:** pulsed electromagnetic impact joining — solid-state, no heat-affected
  zone, ideal for dissimilar conductors; the engineering problem is coil life and window
  robustness, both electronics-controllable.
- **Why incumbents miss it:** ultrasonic incumbents defend their process; EM-forming
  specialists never built battery-line-rated machines; coil consumable economics scared
  everyone off — which is exactly the engineering wedge.
- **Not a duplicate:** Nearest survivor C-09 (pulsed-power modulators — accelerator/RF
  drive, entirely different application and buyer). No survivor touches EM
  forming/welding. EM *forming* is not on the atlas enthusiasm-zone list (EHD, acoustic
  levitation, EM launch, solid-state cooling are); the demand bridge is the documented
  equipment-buyer base, not physics enthusiasm.
- **Decisive experiment + budget:** Al–Cu busbar joints inside a mapped window with
  >=10,000-shot coil life and pull/conductivity parity vs ultrasonic — $350k, 2027–28.
- **TRL:** 5. **2026–2029 plan:** lab rig + coil-life engineering → 2028 co-development
  with a CN integrator (founder supplies pulsed-power + process IP; partner integrates
  and sells — the foreign-founder access path) → 2029 pilot busbar cell with cycle-life
  economics.
- **Named triggers 2030–2034:** CN — battery equipment replacement/expansion at
  CATL/BYD-class plants and cell-to-pack busbar architectures thickening interconnects
  (procured through the L16-028 integrator ecosystem); 800 V platform proliferation.
- **2030 competition:** Jiaocheng Ultrasonic defending (L16-028), laser welding, EU MPW
  specialists (Bmax/PSTproducts-class, judgment); certain CN fast-follow once windows
  publish — IP + coil know-how must stay ahead.
- **Window/access risk:** process substitution is slow; access is integrator-mediated.
- **Kill date:** 2034; kill triggers — coil life <10,000 shots at spec by end-2028, or no
  integrator agreement by end-2030.
- **Big vision:** solid-state joining as the default for dissimilar-metal electrification
  hardware.
- **Nearest substitutes:** ultrasonic welding, laser welding, mechanical fastening.
- **Key uncertainty:** coil lifetime economics at production duty.
- **[FIX applied 2026-07-13 R2]:** coil-life gate (>=10,000 shots at spec by end-2028) made binding - the engineering thesis; 2028 CN integrator co-development with a contractualized IP split (founder retains pulsed power + recipes; integrator sells); 2028 cost-per-joint/line-rate model vs ultrasonic AND laser (laser is the real substitute); L16-028 refresh required before final scoring.

## P3R2-F-12 — Class-certified marine battery DC power & protection stacks for electric inland vessels (CN-primary)

- **Product:** Type-approved marine DC stack: string-level protection/isolation,
  insulation monitoring, containerized-swap-pack power/comms interface per CCS Rules,
  shore-monitoring data gateway; sold to shipyards/integrators.
- **Buyer + pain (CN):** shipyards and integrators building Jining "6006"-class swap
  cargo vessels (national transport benchmark, L10-040) must comply with the CCS Rules
  for Battery-Powered Ships 2025 edition (effective 2025-12-31: containerized mobile
  power inspection, shore-based monitoring, online data exchange — L10-045) with no
  specialist merchant electrics supplier; Maersk–CATL port MOUs show the ecosystem
  scaling (L10-036).
- **Mechanism:** DC protection + IMD + pack-interface engineering mapped one-to-one onto
  class-rule clauses; the type-approval dossier is the moat.
- **Why incumbents miss it:** CATL integrates packs, not class-rule electrics; European
  marine-electric houses are locked out of the inland CN fleet on cost; shipyards
  improvise per vessel.
- **Not a duplicate:** Nearest survivor C-01 (800VDC rack protection — datacenter racks,
  entirely different rules, buyers, and environment). No survivor addresses marine class
  rules.
- **Decisive experiment + budget:** full stack built to CCS 2025-edition clauses passing
  a class-society design appraisal (paper + bench) — $300k, 2028.
- **TRL:** 5. **2026–2029 plan:** clause-to-architecture mapping → 2028 JV/licensed
  manufacturing partner (the honest foreign-founder access path) + CCS type-approval
  start → 2029 pilot vessel retrofit; DNV variant scoped as export hedge.
- **Named triggers 2030–2034:** CN — CCS-rule enforcement on newbuilds/refits from 2026
  and the next rules edition (2023→2025 cadence implies ~2027–2029, L10-045); provincial
  canal-electrification programs following the national-benchmark designation (L10-040).
- **2030 competition:** CATL-integrated electrics (dominant), CSSC-affiliated suppliers,
  Danfoss Editron-class (judgment). Domestic substitution fast: JV concedes manufacturing,
  retains protection IP + type-approval ownership.
- **Window/access risk:** if CATL bundles the full electrical stack with packs, the
  merchant socket closes — the wedge is non-CATL integrators + class-rule complexity.
- **Kill date:** 2034; kill trigger — no CCS type approval + pilot vessel by end-2031.
- **Big vision:** the class-rule-native electrical backbone of electric shipping,
  exportable to DNV/ABS markets.
- **Nearest substitutes:** pack-vendor bundled electrics; shipyard bespoke integration.
- **Key uncertainty:** how much electrical scope CCS-era pack vendors will bundle.
- **[Adjudication 2026-07-13 R2 - PROMOTE]:** best CN-primary seed of the wave (N6/E6/C7/V6/T7): dated CCS 2025-edition trigger, type-approval-dossier moat, honest JV structure, $300k class-design-appraisal experiment, named CATL-bundling kill. P4: confirm the non-CATL integrator/shipyard share, map CSSC-affiliated suppliers, scope the DNV/ABS export hedge.

## P3R2-F-13 — Teleoperation/autonomy retrofit power-and-actuation electronics for SOE mining fleets (CN-primary)

- **Product:** Standardized retrofit kit: safety-rated power distribution with redundant
  supplies, electro-hydraulic actuation drive modules, drive-by-wire VCU with certified
  E-stop chain, hardened for 45 C/dust/vibration; sold as components to CN autonomy
  integrators.
- **Buyer + pain (CN):** SOE mines tender remote-intelligent-control retrofits at project
  scale (Baogang Barun: ~RMB3.75M tender within an RMB18.06M project, bids due July 2026,
  L10-035) against 60+-truck fleet baselines (China Gold, L10-034); every integrator
  re-solves safety power, actuation, and E-stop hardware vehicle-by-vehicle. Global
  autonomy integration precedent: BHP/Rio/Cat Jimblebar (L10-030); SPIC swap fleet ops
  (L10-031).
- **Mechanism:** functional-safety-grade power integrity + actuation electronics
  packaged as a certified kit that drops bid cost for integrators.
- **Why incumbents miss it:** autonomy integrators compete on software and treat retrofit
  hardware as project cost; vehicle OEMs only electrify new machines.
- **Not a duplicate:** No survivor covers mining teleoperation retrofits; nearest
  neighbors A-21/B-14 (charging/interface — different function) and A-14 (300 C
  electronics — different environment class).
- **Decisive experiment + budget:** kit v0 on one dozer-class machine, 500 h dusty-site
  remote operation with zero E-stop-chain faults — $400k, 2027–28.
- **TRL:** 6. **2026–2029 plan:** kit build + partner test site → 2028 channel
  agreements with two CN integrators (component supply via HK/bonded routes + local
  licensed assembly — the access path) → 2029 functional-safety documentation + first
  tender-embedded deployment.
- **Named triggers 2030–2034:** CN — recurring SOE "intelligent mine" retrofit tender
  rounds (Baogang phase cadence, L10-035) and safety-driven operator-removal programs;
  fleet-renewal procurement at China Gold-class scales (L10-034).
- **2030 competition:** integrator in-house hardware (Huawei-ecosystem), CRRC-affiliated
  suppliers; Western retrofit specialists locked out of SOE channels.
- **Window/access risk:** foreign content in SOE mine-safety systems is politically
  fragile — licensing-first structure; margins thin.
- **Kill date:** 2034; kill trigger — no integrator channel agreement by end-2030.
- **Big vision:** the electrical nervous system of the retrofit-automated heavy fleet,
  extending to ports/construction/agriculture.
- **Nearest substitutes:** integrator bespoke builds; OEM new autonomous machines.
- **Key uncertainty:** thin technical-source base in the atlas for this niche — P4 must
  add retrofit-architecture evidence.
- **[Adjudication 2026-07-13 R2 - REJECT]:** demand real and dated (Baogang, July 2026) but structurally captured: Huawei-ecosystem integrators self-supply, CRRC-class suppliers replicate fast (no hard physics), foreign content in SOE mine-safety chains politically fragile (self-flagged), RMB3.75M tender scale implies project-shaped thin-margin revenue, thin atlas technical base. Demand without a defendable technical wedge in the hardest-access market. Record retained as audit trail.

## P3R2-F-14 — Licensed high-end pulsed-RF power-stage IP for Chinese RF-generator makers (CN-primary)

- **Product:** Licensed IP blocks + golden-reference subassemblies: 13.56–60 MHz pulsed
  PA pallets, arc-response firmware, calibration methodology, factory test benches.
  Foreign founder keeps IP and metrology; CN licensee manufactures. Scope: >=28 nm /
  panel / display (export-control safety).
- **Buyer + pain (CN):** Hengyunchang (top-customer concentration 45–63%, top-5 = 90.6%
  — documented pressure to broaden product depth, L06-042/043) and Injet (PECVD RF orders
  growing, L06-044) must reach AE/MKS platform parity (L06-039/040) for tool OEMs scaling
  40–55%/yr (L06-048), against <12% component localization (L06-054).
- **Mechanism:** high-frequency pulsed PA design + arc-response + calibration know-how
  packaged as licensable engineering assets; the golden-reference + test-bench bundle
  keeps certification power with the licensor.
- **Why incumbents miss it:** AE/MKS will not license their core to CN rivals; CN
  entrants under-invest in high-frequency pulsed depth while racing revenue.
- **Not a duplicate:** Nearest rejected concept B-15 (merchant mid-market CN plasma
  supplies — a commodity knife fight this seed deliberately avoids by licensing instead
  of competing). Distinct from F-01 (matching hardware) — different element of the RF
  chain; and from A-10 (process-control layer).
- **Decisive experiment + budget:** 60 MHz/3 kW pulsed PA reference stage with
  arc-response firmware, third-party-witnessed benchmark vs a commercial generator —
  $250k, 2027.
- **TRL:** 5. **2026–2029 plan:** reference design → 2027 EAR classification counsel
  gate → 2028 first license negotiation via HK-structured IP entity → 2029 second
  licensee or a US licensing deal to prove the two-sided model.
- **Named triggers 2030–2034:** CN — 15th FYP semiconductor-equipment localization
  programs and mature-node fab expansion driving licensee product-line extensions
  (L06-051/052); IPO proceeds (RMB ~1.5B, L06-042/043) fund exactly such capability
  acquisition.
- **2030 competition:** licensees' own R&D (the built-in kill risk), poached-team
  knockoffs, AE/MKS integrated platforms.
- **Window/access risk:** export-control and IP-leakage tightrope; milestone-based
  contracts with know-how held in calibration/test assets.
- **Kill date:** 2034; kill triggers — export counsel blocks scope (2027) or no signed
  license by end-2030.
- **Big vision:** the ARM of plasma RF power, licensing on both sides of the
  export-control wall.
- **Nearest substitutes:** licensee in-house development; hiring ex-AE/MKS teams.
- **Key uncertainty:** enforceability of IP structure against absorption by 2032.
- **[Adjudication 2026-07-13 R2 - REJECT]:** B-12 precedent applies in full - in license-into-China know-how models the licensee is the accumulating asset; the seed names its own mechanism as the kill risk and golden-reference retention does not survive its own 2032 absorption horizon. Licensing mechanics + Hengyunchang/Injet buyer evidence imported into P3R2-F-01's CN chapter. Record retained as audit trail.

## P3R2-F-15 — Multi-stack DC distribution & per-stack management skids for electrolyzer parks (CN-primary)

- **Product:** DC skids between rectifier and stacks: per-stack isolation/hot-swap,
  active current-share balancing, stray/shunt-current mitigation, per-stack telemetry;
  sold to EPCs/owners as balance-of-plant. Sells no stacks (respects L11 overcapacity
  finding); deliberately complementary to C-07-class rectifier retrofits.
- **Buyer + pain (CN):** parks deploy dozens of sets per site (Uxin Banner 24-set/LONGi,
  L11-050; CEC 125-set tender, L11-051) and run below nameplate under renewable-following
  operation (Kuqa ~20→51% utilization episodes, L11-049); shunt/stray currents and
  per-stack imbalance are documented electrochemical-engineering problems (L11-012/013)
  that neither rectifier vendors nor stack OEMs own at park level.
- **Mechanism:** per-stack DC power management (isolation, balancing, telemetry) turning
  a monolithic DC bus into a managed array — the "string inverter moment" for hydrogen.
- **Why incumbents miss it:** rectifier vendors stop at the bus; stack OEMs stop at the
  flange; EPCs integrate but don't productize.
- **Not a duplicate:** Nearest survivor C-07 (low-ripple *rectification retrofit* —
  power-quality economics at the rectifier). F-15 is the *distribution and per-stack
  management layer downstream of any rectifier*, including retrofitted ones. Also
  distinct from C-22 (offline test benches).
- **Decisive experiment + budget:** HIL park model + 4-stack sub-array pilot showing >=3%
  utilization/specific-energy gain from balancing + isolation-enabled availability —
  $500k, 2028–29.
- **TRL:** 5. **2026–2029 plan:** park-level loss modeling on published Kuqa-type data →
  2028 CN EPC retrofit study partnership (engineering-services JV access path) → 2029
  sub-array pilot; Sungrow/LONGi verticalization monitored as the kill signal.
- **Named triggers 2030–2034:** CN — 15th FYP green-hydrogen consumption mandates and SOE
  performance audits forcing utilization retrofits at Kuqa-class parks (L11-049);
  successive Sinopec/CEC multi-set procurement rounds specifying park-level management
  (L11-050/051 cadence).
- **2030 competition:** Sungrow Hydrogen / LONGi vertical integration (the documented
  threat), Siemens/ABB BOP on export projects.
- **Window/access risk:** licensing/JV-only access to SOE parks; squeezed from both sides
  of the value chain.
- **Kill date:** 2034; kill triggers — Sungrow/LONGi-equivalent product before a 2031
  pilot, or no EPC partner by end-2030.
- **Big vision:** parks as managed stack arrays with degradation-weighted dispatch.
- **Nearest substitutes:** bigger rectifier blocks per stack; manual isolation switchgear.
- **Key uncertainty:** whether measured imbalance losses at real parks justify the skid
  cost (the 2028 study is the gate).
- **[FIX applied 2026-07-13 R2]:** 2028 EPC retrofit-study partnership made the binding demand gate (measured park losses must justify skid cost, >=3% gain target); Sungrow/LONGi verticalization kill retained; P4 must evidence a licensed JV winning park-management retrofit scope at one named SOE park; boundary coordination with C-07/F-23 codified - one L11 power story, at most two funded.

## P3R2-F-16 — Inline-metrology plasma surface treatment for PCB/advanced packaging (CN-primary)

- **Product:** Plasma cleaning/activation cell with built-in metrology: plasma-dose
  monitoring, inline surface-energy/contamination sensing, closed-loop "treat-to-spec"
  recipe control with lot traceability; premium position above commodity cleaners.
- **Buyer + pain (CN):** PCB/packaging makers already procure plasma cleaners by tender
  (Wuxi Shennan Circuit retender, L01-114) in a category proven durable globally (Nordson
  MARCH line inside an audited 10-K, L01-115); treatment is open-loop, so yield
  excursions surface downstream at bond/underfill — acute as CN advanced packaging
  densifies (equipment ecosystem growth, L01-044).
- **Mechanism:** couple plasma source control to inline surface-state sensing so the tool
  certifies its result, not its runtime.
- **Why incumbents miss it:** commodity cleaner makers compete on price (the B-15
  knife-fight); metrology integration is a systems problem outside their DNA.
- **Not a duplicate:** No survivor owns plasma surface treatment; the *rejected* B-15
  (mid-market CN plasma power) is the cautionary neighbor — this seed survives only as a
  metrology-differentiated premium tool, and says so.
- **Decisive experiment + budget:** lab cell with inline surface-energy proxy sensing,
  closed-loop treat-to-spec on contaminated coupons, downstream bond-strength correlation
  — $200k, 2027.
- **TRL:** 5. **2026–2029 plan:** sensor integration → 2028 beta at one CN PCB maker via
  the open tender channel (L01-114 proves the route) → 2029 yield-correlation dataset
  justifying >=30% premium. Direct equipment sales by a foreign vendor are routine in
  this category (access path).
- **Named triggers 2030–2034:** CN — packaging-substrate capacity build under 15th FYP
  electronics localization and AI-hardware substrate demand; recurring PCB-maker tenders
  with tightening traceability for automotive/high-reliability lines.
- **2030 competition:** Nordson MARCH (L01-115), Panasonic/Samco (JP), low-cost CN
  cleaner makers (the commodity floor).
- **Window/access risk:** commodity price war erodes any premium that metrology fails to
  defend — the 2030 premium test is the gate.
- **Kill date:** 2034; kill trigger — beta fails to justify >=30% premium by end-2030.
- **Big vision:** surface state as a controlled, logged process variable across
  electronics manufacturing.
- **Nearest substitutes:** commodity plasma cleaners + offline dyne/contact-angle QC.
- **Key uncertainty:** robustness of inline surface-energy proxies at production speed.
- **[FIX applied 2026-07-13 R2]:** 2028 beta must carry a PAID premium commitment (>=30% premium thesis tested before the 2030 gate, not at it); 2027 experiment must validate inline surface-energy proxy robustness at line rate; P4 Nordson MARCH/Panasonic/Samco roadmap check (closed-loop treat-to-spec is absorbable by the incumbent premium tier).

## P3R2-F-17 — Active safety-interlock modules for handheld laser welders (CN-primary)

- **Product:** Drop-in safety module: workpiece return-path sensing, capacitive
  body-proximity detection, sub-millisecond beam-disable chain with certified
  diagnostics; the compliance dossier (ISO 11553/IEC 60825 mapping + anticipated
  revisions) is as much the product as the hardware.
- **Buyer + pain (CN):** handheld laser welding exports are exploding (Raycus handheld
  units +66.22% in 2025, L12-038) while the governing standard (ISO 11553-2) still dates
  to 2007 (L12-050); the price war (Han's high-power revenue −6.6% on +30.5% units,
  L12-037) makes safety a purchasable differentiator rather than an in-house project.
  OEM design-in licensing is the access path.
- **Mechanism:** Class-4 beam control tied to human-presence and circuit-continuity
  sensing with a certified sub-ms disable chain — safety-PLC discipline shrunk into a
  tool.
- **Why incumbents miss it:** OEMs race on price; generic safety-PLC vendors don't build
  laser-tool-specific sensing; standards bodies move slower than the product class.
- **Not a duplicate:** No survivor is close; C-13 (laser-diode drivers) shares the laser
  industry only. New territory (photonics safety).
- **Decisive experiment + budget:** prototype sensing + <1 ms disable on a 1.5 kW
  handheld welder, third-party-witnessed hazard-scenario matrix — $150k, 2027.
- **TRL:** 4. **2026–2029 plan:** prototype + human-factors testing → 2028 standards
  committee engagement (ISO 11553-2 revision window) + one CN OEM design-in LOI → 2029
  certification-body architecture assessment.
- **Named triggers 2030–2034:** CN — export-market access defense: anticipated EU/US
  enforcement or revised ISO/IEC requirements on handheld Class-4 tools forcing OEM
  redesign purchases (standards-lag evidence L12-050/048/049).
- **2030 competition:** OEM in-house circuits; Pilz/Sick-class safety vendors entering
  sideways (judgment).
- **Window/access risk:** demand is contingent on regulatory tightening that is plausible
  but not yet dated — an explicitly priced option purchase with tiny pre-company cost.
- **Kill date:** 2034; kill trigger — no standards-revision signal or OEM design-in by
  end-2030.
- **Big vision:** the safety-silicon of industrial lasers.
- **Nearest substitutes:** passive PPE + training; OEM basic interlocks.
- **Key uncertainty:** timing of enforcement/standards revision (the entire demand
  thesis).
- **[FIX applied 2026-07-13 R2]:** held as a priced option - pre-company spend capped at the $150k prototype until a dated signal exists; 2028 gate: documented ISO/IEC revision work-item, EU/US market-surveillance action on handheld Class-4 welders, or insurer/OEM requirement (one of three, else kill at end-2030); P4 chases European welding-association handheld-laser safety materials for an eligible dated anchor; OEM design-in LOI remains the second gate.

## P3R2-F-18 — sCO2 retrofit "electrical island" packages for the CNNC sintering ecosystem (CN-primary; option/merge candidate)

- **Product:** Licensed electrical-island package for 15–30 MW sCO2 waste-heat retrofit
  units: generator-converter spec, protection/grid interface, commissioning toolkit,
  operator training — delivered via license/JV to CN EPC partners.
- **Buyer + pain (CN):** Chaotan One proved the retrofit commercially (30 MW, ~50% more
  net power than steam WHR, L04-048); the pipeline is framed at RMB ~100B (single-source,
  flagged, L04-051) but retrofit engineering capacity is concentrated in one CNNC
  institute team — serial rollout will be EPC-capacity-constrained, and the electrical
  island is the standardizable half.
- **Mechanism:** standardized electrical/grid-interface package making each retrofit a
  ~12-month project instead of a bespoke build.
- **Why incumbents miss it:** the institute team optimizes cycle technology, not rollout
  industrialization; Chinese electrical OEMs will absorb this scope eventually — the
  window is the rollout ramp.
- **Not a duplicate:** Nearest neighbors C-08/C-19 (thermal-mechanical components) and
  sibling F-03 (merchant cartridge). F-18 is the CN-primary *plant-integration licensing*
  variant; the orchestrator may merge it into F-03's CN chapter — flagged as an
  option/merge candidate.
- **Decisive experiment + budget:** validated reference design benchmarked on Chaotan One
  public data + STEP/KAERI analogs; one CN EPC co-bidding memorandum — $150k, 2028–29.
- **TRL:** 6 (engineering package). **2026–2029 plan:** architecture reconstruction →
  2028 EPC partnership development outside the CNNC core → 2029 package v1 aligned to
  Xinjiang first-set learnings (completion ~2028, L04-051).
- **Named triggers 2030–2034:** CN — post-2028 serial sintering-retrofit procurement
  following Xinjiang "first (set) major technical equipment" completion, under steel
  dual-carbon targets in the 15th FYP cycle (L04-048/051).
- **2030 competition:** CNNC institute as prime; Shanghai Electric/Dongfang-class OEMs
  absorbing the island scope.
- **Window/access risk:** foreign IP in a state-led program is fragile; single-source
  TAM.
- **Kill date:** 2034; kill triggers — no serial retrofit tenders by end-2031 or no EPC
  license by end-2032.
- **Big vision:** the retrofit playbook that ports sCO2 waste-heat power to global
  steel/cement.
- **Nearest substitutes:** CNNC in-house rollout; conventional steam WHR upgrades.
- **Key uncertainty:** whether serial tenders materialize outside CNNC's own channel.
- **[Adjudication 2026-07-13 R2 - MERGED INTO P3R2-F-03]:** self-flagged CN-primary licensing variant of F-03's cartridge (same CNNC ecosystem, same single-source TAM). EPC co-bidding memorandum, Xinjiang first-set alignment, and rollout-industrialization framing imported into F-03's CN chapter. Record retained as audit trail; not independently promotable.

## P3R2-F-19 — In-service coolant-health monitoring & conditioning for liquid-cooled AI fleets (dual US+CN; datacenter-dependent 1/4)

- **Product:** Side-stream skid per cooling loop: continuous chemistry/particulate/
  bio/wear-metal sensing plus automated dosing/filtration, fleet analytics, and
  spec-compliance reporting mapped to OCP and T/CIEP requirements; consumables +
  telemetry model.
- **Buyer + pain per market:** US — liquid-cooled fleets are entering service at scale
  (Vertiv liquid-cooling orders +50%, $15B backlog, L14-048; Deschutes-class CDUs from 7+
  vendors, L14-043) governed by installation specs with no multi-year coolant-operations
  layer (OCP fluid specs exist, L14-041). CN — GB 40879 PUE acceptance (L14-035) and
  T/CIEP 0263-2025 (L14-039) create audit/renewal events that coolant condition can fail;
  the debunked "100% liquid-cooling mandate" is deliberately NOT relied on (L14-036
  primary-text finding respected).
- **Mechanism:** water-treatment discipline (side-stream sensing + correction) rebuilt
  fleet-native for PG25-class DLC fluids, with cross-fleet failure-signature learning.
- **Why incumbents miss it:** CDU vendors sell hardware, fluid vendors sell fluid; the
  in-service chemistry-operations layer is orphaned between them.
- **Not a duplicate:** Nearest survivor C-05 (thermal *test/metrology benches* for
  qualification, incl. absorbed fluid-qual rigs). F-19 is the *always-on operations
  subsystem plus consumables* in production halls — different product, buyer motion, and
  revenue model; complementary to C-05's lab role. Flagged for the judge to confirm the
  boundary.
- **Decisive experiment + budget:** 12-month accelerated-aging loop across three
  commercial coolants; failure-signature library + side-stream correction efficacy —
  $300k, 2027–28.
- **TRL:** 6. **2026–2029 plan:** aging studies → 2028 colocation pilot → 2029 fleet
  analytics MVP + operator LOI; CN route via licensed manufacture with a domestic thermal
  vendor (Envicool-class, L14-043).
- **Named triggers 2030–2034:** US — warranty/insurance requirements after the first
  coolant-driven outages in 2028–2031 fleets (installed-base scale per L14-048). CN — GB
  40879 acceptance renewals and T/CIEP operational audits (L14-035/039).
- **2030 competition:** CDU vendors adding sensors (Vertiv/Motivair-class,
  L14-047/045), fluid suppliers bundling service (GS Caltex, L14-049), water-treatment
  majors entering sideways — crowded by 2032; dataset + speed are the defenses.
- **Window/access risk:** explicitly datacenter-capex-correlated (counted against the
  cap); maintenance demand is partially downturn-resistant since installed fluid ages
  regardless.
- **Kill date:** 2034; kill trigger — CDU vendors bundle equivalent monitoring as
  standard before a 2030 design win.
- **Big vision:** the water-treatment industry of the AI era, with the coolant "blood
  test" standard as the moat.
- **Nearest substitutes:** periodic manual fluid sampling; CDU-integrated basic sensors.
- **Key uncertainty:** direct atlas evidence of coolant-failure pain is thin (inference
  from spec structure + fleet scale); P4 must source operator incident/warranty data.
- **[FIX applied 2026-07-13 R2]:** P4 must source operator incident/warranty data (pain evidence is inference from spec structure + fleet scale); 2028 colocation pilot + operator LOI made binding; the 12-month aging study must produce the failure-signature dataset that IS the moat (else a CDU-vendor feature - bundling kill stands); C-05 boundary confirmed: pair commercially, do not merge prematurely. Counted 1/4 against the datacenter cap.

## P3R2-F-20 — Merchant precision HV DC modules (50–300 kV) for beam-tool OEMs (dual US+CN)

- **Product:** Modular HV platform: oil-free solid-state multipliers, active ripple
  cancellation, arc-quench with <10 ms full-spec recovery, integrated HV telemetry;
  50–300 kV / 10–100 kW classes with a published acceptance protocol.
- **Buyer + pain per market:** US — SiC-implant capacity expansion (Axcelis/Wolfspeed,
  L06-041) and cargo/NDT source growth (Varex +25% industrial quarter, >$55M cargo
  orders, L05-033) stress a merchant HV base that has consolidated to effectively one
  dominant vendor (Spellman — judgment, P4 to source); qualification leans on generic IEC
  60060 practice (L05-043). CN — CGN Dasheng accelerator capacity additions per municipal
  EIA cadence (L05-038; order growth per its H1-2025 filing L05-035, figures flagged for
  P4 re-extraction) and cyclotron-center tenders (L05-036).
- **Mechanism:** solid-state HV generation with active ripple cancellation and
  arc-event-learning telemetry — reliability engineering where incumbents ship legacy
  topologies.
- **Why incumbents miss it:** a near-monopoly has little pressure to re-architect; tool
  OEMs hate single-sourcing but have no alternative to qualify.
- **Not a duplicate:** Nearest survivor C-09 (pulsed modulators) — this is precision *DC*
  HV, a different product class; D-08 (sterilization machines) is a downstream customer
  category, not a competitor.
- **Decisive experiment + budget:** 100 kV/10 kW module: <10 ppm ripple, arc-quench with
  <10 ms recovery, 1,000 h burn-in telemetry — $350k, 2027–28.
- **TRL:** 5. **2026–2029 plan:** prototype → 2028 two OEM evaluations (one US tool OEM,
  one accelerator lab) → 2029 reliability database + acceptance-protocol publication; CN
  channel via non-controlled-application counsel.
- **Named triggers 2030–2034:** US — SiC fab-equipment cycles (L06-041) and
  cargo-scanning upgrade programs (L05-033). CN — CGN Dasheng expansion cadence
  (L05-035/038) and CN accelerator localization tenders (L05-036 pattern).
- **2030 competition:** Spellman (dominant, will defend), Technix/Heinzinger, XP
  Power-class lines, CN HV makers scaling (judgment; P4 map).
- **Window/access risk:** if the incumbent's lead survives untouched this collapses to a
  niche lab-supply business.
- **Kill date:** 2034; kill trigger — no OEM design-in by end-2032.
- **Big vision:** the default precision-HV layer for the beam economy.
- **Nearest substitutes:** incumbent HV supplies; OEM in-house HV decks.
- **Key uncertainty:** OEM willingness to requalify a mission-critical component from a
  startup.
- **[FIX applied 2026-07-13 R2]:** P4 competitor map made a pre-promotion requirement (Spellman AND Advanced Energy HiTek/UltraVolt, AMETEK/Glassman, Matsusada, iseg, Heinzinger, Technix, XP Power, CN HV makers) - the one-dominant-vendor thesis must survive it; two PAID OEM evaluations by 2028 binding; CN chapter reduced pending a named CN OEM/tender channel in P4 (else license notes); pre-agreed fold-down into C-09's platform family if OEM appetite fails. Counted dual-conditional.

## P3R2-F-21 — Merchant HTS current leads & cryogenic feedthroughs (dual US+CN; option/fold candidate)

- **Product:** Catalog binary current leads (0.5–20 kA): optimized copper + REBCO stages,
  vacuum-tight instrumented feedthroughs (integrated taps/sensors), published heat-load
  and quench-tolerance data. Complements F-02 and D-01-class protection.
- **Buyer + pain per market:** US — merchant magnet commerce (CFS→Realta/WHAM, L03-035)
  turns leads from lab craft into purchased components; cryocooler capacity is the scarce
  resource leads consume (10 mW at 2.5 K per 1.1 kW input, L03-050). CN — domestic REBCO
  systems build-out (Shanghai Superconductor, L03-041/052) and ASIPP magnet-power tender
  cadence (L01-037/038) via big-science procurement routes.
- **Mechanism:** thermal-electrical optimization + instrumentation integration under one
  certification methodology.
- **Why incumbents miss it:** every lab builds its own; tape vendors bundle
  half-heartedly; no one publishes certified heat-load data.
- **Not a duplicate:** Nearest survivors E-04 (cryo *signal* I/O for quantum — different
  function/market) and C-12 (cryoplants — the capacity leads consume). No survivor sells
  power leads. Honestly flagged: likely folds into F-02 as the entry SKU.
- **Decisive experiment + budget:** 5 kA binary lead: heat load within 10% of model,
  vacuum integrity over 50 thermal cycles, taps validated during driven quench — $200k,
  2027–28.
- **TRL:** 5. **2026–2029 plan:** optimization models → 5 kA instrumented prototype with
  a university magnet group → 2029 certification methodology + first lab POs.
- **Named triggers 2030–2034:** US — DOE milestone-program follow-on and merchant-magnet
  order growth (L03-032/035). CN — REBCO capacity build (L03-052) and big-science magnet
  tenders (L01-037/038).
- **2030 competition:** lab in-house, tape vendors bundling, specialty cryo shops
  (judgment).
- **Window/access risk:** small standalone TAM — the honest ceiling.
- **Kill date:** 2034; standalone kill at end-2031 if <$1M cumulative orders (then fold
  into F-02).
- **Big vision:** the standard cryogenic power connector of the superconducting economy.
- **Nearest substitutes:** in-house lead builds; vapor-cooled legacy designs.
- **Key uncertainty:** whether magnet vendors bundle leads with magnets by default.
- **[Adjudication 2026-07-13 R2 - MERGED INTO P3R2-F-02]:** self-flagged fold. Catalog binary-lead SKU, instrumented feedthroughs, certified heat-load datasheets, and the end-2031 <$1M standalone milestone imported into F-02 as its entry SKU + gate. Record retained as audit trail; not independently promotable.

## P3R2-F-22 — Second-source vacuum variable capacitors + fast tuning components (dual US+CN)

- **Product:** Qualified vacuum variable capacitor line (10–2,000 pF, 5–30 kV) plus
  solid-state tuning elements, built with modern brazing/bellows automation; merchant
  sales to US/EU OEMs, licensed assembly for CN mature-node ecosystems.
- **Buyer + pain per market:** US — matchbox/generator OEMs carry single-source exposure
  on the tuning element of every matchbox; the incumbent itself reports 23.8%
  single-customer concentration (Comet, L05-034), evidencing a brittle supply
  structure both directions. CN — generator entrants localize systems but import the
  capacitor layer (component localization <12%, L06-054; buyers Hengyunchang/Injet,
  L06-042/043/044).
- **Mechanism:** precision ceramic-metal brazing + bellows manufacturing modernized; dual
  track with solid-state tuning elements hedges the technology transition (bridge to
  F-01).
- **Why incumbents miss it:** a profitable near-monopoly has no incentive to create its
  own second source; entrants fear the craft barrier — which is the moat once crossed.
- **Not a duplicate:** Nearest sibling F-01 (solid-state *matching systems*); F-22 is the
  *component layer* (and its solid-state successor elements). No survivor touches it.
- **Decisive experiment + budget:** 12 kV/1,000 pF capacitor life-tested to incumbent
  datasheet limits (Q, current, cycle life) with third-party witness — $450k, 2028.
- **TRL:** 4. **2026–2029 plan:** process development with a vacuum-components partner →
  2028 first family qualification → 2029 OEM second-source evaluations; CN licensing
  scoped with export counsel.
- **Named triggers 2030–2034:** US — OEM dual-sourcing mandates as RF platforms mature
  (L06-039/040). CN — component-localization programs targeting the RF gap under
  15th/16th FYP cycles (L06-054).
- **2030 competition:** Comet defending its core; Jennings legacy; CN startups attacking
  the same gap.
- **Window/access risk:** if solid-state matching (F-01-style) wins fast, the vacuum-cap
  market shrinks — hence the dual-track design.
- **Kill date:** 2034; kill trigger — qualification lags incumbent-equivalent specs at
  end-2030.
- **Big vision:** own the tuning-component layer across both matching eras.
- **Nearest substitutes:** incumbent capacitors; frequency-tuning generator architectures.
- **Key uncertainty:** manufacturing yield economics of precision vacuum brazing at
  startup scale.
- **[FIX applied 2026-07-13 R2]:** vacuum-components manufacturing-partner route made a binding 2027 gate (the $450k experiment does not make a qualified line); one PAID OEM qualification by 2029; P4 must map CN vacuum-capacitor makers (credible domestic caps collapse the CN licensing leg) and verify the Comet/Jennings supply structure; portfolio pre-agreement: if F-01 and F-22 both survive P4 they merge into one RF-components company.

## P3R2-F-23 — PEM "protective operating envelope + warranty black-box" controllers (dual US+CN)

- **Product:** Embedded controller between plant control and stack: enforces
  manufacturer-agnostic protective envelopes (ramp shaping, OCV-rest management, ripple
  guards), logs tamper-evident stress histories, issues warranty-compliance
  certificates; sold to OEMs, developers, and financiers.
- **Buyer + pain per market:** US — H2Hub developers/financiers price unknown degradation
  into project debt (up to $2.2B committed across two hubs, L11-032) while the industry
  still cannot attribute degradation to specific stresses (L11-001/003/004/031); Plug's
  named deployments carry warranty exposure (L11-046). CN — Kuqa demonstrates
  renewable-following underperformance (L11-049) across parks built by LONGi/Peric/
  Sungrow (L11-050/051); access via OEM design-in.
- **Mechanism:** codify published stress-degradation maps into real-time envelope
  enforcement + notarized logging — converting degradation science into bankable
  evidence.
- **Why incumbents miss it:** stack OEMs won't self-police warranties; DCS vendors lack
  electrochemical depth; test companies stay offline.
- **Not a duplicate:** Nearest survivor C-22 (degradation-truth *test benches* +
  financier datasets — offline infrastructure). F-23 is the *always-on plant device*
  producing per-asset evidence; scoped to stay complementary (C-22 calibrates the maps
  F-23 enforces). Also distinct from C-07 (rectifier hardware upstream).
- **Decisive experiment + budget:** short-stack A/B: envelope-protected vs naive
  renewable-following over 2,000 h, measurable degradation-rate reduction + audit-grade
  logging — $300k, 2028.
- **TRL:** 5. **2026–2029 plan:** envelope algorithms from published maps → bench
  validation → 2029 one OEM/developer LOI (US) + one CN OEM design-in discussion;
  coordinate scope with C-22.
- **Named triggers 2030–2034:** US — H2Hubs Phase-2 construction transitions forcing
  lender technical requirements (L11-032). CN — utilization audits at Kuqa-class parks
  and lifetime-guarantee clauses in successive multi-set procurement rounds
  (L11-049/050/051).
- **2030 competition:** stack-OEM in-house monitoring, DCS vendors, C-22-class testers
  extending online; feature absorption is the threat, notarized-evidence-for-financiers
  the defense.
- **Window/access risk:** hydrogen FID depression (documented Western order-book
  contraction) can starve volume; the same device retargets battery/fuel-cell warranties.
- **Kill date:** 2034; kill trigger — no OEM/financier adoption commitment by end-2032.
- **Big vision:** bankability hardware for electrochemical assets — cross-fleet
  degradation actuarial tables.
- **Nearest substitutes:** OEM BMS-equivalents; contractual (non-instrumented)
  warranties.
- **Key uncertainty:** whether envelope enforcement demonstrably reduces degradation
  enough to move warranty/debt pricing.
- **[FIX applied 2026-07-13 R2]:** binding 2029 gate added (named H2Hub lender/financier technical requirement or developer LOI referencing instrumented warranty evidence, plus one OEM design-in agreement); the 2,000 h A/B experiment made the binding existence proof (measurable degradation-rate reduction); data-interface pre-agreement with C-22 (no duplicate bench); battery/fuel-cell retarget hedge scoped (not asserted) by 2029.

---

Generic EE/CE transfer note (appended after seed freeze): across all 23 seeds the
recurring transferable pattern is classical electrical/control engineering — precision
power conversion, protection, impedance/thermal management, and instrumented
qualification — applied as the standardizing layer inside someone else's scaling
industry.
