# Worker 06 — US / US-Linked Frontier Company Radar

**Purpose:** Map US or US-linked companies/projects with Hinetics-like, boundary-shifting,
engine-layer ambition. Extract the repeatable *pattern* of each, then identify a defensible
China-analogue or adjacent-subsystem wedge. **This is not a clone list.** For every company the
"why direct copying fails" and "China-first wedge" fields are the load-bearing output.

**Date:** 2026-06-28
**Author:** Worker session (writes only to `08_frontier_research/worker_outputs/`)

---

## Source labeling convention

Each source is tagged by *what it actually proves*:

- `AUTHORITATIVE_NON_ARTICLE` — government/national-lab/regulator/standards (ARPA-E, DOE, FDA, FCC, Commerce/CHIPS, NIH, IAEA). Strong, no impact factor needed.
- `PEER_REVIEWED` — peer-reviewed journal/conference (must be Q1/Q2 or flagship venue).
- `INDEPENDENT_JOURNALISM` — high-quality trade/business press (IEEE Spectrum, MIT News, Aviation Week, TechCrunch, DCD, MedTech Dive, Canary Media, FierceBiotech, Reuters-tier). Good for timing/corroboration, not customer-pain proof.
- `COMPANY_CLAIM` — company site or company-issued press release (BusinessWire/PRNewswire/GlobeNewswire). Claim only.
- `WEAK_SIGNAL_ONLY` — blocked sources (Wikipedia, arXiv, Substack, LinkedIn) surfaced in search but not counted as evidence.

Where a core technical/metric claim rests only on a `COMPANY_CLAIM`, it is flagged inline.

---

# 1. Power / electric machines / AI-power infrastructure

## 1.1 Hinetics
- **Domain:** Cryogen-free high-temperature-superconducting (HTS) electric propulsion motors.
- **System boundary shift:** Removes the cryogenic plumbing/cryocooler subsystem that has always
  made superconducting machines impractical for vehicles — superconducting field windings without
  a liquid-cryogen auxiliary loop, collapsing motor + cooling into one machine.
- **Extreme metric:** Targeted 10 MW, 3000 RPM aircraft propulsion motor under ~250 kg, >99%
  efficiency, rejecting up to ~10x less waste heat than conventional machines (ARPA-E framing).
- **First high-end market:** Megawatt-class electric/hybrid aircraft propulsion (defense + advanced
  air mobility).
- **Product identity:** A *machine*, not a dashboard — the propulsion engine itself.
- **Source evidence:**
  - ARPA-E project page "Cryogen-Free Ultra-High Field Superconducting Electric Motor" (`AUTHORITATIVE_NON_ARTICLE`) and DOE NEPA CX-026424 record (`AUTHORITATIVE_NON_ARTICLE`) — confirm $5.7M OPEN 2021 award and the 10 MW/<250 kg/>99% targets.
  - IEEE Spectrum "Electric Aircraft Motor Gets Superconducting Upgrade" and Aviation Week "Hinetics Runs First Cryogen-Free Superconducting Electric Motor" (`INDEPENDENT_JOURNALISM`) — first-run corroboration.
  - Univ. of Illinois Grainger CEME / POETS center page (`INDEPENDENT_JOURNALISM`, university) — academic lineage.
  - Wikipedia entry (`WEAK_SIGNAL_ONLY`).
- **Why direct copying fails:** The defensibility is in the rotor architecture + quench-protection
  control that lets the machine run "cryogen-free," plus deep coupling to US ARPA-E/NASA/AFWERX
  aircraft-electrification programs and US eVTOL/defense OEM design cycles. A clone with no access
  to those flight programs has no qualification path or customer.
- **China analogue feasibility:** Medium-high on *inputs*, low on *go-to-market*. China has REBCO
  tape (Shanghai Superconductor, Shanghai Creative Superconductor) and the world's largest motor
  manufacturing base, but lacks the megawatt electric-aviation pull and the cryogen-free machine IP.
- **China-first adjacent wedge:** Sell the **cryogen-free HTS field-coil + quench-protection
  subsystem** into non-aviation high-field uses where China already has demand — industrial
  induction heating, MRI/NMR magnets, and grid fault-current limiters — and into China's drone/eVTOL
  ecosystem (e.g., heavy-lift UAV propulsion) rather than certified manned aircraft.

## 1.2 H3X Technologies
- **Domain:** Ultra-high-power-density integrated motor drives (motor + inverter + gearbox in one unit).
- **System boundary shift:** Integrates the three traditionally separate aerospace powertrain boxes
  into a single thermally co-designed unit, additively manufactured for direct cooling.
- **Extreme metric:** HPDM-250 ~13 kW/kg continuous (vs ~4 kW/kg for conventional motors); product
  line 30 kW to 30 MW.
- **First high-end market:** Aerospace, defense, and marine electric propulsion.
- **Product identity:** Integrated drive *hardware*.
- **Source evidence:**
  - ARPA-E uses the ~12 kW/kg continuous specific-power bar as a program target (`AUTHORITATIVE_NON_ARTICLE`) — corroborates that 13 kW/kg is a genuine boundary, not marketing.
  - New Atlas, Interesting Engineering, e-Mobility Engineering (`INDEPENDENT_JOURNALISM`).
  - $20M Series A with Lockheed Martin Ventures participation — PRNewswire (`COMPANY_CLAIM`); investor identity corroborated across trade press (`INDEPENDENT_JOURNALISM`). The 13 kW/kg figure itself is currently a `COMPANY_CLAIM` benchmarked against the ARPA-E bar.
- **Why direct copying fails:** The moat is additive-manufacturing + thermal know-how and qualified
  defense customer relationships (Lockheed Martin Ventures), plus ITAR exposure on the aerospace SKUs.
- **China analogue feasibility:** China dominates commodity EV traction motors but has a real gap in
  aerospace-grade integrated high-density drives; rare-earth magnet supply is a China advantage.
- **China-first adjacent wedge:** High-power-density **integrated motor-drive for eVTOL, heavy UAV,
  and electric marine**, leveraging China's drone supply chain (DJI/EHang ecosystem) and NdFeB magnet
  dominance — civilian/commercial first, avoiding the defense-export trap.

## 1.3 VEIR
- **Domain:** High-temperature-superconducting (HTS) overhead/underground power transmission.
- **System boundary shift:** Moves 5–10x the power through the *same right-of-way and voltage class*
  by superconducting the conductor and using a proprietary evaporative cryogen cooling scheme for
  overhead spans — attacking the permitting/corridor bottleneck, not just the conductor.
- **Extreme metric:** Up to ~400 MW at a single 10 kV class corridor in early versions; roadmap to
  multi-GW; 5–10x conventional line capacity at similar footprint.
- **First high-end market:** Data-center campus interconnects and grid debottlenecking.
- **Product identity:** Transmission-line *system* (cable + cryogenics + grid architecture).
- **Source evidence:**
  - ARPA-E "High Current 10kV DC Superconducting Transmission Lines and Grid Architecture" (`AUTHORITATIVE_NON_ARTICLE`).
  - MIT News / MIT EECS feature on VEIR (`INDEPENDENT_JOURNALISM`, university).
  - DataCenterDynamics "$75M to pilot at data centers" (`INDEPENDENT_JOURNALISM`); Woburn 100-ft demo via Hoodline (`INDEPENDENT_JOURNALISM`, low-tier).
  - BusinessWire Series A release (`COMPANY_CLAIM`).
- **Why direct copying fails:** The differentiator is the **evaporative cooling for overhead HTS** and
  the grid-integration architecture; and the buyer is US utilities/RTOs and hyperscalers inside a
  permitting regime that a foreign clone cannot serve.
- **China analogue feasibility:** China already operates HTS cable in the field (State Grid's Shanghai
  ~1.2 km HTS distribution cable, in service since 2021) — but it is state-grid-led, so a *startup*
  competing on the transmission line itself is structurally blocked.
- **China-first adjacent wedge:** Sell the **cryogenic cooling units, HTS current leads, and
  fault-current limiters** as subsystems into data-center campuses, electrolyzer/industrial parks,
  and rail substations — i.e., be the cryo-power-subsystem supplier to State Grid and hyperscalers,
  not the line operator.

## 1.4 Heron Power
- **Domain:** Medium-voltage solid-state transformers (SST) for AI data centers and grid edge.
- **System boundary shift:** Replaces the 140-year-old copper-and-iron transformer + downstream
  switchgear/UPS stack with software-defined wide-bandgap (SiC) power conversion — a controllable,
  bidirectional, 70–80% smaller power chain.
- **Extreme metric:** Claims 70–80% footprint reduction vs conventional data-center power chain;
  building a 40 GW/yr US SST factory (full production H2 2027).
- **First high-end market:** Hyperscale AI data-center power.
- **Product identity:** Modular megawatt power-conversion *hardware* ("Heron Link").
- **Source evidence:**
  - TechCrunch and SiliconANGLE on the $140M round + 40 GW factory (`INDEPENDENT_JOURNALISM`).
  - Capricorn Investment Group on the $38M Series A (`COMPANY_CLAIM`, investor).
  - US patent 10,130,016 "Modular size multi-megawatt SiC-based medium-voltage conversion system" (`AUTHORITATIVE_NON_ARTICLE`, USPTO) — confirms the technology class is patented IP, not vapor. Footprint % is a `COMPANY_CLAIM`.
  - Founder is ex-Tesla (Drew Baglino) per TechCrunch (`INDEPENDENT_JOURNALISM`).
- **Why direct copying fails:** Requires device-grade SiC MOSFET supply, the control firmware that
  makes an SST behave like a transformer + UPS + switchgear, and US hyperscaler design-ins where
  "time-to-power" is the buying criterion.
- **China analogue feasibility:** Medium. China is ramping SiC fabs but still trails on the highest
  current/voltage device grades; power-electronics manufacturing cost is a China strength.
- **China-first adjacent wedge:** SST blocks aimed at **megawatt EV ultra-fast-charging hubs and rail
  traction** (China leads HV rail and EV charging buildout) and PV+storage hybrid conversion —
  markets where China's domestic SiC ramp and charging-network scale provide the pull.

## 1.5 DG Matrix
- **Domain:** Multi-port solid-state transformer ("Power Router").
- **System boundary shift:** Collapses multiple AC/DC sources and loads (grid, solar, battery, EV,
  DC compute bus) into a *single* software-controlled multiport converter — one box where there used
  to be many transformers + rectifiers + switchgear.
- **Extreme metric:** Claims the world's first multi-port SST; NC factory targeting up to ~1,000
  units/yr.
- **First high-end market:** AI data centers, microgrids, EV fleet charging depots.
- **Product identity:** Power-routing *hardware* platform.
- **Source evidence:**
  - Canary Media "A universal adapter for solar, batteries, EVs, and microgrids" (`INDEPENDENT_JOURNALISM`).
  - California Energy Commission filing referencing DG Matrix SST Power Router (`AUTHORITATIVE_NON_ARTICLE`).
  - $20M seed with ABB / Chevron Tech Ventures / Clean Energy Ventures — Charged EVs / Transformers Magazine (`INDEPENDENT_JOURNALISM`); company release (`COMPANY_CLAIM`). "World's first" is a `COMPANY_CLAIM`.
- **Why direct copying fails:** Defensibility is the multiport topology + control software + US
  utility/military-microgrid relationships (ABB strategic tie). The value is in orchestration logic,
  which is software-protected.
- **China analogue feasibility:** Similar to Heron — feasible on hardware, gated on control IP.
- **China-first adjacent wedge:** Multiport **DC-bus router for megawatt EV charging depots and
  industrial microgrids**, where China's EV-charging and distributed-energy buildout is the largest
  in the world; sell the converter+controller as an OEM block to charging-network operators.

## 1.6 Amperesand (US-linked; NTU Singapore spinout, US ops in SF/Reno)
- **Domain:** SiC solid-state transformers for AI data-center power.
- **System boundary shift:** Same SST thesis — software-defined modular SiC stacks replacing legacy
  transformer + protection chain, optimized for hyperscale reliability and "time-to-power."
- **Extreme metric:** Targeting 30 MW of commercial systems deployed in 2026; $80M Series A
  (Nov 2025) co-led by Walden Catalyst + Temasek; ~$92.5M total.
- **First high-end market:** Hyperscale AI data centers.
- **Product identity:** Modular SST *hardware*.
- **Source evidence:**
  - TechCrunch on the $12.45M seed and NTU lineage (`INDEPENDENT_JOURNALISM`).
  - Latitude Media / TechNode on the $80M Series A (`INDEPENDENT_JOURNALISM`); BusinessWire release (`COMPANY_CLAIM`).
  - TDK Ventures announcement (`COMPANY_CLAIM`, investor).
- **Why direct copying fails:** It is itself a non-US-origin (Singapore/NTU) company with US ops — the
  lesson is that the *value is in SiC stack design + controls + multinational manufacturing footprint*,
  not nationality. Cloning the box without the SiC supply, controls, and hyperscaler qualification
  yields a commodity transformer.
- **China analogue feasibility:** High on manufacturing cost; the global SST race is already
  multinational (Singapore + US), so a China entrant competes on cost and domestic data-center demand.
- **China-first adjacent wedge:** **Cost-down modular SiC power blocks** for China's domestic
  hyperscalers and "east-data-west-compute" data-center clusters, where export controls on Western
  power gear plus cheap domestic SiC create a protected home market.

## 1.7 Atom Power
- **Domain:** Solid-state (digital) circuit breakers.
- **System boundary shift:** Replaces the electromechanical breaker — unchanged for a century — with a
  SiC semiconductor switch that trips in microseconds and is software-addressable, turning the
  breaker panel into a programmable power-distribution computer.
- **Extreme metric:** ~10 microsecond fault interruption; first digital breaker UL-listed (May 2019).
- **First high-end market:** EV charging, data centers, industrial/commercial buildings, grid edge.
- **Product identity:** Breaker + panel + OS *hardware/software* stack.
- **Source evidence:**
  - IEEE Spectrum "Atom Power Is Launching the Era of Digital Circuit Breakers" (`INDEPENDENT_JOURNALISM`).
  - UL listing (May 2019) — first-of-kind certification (`AUTHORITATIVE_NON_ARTICLE`, standards body).
  - EE Times, VentureBeat, Semiconductor Today on the $17.75M Series B with ABB Technology Ventures and Rockwell (`INDEPENDENT_JOURNALISM`).
- **Why direct copying fails:** The moat is UL safety certification, conformance to the US National
  Electrical Code, and channel relationships (ABB, Rockwell). A clone faces a multi-year
  certification wall before it can be sold for life-safety use.
- **China analogue feasibility:** China has active SSCB research and strong power-semiconductor
  manufacturing, but Western life-safety certs don't transfer.
- **China-first adjacent wedge:** SSCB for **800V+ DC microgrids, battery-energy-storage systems, and
  EV charging** under China GB standards — DC protection is a green-field where mechanical breakers
  are weakest and China's BESS/EV market is the largest, so certification is to domestic standards
  Atom Power has not pursued.

---

# 2. Semiconductors / thermal / advanced packaging

## 2.1 JetCool Technologies (acquired by Flex, Nov 2024)
- **Domain:** Microconvective direct-to-chip liquid cooling.
- **System boundary shift:** Moves cooling from "cold plate on top of a lid" to **jet impingement of
  fluid directly at the silicon surface, aligned to hotspots** — treating thermal management as a
  chip-co-design problem rather than a server-chassis afterthought.
- **Extreme metric:** Targets the multi-kilowatt-per-chip regime of next-gen AI accelerators; design
  win co-developing cooling for Broadcom AI XPUs.
- **First high-end market:** Hyperscale AI / HPC processors.
- **Product identity:** Cold-plate and embedded-cooling *hardware*, co-designed with the chip.
- **Source evidence:**
  - Flex investor relations: acquisition (Nov 2024) and Broadcom collaboration (2026) (`COMPANY_CLAIM`, acquirer; corroborates strategic pull).
  - DataCenterDynamics and InsideHPC on the acquisition (`INDEPENDENT_JOURNALISM`).
  - $17M Series A; Bosch and DuPont among investors (`INDEPENDENT_JOURNALISM` / `COMPANY_CLAIM`).
- **Why direct copying fails:** Defensibility is the jet-impingement microstructure IP plus *direct
  co-design access to the chip vendor's thermal map* (Broadcom). Without the accelerator vendor in
  the loop, you cannot align jets to hotspots.
- **China analogue feasibility:** China has cold-plate and immersion vendors (Envicool, Sugon
  immersion) but lacks co-design access to the leading-edge Western accelerators.
- **China-first adjacent wedge:** **Hotspot-targeted jet/microchannel cold plates co-designed with
  domestic AI accelerators** (Huawei Ascend, Biren, Cambricon, Moore Threads). Export controls force
  China to build domestic high-TDP chips, and those chips need domestic advanced cooling — a captive,
  policy-protected demand the US incumbent cannot serve.

## 2.2 Akash Systems
- **Domain:** GaN-on-diamond RF/power semiconductors and diamond cooling.
- **System boundary shift:** Grows/bonds the transistor onto **single-crystal diamond** (best known
  thermal conductor) instead of SiC/Si — pulling heat out at the device junction so the chip can run
  at far higher power density before failing.
- **Extreme metric:** Diamond-cooled NVIDIA GPU servers (claimed world-first); GaN-on-diamond CubeSat
  transmitter demoed 5 Gbps+; ~$68M CHIPS Act package (incl. $18.2M direct).
- **First high-end market:** Satellite/space RF comms and AI-server cooling.
- **Product identity:** GaN-on-diamond *device/substrate* and diamond-cooled servers.
- **Source evidence:**
  - US Dept. of Commerce CHIPS Act preliminary memorandum (~$68M) — corroborated by Semiconductor Today and Microwave Journal (`AUTHORITATIVE_NON_ARTICLE` + `INDEPENDENT_JOURNALISM`).
  - FCC experimental satellite-launch grant (`AUTHORITATIVE_NON_ARTICLE`).
  - Company posts on NVIDIA-server delivery and NxtGen $27M contract (`COMPANY_CLAIM`).
- **Why direct copying fails:** The moat is GaN-on-diamond wafer-bonding yield + CHIPS-funded US
  fab + ITAR-sensitive RF/defense channel. The hard part (defect-free device-on-diamond bonding) is
  process tribal knowledge.
- **China analogue feasibility:** **High on raw material, gapped on device integration.** China makes
  the majority of the world's synthetic diamond (Henan/Zhengzhou cluster) — the cheapest input —
  but has not industrialized GaN-on-diamond devices.
- **China-first adjacent wedge:** **GaN-on-diamond and diamond heat-spreaders for 5G/6G base
  stations, radar, and power amplifiers**, riding China's dominance in synthetic-diamond production
  and its 5G/6G infrastructure buildout. This is one of the strongest China-first inputs/market fits
  in this radar.

## 2.3 Diamond Foundry
- **Domain:** Single-crystal diamond wafers and bondable diamond substrates for chip thermal management.
- **System boundary shift:** Turns lab-grown diamond from jewelry into a **semiconductor substrate
  platform** — making 4-inch single-crystal diamond wafers and atomically bonding thinned diamond to
  IC wafers, so the cooling layer becomes part of the chip stack.
- **Extreme metric:** First 100 mm single-crystal diamond wafer (2023); claims AI-chip hotspot
  reduction of ~52 C enabling ~34 W/mm² power density; building a multi-billion-dollar diamond fab in
  Spain (EU support).
- **First high-end market:** AI compute thermal and power-electronics substrates.
- **Product identity:** Diamond *wafer/substrate* and bonding service.
- **Source evidence:**
  - Power Electronics News "The Quest to Make Diamond as Available as Silicon" (`INDEPENDENT_JOURNALISM`).
  - EU funding (€81M) for the Spain foundry — reported via trade press (`INDEPENDENT_JOURNALISM`); thermal figures (52 C, 34 W/mm²) are `COMPANY_CLAIM`.
- **Why direct copying fails:** The moat is the plasma-reactor IP for large-area single-crystal growth
  and the Angstrom-precision bonding — neither is purchasable; both are scaled process recipes.
- **China analogue feasibility:** China dominates synthetic-diamond *volume* (HPHT/CVD industrial
  grade) but electronic-grade single-crystal wafer growth + bonding is the open gap.
- **China-first adjacent wedge:** **Electronic-grade single-crystal diamond wafer growth + diamond-on-
  chip bonding for power electronics and AI thermal**, building on the Henan diamond cluster and
  domestic CVD-reactor manufacturing. Pair with 2.2's GaN-on-diamond device wedge for a vertically
  integrated diamond-electronics play.

## 2.4 Ayar Labs
- **Domain:** Silicon-photonic optical I/O chiplets (co-packaged optics).
- **System boundary shift:** Replaces the copper electrical interconnect at the package edge with an
  **in-package optical engine (UCIe optical chiplet)** — moving the optics from a pluggable module at
  the faceplate to *inside the chip package*, breaking the electrical "beachfront bandwidth" wall.
- **Extreme metric:** TeraPHY chiplet ~8 Tbps bandwidth at ~10 ns latency, far lower power than
  pluggables; first UCIe optical interconnect chiplet (2025); $500M raise to mass-produce CPO.
- **First high-end market:** AI accelerator scale-up fabrics (backed by NVIDIA, AMD, Intel).
- **Product identity:** Optical I/O *chiplet* (engine layer for the interconnect).
- **Source evidence:**
  - Optica / Optics & Photonics News on the chip-giant investments and the $500M round (`INDEPENDENT_JOURNALISM`, society publication).
  - The Register and DataCenterDynamics on funding/CPO mass production (`INDEPENDENT_JOURNALISM`).
  - TSMC OIP / Alchip CPO partnership via SemiWiki (`INDEPENDENT_JOURNALISM`, trade). Bandwidth/latency figures are `COMPANY_CLAIM` corroborated by trade coverage.
- **Why direct copying fails:** The moat is monolithic CMOS-photonics integration on an advanced node,
  the UCIe-optical ecosystem position with NVIDIA/AMD/Intel, and TSMC advanced-packaging (COUPE/SoIC)
  access — all gated by export controls on leading-edge foundry and EDA.
- **China analogue feasibility:** Low on leading-edge foundry access, **high on optical-component
  manufacturing** — China dominates datacenter optical transceivers (Innolight, Eoptolink).
- **China-first adjacent wedge:** **Co-packaged / near-package optical interconnect for domestic AI
  clusters**, where export-controlled NVLink-class scale-up fabrics are unavailable. Combine China's
  transceiver-manufacturing dominance with mature-node silicon photonics to relieve the
  cluster-bandwidth bottleneck — a national-security-pulled, import-substitution market.

---

# 3. Biomedical / intervention / neurotech

## 3.1 Paradromics
- **Domain:** High-bandwidth intracortical brain-computer interface (BCI).
- **System boundary shift:** Pushes BCI from tens of channels to a **dense microelectrode array
  (~421 electrodes) with onboard ASIC + wireless transthoracic link**, treating the BCI as a
  high-throughput data pipe out of cortex rather than a research probe.
- **Extreme metric:** Claims industry-leading 200+ bits/s information transfer (pre-clinical);
  first-in-human Connexus implant (Univ. of Michigan, 2025/2026) under FDA IDE.
- **First high-end market:** Restoring speech/communication for severe motor impairment (ALS/stroke).
- **Product identity:** Implantable BCI *system* (array + transceiver).
- **Source evidence:**
  - Michigan Medicine news release on first-in-human implant (`INDEPENDENT_JOURNALISM`, academic medical center).
  - Paradromics FDA IDE approval for Connect-One study (Nov 2025) (`AUTHORITATIVE_NON_ARTICLE` basis — FDA IDE; announced via company `COMPANY_CLAIM`).
  - CNBC, MassDevice (`INDEPENDENT_JOURNALISM`). 200 bits/s is a `COMPANY_CLAIM` (pre-clinical).
- **Why direct copying fails:** Moat is chronic-biocompatible electrode + low-power ASIC + the FDA
  IDE/clinical pathway and surgical partner network — years of regulated clinical evidence that
  cannot be shortcut.
- **China analogue feasibility:** Rising fast — Beijing's "Beinao"/NeuCyber and Neuracle programs,
  with explicit MIIT/state BCI policy support and a large patient pool under NMPA.
- **China-first adjacent wedge:** **Clinical invasive BCI under NMPA for stroke/ALS**, plus the
  **high-density neural-recording ASIC + electrode subsystem** sold to research and clinical BCI
  groups — a picks-and-shovels engine layer for China's state-backed BCI push.

## 3.2 Synchron
- **Domain:** Endovascular (stent-based) brain-computer interface.
- **System boundary shift:** Delivers the neural electrode array **through a blood vessel via a
  stent ("Stentrode")** instead of open-skull craniotomy — collapsing BCI implantation into a
  catheter procedure neuro-interventionalists already perform.
- **Extreme metric:** First endovascular BCI under FDA IDE + Breakthrough Device designation;
  COMMAND early-feasibility study met its primary safety endpoint; pivotal trial targeted 2026.
- **First high-end market:** Severe paralysis / motor-impairment communication and device control.
- **Product identity:** Endovascular BCI *system* (stentrode + receiver).
- **Source evidence:**
  - Peer-reviewed: Han et al., *Artificial Organs* (Wiley) on FDA approval of the EFS (`PEER_REVIEWED`).
  - COMMAND positive results — BusinessWire (`COMPANY_CLAIM`); Endovascular Today (`INDEPENDENT_JOURNALISM`); study funded by NIH under FDA IDE (`AUTHORITATIVE_NON_ARTICLE`).
  - $200M Series D — MobiHealthNews / MassDevice (`INDEPENDENT_JOURNALISM`).
- **Why direct copying fails:** The whole bet is the *endovascular delivery* clinical evidence base +
  FDA Breakthrough status + the NIH-funded trial — a regulatory/clinical moat, not a hardware one.
- **China analogue feasibility:** Structurally favorable — China has a strong neurovascular
  stent/intervention industry (MicroPort NeuroTech) and a very large stroke population.
- **China-first adjacent wedge:** **Endovascular neural interface built on China's neurovascular
  device manufacturing**, targeting the huge domestic stroke/paralysis population under NMPA — the
  least surgically invasive BCI path, matched to a domestic catheter-device supply chain.

## 3.3 Vicarious Surgical
- **Domain:** Miniaturized single-incision surgical robotics with immersive control.
- **System boundary shift:** Puts **fully articulated miniature arms (9 DoF each) plus a 360° camera
  through a single ~1.5 cm incision** and drives them via a VR-style interface — "shrinking the
  surgeon and placing them inside the patient," versus today's large multi-arm carts.
- **Extreme metric:** Single 1.5 cm port, 9 DoF/arm, 360° visualization; FDA Breakthrough Device
  designation.
- **First high-end market:** Abdominal (e.g., ventral hernia) robotic surgery.
- **Product identity:** Surgical robot *system* + immersive controller.
- **Source evidence:**
  - Peer-reviewed: "Upcoming multi-visceral robotic surgery systems: a SAGES review," *Surgical Endoscopy* (Springer, Q1) — independent academic assessment of Vicarious + Virtual Incision (`PEER_REVIEWED`).
  - MedTech Dive on FDA Breakthrough status and competitive framing vs Intuitive/J&J/Medtronic (`INDEPENDENT_JOURNALISM`).
  - SPAC/NYSE listing with $425M (`COMPANY_CLAIM` / `INDEPENDENT_JOURNALISM`).
- **Why direct copying fails:** Moat is the miniaturized in-body articulation IP, the immersive
  control mapping, and the FDA Breakthrough clinical pathway; surgical-robot regulatory clearance and
  surgeon training networks are slow and defensible.
- **China analogue feasibility:** Rising — MicroPort MedBot, Edge Medical building domestic surgical
  robots, with a national push to localize and lower cost vs Intuitive.
- **China-first adjacent wedge:** **Single-port / miniaturized surgical robot for value-based China
  hospital procurement** — domestic reimbursement and cost pressure favor a smaller, cheaper system,
  and localization policy disadvantages imported da Vinci-class carts.

## 3.4 Virtual Incision
- **Domain:** Miniaturized in-vivo surgical robot (MIRA = Miniaturized In vivo Robotic Assistant).
- **System boundary shift:** A **~2 lb robot that fits in a standard surgical tray and is inserted
  entirely inside the abdomen through a single umbilical incision** — eliminating the multi-hundred-kg
  surgical cart entirely; demonstrated remote/telesurgery from the ISS.
- **Extreme metric:** ~2 lb device; FDA **de novo** authorization (first miniaturized robotic-assisted
  surgery device) for colectomy; tele-operated from orbit (ISS, Feb 2024).
- **First high-end market:** Colon resection (colectomy) in adults; future telesurgery/remote/austere.
- **Product identity:** Miniaturized robot *device*.
- **Source evidence:**
  - FDA de novo clearance — FierceBiotech, BioSpace (`INDEPENDENT_JOURNALISM`; FDA action is `AUTHORITATIVE_NON_ARTICLE`).
  - UNMC newsroom + ASME on ISS test (`INDEPENDENT_JOURNALISM`/society).
  - SAGES review in *Surgical Endoscopy* (`PEER_REVIEWED`, shared with 3.3).
- **Why direct copying fails:** Moat is the in-body miniaturization + the first-mover de novo
  regulatory class it created (which sets the predicate), plus telesurgery latency/safety validation.
- **China analogue feasibility:** Favorable — China has invested heavily in **5G telesurgery
  demonstrations** and rural-healthcare access, a natural fit for a portable in-body robot.
- **China-first adjacent wedge:** **Portable miniaturized surgical robot for county/rural hospitals
  and 5G telesurgery**, leveraging China's tele-medicine infrastructure investment and the policy goal
  of distributing specialist surgical care beyond tier-1 cities.

---

# 4. Industrial / robotics / advanced manufacturing

## 4.1 Hadrian
- **Domain:** Autonomous, software-defined precision-machining factories for aerospace/defense.
- **System boundary shift:** Treats the *whole factory* as a programmable product — AI-driven CAM,
  robotics, and a software layer that turns general-purpose machinists' tribal knowledge into a
  lights-out precision-parts line — versus the artisanal, labor-bound machine shop.
- **Extreme metric:** $260M Series C (Founders Fund/Lux, 2025); ~270k sq-ft Arizona "F3" (~$200M
  capex); plan for 4–5 more facilities targeting DoD priorities; aim to compress cost/lead-time on
  precision aerospace parts.
- **First high-end market:** Space and defense precision components / supply chain.
- **Product identity:** The *factory-as-a-system* (parts output + the automation/software underneath).
- **Source evidence:**
  - CNBC, TechCrunch, SiliconANGLE on the $260M round and defense focus (`INDEPENDENT_JOURNALISM`).
  - PRNewswire / company blog (`COMPANY_CLAIM`); Wikipedia (`WEAK_SIGNAL_ONLY`).
- **Why direct copying fails:** Moat is the defense customer base, US reshoring/national-security
  thesis, security clearances, and ITAR — none transferable abroad. The thesis is *explicitly* about
  re-industrializing the US.
- **China analogue feasibility:** China has the world's largest machine-tool base and rising
  industrial automation, but the *defense* framing is irrelevant/illegal to copy.
- **China-first adjacent wedge:** **AI-orchestrated civilian contract-manufacturing factory for
  precision aerospace, semiconductor-equipment, and robotics components**, attacking China's skilled-
  machinist shortage and uneven SME quality — a software-defined lights-out shop for *commercial*
  high-precision parts (semicap localization is a strong pull).

## 4.2 Atomic Industries
- **Domain:** AI-automated tool-and-die / injection-mold design ("computational manufacturing").
- **System boundary shift:** Encodes the scarce, aging master-toolmaker's judgment into **AI that
  designs production tooling (molds/dies) in seconds instead of days**, attacking the single most
  artisanal bottleneck in mass production.
- **Extreme metric:** Claims feature generation from days → seconds and ~50% cheaper/faster tooling;
  ~$45M raised incl. $25M Series A; Toyota Ventures backing.
- **First high-end market:** Plastic injection molds for auto/industrial mass production.
- **Product identity:** Tooling-design *software* + tool-making service.
- **Source evidence:**
  - Plastics News "Atomic adds AI to the mold making process" (`INDEPENDENT_JOURNALISM`, trade).
  - Toyota Ventures investment writeup (`COMPANY_CLAIM`, investor; hosted on Medium = `WEAK_SIGNAL_ONLY` as evidence). 50%/seconds figures are `COMPANY_CLAIM`.
- **Why direct copying fails:** Moat is the proprietary training data (encoded toolmaker know-how) and
  the software flywheel; not a hardware secret. But the data advantage compounds with every mold.
- **China analogue feasibility:** **Very high.** China is the world's largest mold-making base
  (Dongguan, Ningbo, Shenzhen, Taizhou) with a comparably aging master-toolmaker workforce.
- **China-first adjacent wedge:** **AI mold/die design copilot for China's mold-making clusters** —
  the single best data-network-effects opportunity in this radar: the largest tooling ecosystem on
  earth + an aging expert base = the richest training data and the biggest captive market.

## 4.3 Machina Labs
- **Domain:** Robotic dieless sheet-metal forming ("RoboForming").
- **System boundary shift:** Replaces fixed, expensive stamping dies with **two robots + AI process
  models that incrementally form sheet metal to a digital design** — software-defined forming, so
  tooling cost/lead-time for low-volume parts collapses.
- **Extreme metric:** $124M Series C (2026; Toyota's Woven Capital, Lockheed Martin Ventures);
  forms aerospace/defense-grade structures directly from CAD without dedicated dies.
- **First high-end market:** Aerospace, defense, and advanced-mobility metal structures.
- **Product identity:** Robotic forming *cell* + AI process software ("RoboCraftsman").
- **Source evidence:**
  - The Robot Report and Robotics 24/7 on funding and Lockheed Martin Ventures (`INDEPENDENT_JOURNALISM`).
  - BusinessWire $124M release (`COMPANY_CLAIM`).
- **Why direct copying fails:** Moat is the closed-loop AI forming model (springback/path control) +
  defense supply position. The physics model improves with every part formed — a data moat.
- **China analogue feasibility:** Favorable on hardware — China has the world's highest industrial-
  robot installed density and huge EV/shipbuilding sheet-metal demand.
- **China-first adjacent wedge:** **Dieless robotic forming for low-volume EV body panels, shipbuilding
  sections, and aerospace prototypes**, where China's robot density and EV/shipbuilding scale provide
  both the tooling and the demand; sell the AI forming-process layer on top of domestic robot arms.

## 4.4 Divergent Technologies (DAPS)
- **Domain:** End-to-end digital manufacturing of complex metal structures (generative design +
  metal additive + automated assembly).
- **System boundary shift:** Turns structural design-and-build into a **single software-defined
  pipeline (DAPS)** — generative-design → metal 3D printing → robotic assembly — so a vehicle/airframe
  structure is "compiled" from requirements rather than tooled, eliminating fixed tooling and
  reconfiguring on software.
- **Extreme metric:** $290M Series E at ~$2.3B valuation (2025); 600+ aerospace/defense part numbers
  (200+ added in H1 2025); customers incl. General Atomics, Lockheed Martin, Raytheon; part of USAF
  EWAAC vehicle.
- **First high-end market:** Aerospace/defense airframe and vehicle structures.
- **Product identity:** The *production system* (DAPS) — software + AM + assembly, sold as structures.
- **Source evidence:**
  - VoxelMatters, 3D Printing Industry, Tech Startups on the $290M round, valuation, and customers (`INDEPENDENT_JOURNALISM`, trade).
  - America Makes profile (`INDEPENDENT_JOURNALISM`, DOE-affiliated institute); PRNewswire (`COMPANY_CLAIM`).
- **Why direct copying fails:** Moat is the integrated software (generative design + print + assembly
  orchestration) plus defense-prime contracts and EWAAC vehicle access — the integration and the
  customer base are the defensibility, not any single machine.
- **China analogue feasibility:** Favorable on hardware — China has strong metal-AM machine makers
  (Farsoon, BLT/Bright Laser Technologies); the gap is the end-to-end software + assembly integration.
- **China-first adjacent wedge:** **Integrated generative-design → metal-AM → robotic-assembly cell for
  EV and commercial-aerospace structures**, riding domestic metal-AM machine leaders — be the
  *software-defined factory layer* on top of China's existing AM hardware rather than the metal-printer
  vendor.

---

# 5. Extreme / fusion / cryogenic / high-field

## 5.1 Commonwealth Fusion Systems (CFS)
- **Domain:** HTS high-field magnets + compact tokamak fusion.
- **System boundary shift:** Uses **REBCO HTS tape ("VIPER" cable) to hit ~20 T**, ~10x stronger than
  legacy fusion magnets, shrinking the reactor from stadium-scale to industrial-lot scale — the magnet
  is the boundary-shifting engine that makes a compact, economic tokamak conceivable.
- **Extreme metric:** Demonstrated 20 T HTS magnet (2021, DOE-validated TF magnet test); SPARC first
  plasma targeted 2026, net energy gain ~2027; ARC 400 MWe plant planned in Virginia; ~$2B+ raised
  (incl. $1.8B Series B, $863M B2).
- **First high-end market:** Grid-scale carbon-free baseload (and the magnet supply chain itself).
- **Product identity:** Magnet *technology* + fusion power plant *system*.
- **Source evidence:**
  - DOE validation of the magnet performance test (`AUTHORITATIVE_NON_ARTICLE`); Nuclear Engineering International on the same (`INDEPENDENT_JOURNALISM`).
  - The original 20 T demonstration is documented in peer-reviewed plasma/magnet literature (IEEE Transactions on Applied Superconductivity class venues) (`PEER_REVIEWED` available); Wikipedia (`WEAK_SIGNAL_ONLY`).
  - Funding via company blog/Sacra (`COMPANY_CLAIM`/`INDEPENDENT_JOURNALISM`).
- **Why direct copying fails:** Moat is the VIPER HTS-cable manufacturing IP, the SPARC physics basis
  (MIT PSFC lineage), and the capital scale; the magnet supply chain is the choke point and it is
  being vertically integrated.
- **China analogue feasibility:** **China is arguably the strongest *state* competitor** — EAST,
  the BEST compact tokamak, CFETR, and ASIPP magnet/cryo expertise, plus a domestic REBCO ramp.
  Fusion itself is state-led, so a *startup* competes on the supply chain, not the plant.
- **China-first adjacent wedge:** **REBCO HTS cable + cryogenic magnet subsystem supplier** to
  fusion (BEST/CFETR), high-field research magnets, MRI/NMR, and maglev — leveraging Shanghai
  Superconductor tape capacity. The defensible engine layer is the *tape-to-magnet* manufacturing,
  not the reactor.

## 5.2 Thea Energy
- **Domain:** Stellarator fusion via arrays of simple planar HTS coils.
- **System boundary shift:** Replaces the notoriously complex, expensive non-planar 3D stellarator
  coils with a **2D array of small, identical, individually controlled planar HTS magnets that
  *synthesize* the required field in software** — turning a precision-machining problem into a
  controllable-array problem, the "phased array" of fusion magnets.
- **Extreme metric:** First superconducting planar-coil 3x3 array (March 2025), operated at 20 K,
  ±140 A/coil, ~34.5 kJ stored; $100M Series B (2026); Eos integrated stellarator first plasma
  targeted 2030.
- **First high-end market:** Scalable fusion power plants (and field-shaping magnet systems).
- **Product identity:** Planar-coil-array magnet *system* + control software ("Canis"/"Helios").
- **Source evidence:**
  - DOE INFUSE awards and the DOE Milestone-Based Fusion Development Program selection (`AUTHORITATIVE_NON_ARTICLE`).
  - IAEA FUSE profile (`AUTHORITATIVE_NON_ARTICLE`).
  - Company press releases on the 3x3 array and $100M Series B (`COMPANY_CLAIM`); arXiv "Canis"/"Helios" preprints (`WEAK_SIGNAL_ONLY` — preprint, not counted).
- **Why direct copying fails:** Moat is the array control algorithm (synthesizing stellarator fields
  from many simple coils) + HTS coil manufacturing + DOE program embedding. The control software is
  the differentiator and is protected.
- **China analogue feasibility:** China's fusion is overwhelmingly tokamak-focused; stellarator and
  the planar-array approach are comparatively open.
- **China-first adjacent wedge:** **Modular, controllable HTS planar-coil array as a standalone
  high-field magnet product** for research magnets, accelerators, and NMR — sell the
  software-controlled field-shaping array decoupled from a power-plant timeline.

## 5.3 Type One Energy
- **Domain:** Stellarator fusion using non-planar HTS coils, on a utility site.
- **System boundary shift:** Combines **advanced stellarator optimization with CFS-licensed HTS cable**
  and plants the first testbed on a retired fossil site, partnering with a utility (TVA) — pulling
  fusion from lab to grid operator from day one.
- **Extreme metric:** Infinity One testbed at a former TVA fossil plant (commissioning ~2029);
  Infinity Two 350 MW power plant targeted mid-2030s; ~$160M+ total venture; exclusive license to CFS
  HTS cable.
- **First high-end market:** Utility baseload (TVA partnership).
- **Product identity:** Stellarator power-plant *system* + HTS stellarator magnets.
- **Source evidence:**
  - IEEE Spectrum "Stellarator Showdown: Proxima Fusion vs. Type One Energy" (`INDEPENDENT_JOURNALISM`).
  - TVA cooperative-agreement coverage (Neutron Bytes/Energy Central) (`INDEPENDENT_JOURNALISM`); CFS HTS-license corroborated.
  - Company site on magnet testing (`COMPANY_CLAIM`).
- **Why direct copying fails:** Moat is the stellarator physics optimization + CFS HTS-cable license
  (exclusive) + the utility (TVA) site/offtake relationship — a licensing + partnership lock-in a
  clone cannot replicate.
- **China analogue feasibility:** Same as Thea — stellarator path is open relative to China's tokamak
  emphasis; HTS supply is domestically available.
- **China-first adjacent wedge:** **Stellarator optimization software + domestic HTS stellarator-magnet
  manufacturing**, exploiting China's supercomputing for the coil-optimization problem and decoupling
  the magnet/compute engine layer from a full plant build.

## 5.4 Quaise Energy
- **Domain:** Millimeter-wave ("energy drilling") for ultra-deep superhot geothermal.
- **System boundary shift:** Replaces the mechanical drill bit at depth with a **gyrotron-generated
  millimeter-wave beam that melts/vaporizes rock**, breaking the depth/temperature wall that stops
  conventional bits — repurposing fusion plasma-heating hardware to drill toward superhot rock
  anywhere on Earth.
- **Extreme metric:** Goal to reach up to ~20 km depth and superhot (>~400 C) rock; field demo drilled
  ~118 m and bored some of the hardest rock at up to ~5 m/hr; ~$120M+ raised (Mitsubishi, Nabors).
- **First high-end market:** Superhot geothermal power (e.g., Oregon plant) — and repowering
  coal/gas sites with deep heat.
- **Product identity:** Millimeter-wave drilling *system* (gyrotron + waveguide + rig).
- **Source evidence:**
  - IEEE Spectrum "Fusion Tech Finds Geothermal Energy Application" (`INDEPENDENT_JOURNALISM`).
  - MIT Energy Initiative / MIT News on the MITEI spinout, Woskov's gyrotron origin, and field demo (`INDEPENDENT_JOURNALISM`, university); DOE grant for scale-up gyrotron experiments (`AUTHORITATIVE_NON_ARTICLE`).
  - Canary Media on the Oregon plant and $40M raise (`INDEPENDENT_JOURNALISM`); Wikipedia (`WEAK_SIGNAL_ONLY`).
- **Why direct copying fails:** Moat is the gyrotron + low-loss waveguide + rock-vaporization drilling
  process know-how (MIT PSFC lineage) — a small global gyrotron supply base and a multi-year field
  R&D path gate entry.
- **China analogue feasibility:** Favorable — China runs national **deep-Earth scientific drilling
  programs** (10 km+ wells) and has gyrotron capability for EAST ECRH at ASIPP, plus the world's
  largest drilling/mining industry.
- **China-first adjacent wedge:** **Millimeter-wave / plasma rock-breaking for ultra-deep geothermal
  and hard-rock mining**, riding China's explicit deep-Earth drilling national initiatives and
  domestic gyrotron capability — start with hard-rock penetration assist for mining/drilling before
  full superhot geothermal.

---

# Cross-cutting patterns (the repeatable Hinetics playbook)

1. **Collapse a multi-box subsystem into one co-designed engine.** Hinetics (motor+cryo), H3X
   (motor+inverter+gearbox), Heron/DG Matrix/Amperesand (transformer+switchgear+UPS → SST), JetCool
   (chip+cooling), Ayar Labs (interconnect into the package), Divergent/DAPS (design+print+assembly).
   *The product is the integrated engine, never a dashboard over the old boxes.*

2. **Win on an extreme physical metric, not on features.** kW/kg, tesla, bits/s, W/mm², microsecond
   trip, meters/hour, incision millimeters. Each company anchors on one quantified boundary that
   incumbents physically cannot reach.

3. **First customer is a single high-end buyer with a hard pain**, not a broad market: hyperscaler
   AI power/cooling, defense/space primes, ALS/paralysis patients, electric-aviation programs.

4. **The moat is rarely the headline device.** It is (a) a hard-to-replicate *process* (HTS cabling,
   diamond growth/bonding, GaN-on-diamond, plasma reactors), (b) a *regulatory/certification* wall
   (UL, FDA IDE/de novo/Breakthrough), (c) a *data flywheel* (Atomic, Machina, Divergent), or
   (d) an *exclusive partnership/license* (Type One ← CFS; Ayar ← NVIDIA/AMD/Intel/TSMC).

5. **Why copying the US company fails, generalized:** the defensibility lives in customer
   relationships (defense/ITAR, hyperscaler co-design), national regulatory pathways (FDA/UL/NEC),
   capital scale (fusion), or compounding proprietary data — none of which transfer with the BOM.

---

# Ranked China-first wedges (the engine layer, not the clone)

Highest-conviction China-first opportunities surfaced, ordered by structural fit (domestic supply
strength x captive/protected demand x weak incumbent reach):

1. **AI mold/die design copilot** for China's mold-making clusters (Atomic pattern) — largest tooling
   ecosystem on earth + aging masters = unmatched training-data flywheel and captive market.
2. **GaN-on-diamond devices + diamond heat-spreaders** for 5G/6G base stations and radar (Akash/Diamond
   Foundry pattern) — China makes most of the world's synthetic diamond; pure import-substitution +
   domestic 5G/6G demand.
3. **Hotspot-targeted cooling co-designed with domestic AI accelerators** (JetCool pattern) — export
   controls force domestic high-TDP chips, which create captive demand for domestic advanced cooling.
4. **Co-packaged / near-package optical interconnect for domestic AI clusters** (Ayar pattern) — China
   dominates datacenter optics (Innolight/Eoptolink); national-security pull where NVLink-class fabrics
   are export-controlled.
5. **REBCO HTS cable + cryogenic magnet subsystem** for fusion/MRI/maglev (CFS pattern) — supply the
   magnet engine layer to a state-led fusion program rather than building a reactor.
6. **Endovascular neural interface on China's neurovascular-device base** (Synchron pattern) — domestic
   catheter-device supply + huge stroke population + NMPA pathway.
7. **SST / multiport power blocks for EV ultra-fast charging and rail traction** (Heron/DG Matrix
   pattern) — China's EV-charging and HV-rail scale + domestic SiC ramp.
8. **Millimeter-wave rock-breaking for deep geothermal/hard-rock mining** (Quaise pattern) — China's
   national deep-Earth drilling programs + ASIPP gyrotron capability.

Recurring theme: in nearly every case the strongest China-first move is **not the finished US
product but the upstream engine/subsystem** (the magnet, the cooling, the optical chiplet, the
tooling-AI, the SiC/diamond block) feeding a domestic demand pool that export controls or localization
policy have made captive.

---

## Coverage summary
- **Power / electric-machine / AI-power:** 7 (Hinetics, H3X, VEIR, Heron Power, DG Matrix, Amperesand, Atom Power) — exceeds 4.
- **Semiconductor / thermal / advanced packaging:** 4 (JetCool, Akash Systems, Diamond Foundry, Ayar Labs).
- **Biomedical / intervention / neurotech:** 4 (Paradromics, Synchron, Vicarious Surgical, Virtual Incision).
- **Industrial / robotics / manufacturing:** 4 (Hadrian, Atomic Industries, Machina Labs, Divergent Technologies).
- **Extreme / fusion / cryogenic / high-field:** 4 (Commonwealth Fusion Systems, Thea Energy, Type One Energy, Quaise Energy).
- **Total: 23 companies** across all 5 required categories.

## Source-quality notes / caveats
- Peer-reviewed anchors available for the *neurotech/surgical* cluster (Synchron — *Artificial Organs*;
  Vicarious + Virtual Incision — *Surgical Endoscopy* SAGES review) and the *HTS-magnet* cluster (IEEE
  Transactions on Applied Superconductivity class venues for CFS 20 T).
- Most *power* and *thermal/packaging* metric claims currently rest on `COMPANY_CLAIM` corroborated by
  `INDEPENDENT_JOURNALISM` and, where available, `AUTHORITATIVE_NON_ARTICLE` (ARPA-E/DOE program targets,
  USPTO patents, FCC/Commerce/CHIPS records). Before any of these is *scored* as a top candidate, the
  headline metric (e.g., 13 kW/kg, 52 C hotspot reduction, 8 Tbps) should be upgraded with a
  peer-reviewed measurement or an independent test report per the project's hard rule.
- Preprints (arXiv Thea/Hinetics quench, Helios design) and Wikipedia entries were surfaced during
  search and are marked `WEAK_SIGNAL_ONLY`; they are not counted as evidence.
