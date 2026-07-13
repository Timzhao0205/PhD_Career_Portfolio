# P3R2 Batch D — Frontier Energy/Physics Wildcards (20 seeds, generated 2026-07-13)

Generator: Fable 5 (claude-fable-5) / xhigh. Inputs: repaired ATLAS.md, lane briefs L01–L16 with
P2A repair sections, INDIA_SOURCE_ORIGIN_AUDIT.md (42 excluded IDs). Every cited ID was verified
in `90_BIBLIOGRAPHY/sources.json` as `accepted: true` with an eligible `india_origin_audit`
status; candidate IDs found rejected (L08-016, L03-053, L09-036, L12-052, L14-047, L15-044) were
NOT cited and claims were adjusted accordingly. SEEDS_A–D drafts were not read or reused.
Geography: US/CN primary only; JP/TW/KR appear only as side markets; India and Singapore excluded.
Company launch year: 2030. All physics claims separate Evidence / Calculation / Judgment.


> **Adjudication applied 2026-07-13:** the independent elegance/novelty verdicts (`P3R2_ELEGANCE_ADJUDICATION.md`) have been applied to every seed below - PROMOTE/FIX_APPLIED/MERGED/REJECT annotations appear at the end of each seed section and in the batch JSON (`elegance_verdict` fields). See `P3R2_FIX_APPLICATION_LOG.md`.

---

## P3R2-D-01 — QuenchGuard: merchant quench detection + protection for HTS magnets

- **Product:** Retrofittable safety subsystem for REBCO magnets: distributed Rayleigh-backscatter
  fiber co-wound in the coil plus RF/acoustic hotspot channels, fused in a deterministic FPGA
  trigger that fires a qualified multi-kV energy-extraction (CLIQ-class) dump. Sold with a
  qualification dossier, not as a lab curiosity.
- **Buyer + pain evidence:** Fusion magnet builders and labs. HTS quench detection is unsolved at
  multi-tesla/multi-MJ scale; builders choose between no-insulation windings (poor ramp control)
  and unproven detection (L03-004, L03-018); strain/screening-current degradation compounds the
  certification problem (L03-020, L03-021). Buyers with money: DOE milestone fusion program
  ($415M authorized, L03-032), CFS selling magnets to third parties (L03-035), Tokamak Energy's
  $335M program (L03-033).
- **Technical mechanism + physics red-team.** *Evidence:* HTS normal zones propagate ~cm/s vs m/s
  in LTS, so voltage taps see microvolts against inductive noise — the detection failure mode is
  documented physics, not engineering sloppiness (L03-004, L03-018). *Calculation:* a 20 T-class
  TF coil stores 10–100 MJ; at 10 ms detection + 100 ms dump into an external resistor, hotspot
  temperature stays under ~200 K for typical Cu fraction; Rayleigh fiber interrogation gives
  ~1 cm spatial / ~kHz frame rates over ~100 m per interrogator, so a full coil needs multiplexed
  interrogators — a cost, not a physics, problem. *Judgment:* fusing fiber strain/temperature
  precursors with RF/acoustic emission can buy the needed 100 ms; the moat is the qualification
  data set, since no physics here is proprietary. *Red-team:* fiber survivability during winding
  and under 10^19 n/m2-class fluence in fusion service is the honest open question; energy
  balance of the dump path is standard engineering.
- **Why incumbents miss it:** magnet builders treat protection as an internal cost center and
  keep re-inventing it per project; instrumentation vendors sell sensors, not protection power
  electronics; CERN-lineage CLIQ was tuned for LTS.
- **Decisive experiment + budget:** co-wound fiber + RF pickup on a 1–2 T REBCO double-pancake,
  controlled quenches, >=100 ms warning with <1% false triggers — $250k, 2027, university magnet lab.
- **TRL:** 3.
- **2026–2029 plan:** university lab access + instrumented pancakes (2026-27); DOE SBIR/INFUSE
  grants with a fusion partner and controlled-quench campaigns (2027-28); multi-kA coil demo and
  frozen v1 architecture + qualification plan (2029). No operating company assumed.
- **2030–2034 trigger (named):** post-SPARC pilot-plant magnet builds (CFS ARC-class; ST80-HTS
  follow-on) and the DOE Milestone Program re-authorization decision after FY2027 (L03-032);
  CFETR procurement (L03-024) is upside only.
- **2030 competition:** in-house teams at CFS/TE Magnetics (L03-035, L03-044); national-lab
  one-offs; no merchant vendor in the atlas.
- **Window/timing risk:** NI windings proving "good enough" at pilot scale; a builder
  open-sourcing its solution.
- **Kill date:** 2033-12 if no method demonstrates reliable sub-100 ms pre-quench warning at
  >10 T on full-scale coils.
- **Big vision:** the certification-grade protection layer for every high-field HTS magnet in
  fusion, NMR, accelerators, and industry.
- **Nearest substitutes:** voltage taps + co-wound wire, NI winding passivity, in-house CLIQ.
- **Key uncertainty:** radiation- and winding-survivable fiber packaging; buyer willingness to
  outsource a safety-critical function.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical quench detection/protection. Falsifiable 2027 experiment; honest NI-winding substitution risk. Absorb A-04 protocol framing, E-07 precursor-dataset moat + KEPCO/LS side market; CN only if counsel clears. 2026-07-13: absorbed A-04 (acceptance-test protocol / warranty framing for merchant magnet sales; multi-modal sensing sources L03-005/006/007/008), C-17 (CN ASIPP/CFETR chapter - documented as license-out-only, counsel-gated; china_beachhead stays false), and E-07's protection half (precursor-dataset moat + KEPCO/LS cable-monitoring side market; its QA-bench half went to D-02).

## P3R2-D-02 — TapeMap: reel-to-reel REBCO quality metrology

- **Product:** 77 K contactless critical-current and defect mapping — dense Hall-sensor array plus
  lock-in thermography — at m/s reel-to-reel speed, plus coil/cable acceptance heads; certified,
  buyer-trusted quality maps in a shared data format.
- **Buyer + pain evidence:** tape vendors and magnet builders. Under 10 vendors supply the world
  and one fusion order absorbs a meaningful share of annual output (L03-003, L03-019);
  strain/delamination/screening-current degradation makes buyers over-specify and re-test
  (L03-018, L03-020, L03-021); Furukawa's several-hundred-km supply deal shows the volumes at
  stake (L03-044). CN path: Shanghai Superconductor's domestic capacity buildout (L03-052) and
  CFETR's magnet program (L03-024) — metrology tools are a lower-export-risk product class than
  magnets themselves (judgment).
- **Technical mechanism + physics red-team.** *Evidence:* magnetization (remanent-field) scanning
  of coated conductors is established lab physics; degradation modes are position-localized
  (L03-018, L03-020). *Calculation:* a 100 µm-pitch Hall array at 1 m/s and 10 kHz sampling
  resolves mm-scale dropouts on 12 mm tape; inverting the Biot–Savart kernel from remanent field
  to local Jc is a well-conditioned 1D deconvolution at this geometry; correlation to transport
  Ic should reach a few percent. *Judgment:* the hard part is industrial calibration discipline,
  not physics. *Red-team:* remanent-field methods measure self-field Ic at 77 K, not in-field Ic
  at 20 K — the product must ship validated transfer functions, or magnet builders will discount
  the data; this transfer function is the real R&D.
- **Why incumbents miss it:** vendors run in-house scanners whose data buyers do not trust as
  acceptance evidence; no neutral-referee instrument with a shared reporting format exists
  (bespoke acceptance negotiation is the documented norm).
- **Decisive experiment + budget:** benchtop reel-to-reel scan of 100 m commercial tape;
  blind-correlate predicted vs transport Ic on 50 samples to <5% — $120k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** benchtop rig and published correlation study (2026-27); NRE-funded pilots
  with one magnet builder + one vendor (2027-28); inline-speed prototype and open
  acceptance-report schema (2029).
- **2030–2034 trigger (named):** ARC-class and ST80-HTS-class tape procurement waves (L03-044,
  L03-033), Chinese domestic REBCO expansion (L03-052), CFETR if it opens (L03-024).
- **2030 competition:** vendor in-house systems (THEVA Tapestar-class — judgment), lab
  instruments; no merchant acceptance-metrology vendor in the record set (L03-046, L03-052
  document the supplier landscape).
- **Window/timing risk:** exclusive capture by the largest vendor; "good-enough" vendor data.
- **Kill date:** 2034-06 if no vendor or builder adopts third-party acceptance metrology
  commercially.
- **Big vision:** the KLA of superconductors, closing metrology into deposition process control.
- **Nearest substitutes:** in-house Tapestar-class scanners, destructive sample testing.
- **Key uncertainty:** whether 77 K self-field maps predict 20 K in-field performance well enough
  to change purchasing behavior.
- **[Adjudication 2026-07-13 - PROMOTE]:** Best instrument seed in pool; demand scales with conductor volume not fusion success (low-beta). Absorb C-11 cable acceptance stations + insurer packages, B-10 passport framing + CN buyers, E-07 QA-bench half. 2026-07-13: absorbed C-11 (cable/CICC acceptance stations, financier/insurer data packages), B-10 (conductor-passport framing + CN buyer set: WST, ASIPP), and E-07's QA-bench half (conductor/joint benches, Furukawa/Fujikura JP channel). China leg already primary (US+CN, china_beachhead true) and strengthened with eligible CN evidence (L03-041/029/037/031) - flags unchanged.

## P3R2-D-03 — Mid-scale 20 K turbo-Brayton cryoplant skid

- **Product:** containerized 0.5–2 kW @ 20 K turbo-Brayton refrigerator (gas-bearing turboalternator,
  neon/helium), catalog-priced, automated, with an optional 4.5 K stage — the missing tier between
  10 mW catalog cryocoolers (L03-050) and JT-60SA-class bespoke plants (~9.5 kW @ 4.5 K, L03-025/026).
- **Buyer + pain evidence:** mid-scale magnet/cable programs that cannot justify a bespoke helium
  plant (documented capability gap, L03-025, L03-026, L03-050); HTS cable demonstrators explicitly
  pairing turbo-Brayton cryogenics with cables (SupraMarine, L03-034); ITER's helium supply
  contracting shows big-science cryogen logistics cost (L07-041); KEPCO/LS AI-datacenter
  superconducting grid is the KR side-market (L03-043).
- **Technical mechanism + physics red-team.** *Evidence:* turbo-Brayton machines exist at space
  (W-class) and LNG (MW-class) scales; the 0.5–2 kW @ 20 K product point is unserved in the atlas
  record set. *Calculation:* Carnot ratio at 20 K is ~14; at 30% of Carnot, 1 kW @ 20 K needs
  ~47 kW electric — a rack-scale power draw, fine for labs and cable vaults. Operating at 20 K
  instead of 4.5 K cuts input power ~4–5x, which is exactly why REBCO systems want this tier.
  *Judgment:* componentry (gas bearings, high-speed alternators) is mature enough to integrate;
  the risk is manufacturing cost, not physics. *Red-team:* incumbents (Air Liquide, Linde —
  judgment) could descend into this niche; development capital for turbomachinery is real; 4.5 K
  option re-introduces the hard regime and should not gate v1.
- **Why incumbents miss it:** industrial-gas majors sell engineered projects, not catalog skids;
  cryocooler vendors are stuck at watt scale; the mid-market is too small for the former and too
  big for the latter — classic orphan tier.
- **Decisive experiment + budget:** 100 W @ 20 K closed-loop subscale with gas-bearing
  turboalternator, %Carnot and 1,000 h unattended run — $400k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** FEED + vendor quotes, DOE SBIR, national-lab CRADA (2026-27); subscale loop
  (2027-28); 500 W engineering unit on a borrowed HTS load with availability data (2029).
- **2030–2034 trigger (named):** fusion component test-stand buildout after the DOE milestone
  FY2027 renewal (L03-032); SupraMarine-class cable deployments post-2028 testing (L03-034);
  KEPCO/LS-type datacenter feeders (L03-043, side market).
- **2030 competition:** Air Liquide/Linde (top-down, judgment), Cryomech/Sumitomo cluster
  configurations (L03-050), Stirling vendors.
- **Window/timing risk:** if HTS deployment disappoints, the tier stays orphaned; incumbents
  react fast once volume is proven.
- **Kill date:** 2034-06 without a signed lead customer for the 500 W-class unit.
- **Big vision:** 20 K as a utility — packaged cryogenic power for the HTS buildout.
- **Nearest substitutes:** cryocooler arrays, LN2-precooled single-stage systems, bespoke plants.
- **Key uncertainty:** manufactured cost at low initial volume vs cryocooler-array workarounds.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-12]:** Import catalog-price/6-month-lead-time product definition into C-12. Record retained as audit trail.

## P3R2-D-04 — Cryo-busway: superconducting fault-current-limiting MVDC feeder for AI campuses

- **Product:** factory-built 10–50 MW cryogenic DC feeder modules: REBCO conductor in rigid
  cryostat busway whose engineered quench resistance inherently limits fault current, integrated
  20 K cryo-loop, OCP-compatible terminations. A repeatable product, not a utility project.
- **Buyer + pain evidence:** hyperscale campus developers moving to 800VDC racks and MVDC
  backbones (NVIDIA 800VDC ecosystem, L02-043; OCP Mount Diablo, L02-044) while DC fault
  interruption remains the documented "showstopper" (hybrid/solid-state breakers immature:
  L08-001, L08-003, L08-004); datacenter electrification demand is booked in billions per quarter
  (GE Vernova, L08-033). Technical precedent: Shanghai 35 kV HTS cable in commercial operation
  since 2021 (L03-041) and State Grid SFCL prototypes (L03-011, L03-013); KEPCO/LS AI-datacenter
  superconducting grid MOU (L03-043) is the side-market echo.
- **Technical mechanism + physics red-team.** *Evidence:* superconducting fault-current limiting
  is demonstrated at grid pilots (L03-011, L03-013, L03-041). *Calculation:* a 25 MW feeder at
  ±10 kV carries 1.25 kA/pole — comfortable REBCO territory; on a bolted fault the tape's normal-
  state resistance (engineered via stabilizer fraction) limits prospective 10x faults to <2x within
  ~1 ms, letting a cheap mechanical disconnect open at near-zero current; cryostat heat load
  ~1–2 W/m at 20 K means a 500 m corridor needs ~1 kW cryo — one D-03-class skid. *Judgment:* the
  buyer that makes HTS finally repeatable is the private-wire campus owner, not the utility —
  short runs, dense power, no regulatory rate case. *Red-team (honest):* the atlas's negative
  finding stands — no repeat third-party commercial HTS cable orders exist (L03 adjudication);
  recovery-under-load after a quench is the known SFCL weakness and must be engineered (re-cool
  time vs redundancy); the default competitor is simply more copper at 800 V, which wins below
  ~10 MW per corridor. This is a wildcard with an explicit demand bridge, priced accordingly.
- **Why incumbents miss it:** cable incumbents sell utility projects with state sponsors; breaker
  vendors are trying to solve DC protection with semiconductors (L08-052) rather than making the
  conductor itself the protection element; datacenter electrical houses don't do cryogenics.
- **Decisive experiment + budget:** 10 m REBCO DC feeder at 20 K — inject 10x prospective fault,
  verify self-limiting <2x within 1 ms and recovery under 50% load within 10 s — $450k, 2028,
  national-lab HV facility.
- **TRL:** 4.
- **2026–2029 plan:** campus one-line studies + lab partnership (2026-27); 10 m fault-physics
  prototype (2027-28); 100 m pilot corridor at a colo/test microgrid with availability dossier (2029).
- **2030–2034 trigger (named):** gigawatt single-campus builds on the NVIDIA/OCP 800VDC-to-MVDC
  roadmap (L02-043, L02-044: 600 kW–1 MW racks from ~2027) and the GE Vernova-class datacenter
  electrification order supercycle (L08-033).
- **2030 competition:** LS Cable/KEPCO template (KR), Shanghai Superconductor (CN, L03-052), AMSC
  (L03-046), Hitachi-class hybrid breakers + copper (L08-052).
- **Window/timing risk:** solid-state breakers maturing faster than expected; campuses staying at
  LV DC; cryo-uptime culture clash.
- **Kill date:** 2033-12 if recovery-under-load and availability cannot be demonstrated to
  datacenter-grade (99.99%+) standards at pilot scale.
- **Big vision:** protection as a material property; zero-resistance campus backbones, then urban
  feeders.
- **Nearest substitutes:** parallel copper busway + fuses/hybrid breakers; 800 V distributed
  rectification.
- **Key uncertainty:** whether any hyperscaler will pilot cryogenics in production power paths
  this decade.
- **[Adjudication 2026-07-13 - REJECT]:** Elegant science without a credible buyer in-window: uptime-conservative hyperscalers will not adopt cryogenic distribution 2030-2034; atlas negative finding on HTS cable repeat orders applies a fortiori. Record retained as audit trail.

## P3R2-D-05 — Open-standard Marx bricks: the OCP of pulsed power

- **Product:** catalog 3 kV/1 kA solid-state Marx bricks with a published electrical/mechanical/
  controls interface spec, active droop-correction firmware, N+2 hot-swap; stacks configure from
  20 kV medical to 120 kV accelerator modulators under one test protocol.
- **Buyer + pain evidence:** at least five independent, non-interoperable solid-state modulator
  designs across labs/vendors with an explicit standardization gap (L05-003–L05-009) and no
  accelerator-specific pulsed-power test standard beyond IEC 60060 (L05-043); real purchases: ESS
  bought 18 modulators from one vendor (L05-030), CGN Dasheng signed RMB 340M in H1 2025 (L05-035,
  CN market proof), e-beam sterilization is backlogged (L05-028), cargo linacs growing +25%
  (L05-033); DOE funds the industrial base via ARDAP (L05-031).
- **Technical mechanism + physics red-team.** *Evidence:* IGBT Marx topology is proven at
  115 kV/100 A/3.5 ms class (L05-003, L05-030). *Calculation:* 40 bricks × 3 kV gives 120 kV with
  <1% droop via staggered-module PWM; N+2 redundancy at 98%/brick/year reliability yields >99.9%
  stack availability; brick BOM at scale is dominated by capacitors + IGBTs — commodity curves.
  *Judgment:* the innovation is institutional (an open interface standard backed by conformance
  testing), which incumbents structurally resist. *Red-team:* no physics risk; the risk is
  commoditization — ScandiNova could publish its own "standard" and outrun a startup; margins
  live in controls, conformance and the highest-spec bricks.
- **Why incumbents miss it:** ScandiNova/Jema sell closed cabinets (L05-047, L05-030); labs
  hand-roll one-offs; nobody profits today from interoperability, but buyers would (documented
  bespoke-acceptance pain, L05-043).
- **Decisive experiment + budget:** 10^8-pulse life test of one brick + 10-brick 30 kV stack with
  <0.5% flat-top and hot-swap under load — $200k, 2027.
- **TRL:** 5.
- **2026–2029 plan:** draft interface spec co-authored with two national labs (2026-27); stack
  demo + third-party acceptance test (2027-28); first paid retrofit of a PFN/thyratron modulator
  at a university accelerator (2029).
- **2030–2034 trigger (named):** EtO-replacement e-beam capacity build (L05-028), cargo-screening
  fleet growth (L05-033), lab modulator refit cycles (L05-030), ISO 11137-1:2025-driven
  revalidation (L05-042).
- **2030 competition:** ScandiNova (L05-047), Jema (L05-030), lab in-house.
- **Window/timing risk:** commoditization before standardization; mitigated only by early lab
  co-authorship.
- **Kill date:** 2033-12 without two external adopters of the interface spec.
- **Big vision:** own the conformance layer and premium bricks of a commoditized pulsed-power
  ecosystem.
- **Nearest substitutes:** closed-cabinet modulators, refurbished PFN/thyratron systems.
- **Key uncertainty:** whether buyers will specify an open standard against incumbent lobbying.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-09]:** The open-interface 'OCP of pulsed power' strategy must survive the merge into C-09; the standalone seed does not. Record retained as audit trail; not independently promotable.

## P3R2-D-06 — Rep-rated LTD bricks: pulsed power by the pallet

- **Product:** standardized 100 kV / 50–100 kA linear-transformer-driver cavity bricks with
  long-life solid-state/magnetically-assisted switching (>=10^6 shots), integrated trigger and
  diagnostics, factory acceptance data — sold by the module.
- **Buyer + pain evidence:** Sandia's LTD program explicitly targets modular, repetition-rated,
  Marx-replacing architectures for fusion and flash radiography (L05-018, L05-019, L05-044,
  L05-020); DOE funds the accelerator/pulsed-power industrial base (70 institutions, L05-031).
  Private magneto-inertial fusion developers are expected buyers by 2030 (judgment, labeled).
- **Technical mechanism + physics red-team.** *Evidence:* LTD cavities summing many parallel
  low-inductance bricks are demonstrated at Sandia (L05-018, L05-019). *Calculation:* a
  100 kV/100 kA brick stores ~50 kJ; at 1 Hz that is 50 kW average per brick — thermal management
  of switches and resistors is bounded and solvable with oil/water loops; switch life is the
  binding constraint: spark gaps erode in 10^3–10^4 shots, thyristor/IGBT stacks with magnetic
  assist plausibly reach 10^6–10^8 at these di/dt with derating. *Judgment:* 2020s semiconductor
  economics make solid-state LTD switching feasible where 2005-era attempts were not. *Red-team:*
  jitter (<10 ns across thousands of bricks), fault propagation in series stacks, and the honest
  market truth that today's buyer base is a handful of government labs; IFE demand is real only
  if private fusion programs survive to driver procurement.
- **Why incumbents miss it:** no company sells LTD bricks; Sandia builds in-house; modulator
  vendors (L05-047) stop at ~MW class; the niche is too weird for power electronics firms and too
  product-like for labs.
- **Decisive experiment + budget:** one 100 kV/50 kA brick, 10^5 full-energy shots at 0.5–1 Hz,
  switch degradation + jitter statistics — $350k, 2028, university pulsed-power lab.
- **TRL:** 3.
- **2026–2029 plan:** switch-lifetime physics program + NNSA/DOE SBIRs (2026-27); single-brick
  life demo (2027-28); 4-brick series stack with published reliability stats (2029).
- **2030–2034 trigger (named):** Sandia/NNSA next-generation pulsed-power (Z-successor) planning
  moving to hardware (L05-044 program lineage), flash-radiography recapitalization (L05-020), DOE
  ARDAP continuity (L05-031); private IFE drivers as upside (judgment).
- **2030 competition:** Sandia in-house, ScandiNova (adjacent, L05-047), CPI-class HV houses
  (L05-050), fusion startups' vertical integration.
- **Window/timing risk:** government-concentrated demand; a Z-successor slip strands the market.
- **Kill date:** 2033-06 if switch life <10^6 shots at full rating remains undemonstrated.
- **Big vision:** the supply chain for rep-rated pulsed fusion drivers and compact radiography.
- **Nearest substitutes:** conventional Marx banks, in-house lab builds.
- **Key uncertainty:** timing of any US next-generation pulsed-power procurement.
- **[Adjudication 2026-07-13 - REJECT]:** Government-concentrated, undated anchor procurement; seed's own line - 'the market is grants, not products' - decides it. Record retained as audit trail.

## P3R2-D-07 — Green RF: multi-stage depressed collector energy recovery

- **Product:** MSDC collector assemblies + adaptive gun/drive electronics, supplied to tube
  OEMs/rebuilders and labs at rebuild cycles, with guaranteed wall-plug efficiency uplift on a
  standard test protocol.
- **Buyer + pain evidence:** accelerator RF sources historically run <50% wall-plug (DOE roadmap,
  L05-039); the simulated-vs-hardware klystron efficiency gap is ~12 points a decade after the
  enabling technique (L05-011 vs L05-012/L05-013); CEPC quantifies ~RMB 130M/yr at stake for one
  facility (L05-013 — CN demand logic; direct sales access is limited, so CN functions as proof
  of value, not beachhead); DOE already brokered a SLAC "GREEN-RF" commercialization partnership
  (L05-032); fusion ECH buys MW gyrotrons in EUR 20M lots (L05-029).
- **Technical mechanism + physics red-team.** *Evidence:* depressed collectors are established
  vacuum-electronics physics; coupler reliability is the named failure mode to respect in any
  retrofit (L05-014). *Calculation:* a 45%-efficient klystron dumps 55% of beam power in the
  collector; a 4-stage MSDC recovering 60% of spent-beam energy lifts wall-plug efficiency by
  ~20 points; a 70-tube fleet at 50 kW average and 8,000 h/yr saves ~$2–3M/yr at $0.10/kWh.
  *Judgment:* retrofit only makes sense at rebuild/refurbishment or in new tubes — position as a
  module supplier to OEMs/rebuilders, not a field-retrofit shop. *Red-team:* secondary-electron
  backstreaming and collector arcing can destabilize the tube; each tube family needs its own
  beam-optics campaign; this is a slow, engineering-heavy business with concentrated buyers.
- **Why incumbents miss it:** tube OEMs sell replacement tubes — efficiency retrofits cannibalize
  their consumable revenue; labs lack productization incentive (GREEN-RF exists precisely because
  SLAC wants a commercial partner, L05-032).
- **Decisive experiment + budget:** MSDC prototype on a decommissioned S-band klystron;
  demonstrate >=15-point wall-plug uplift at >=50% rated output — $300k, 2028, lab test stand.
- **TRL:** 3.
- **2026–2029 plan:** beam-optics/collector design on a donated tube + GREEN-RF collaboration
  (2026-27); collector prototype and recovered-power measurement (2027-28); operating-tube
  retrofit demo with before/after data (2029).
- **2030–2034 trigger (named):** DOE facility electricity/carbon targets driving RF refits
  (L05-039, L05-032); fusion pilot-plant ECH procurement on the ITER/Thales template (L05-029).
- **2030 competition:** CPI (L05-050), Thales (L05-029), Canon (judgment), Vitzro Nextec (KR,
  L05-037) — all could internalize MSDC in new tubes; the retrofit/rebuild channel is the opening.
- **Window/timing risk:** slow procurement; OEM internalization narrows the wedge to drive
  electronics and test protocols.
- **Kill date:** 2034-06 without an OEM/rebuilder channel agreement.
- **Big vision:** every megawatt tube ships energy-recovering; the stack powers fusion-plant
  heating where recirculating power sets plant economics.
- **Nearest substitutes:** new high-efficiency tubes (CEPC-style bunching designs), SSPA
  replacement below ~1 MW (L05-008 trend).
- **Key uncertainty:** how much of the fleet economically reaches a rebuild insertion point
  before SSPAs eat the mid-power segment.
- **[FIX applied 2026-07-13]:** named-facility fleet/$-per-efficiency-point arithmetic task added; 2028 OEM/rebuilder channel-agreement-in-principle milestone; explicit 2029 license-or-fold-into-C-09 decision. Licensing-shaped structure acknowledged (retrofit-at-rebuild + OEM internalization risk).

## P3R2-D-08 — Solid-state e-beam sterilization machine (duopoly breaker)

- **Product:** self-shielded 10 MeV/30 kW-class e-beam (X-ray conversion option) driven by
  mass-produced solid-state RF pallets instead of klystrons; modular shipping-container form
  factor; ISO 11137-1:2025-aligned dose-mapping automation.
- **Buyer + pain evidence:** EtO replacement has the two pure-play e-beam vendors (IBA, L3)
  backlogged into 2026-27 while device makers wait for capacity (L05-028); ISO 11137-1:2025
  tightens validation (L05-042); accelerator demand is broadly rising (Varex cargo +25%,
  L05-033). China's CGN Dasheng RMB 340M half-year order flow proves category economics
  (L05-035) — CN is competitor territory, not a beachhead.
- **Technical mechanism + physics red-team.** *Evidence:* SSPAs are now the default for new
  mid-power CW accelerator RF (ESS, IFMIF-DONES, PAL-class work: L05-007, L05-008, L05-010);
  solid-state modulator/linac integration is mature (L05-004). *Calculation:* 30 kW beam at
  10 MeV = 3 mA average; ~60 kW of RF at 55–65% SSPA wall-plug efficiency ≈ 100 kW site load —
  compatible with a factory feeder; dose throughput at 25 kGy ≈ 4 t/h-class, i.e., a per-factory
  machine, not a mega-facility. *Judgment:* the wedge is capex/footprint (self-shielding + no
  klystron/HV vault) and delivery time against a backlogged duopoly. *Red-team:* accelerating-
  structure engineering and regulatory qualification are multi-year; the honest window question
  is whether incumbent backlogs clear before 2030 — mitigated by the durable regulatory driver
  and by targeting in-house sterilization at device makers, a segment incumbents ignore.
- **Why incumbents miss it:** IBA/L3 optimize large central service facilities; their klystron-
  based architectures don't shrink; backlog removes their urgency to productize a small machine.
- **Decisive experiment + budget:** SSPA-driven 1 MeV/5 kW CW prototype beamline; stable dose
  rate, RF chain wall-plug >55% — $500k, 2028, university accelerator facility.
- **TRL:** 4.
- **2026–2029 plan:** structure design + regulatory mapping with a university lab (2026-27);
  1 MeV prototype (2027-28); 10 MeV injector + shielding/throughput engineering and two contract-
  sterilizer LOIs (2029).
- **2030–2034 trigger (named):** continued EtO-replacement capacity build and ISO 11137-1:2025
  revalidation cycles (L05-028, L05-042).
- **2030 competition:** IBA, L3 (L05-028), Mevex (judgment), CGN Dasheng from China (L05-035);
  Co-60 gamma as a supply-constrained substitute.
- **Window/timing risk:** incumbent backlog clearing + price response; qualification timelines
  pushing revenue past 2031.
- **Kill date:** 2033-12 without a beta unit committed at a sterilization operator.
- **Big vision:** sterilization as a distributed appliance; then food safety and materials
  processing on the same platform.
- **Nearest substitutes:** gamma irradiation, X-ray service facilities, EtO with abatement.
- **Key uncertainty:** true all-in cost per sterilized pallet vs incumbent service pricing.
- **[FIX applied 2026-07-13]:** EtO forcing function flagged for P4 re-sourcing from EPA NESHAP/FDA primaries; SSPA-vs-klystron cost crossover to be validated with quotes by 2028; 2027 backlog-persistence kill check added; A-09's self-shielded in-house cell absorbed as a deployment option (with its licensing-friction caveat).

## P3R2-D-09 — UHDR/FLASH beam metrology: the traceable ammeter

- **Product:** hybrid non-intercepting monitor — cavity-resonator charge measurement
  cross-calibrated to an integrated Faraday/calorimetric reference — with a metrology-grade
  uncertainty budget, in drop-in BCT form factors.
- **Buyer + pain evidence:** two independent 2024-25 groups showed beam current transformers are
  corrupted by charge buildup at FLASH dose rates — an unresolved traceability problem for
  clinical and industrial e-beam (L05-023, L05-024); industrial sterilization operators must
  satisfy tightened ISO 11137-1:2025 dosimetry (L05-042) amid the EtO-driven capacity build
  (L05-028).
- **Technical mechanism + physics red-team.** *Evidence:* the BCT failure mechanism
  (field-driven charge buildup) is published; cavity monitors measure stored EM energy rather
  than magnetization, sidestepping it (L05-023, L05-024 context). *Calculation:* FLASH pulses of
  µs duration at mA–A peak put cavity signals tens of dB above thermal noise; a 1% absolute
  chain needs Faraday/calorimetric anchoring — standard metrology engineering. *Judgment:* small
  physics risk; the product is the certified uncertainty budget. *Red-team:* the market is an
  instrument niche (tens of $M) unless FLASH goes clinical at scale; Bergoz's installed-base
  trust is formidable (L05-049).
- **Why incumbents miss it:** Bergoz-class instruments were optimized for storage rings and
  conventional linacs; UHDR transients are new territory the incumbent has not productized.
- **Decisive experiment + budget:** side-by-side cavity vs BCT vs Faraday cup on a FLASH-capable
  linac; quantify BCT error vs dose rate; <1% cavity/calorimetry agreement — $150k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** uncertainty-budget design + beam time via medical-physics collaborations
  (2026-27); published comparison campaign (2027-28); beta units at one clinical program and one
  industrial e-beam plant, NIST-traceable calibration chain drafted (2029).
- **2030–2034 trigger (named):** FLASH device qualification campaigns reaching regulators
  (pain per L05-023/024) and EtO-replacement e-beam plants requiring compliant dosimetry
  (L05-028, L05-042).
- **2030 competition:** Bergoz (L05-049); in-house lab diagnostics.
- **Window/timing risk:** FLASH clinical timeline slip caps the market at industrial e-beam.
- **Kill date:** 2034-06 without OEM design-in.
- **Big vision:** the traceability layer for every high-dose-rate beam; expand to full
  diagnostics suites.
- **Nearest substitutes:** conventional BCTs + correction factors, offline film dosimetry.
- **Key uncertainty:** regulatory demand pull timing for UHDR-specific instrumentation.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical UHDR metrology. Documented unresolved failure, cheap decisive experiment, honest small-TAM admission; pairs with C-09/D-08. 2026-07-13: absorbed A-08 (ISO 11137-1:2025 sterilization-QA channel and calibration-certificate product tier). C-10's CN leg NOT imported (mirrored assertion without CN procurement/regulatory evidence - 'fake dual' per adjudication); D-09 remains US-primary.

## P3R2-D-10 — CBC phase engine: the conductor for a thousand lasers

- **Product:** channel-scalable coherent-beam-combining control stack — per-channel EO modulator
  front ends + deterministic sub-µs controller (SPGD/interferometric hybrid) proven 16→1,000+
  channels, vibration-hardened, open telemetry — sold to DEW primes and ultrafast OEMs.
- **Buyer + pain evidence:** TMI caps single-fiber power, making CBC the only route to
  300–500 kW weapons (L12-016, L12-017, L12-018); JLWS just committed $86M/$847M-ceiling to field
  such systems (L12-031, L12-032); DARPA AMPED/MELT are explicitly tile/combining architectures
  (L12-040, L12-041); CBC state of the art is advancing but bespoke (L12-001, L12-002).
- **Technical mechanism + physics red-team.** *Evidence:* record CBC results (260 fs/403 W
  combined ultrafast; new beam-shaping modes) show the physics works at lab scale (L12-001,
  L12-002). *Calculation:* combining efficiency η ≈ exp(−σφ²); λ/30 rms residual gives η ≈ 96%;
  disturbance spectra (acoustic/thermal) roll off by ~10 kHz, so ~1 MHz control bandwidth per
  channel with SPGD dither or heterodyne sensing suffices; 1,000 channels at ~MS/s each is
  RFSoC-class compute — feasible today. *Judgment:* the market failure is that every program
  rebuilds this controls layer; a merchant subsystem with accumulated vibration/thermal
  qualification wins on schedule. *Red-team:* path-length and dispersion management across
  channels (for ultrafast) is harder than phase alone; primes may classify and internalize; ITAR
  bifurcation of product lines is mandatory from day one.
- **Why incumbents miss it:** primes treat beam control as program IP, not a product; component
  vendors sell parts (modulators, mirrors) without the control intelligence.
- **Decisive experiment + budget:** 16-channel array locked to λ/30 rms with >90% combining under
  1 g random vibration — $250k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** university photonics testbed (2026-27); SBIR/STTR + 128-channel demo
  (2027-28); ruggedized brassboard under prime CRADA, ASIC path defined (2029).
- **2030–2034 trigger (named):** JLWS scaling to 300–500 kW production under its $847M ceiling
  (L12-031); AMPED/MELT transitioning to acquisition (L12-040, L12-041); industrial ultrafast CBC
  machining entering the market (L12-002 lineage).
- **2030 competition:** prime in-house controls (nLIGHT, LM Aculight — L12-033, L12-031), Civan
  Lasers integrated approach (judgment), academic spinouts.
- **Window/timing risk:** classification walls; single-aperture breakthroughs (unlikely per TMI
  literature) would reduce channel counts.
- **Kill date:** 2033-12 without a prime design-in or industrial OEM contract.
- **Big vision:** the standard control layer for laser weapons, machining arrays, beamed power,
  phased optical apertures.
- **Nearest substitutes:** spectral beam combining (limited for ultrafast), bigger single fibers
  (TMI-limited), in-house controls.
- **Key uncertainty:** how much of this layer primes will ever outsource.
- **[Adjudication 2026-07-13 - PROMOTE]:** Canonical CBC phase control; right abstraction level; dual-use hedge vs prime NIH; realistic channel-count ladder. Absorb A-17 DM-control + NNSA leg. 2026-07-13: absorbed A-17 (ruggedized deformable-mirror/adaptive-optics control tier; NNSA EYC demand leg L12-042 and MELT/POWER follow-ons L12-047; AO sources L12-009/010/011).

## P3R2-D-11 — 2-micron EUV drive-laser modules (architecture-change option)

- **Product:** modular kW-class 2 µm short-pulse drive/pre-pulse laser modules (coherently
  combined Tm:fiber front ends + Ho:YLF/Ho:YAG power amplifiers) plus a tin-droplet interaction
  test service mapping conversion efficiency vs pulse format.
- **Buyer + pain evidence:** ASML's own milestone history (250→500→1,000 W, each step a
  re-engineering, >EUR 6B cumulative EUV R&D, L12-034) documents architecture-change risk;
  peer-reviewed modeling shows a 2 µm drive could reach ~5% CE vs the CO2 chain (L12-003), with
  active tin-plasma atomic physics refinement ongoing (L12-006); Gigaphoton's continued
  next-generation source R&D is the second buyer path (L12-053, JP side market).
- **Technical mechanism + physics red-team.** *Evidence:* the 5% CE figure is modeling only
  (L12-003) — stated as such; shorter drive wavelength couples to higher-density plasma regions,
  raising CE and shrinking optics. *Calculation:* at 5% CE, 1 kW EUV needs ~20 kW drive vs
  ~40 kW+ for CO2 at ~2.5%; a 50 kHz droplet train at 400 µJ–1 mJ/pulse pre-pulse plus ~0.4 J
  main pulse implies ~20 kW average — beyond any demonstrated 2 µm source by ~30x; TMI and
  photodarkening in Tm fiber at kW average power are unproven territory (TMI physics per
  L12-016, L12-017 transfers qualitatively). *Judgment:* this is a real option-value play: build
  the 100–300 W modules and the CE dataset that make us the obvious partner if/when the CO2
  chain saturates. *Red-team:* ASML may scale CO2 past 1.5 kW and never switch; the buyer class
  is one company plus one challenger; debris/collector lifetime at 2 µm is uncharacterized.
- **Why incumbents miss it:** TRUMPF's CO2 amplifier franchise (L12-039) is the incumbent
  architecture — a classic innovator's-dilemma blind spot; fiber-laser majors chase industrial
  margins, not a speculative single-customer program.
- **Decisive experiment + budget:** measure EUV CE on tin droplets with a 2 µm ps source at
  relevant intensity; kill/continue gate at CE >=3% experimental — $600k, 2028, university EUV
  plasma lab.
- **TRL:** 2.
- **2026–2029 plan:** 100 W 2 µm ps source in a university ultrafast lab + EUV-plasma partnership
  (2026-27); droplet CE campaign and published CE-vs-format map (2028); 300 W engineering module
  and source-OEM engagement (2029).
- **2030–2034 trigger (named):** EUV source power roadmap pressure past the 1,000 W milestone as
  high-NA tools ramp (L12-034); Gigaphoton next-gen source program decisions (L12-053).
- **2030 competition:** TRUMPF CO2 chain (L12-039), IPG/Coherent 2 µm programs (judgment),
  national-lab prototypes.
- **Window/timing risk:** the highest physics risk in this batch; also single-buyer procurement
  risk.
- **Kill date:** 2032-12 if experimental CE <3% at relevant droplet targets, or if no source OEM
  engagement by then.
- **Big vision:** supply the drive photons of the post-CO2 EUV era and beyond-EUV scaling.
- **Nearest substitutes:** continued CO2 scaling (incumbent), solid-state 1 µm drives (worse CE
  per current modeling).
- **Key uncertainty:** whether modeled 2 µm CE survives contact with experiment.
- **[FIX applied 2026-07-13]:** adopted E-13's stricter kill gate (CE >=4% at relevant rep-rate by end-2033; kill date moved 2032-12 -> 2033-12 with the harder bar); Gigaphoton second-buyer hedge imported; acqui-license stated as the likely exit; capital capped at the consortium experiment until the gate passes. Merged in E-13's amplifier-module framing sources (coherent combining L12-001/002; pre-pulse shaping L06-016/017).

## P3R2-D-12 — Field-driven boiling: EHD-pumped two-phase cold plates

- **Product:** two-phase microchannel cold plate with embedded EHD conduction micropumps that
  modulate per-channel flow ±20%+ against live hotspot maps — silent, no local moving parts,
  milliwatt drive — qualified on non-PFAS low-GWP dielectric fluid; sold to cold-plate OEMs.
- **Buyer + pain evidence:** accelerator TDP is heading to 3,000–5,000 W with ~1,000 W/cm2 local
  flux (L14-010); Google's Deschutes spec already demands a 3°C approach at 2 MW (L14-043);
  NVIDIA frames liquid cooling as the enabling technology (L14-044); COOLERCHIPS funded exactly
  this frontier (L14-030). CN path: GB 40879 PUE tightening toward <=1.25/1.2 (L14-035) and the
  April 2026 national AI-energy plan's high-efficiency-cooling push (L14-036) — respecting the
  documented finding that the "100% liquid cooling mandate" is NOT in the primary text (L14-036).
- **Technical mechanism + physics red-team.** *Evidence:* EHD conduction pumping controls
  microchannel-evaporator flow in 2024-25 peer-reviewed work (L16-001, L16-002); two independent
  2025 reviews say EHD remains short of industrial deployment (L16-003, L16-004) — this is the
  atlas's enthusiasm zone, entered here with an explicit demand bridge. *Calculation:* EHD
  conduction stages generate ~0.1–2 kPa each at mW electric power; two-phase loop drops are
  10–50 kPa, so EHD cannot replace the CDU — the product does per-channel trim (±20% flow) and
  boiling-instability suppression, a role needing only ~1–5 kPa of authority; microchannel
  targets of ~200 W/cm2 at <0.2 K/W are the published state of the art to beat (L14-009).
  *Judgment:* the winning form is "smart plate + dumb pump," not pump replacement. *Red-team:*
  electrode fouling/charge injection aging over years, EMI in dense racks, and the fluid triple
  constraint (dielectric + low-GWP + non-PFAS under AIM Act/EU F-gas, L14-033, L14-034) may not
  intersect in one qualified fluid — this is the kill-gate.
- **Why incumbents miss it:** JetCool/ZutaCore/Vertiv (L14-045, L14-046, L14-048) all iterate
  mechanical pumping and manifolds; EHD sits in an academic ghetto the cooling industry doesn't
  read; hyperscalers spec systems, not in-plate physics.
- **Decisive experiment + budget:** EHD-assisted two-phase plate on a 500 W emulator: >=20%
  per-channel modulation, measurable CHF uplift, 1,000 h electrode stability in a non-PFAS
  fluid — $180k, 2027.
- **TRL:** 3.
- **2026–2029 plan:** EHD cell characterization in candidate fluids at a university thermal lab
  (2026-27); integrated plate + COOLERCHIPS-adjacent funding (2027-28); OEM evaluation units with
  reliability/EMI data and OCP-aligned spec sheet (2029).
- **2030–2034 trigger (named):** post-Deschutes OCP cooling spec cycles for 600 kW–1 MW racks
  (L14-043, L14-044, L02-043 roadmap), COOLERCHIPS commercialization wave (L14-030), China PUE
  standard enforcement (L14-035, L14-036).
- **2030 competition:** Flex/JetCool (L14-045), ZutaCore (L14-046), Vertiv-scale integrators
  (L14-048), Taiwanese two-phase supply chain (ITRI lineage, side market).
- **Window/timing risk:** documented EHD industrialization failure pattern; brute-force CDU
  scaling as the boring alternative.
- **Kill date:** 2032-12 if EHD authority/lifetime in a qualified non-PFAS fluid is not
  demonstrated at system-relevant conditions.
- **Big vision:** electric fields as the last-centimeter coolant pump across GPUs, power
  electronics, and laser diodes.
- **Nearest substitutes:** microjet plates, passive manifold tuning, bigger pumps.
- **Key uncertainty:** fluid qualification intersection (dielectric, low-GWP, non-PFAS,
  EHD-compatible conductivity).
- **[FIX applied 2026-07-13]:** 2028 named-OEM/COOLERCHIPS co-development demand-bridge gate added; 2027 experiment upgraded to require beating the best mechanical-pump plate on CHF/hotspot-following (parity = kill); hard dielectric+non-PFAS+low-GWP fluid-intersection gate codified.

## P3R2-D-13 — Thermal magazine: burst-mode thermal capacitor for directed energy

- **Product:** containerized thermal capacitor LRU: two-phase spreaders (100+ W/cm2 at the diode/
  gain modules) charging tonne-scale engineered PCM banks (300+ MJ over minutes), recharged by a
  right-sized trickle chiller between engagements; thermal state-of-charge telemetry included.
- **Buyer + pain evidence:** JLWS commits to containerized 150→300–500 kW lasers (L12-031); GAO
  documents the prototype-to-fielding gap where support-subsystem SWaP-C is a core obstacle
  (L12-045); DoD thermal management has been an open research thread for three decades (L14-025);
  loop-heat-pipe/two-phase and radar thermal co-design literature is active, not settled
  (L14-024, L14-027, L14-001).
- **Technical mechanism + physics red-team.** *Evidence:* PCM latent-heat storage and two-phase
  spreading are established physics; the gap is a qualified, integrated LRU (L14-025 context).
  *Calculation:* 500 kW optical at ~33% wall-plug → ~1 MW heat; a 300 s engagement = 300 MJ; at
  ~200 kJ/kg usable (latent + sensible) that is ~1.5 t of PCM plus structure — heavy but
  container-compatible; steady-state chiller shrinks ~10x to ~100 kW, recharging in ~50 min.
  *Judgment:* engagement duty cycles make peak-rated chillers irrational; a thermal battery is
  the correct architecture and nobody productizes it. *Red-team:* PCM thermal conductivity is the
  classic weakness — requires graphite/metal-foam loading (halving energy density in practice);
  cycle life under repeated melt/freeze and platform shock/vibe is the qualification burden;
  mass may still lose to chillers on weight-critical mobile platforms — target containerized and
  fixed-site first.
- **Why incumbents miss it:** primes engineer lasers and buy chillers; thermal storage falls
  between laser IP and COTS HVAC, and three decades of DARPA programs (L14-025) produced papers,
  not an LRU.
- **Decisive experiment + budget:** 100 kW-for-60 s brassboard: >=100 W/cm2 source flux, <10 K
  cold-plate excursion, 500 cycles without capacity fade — $220k, 2027.
- **TRL:** 4.
- **2026–2029 plan:** PCM/encapsulation trades + SBIR entry (2026-27); brassboard cycling data
  (2027-28); 300 kW pallet demonstrator evaluated by a prime, MIL-E qualification plan (2029).
- **2030–2034 trigger (named):** JLWS 300–500 kW fielding decisions under the $847M ceiling
  (L12-031); MELT-class modular HEL platforms (L12-041 program goals).
- **2030 competition:** prime in-house thermal teams (L12-033 context), thermal-engineering
  houses (judgment: ACT-class), COTS chiller vendors.
- **Window/timing risk:** fielded power plateauing at 150 kW keeps chillers adequate.
- **Kill date:** 2034-06 without a prime evaluation contract.
- **Big vision:** thermal energy storage as a standard military LRU across lasers, radars, EW,
  and hypersonic test assets.
- **Nearest substitutes:** oversized vapor-compression chillers, expendable coolant blowdown.
- **Key uncertainty:** PCM cycle life and effective energy density after conductivity loading.
- **[Adjudication 2026-07-13 - PROMOTE]:** Unique in pool; latent-heat magazine vs peak-rated chiller aimed at a GAO-named SWaP gap with dated program ladder; risks named and testable by 2027 brassboard.

## P3R2-D-14 — 400 °C-class downhole electronics for the superhot decade

- **Product:** modular 300–500 °C telemetry/control node: NASA-heritage SiC JFET analog front
  ends, HT-SOI where sufficient, ceramic/HT die-attach packaging, partitioned hot-front-end +
  insulated-DSP architecture; sold as qualified modules with published HPHT life data.
- **Buyer + pain evidence:** ARPA-E SUPERHOT targets >375 °C reservoirs ($30M, 10–20 GW framing,
  L15-029) while commercial HT ICs stop at 225 °C and CISSOID's CHT family is obsolete/
  last-time-buy with no successor (L15-043) — a documented supply gap with funded buyers: FORGE
  solicitations ($49M + $44M, L15-027, L15-028), Baker Hughes' $2.0B New Energy orders including
  a 300 MW geothermal ORC contract (L15-040), SLB–Ormat commercial EGS pilot (L15-041).
- **Technical mechanism + physics red-team.** *Evidence:* NASA Glenn SiC JFET ICs ran >1 year at
  500 °C (L15-009, L15-030); SiC junctions are viable to ~600 °C (L15-001); DARPA THERMAL is
  still funding 800 °C mixed-signal, i.e., government treats this as open (L15-026); packaging/
  die-attach is the repeatedly-documented limiter (L15-005). *Calculation:* at 400 °C, SiC JFET
  leakage remains orders of magnitude under signal currents; the module architecture needs only
  ~100-transistor-class hot front ends (amplify/digitize-lite/multiplex) with conventional
  silicon behind a thermal barrier — matching demonstrated SiC SSI complexity rather than
  wishing for HT microprocessors. *Judgment:* productizing the demonstrated NASA device class
  into oilfield-qualified modules is a packaging-and-reliability venture, not device research.
  *Red-team:* the documented rival strategy is active cooling of conventional electronics
  (dewars/sorption cooling — L15 brief's competing literature); vibration + 400 °C + corrosive
  brine co-qualification is brutal; volumes are small and sales cycles long.
- **Why incumbents miss it:** Honeywell exited/legacy (L15-031 heritage, obsolescence
  cross-referenced in L15-043); CISSOID retreated; oilfield majors buy rather than fab; DARPA
  performers target 800 °C papers, not 400 °C products.
- **Decisive experiment + budget:** SiC JFET sensor front-end, 1,000 h at 400 °C in HPHT
  autoclave, <5% parameter drift vs 225 °C SOI baseline — $200k, 2027-28.
- **TRL:** 3.
- **2026–2029 plan:** SiC-JFET IC access via NASA lineage/university fabs + module architecture
  with two tool OEMs (2026-27); autoclave campaign + SUPERHOT-aligned SBIRs (2027-28); full node
  field trial in a FORGE-class well (2029).
- **2030–2034 trigger (named):** SUPERHOT program wells entering >375 °C regimes (L15-029), FORGE
  continuation (L15-027, L15-028), Baker Hughes/SLB-Ormat commercial EGS scale-up (L15-040,
  L15-041).
- **2030 competition:** CISSOID remnants (L15-043), Ozark-class SBIR shops (judgment), DARPA
  THERMAL spinouts (L15-026) — likely still device-level, not module-level.
- **Window/timing risk:** dewar-cooled conventional electronics winning on cost; superhot
  drilling schedule slip.
- **Kill date:** 2033-12 without a funded field trial slot in a >300 °C well.
- **Big vision:** the HTMOS successor platform for geothermal, aero-engine, hypersonics, and
  Venus-surface systems (HOTTech lineage, L15-030).
- **Nearest substitutes:** actively cooled conventional tools; measure-after-cooldown workflows.
- **Key uncertainty:** total-cost comparison vs active cooling at fleet scale.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-14]:** Import 400C SiC-JFET tier and FORGE field-trial step into A-14 roadmap. Record retained as audit trail; not independently promotable.

## P3R2-D-15 — Rad-tolerant GaN power tiles for electric propulsion

- **Product:** standardized rad-tolerant GaN power bricks (anode supply, heater/keeper, PMAD
  interfaces) with published SEE/TID maps, honest derating envelopes, SET-mitigated topologies,
  and a reusable qualification file spanning 300 W–12 kW thruster classes.
- **Buyer + pain evidence:** PPU topologies have not converged in 50+ years — US/JP/CN groups
  still publish competing architectures (L09-001, L09-008), so every program pays bespoke NRE;
  GaN/SiC radiation qualification is genuinely unfinished — TID/displacement synergy (L09-020),
  heavy-ion SEB near ~50% of rated voltage (L09-014, L09-103, L09-104). Paying buyers exist at
  scale: AEPS $67M and NEXT-C $18.4M PPU contracts (L09-034, L09-012), Gateway PPE named chain
  (L09-043), SDA Tranche 3 $3.5B and Maneuverable GEO $905M (L09-039, L09-037 — EP content
  inferred, flagged per the lane's own caution), NASA SBIR awards for rad-hard power ASICs
  (L09-112, L09-113).
- **Technical mechanism + physics red-team.** *Evidence:* rad-tolerant GaN parts now exist at
  component level (EPC Space, CERN-lineage ASIC — L09-054, L09-055), but system-level SEE data is
  vendor-claimed, not independently validated (lane pain 12). *Calculation:* GaN at 60% of rated
  voltage with SET-filtered gate drive (per L09-108-class mitigation) still beats silicon rad-hard
  parts by ~2x on converter mass/efficiency at 300 V-class buses; a common 1 kW brick paralleled
  N-wide covers 300 W–12 kW with one qualification. *Judgment:* the product is the qualification
  dossier — the physics is characterization, not invention. *Red-team:* derating erodes the GaN
  advantage; primes may insist on their own quals; export control (ITAR/EAR) shapes the customer
  list from day one.
- **Why incumbents miss it:** Aerojet/L3Harris PPU capability now sits inside a missile-focused
  parent (L09-041 context via lane), Moog serves primes program-by-program (L09-043); nobody
  sells merchant qualified bricks; Japan's Furukawa/JAXA GaN PPU effort validates the approach in
  a side market (L09-042).
- **Decisive experiment + budget:** heavy-ion SEE campaign on a GaN half-bridge PPU stage across
  LET spectrum at operating voltage; safe-operating-area map + SET-mitigation efficacy — $180k,
  2027, university cyclotron.
- **TRL:** 3.
- **2026–2029 plan:** beam-time campaigns + published SEE maps (2026-27); NASA SBIR brick
  prototype with thermal-vac/TID cycles (2027-28); engineering-model tile on a commercial
  thruster test stand + qualification dossier to AIAA/ECSS-class standards (2029).
- **2030–2034 trigger (named):** SDA tranche cadence and Space Force Maneuverable GEO-class
  procurements (L09-039, L09-037), NASA Gateway/MSR EP lineage (L09-043, L09-034, L09-012).
- **2030 competition:** Aerojet/L3Harris, Moog (L09-043), EPC Space at parts level (L09-054,
  L09-055), Furukawa/JAXA in Japan (L09-042).
- **Window/timing risk:** prime vertical integration; a converged in-house standard emerging at
  one large constellation builder.
- **Kill date:** 2034-06 without a flight-demo manifest slot.
- **Big vision:** one qualified tile family from cubesat EP to 100 kW tugs and lunar PMAD.
- **Nearest substitutes:** silicon rad-hard converters (mass penalty), program-bespoke PPUs.
- **Key uncertainty:** whether SEB-safe derating leaves enough advantage to force adoption.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-13]:** Import SEE-map-first sequencing and qualified-once qualification-file framing into A-13. Record retained as audit trail; not independently promotable.

## P3R2-D-16 — Merchant 100 kWe space Brayton PCU + lunar PMAD

- **Product:** flight-weight He-Xe closed-Brayton turboalternator modules (25–50 kWe, paralleled
  to 100+ kWe) with foil bearings and radiator-matched interfaces, plus kV-class DC PMAD/cabling
  for kilometer-scale lunar distribution — sold to all reactor teams, not one.
- **Buyer + pain evidence:** NASA/DOE Fission Surface Power tripled its spec (40 kWe → >=100 kWe
  closed Brayton) within one cycle, stranding Phase 1 baselines (L09-031 vs L09-033); the April
  2026 NSTM-3 memo directs a >=100 kWe-class reactor with Q1 FY2030 launch-readiness targeting
  (L09-033); Westinghouse's eVinci continuation shows contract flow (L09-032, L09-047). No
  merchant flight Brayton PCU exists — each team builds captive.
- **Technical mechanism + physics red-team.** *Evidence:* closed-Brayton space conversion has
  NASA heritage (BRU-era) and the modern Kilopower/KRUSTY program proved fission-to-electric
  integration at 1 kWe with Stirling (L09-105); radioisotope-TPV studies (L04-107) bound the
  alternative-converter trade space. *Calculation:* 100 kWe at ~25% cycle efficiency rejects
  ~300 kWt at ~500 K — order 200-300 m2 of radiator; turboalternator at 60–90 krpm on foil
  bearings is within terrestrial microturbine practice; specific mass target ~5–8 kg/kWe for the
  PCU is aggressive but not physics-limited. *Judgment:* a merchant PCU supplier de-risks all
  three teams simultaneously — the natural subcontract position. *Red-team:* program risk
  dominates (already one re-baseline); He-Xe turbomachinery at flight mass has never flown;
  radiators, not the PCU, may bound system mass; if FSP slips past 2034 this market is study
  contracts.
- **Why incumbents miss it:** each FSP team treats conversion as captive scope (Creare inside
  Lockheed's team, L09-031); no one sells across teams; terrestrial microturbine firms don't do
  flight qualification.
- **Decisive experiment + budget:** 10 kWe-class He-Xe turboalternator on foil bearings with
  electric heater loop: >=20% cycle efficiency at flight-relevant turbine inlet temperature,
  validated specific-mass model — $500k, 2028.
- **TRL:** 3.
- **2026–2029 plan:** cycle/mass optimization vs the 100 kWe RFI + NASA SBIR/STTR entries and
  Brayton-heritage recruiting (2026-27); 10 kWe rig (2027-28); 1,000 h vacuum endurance + kV PMAD
  brassboard, positioned as subcontractor to 2+ teams (2029).
- **2030–2034 trigger (named):** FSP downselect and flight procurement per the August 2025 RFI
  and NSTM-3 (L09-033); eVinci-lineage contract continuations (L09-032, L09-047).
- **2030 competition:** Creare (L09-031), Brayton Energy (judgment), prime in-house conversion.
- **Window/timing risk:** single-program dependence; commercial lunar power demand is
  speculative until Artemis-era infrastructure firms commit.
- **Kill date:** 2033-12 if FSP flight procurement has not opened.
- **Big vision:** own the power-conversion layer of off-world energy across reactor generations.
- **Nearest substitutes:** Stirling converters (Kilopower lineage, lower unit power), large
  photovoltaic + storage farms (mass-prohibitive through lunar night).
- **Key uncertainty:** FSP procurement schedule integrity.
- **[FIX applied 2026-07-13]:** held as an option - studies/SBIR only with no hardware capex until FSP downselect/flight dates are contracted (2028 checkpoint); parallel-unit architecture to be validated with >=2 concept teams expressing subcontract interest; terrestrial micro-Brayton fold-down path defined.

## P3R2-D-17 — Cryogenic backplane: superconducting flex + 4 K multiplexing

- **Product:** superconducting-trace flex ribbons with thermally anchored cryo-CMOS FDM/TDM
  multiplexers at 4 K, delivering ~10x lines-per-loader at fixed heat load, in loader-compatible
  modules with certified thermal/microwave specs.
- **Buyer + pain evidence:** cryo I/O density is an acknowledged scaling wall — 256 channels/
  loader today vs thousands needed, with only one vendor's unvalidated 4x/2yr roadmap (L13-042);
  every line spends dilution-fridge cooling power that tops out at tens of µW–mW research levels
  (L07-014–L07-017); cryo-CMOS power-per-channel is the binding constraint the literature
  optimizes (L13-004, L13-005, L13-021, L13-023). Funded buyers: DOE QIS centers ($625M,
  L13-028), Fermilab–Qblox QICK domestication (L13-032); Keysight's 1,000+-qubit control delivery
  to AIST shows system scale arriving (L13-037, JP side).
- **Technical mechanism + physics red-team.** *Evidence:* 28 nm cryo-CMOS readout at ~1 mW/qubit
  class is published (L13-023); superconducting flex is an established fabrication art.
  *Calculation:* replacing 4 coax with 1 flex + 4:1 mux at 4 K cuts conducted load ~4x per
  logical line; a 1 mW mux die at 4 K fits pulse-tube budgets (W-class at 4 K) but must never
  touch the mK stage (µW budget) — architecture keeps active elements at 4 K and passives below.
  *Judgment:* a second credible supplier wins on procurement diversification alone. *Red-team:*
  SFQ single-chip control (SEEQC–ITRI, L13-038) would collapse external line counts if it wins —
  the honest substitution risk; microwave crosstalk in dense flex is the engineering grind;
  quantum vendors are secretive integrators with long design-ins.
- **Why incumbents miss it:** Delft Circuits sells passive cabling without cold electronics
  (L13-042); Bluefors integrates fridges, not signal chains (L13-041); control vendors stop at
  room temperature.
- **Decisive experiment + budget:** flex ribbon + 4:1 cryo-CMOS mux at 4 K: per-channel heat load
  <=25% of coax baseline with qubit-grade signal integrity — $250k, 2028, university/DOE cryostat.
- **TRL:** 3.
- **2026–2029 plan:** university cleanroom flex fab + heat-load metrology (2026-27); MPW
  cryo-CMOS mux integration (2027-28); 1,000-line loader-format prototype under DOE-center or
  fridge-OEM CRADA (2029).
- **2030–2034 trigger (named):** DOE QIS funding continuity (L13-028), QICK supply-chain
  commercialization (L13-032), error-corrected-machine wiring demand as 1,000+-qubit systems
  proliferate (L13-037, L13-042 roadmap gap).
- **2030 competition:** Delft Circuits (L13-042), Bluefors vertical moves (L13-041), SFQ
  alternative architecture (L13-038).
- **Window/timing risk:** control-architecture shifts (cryo-CMOS at 4 K everywhere, or SFQ)
  capping external line growth.
- **Kill date:** 2033-12 without a design-in at a major quantum program.
- **Big vision:** the cryogenic backplane standard for quantum computers, detectors, and cryo
  electronics.
- **Nearest substitutes:** more coax looms + bigger fridges; photonic links (immature at mK).
- **Key uncertainty:** which control architecture wins the 10,000-qubit era.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-E-04]:** Import SFQ/cryo-CMOS substitution-risk framing and roadmap-validation angle into E-04. Record retained as audit trail.

## P3R2-D-18 — Ka-band metamaterial ESA tiles at the Army's $300k price point

- **Product:** metasurface aperture tiles (varactor/liquid-crystal-tuned cells) steering a
  Ka-band beam from a handful of RF chains instead of thousands of T/R modules; calibrated tiles
  + beam-control software with open interfaces to third-party radar back ends.
- **Buyer + pain evidence:** the Army's own SBIR topic A254-049 states the pain: affordable
  Ka-band (30–40 GHz) metamaterial ESA radar for test/training, Phase I up to $250k, production
  target $300k/unit, opens April 15, 2026 (L16-020). Category proof at scale: Guangqi's
  RMB 516M single-disclosure and ~RMB 2.6B cumulative 2025 metamaterial defense orders in China
  (L16-017); allied-side transfer precedent KRISS→KER (~KRW 500M, L16-018, KR side market).
- **Technical mechanism + physics red-team.** *Evidence:* RCS/metasurface control physics is
  mature and actively extended (L16-010, L16-011); reconfigurable-surface architectures remain
  unsettled — an opening, not a defect, at radar (vs telecom) requirements (L16-013, L16-014).
  *Calculation:* a 256-element tile at 35 GHz spans ~11 cm; unit-cell varactor tuning gives
  ~300°-class phase range with 1–3 dB loss — acceptable for test-range tracking at km scale;
  removing ~1,000 T/R modules ($100s each) is the cost mechanism that reaches $300k/unit.
  *Red-team:* metasurface insertion loss and tuning speed at Ka-band can eat the link budget for
  long-range missions; GaN AESA costs also fall by 2030; Echodyne (judgment) proved the concept
  commercially at lower bands and could move up-band first.
- **Why incumbents miss it:** AESA primes profit from T/R module counts; the test/training and
  counter-UAS segments are below their margin floor — the Army had to open an SBIR to get a
  $300k radar at all (L16-020).
- **Decisive experiment + budget:** 64-element Ka-band tile: ±45° steering, insertion loss, and
  switching latency vs the A254-049 spec — $250k, 2027.
- **TRL:** 3.
- **2026–2029 plan:** Phase I SBIR (topic opens 2026-04-15) via university-affiliated team;
  Phase II 256-element tile + range event (2027-28); DFM cost-down with US supply chain and
  audited unit-cost projection (2029).
- **2030–2034 trigger (named):** Army test/training radar procurement via the A254-049 SBIR
  Phase III path (L16-020) and JLWS-era counter-UAS sensing build-out needing cheap Ka trackers
  (L12-031).
- **2030 competition:** Echodyne (judgment), conventional AESA primes, Guangqi in the Chinese
  sphere (L16-017).
- **Window/timing risk:** falling GaN AESA costs narrowing the gap; metasurface loss physics.
- **Kill date:** 2033-06 if tile loss/steering cannot meet the topic spec at the cost target.
- **Big vision:** 10x cheaper steered watts — radars on every range pole and drone; shared tile
  technology with 6G RIS infrastructure.
- **Nearest substitutes:** mechanically scanned dishes, low-cost GaN AESAs, Ku/K-band metamaterial
  ESAs.
- **Key uncertainty:** achievable insertion loss + reliability of tunable cells at 35 GHz in
  field conditions.
- **[FIX applied 2026-07-13]:** 2028 second-demand-anchor gate (second program office, prime teaming, or Phase II award); P4 incumbent mapping (Echodyne-class + prime AESA cost curves); E-12's KR allied-variant kept as upside only.

## P3R2-D-19 — Kinetic shock absorbers for the AI grid (composite flywheel strings)

- **Product:** 250–500 kW / 10–25 MJ composite-rotor flywheel modules on active magnetic bearings
  in vacuum, inverter-coupled to 800VDC/MV buses, deployed as parallel strings at PDU/feeder level
  with millisecond response and >10^6-cycle life — a power-quality machine, not bulk storage.
- **Buyer + pain evidence:** a 400 MW off-grid US AI datacenter already selected flywheel
  stabilization (Piller SHIELDX + Bergen engines, first shipments Dec 2025, L16-052) because
  engine/turbine plants cannot follow AI load steps; datacenter electrification orders run
  $2.4B/quarter at one vendor (L08-033); 800VDC rack architecture creates native DC coupling
  points (L02-043, L02-044). That GPU training loads swing at sub-second scale is labeled
  judgment/industry-inference here — the procurement evidence (L16-052) is the anchor.
- **Technical mechanism + physics red-team.** *Evidence:* flywheel stabilization at AI-plant
  scale is now a procured architecture (L16-052); axial-flux machine design/thermal literature
  supports high-power-density integrated motor-generators (L16-037, L16-038). *Calculation:*
  25 MJ at 500 kW rides through 50 s; for microcycle smoothing the relevant metric is power, not
  energy — a carbon-fiber rim at ~700 m/s tip speed stores ~50 Wh/kg with burst capability far
  beyond batteries' C-rates, and magnetic bearings in vacuum keep standby loss <1%/hour-class.
  *Judgment:* millions of daily microcycles age lithium cells (calendar+cycle) while flywheels
  are cycle-immortal — the economics favor kinetic buffering precisely in this duty. *Red-team:*
  composite rotor burst containment drives mass/cost; BESS with grid-forming inverters is a
  formidable, falling-cost substitute; NVIDIA could smooth loads in software/rack capacitors and
  shrink the niche to harmonics scale.
- **Why incumbents miss it:** Piller's synchronous-machine architecture is facility-scale AC
  (L16-052); BESS vendors optimize energy, not microcycle power; nobody builds DC-native
  distributed kinetic buffers sized to training-load spectra.
- **Decisive experiment + budget:** 50 kW / 2 MJ composite rotor on magnetic bearings in vacuum:
  100,000 microcycles, <1% loss growth, ms-class response — $350k, 2028.
- **TRL:** 4.
- **2026–2029 plan:** rotor/bearing design + AI-cluster load-spectrum instrumentation study with
  a datacenter partner (2026-27); subscale spin/cycle testing (2027-28); 250 kW prototype string
  vs synthetic GPU load at a power-island testbed (2029).
- **2030–2034 trigger (named):** off-grid/weak-grid AI power-plant build-outs following the
  documented 400 MW SHIELDX/Bergen architecture (L16-052) and the datacenter electrification
  supercycle (L08-033); 800VDC standardization (L02-043, L02-044).
- **2030 competition:** Piller (L16-052), BESS + grid-forming inverters, synchronous condensers
  at grid scale (L08-036, L08-037), supercapacitors.
- **Window/timing risk:** software-side load smoothing; BESS cost decline.
- **Kill date:** 2034-06 without a power-island integrator partnership.
- **Big vision:** every gigawatt campus carries spinning inertia sized to its training-job power
  spectrum; extension to grid-forming inertia services.
- **Nearest substitutes:** supercaps (seconds, cost/aging), BESS (cycle aging), oversized gensets.
- **Key uncertainty:** quantified value of microcycle smoothing to plant owners (needs the
  2026-27 load-spectrum study).
- **[FIX applied 2026-07-13]:** 2026-27 instrumented load-spectrum study with a datacenter partner made the sizing basis (niche measured, not asserted); quantified cycle-life economics vs Piller synchronous machines and vs BESS at measured microcycle rates; B-18's CN market absorbed as a license-note only.

## P3R2-D-20 — Hot hydraulics: pumps and valves for 1,400–2,400 °C liquid metal

- **Product:** qualified graphite/SiC/refractory-ceramic pump-and-valve skids with sealed drives,
  freeze-plug safety valves, level/flow instrumentation, and published lifetime data at
  1,400–2,400 °C — the certified "hot hydraulics" kit for thermal-battery and process-heat
  integrators.
- **Buyer + pain evidence:** TPV thermal batteries need molten silicon/tin moved between storage
  and converter walls at emitter temperatures where record cell efficiency lives (>40% cells,
  1,900–2,400 °C emitters — L04-001, L04-002, L04-009); MIT-lineage molten-silicon pumping is
  still a lab demonstration (L04-108); funded developers exist across the architecture spectrum
  (Antora ARPA-E SCALEUP, L04-033; Electrified Thermal FIRES, L04-034; Fourth Power's liquid-tin
  claims — vendor-asserted, flagged, L04-052), and industrial heat-battery purchases are real
  (Rondo at SCG cement and a California fuels site — L04-042, L04-043).
- **Technical mechanism + physics red-team.** *Evidence:* ceramic/graphite pumping of molten
  metals at extreme temperature was demonstrated in the peer-reviewed record (L04-108); emitter-
  temperature materials stability is the documented TPV bottleneck (L04-009). *Calculation:* a
  10 MWh-class liquid-metal battery cycling daily moves ~10–50 t of metal/hour at ~1 m head —
  low-power pumping (kW-class shaft power) but extreme-materials sealing; corrosion/dissolution
  rates of SiC/graphite in Si/Sn set life — published data support multi-year life for graphite
  in tin, while silicon service is the harder frontier. *Judgment:* every developer hand-builds
  this today; an outsourced, life-tested skid becomes obvious at commercial multi-unit scale —
  the 2026-2029 window exists precisely because nobody has accumulated 10,000-hour datasets.
  *Red-team:* the whole category dies if solid-media architectures (firebrick conduction,
  carbon-block radiation) win — an explicit architectural bet; also single-digit initial customer
  count and vendor-asserted economics upstream (L04-052 flagged).
- **Why incumbents miss it:** industrial pump makers stop at ~700 °C molten salt; graphite job
  shops sell parts, not qualified systems; thermal-battery startups are forced vertical but would
  rather not be (classic EV-supply-chain analogy).
- **Decisive experiment + budget:** 1,000 h molten-tin loop at 1,400 °C with instrumented ceramic
  pump: seal wear, flow stability, materials attack, lifetime model — $300k, 2027-28.
- **TRL:** 3.
- **2026–2029 plan:** university high-temperature materials rig replicating published pumping
  baselines (2026-27); 1,000 h tin loop + ARPA-E-adjacent funding (2027-28); molten-silicon loop
  campaign and first paid pilot kit to a thermal-battery developer (2029).
- **2030–2034 trigger (named):** thermal-battery commercial scale-ups following the ARPA-E
  SCALEUP/FIRES cohorts (L04-033, L04-034), heat-battery purchase precedents (L04-042, L04-043),
  and 24/7 clean-power procurement architectures (Google–Fervo template, L04-050).
- **2030 competition:** in-house builds at Antora/Fourth Power (L04-033, L04-052); graphite
  component shops; solid-media architectures as substitutes (L04-034).
- **Window/timing risk:** architecture selection risk (liquid vs solid media); slow capital
  formation in industrial heat.
- **Kill date:** 2033-12 if no liquid-metal thermal-battery developer has committed to a
  commercial-scale deployment.
- **Big vision:** own the plumbing of the >1,400 °C economy — thermal batteries, solar
  thermochemistry, metallurgy electrification, liquid-metal fusion blankets.
- **Nearest substitutes:** thermosiphon/gravity-drain designs (limited controllability),
  solid-media storage (no plumbing at all).
- **Key uncertainty:** molten-silicon compatibility lifetime at >1,600 °C.

---

### Generic EE/CE transfer note (appended after seed freeze)

Across all twenty seeds, the recurring buildable core is a disciplined electrical/computer-
engineering stack — precision power conversion, fast deterministic control (FPGA/ASIC),
low-noise instrumentation, and qualification-grade telemetry — wrapped around one extreme
physics element, so competence in that generic EE/CE stack transfers to every seed in this batch.
- **[FIX applied 2026-07-13]:** 2028 gate requiring >=1 liquid-metal thermal-battery developer with a commercial order book (else kill); buyer hypothesis broadened beyond one architecture to solar-thermochemical and metallurgy/process-heat pilots; first capital capped at molten-tin-loop scale until the gate passes.

