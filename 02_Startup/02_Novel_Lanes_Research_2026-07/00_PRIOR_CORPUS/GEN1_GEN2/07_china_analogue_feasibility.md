# 07 — China Analogue Feasibility (Worker: china_feasibility_07)

**Date accessed:** 2026-06-28
**Scope:** Which frontier startup directions are feasible as China-first or China-early companies, across five domains. Engine-layer subsystem wedges only — no direct clones.
**Method:** Domain-level analysis grounded in authoritative non-article sources (gov.cn, NDRC/MIIT/NMPA, BIS, Federal Register, USITC, Congress/CRS, USCC, IEA, IFR, CAS) plus peer-reviewed Q1 articles, with journalism used only for timing. Company/press-release/trade-press claims are flagged WEAK_SIGNAL_ONLY.

---

## 0. How to read the labels

Every wedge below is tagged with EXACTLY one recommended posture:

- **China-first attractive** — strongest supply chain + buyer + policy alignment, manageable risk.
- **China-first possible but dangerous** — feasible but exposed to export-control, IP, or commodity risk that can kill it.
- **China-first not recommended** — China builds it faster but the venture is structurally undefensible there.
- **US-first then China manufacturing** — design/IP/certification anchored in US/allied jurisdiction, contract-manufacture or co-develop hardware in China.
- **Dual-track from day one** — two legal entities / two supply chains from inception to survive bifurcation.

---

## 1. China feasibility matrix by domain

Ratings: H = High, M = Medium, L = Low. "Advantage" columns: higher = better for a China-first founder. "Risk/Barrier" columns: higher = worse.

| Domain | China supply-chain advantage | Buyer access (China) | Policy tailwind | Commodity-competition risk | IP / copycat risk | Export-control / dual-use risk | US-expansion barrier | Overall feasibility & dominant posture |
|---|---|---|---|---|---|---|---|---|
| **1. Power / AI data-center infra** | H — transformer, switchgear, magnetics, SiC localization, world-largest storage manufacturing | H — hyperscalers, telco DCs, State Grid all domestic and reachable | H — East Data West Computing, PUE mandates, 180 GW storage-by-2027 plan | H — PSUs, cold plates, LFP packs commoditize fast | M — co-dev with hyperscalers leaks reference designs | M — power electronics mostly EAR99/low; SiC fab tools sensitive | H — UL/NRTL, NEC, utility trust, connected-firmware bans | **High / China-first attractive (with dual-track on firmware)** |
| **2. Semiconductor / adv. packaging / thermal** | M-H — OSAT depth (JCET, Tongfu, TFME), materials; weak on front-end tools | H — domestic AI-chip + foundry buyers want de-Americanized supply | H — strategic priority, large state funds | M — substrate/cold-plate commoditize; packaging IP less so | H — co-dev with OSAT/fabless leaks process flows | **H** — EUV/DUV SME, TC-bonder + advanced-packaging tools now targeted; Entity List | H — NDAA/1260H, hyperscaler vendor bans, fab tool re-export | **Medium / China-first possible but dangerous; US-first-then-China for tool-adjacent IP** |
| **3. Biomedical / high-end medtech** | M-H — manufacturing + domestic imaging/robot OEMs seeking local components | H — NMPA innovation fast-track, domestic-substitution procurement, huge patient volume | H — 10 high-end-device measures (2025), import-localization rules | M — low-end consumables commoditize; high-end detectors do not | M-H — OEM co-dev leakage; design-around of modules | M — genomic/health data export (PIPL, HGR rules); some US Biosecure exposure | **H** — FDA 510(k)/PMA, IEC 60601, clinical trust, hospital trust | **Medium-High / China-first attractive for components; US-first for clinical-data plays** |
| **4. Industrial / robotics / adv. manufacturing** | H — 54% of global robot installs, NdFeB monopoly, supplier density | H — domestic OEMs + humanoid programs are local and aggressive | H — humanoid action plan, RMB 10B fund, 15th FYP robotics priority | **H** — reducers, servos, frames, "whole humanoid" all commoditizing | H — fast copycat of mechanical subsystems | M — some embodied-AI/compute + magnet-export exposure | M-H — trust for connected robots, buy-American, data | **High / China-first attractive ONLY at sensing/controls/thermal layer; commodity-trap at the joint/frame** |
| **5. Extreme / HTS / cryo / nuclear / fusion / geothermal** | H — 2G REBCO tape scale-up, BEST/EAST, cryo supply chain, SMR commercial 2026 | H — fusion startups (ENN, Energy Singularity, Startorus), ASIPP/CAS, CNNC/CGN | H — fusion in strategic emerging industries; SMR commercialized | L-M — niche, not yet price-compressed | H — process IP leakage; few players, high mobility | **H** — HTS, cryogenics, nuclear are dual-use; Entity-List + 10 CFR 810 / NSG exposure | **H** — nuclear/fusion procurement nationalistic both sides; trust | **Medium / China-first possible but dangerous; dual-track or non-US-facing structure for HTS/nuclear** |

**One-line domain read:**
- Power: pursue China-first, isolate firmware/controls IP.
- Semis/packaging: the front-end is a trap; the **in-package thermal + substrate** adjacency is the opening, but tool-adjacency forces US-first or dual-track.
- Medtech: sell **components to domestic OEMs** China-first; keep clinical-data/AI plays US-first.
- Robotics: do NOT clone the joint; win at **tactile sensing, thermal-managed continuous-duty actuation, and control firmware**.
- Extreme: real frontier demand, but HTS/cryo/nuclear are the most export-control-radioactive — structure for it from day one.

---

## 2. High-potential China-first / China-early wedges (adjacent, defensible — NOT clones)

Each wedge: product → why China advantage → defensibility moat → kill criterion → label.

### Power / AI data-center infrastructure

**W1 — Megawatt-class medium-voltage DC (MVDC) "power sidecar" for AI clusters.**
Direct ~10–35 kV (or solid-state-transformer) feed to an 800 V DC busbar that bypasses the cascade of transformers/PSUs, co-designed with the rack. China advantage: domestic SiC device localization, the world's deepest magnetics/transformer supply chain, and domestic hyperscaler pilots created by the East-Data-West-Computing buildout. Moat: high-voltage control firmware, protection coordination, and rack-co-design know-how (not the silicon). Kill criterion: if hyperscalers standardize on a vendor-neutral 800 V spec that turns the converter into a commodity bid before you have a controls/qualification lock-in. **Label: China-first attractive.**

**W2 — Behind-the-meter grid-interactive controller + reversible-load orchestrator for AI campuses.**
Firmware/controller that arbitrages captive storage + renewables + curtailable training load against grid ancillary-service and the new capacity-price signals. China advantage: 74 GW/168 GWh of new storage installed in 2024, a 180 GW-by-2027 target, and an explicit capacity-price floor — i.e., the market signals this product monetizes already exist. Moat: interconnection know-how + dispatch algorithms + utility relationships. Kill criterion: grid operators internalize the function or mandate a closed protocol. **Label: China-first attractive.**

### Semiconductor / advanced packaging / thermal

**W3 — In-package / embedded microchannel cooling subsystem for 2.5D/3D AI accelerators.**
Silicon/interposer-integrated microfluidic cold structures and the manifold + leak-safe coolant interface, sold as a co-design service to OSATs. China advantage: OSAT depth (JCET XDFOI 2.5D in mass production; Tongfu, TFME) and a thermal-hardware manufacturing base; thermal is the gating frontier bottleneck that front-end controls do not touch. Moat: thermo-mechanical reliability data + bonding-compatible process flow co-owned with the OSAT. Kill criterion: a hyperscaler/foundry standardizes a competing in-package cooling reference that you cannot get designed-in against. **Label: China-first possible but dangerous** (TC-bonder/advanced-packaging tool controls can creep into your process; keep tool-independent).

**W4 — Glass-core / panel-level substrate process + warpage-control subsystem.**
Process IP and inline warpage/stress compensation for large glass-core panels feeding chiplet packages. China advantage: panel-level packaging investment wave and substrate-material localization push under tightening US restrictions. Moat: yield-recipe + metrology-fusion know-how. Kill criterion: substrate becomes a price-war commodity (see traps) before you own a yield edge. **Label: US-first then China manufacturing** (substrate IP is cleaner to anchor in an allied entity, then volume-manufacture in China).

### Biomedical / high-end medtech

**W5 — Photon-counting CT / spectral detector modules (CdZnTe/CZT) for domestic imaging OEMs.**
Detector tiles + ASIC readout + calibration, sold to United Imaging, Mindray, Neusoft Medical. China advantage: NMPA's 2025 high-end-device measures + import-localization rules + domestic OEMs actively de-risking from US/EU component dependence; imaging entered NMPA's top innovation categories. Moat: crystal growth yield + charge-sharing-correction firmware + calibration datasets. Kill criterion: a domestic OEM verticalizes detector growth in-house and locks you out. **Label: China-first attractive.**

**W6 — Sterilizable, high-torque-density force/haptic joint module for surgical & rehab robots.**
A "joint as a product": frameless motor + torque sensing + sterilization-survivable encoder + control loop, sold to MicroPort MedBot, Tinavi, and rehab-robot makers. China advantage: NMPA Announcement No. 63 (2025) explicitly fast-tracks medical robots; robotics-component supplier density. Moat: sterilization + biocompatibility qualification + force-control firmware. Kill criterion: surgical-robot OEMs treat the joint as a commodity motor + reducer purchase. **Label: China-first attractive.**

### Industrial / robotics / advanced manufacturing

**W7 — High-bandwidth tactile / electronic-skin sensing array + edge fusion for manipulation.**
Multimodal (force/shear/temperature/proximity) skin + on-sensor fusion, the gating bottleneck for embodied-AI dexterity. China advantage: 54% of global robot installs, the humanoid action plan + RMB 10B fund, and dozens of domestic humanoid OEMs (UBTech, Unitree, AgiBot/Zhiyuan, Fourier) that need hands that work. Moat: sensor MEMS/material + calibration + tactile-representation firmware that improves with deployment data. Kill criterion: a humanoid OEM open-sources a "good enough" skin and the market refuses to pay a premium. **Label: China-first attractive.**

**W8 — Continuous-duty, thermally-managed actuator leveraging domestic NdFeB.**
Not a commodity joint: an axial-flux or high-pole-count actuator with integrated liquid/conductive thermal path + sensor fusion + field-oriented control tuned for hours-long duty cycles (the humanoid endurance wall). China advantage: 85–90% NdFeB monopoly = magnet cost/availability edge unavailable to US founders. Moat: thermal + control + sensing integration and continuous-duty qualification data — NOT the magnet or the gearbox. Kill criterion: commoditization of the integrated joint (high risk — see traps); if margin compresses below qualification-cost recovery within 18 months, exit. **Label: China-first possible but dangerous.**

### Extreme / HTS / cryogenic / nuclear / fusion / geothermal

**W9 — REBCO (2G HTS) tape defect metrology + low-loss jointing subsystem.**
Inline tape critical-current mapping, defect classification, and a qualified low-resistance joint module for the magnet builders. China advantage: aggressive 2G HTS tape scale-up driving BEST (completion end-2027) and commercial fusion startups; tape capacity is being built domestically. Moat: process IP + qualification data that magnet integrators depend on. Kill criterion: tape makers internalize metrology/jointing; or US export-listing cuts you off from allied customers entirely. **Label: China-first possible but dangerous** (dual-use HTS — high listing exposure).

**W10 — HTS-magnet quench detection & active protection subsystem.**
Fiber-optic + electrical quench detection with fast magnet-protection logic — the safety engine layer every high-field HTS magnet (fusion, MRI-class, accelerator) needs. China advantage: a concentrated, fast-iterating domestic fusion-magnet customer base (ASIPP/CAS BEST/EAST, Energy Singularity, Startorus, ENN). Moat: detection algorithms + qualification across magnet designs + safety track record. Kill criterion: a magnet OEM standardizes its own protection IP, or the dual-use classification blocks the only scalable (allied) export markets. **Label: Dual-track from day one** (build a non-US-facing China entity AND an allied-jurisdiction entity to keep both fusion ecosystems reachable).

---

## 3. China commodity traps (price compression kills defensibility — DO NOT enter as a clone)

| Trap | Why it compresses | What survives instead |
|---|---|---|
| LFP cells / battery packs / generic BESS containers | National overcapacity, razor margins | Grid-interactive controls + capacity-market dispatch (W2) |
| Harmonic / cycloidal reducers, generic servo motors | Domestic substitution already crashed prices | Thermal + sensing + control-integrated actuator, qualified for continuous duty (W8) |
| "Whole humanoid robot" clones | Dozens of funded OEMs; race to the bottom | Sell the hand/skin/joint/brain subsystem, not the robot (W7, W8) |
| Commodity AC/DC PSUs and ORv3 power shelves | Standardized, multi-vendor bids | MVDC/SST power block with controls + rack co-design (W1) |
| Generic copper/aluminum liquid cold plates | Sheet-metal economics | In-package / embedded microchannel cooling co-designed with OSAT (W3) |
| Generic SiC substrates / wafers | Chinese substrate price war underway | SiC-enabled MV converter + protection firmware, not the wafer (W1) |
| Generic immersion / dielectric fluids (resold) | Pure resale margins; chemistry owned upstream | Only defensible if you own the fluid chemistry + thermal qualification |
| Low-end CMOS image sensors, basic ultrasound probes | Mature, commoditized | High-end CZT/photon-counting + spectral detector modules (W5) |
| Generic LiDAR / depth cameras | Brutal Chinese price war | Tactile/contact sensing where vision fails (W7) |
| Standard NdFeB magnets | China owns it but it is a commodity input | Use the magnet as a cost input inside a higher-integration actuator (W8) |

---

## 4. US-expansion barriers (trust, certification, export-control, procurement)

1. **Certification gates.** Medtech: FDA 510(k)/PMA + IEC 60601; clinical evidence built on China data is often re-required. Power: UL/NRTL listing, NEC, IEEE 1547/1741 for grid-interactive. Nuclear: NRC licensing (years). These are time-and-trust moats that a Chinese-origin entrant cannot shortcut.
2. **Procurement / blacklist exposure.** NDAA Section 889 (covered telecom/video), Section 1260H "Chinese military companies" list, FCC Covered List, and proposed connected-hardware / connected-vehicle rules can bar Chinese-origin or Chinese-controlled hardware from federal and critical-infrastructure buyers regardless of product merit.
3. **Hyperscaler / OEM vendor security review.** Data-center and medical buyers run supply-chain security and country-of-origin reviews; Chinese-controlled firmware in power, cooling, or robotics frequently fails on principle.
4. **CFIUS / FOCI.** Foreign Ownership, Control or Influence mitigation can block defense, energy, and sensitive-tech sales; equity from Chinese funds taints later US enterprise/government deals.
5. **Buy-American / domestic-content (IRA, BABA).** Tax credits and infrastructure dollars favor domestic-content power and storage hardware, structurally disadvantaging China-built systems.
6. **Trust tax on connected hardware.** Anything with networked firmware (robots, power controllers, medical devices) faces a default-suspicion premium that raises the evidentiary bar for the same spec.

**Implication:** for any wedge whose value is in **connected firmware/controls or regulated clinical use**, plan a US-first or dual-track structure; for **pure component/material wedges sold into allied OEM supply chains**, US-first-then-China manufacturing is cleaner.

---

## 5. Export-control / dual-use risk map (specific regimes)

### US outbound (restricts what reaches China — caps your China-side tech ceiling)
- **BIS / EAR Entity List:** Dec 2024 added ~140 China entities + Footnote 5 designations; Sept 16, 2025 final rule added 32 more (incl. Shanghai Fudan Microelectronics and affiliates) (Federal Register 2025-17893). 2025 also saw 42 (March) + 23 (Sept) PRC additions.
- **Affiliates / 50% rule (Sept 2025):** subsidiaries ≥50% owned by listed parties are swept in — widens contamination of Chinese supply chains you might depend on.
- **SME controls:** EUV and certain DUV lithography, plus etch/deposition/ion-implant/anneal/metrology/inspection/cleaning tools for advanced nodes (CRS R48642). Directly caps front-end semiconductor wedges and creeps toward **advanced-packaging TC-bonders**.
- **Advanced-computing / AI-chip controls (2024–2025):** restrict high-end accelerators into China — shapes which AI data-center hardware can even be deployed there.

### China outbound (your China entity becomes the controlled party)
- **MOFCOM Announcement No. 46 (Dec 3, 2024):** banned export to the US of dual-use items tied to **gallium, germanium, antimony, ultra-hard materials**; tightened graphite end-use review (CSET translation).
- **April 4, 2025 rare-earth controls:** licensing on **7 medium/heavy REEs** and all related metals/oxides/alloys/compounds and **NdFeB/SmCo magnets containing Tb or Dy**; light-REE-only magnets remain freely exportable (IEA).
- **Nov 2025 suspension (MOFCOM 72/2025):** Ga/Ge/Sb/superhard ban suspended through **Nov 27, 2026** — but NOT for US military end-users/end-use. This is a temporary truce, not a repeal; a China-first magnet/material wedge selling to the US lives under a switch Beijing can flip.
- **Export Control Law (2020) + Unreliable Entity List + dual-use catalog** govern HTS, cryogenics, and nuclear-adjacent tech.

### Domain dual-use heat (most → least)
1. **HTS / cryogenics / fusion magnets (W9, W10):** classic dual-use; highest two-sided listing risk.
2. **Nuclear / SMR (extreme domain):** 10 CFR Part 810, NSG, IAEA regime — nationalistic procurement both sides.
3. **Advanced packaging / thermal tool-adjacency (W3, W4):** SME-control creep.
4. **Rare-earth-leveraged actuators (W8):** China magnet-export switch + US 1260H.
5. **Medical genomic/health data plays:** China PIPL + Human Genetic Resources rules restrict outbound data; US Biosecure-style scrutiny inbound.

---

## 6. IP / copycat risk and how each wedge defends

**Structural China IP risks:** (a) OEM/SOE co-development contracts that vacuum reference designs; (b) rapid mechanical design-around of any subsystem whose value is geometry, not process; (c) talent mobility in small frontier fields (fusion, HTS, packaging); (d) trade-secret enforceability variance.

**Defensibility doctrine used above — moats that survive copying:**
- **Process + yield know-how** (CZT growth, glass-substrate warpage, REBCO jointing) — not patent-dependent.
- **Qualification / certification data** (continuous-duty actuators, sterilizable joints, quench protection) — expensive to reproduce, becomes the buyer's spec of record.
- **Firmware/controls that improve with deployment data** (tactile fusion, MVDC protection, grid dispatch) — a moving target, not a static blueprint.
- **Designed-in lock-in** with OSATs/OEMs (in-package cooling, detector modules) — switching cost, not secrecy.

**Anti-pattern to avoid:** any wedge whose only moat is a mechanical CAD file or a single patent. In China those are copied in quarters. This is exactly why W8 (commodity-adjacent actuator) is flagged "possible but dangerous," and why the joint/frame/reducer clones are listed as traps.

---

## 7. Recommended label per wedge (exact tags)

| Wedge | Domain | Recommended label |
|---|---|---|
| W1 — MVDC/SST power sidecar | Power / DC infra | **China-first attractive** |
| W2 — Grid-interactive / reversible-load controller | Power / DC infra | **China-first attractive** |
| W3 — In-package embedded microchannel cooling | Semis / packaging / thermal | **China-first possible but dangerous** |
| W4 — Glass-core / panel-level substrate process | Semis / packaging | **US-first then China manufacturing** |
| W5 — CZT photon-counting detector modules | Biomedical | **China-first attractive** |
| W6 — Sterilizable force/haptic joint module | Biomedical | **China-first attractive** |
| W7 — Tactile / e-skin sensing + fusion | Robotics | **China-first attractive** |
| W8 — Thermal-managed continuous-duty actuator (NdFeB) | Robotics | **China-first possible but dangerous** |
| W9 — REBCO tape metrology + jointing | Extreme / HTS | **China-first possible but dangerous** |
| W10 — HTS quench detection & protection | Extreme / HTS / fusion | **Dual-track from day one** |

**Explicit "not recommended" call-outs (clones, not wedges):** building a domestic clone of a US data-center PSU vendor, a humanoid-robot OEM clone, a harmonic-reducer maker, a generic LFP integrator, or a front-end lithography/EUV play — all **China-first not recommended** (commodity trap or export-control wall).

---

## 8. Thirty (30) China customer-discovery targets

Format: segment — buyer title — representative organizations — what to ask.

**Power / AI data-center infrastructure**
1. Hyperscale cloud infra — VP Data-Center Infrastructure — Alibaba Cloud, Tencent Cloud, ByteDance/Volcano Engine — "At what rack power density does your transformer/PSU cascade become the bottleneck, and would you pilot an MVDC feed?"
2. Telecom data centers — Chief Power Architect — China Mobile, China Telecom, China Unicom (IDC arms) — "What PUE and capex per MW are you held to under East-Data-West-Computing, and what blocks <1.2?"
3. AI-chip server OEMs — Director of Power Engineering — Inspur, H3C, Sugon — "Would you co-design an 800 V DC rack, and who owns the power-controller firmware?"
4. Grid / utility — Head of Ancillary Services — State Grid, China Southern Power Grid — "What do you pay for fast frequency response and capacity, and can a data-center load qualify?"
5. Energy-storage integrators — VP Engineering — Sungrow, Envision Energy, CATL (EnerOne) — "Where do controls (not cells) still cost you projects?"
6. Power-semiconductor makers — Product Director, SiC — StarPower, BYD Semiconductor, JingHe — "What MV converter reliability data would make you a design partner vs. a part vendor?"

**Semiconductor / advanced packaging / thermal**
7. OSAT advanced packaging — Director, 2.5D/3D R&D — JCET, Tongfu Microelectronics, TFME — "What is your junction-temperature ceiling on CoWoS-class parts, and would you co-develop in-package cooling?"
8. Fabless AI accelerators — VP Hardware / Thermal Lead — Cambricon, Biren, Moore Threads, Huawei HiSilicon (Ascend) — "What thermal limit caps your next part, and would you specify an embedded-cooling interposer?"
9. Substrate / interposer makers — CTO — SJ Semiconductor, domestic glass-substrate startups — "What yield/warpage problem most limits panel-level scale-up?"
10. Foundry packaging — Packaging Integration Manager — SMIC, Hua Hong — "Which packaging step is most tool-constrained under current import limits?"
11. Thermal-material suppliers — Application Engineering Lead — domestic TIM/vapor-chamber vendors — "Where does conventional cold-plate cooling fail your hottest customers?"

**Biomedical / high-end medtech**
12. High-end imaging OEM — VP Detector/Component Sourcing — United Imaging, Mindray, Neusoft Medical — "Which imaging-chain component are you most exposed on for US/EU supply, and would you qualify a domestic CZT module?"
13. Surgical-robot OEM — Chief Engineer, Actuation — MicroPort MedBot, Tinavi Medical — "What torque density + sterilization life would let you outsource the joint?"
14. Rehab / exoskeleton makers — Head of Hardware — Fourier Intelligence, Ai-Robotics — "Where do force-control and endurance limit clinical adoption?"
15. Hospital procurement — Director of Medical Equipment — top-tier Class III hospitals (e.g., Peking Union, Huashan) — "Under volume-based procurement, what makes you choose a domestic high-end system?"
16. IVD / bioinstrument makers — R&D Director — domestic mass-spec / sequencing instrument firms — "Which subsystem do you still import, and why?"
17. NMPA innovation-track applicants — Regulatory Affairs Director — firms in the Special Review pathway — "What component qualification slows your innovative-device approval?"

**Industrial / robotics / advanced manufacturing**
18. Humanoid OEM — VP of Hardware / Hand Lead — UBTech, Unitree, AgiBot (Zhiyuan), Fourier — "Is the bottleneck the hand (tactile) or the actuator endurance, and would you buy a subsystem?"
19. Humanoid OEM — Chief Robotics Scientist — Galbot, LimX Dynamics — "What contact-rich task fails today for lack of tactile sensing?"
20. Industrial-robot makers — Director of Core Components — Estun, Inovance, Efort — "Where are you still buying foreign sensing/control, and what would flip you domestic?"
21. Actuator / motor suppliers — Chief Engineer — Leaderdrive, domestic frameless-motor vendors — "What continuous-duty thermal limit are your customers hitting?"
22. EV / automotive manufacturing — Smart-Manufacturing Director — BYD, NIO, Li Auto plants — "Where do current robots fail in your line, and what sensing would fix it?"
23. Logistics / warehouse robotics — Head of Automation — JD Logistics, Cainiao — "What manipulation task can't be automated for lack of dexterity?"
24. Robotics innovation centers — Director — National-Local Humanoid Robot Innovation Centers (Beijing, Shanghai) — "Which shared component would you standardize across member OEMs?"

**Extreme / HTS / cryogenic / nuclear / fusion / geothermal**
25. Commercial fusion startups — Head of Magnets — Energy Singularity, Startorus Fusion, ENN Fusion — "What HTS tape defect rate or joint resistance most limits your magnet program?"
26. National fusion program — Magnet Systems Lead — ASIPP/CAS (EAST, BEST), CFETR team — "What quench-protection or tape-metrology gap would you fund externally?"
27. HTS tape / wire makers — VP Engineering — Shanghai Superconductor, Shanghai Creative Superconductor — "Where does inline critical-current mapping cost you yield?"
28. Cryogenics suppliers — Chief Engineer — domestic cryocooler / current-lead vendors — "What integration problem at the warm-to-cold interface recurs?"
29. Nuclear / SMR developers — Reactor I&C Lead — CNNC (Linglong One/ACP100), CGN, SPIC — "Which instrumentation or magnet-adjacent subsystem is still imported or unqualified?"
30. Geothermal / deep-drilling — Drilling Technology Director — Sinopec Green Energy, deep-geothermal pilots — "What downhole sensing or high-temperature electronics limits deeper wells?"

---

## 9. Thirty (30) US customer-discovery targets (for comparison)

Format: segment — buyer title — representative organizations — what to ask.

**Power / AI data-center infrastructure**
1. Hyperscalers — Distinguished Engineer, Power — Microsoft Azure, Google, AWS, Meta — "What is your roadmap to MV/800 V DC, and what controls do you require to be vendor-neutral?"
2. Neocloud / AI-native DCs — VP Infrastructure — CoreWeave, Crusoe, Lambda — "Where does power/cooling cap your GPU density today?"
3. Power-systems OEMs — Director of Product, Power Conversion — Vertiv, Eaton, Schneider Electric, Delta — "Build vs. partner on MVDC power blocks?"
4. Power-semis / converter — VP Engineering — Vicor, Navitas, Wolfspeed, GE Vernova — "What reliability data gates SiC into MV duty?"
5. Utilities / ISOs — Director, Interconnection & DER — PJM, ERCOT, Dominion, AEP — "Can a flexible AI load qualify for ancillary services, and what controls do you trust?"
6. Storage integrators — Head of Controls — Tesla Energy, Fluence — "Where do controls (not cells) decide projects?"

**Semiconductor / advanced packaging / thermal**
7. Foundry / IDM packaging — Director, Advanced Packaging — Intel Foundry, TSMC Arizona — "What junction-temp ceiling limits your next packaging node?"
8. OSAT (US ops) — Thermal Integration Lead — Amkor (Arizona), ASE US — "Would you co-develop in-package microchannel cooling?"
9. AI-accelerator vendors — VP Silicon/Thermal — NVIDIA, AMD, Broadcom, Tenstorrent — "What thermal limit caps performance, and would you spec embedded cooling?"
10. Substrate / glass-core — CTO — Absolics (SKC), domestic substrate startups — "What yield problem most limits panel-level scale-up?"
11. Thermal startups — Founder/CEO — JetCool, Frore, Mikros — "Where does your approach hit a packaging-integration wall?"

**Biomedical / high-end medtech**
12. Imaging OEM — VP, Detector R&D — GE HealthCare, Siemens Healthineers (US), Philips (US) — "What is your photon-counting detector supply strategy and where is it constrained?"
13. Surgical-robot OEM — Director, Actuation/Haptics — Intuitive Surgical, Medtronic (Hugo), Stryker — "What would let you outsource a sterilizable force-sensing joint?"
14. Rehab robotics — Head of Hardware — Ekso Bionics, ReWalk — "Where do force control and endurance limit reimbursement-grade use?"
15. Hospital systems — Director, Capital Equipment — Mayo, Cleveland Clinic, Kaiser — "What evidence/cert bar must a new high-end device clear?"
16. Bioinstrument makers — R&D Director — Thermo Fisher, Illumina, Bruker — "Which subsystem is most supply-constrained?"
17. Regulatory / reimbursement — VP Regulatory Affairs — mid-stage medtech startups — "What component qualification most delays your FDA path?"

**Industrial / robotics / advanced manufacturing**
18. Humanoid OEM — VP Hardware / Hand Lead — Figure, Tesla Optimus, Apptronik, Agility — "Is the bottleneck tactile sensing or actuator endurance, and would you buy a subsystem?"
19. Humanoid OEM — Chief Robotics Officer — Boston Dynamics, 1X, Sanctuary — "What contact-rich task fails for lack of tactile/force sensing?"
20. Industrial-robot makers — Director, Core Components — Rockwell, Teradyne (Universal Robots/MiR) — "Where are you sensing/control-limited?"
21. Actuator suppliers — Chief Engineer — Allied Motion, Moog, Kollmorgen — "What continuous-duty thermal limit are customers hitting?"
22. Automotive manufacturing — Smart-Manufacturing Director — Ford, GM, Tesla — "Where do robots fail on the line for lack of dexterity?"
23. Logistics robotics — Head of Automation — Amazon Robotics, Symbotic — "What manipulation task can't be automated today?"
24. Defense/dual-use robotics — Program Lead — Anduril, Shield AI — "What ruggedized sensing/actuation subsystem do you wish you could buy?"

**Extreme / HTS / cryogenic / nuclear / fusion / geothermal**
25. Commercial fusion — Head of Magnets — Commonwealth Fusion Systems, Tokamak Energy, Type One Energy — "What HTS tape/joint/quench gap would you fund?"
26. Fusion (non-magnet) — Chief Engineer — TAE Technologies, Helion, Zap Energy — "Which power/cryo subsystem is least mature?"
27. HTS conductor makers — VP Engineering — SuperPower (Furukawa), MetOx, Faraday Factory — "Where does inline metrology cost you yield?"
28. National labs — Magnet/Cryo Division Lead — PPPL, ORNL, Fermilab, LBNL — "What quench-protection or tape-qualification gap recurs across projects?"
29. Advanced nuclear / SMR — Reactor I&C Lead — NuScale, X-energy, Kairos Power, TerraPower — "Which instrumentation/magnet-adjacent subsystem is supply-constrained?"
30. Deep geothermal — Drilling Tech Director — Fervo Energy, Quaise Energy — "What downhole high-temperature sensing/electronics limits depth?"

---

## 10. CSV-ready source rows (for merger to paste into source_evidence_ledger.csv)

Header matches `source_evidence_ledger.csv`. `worker_id = china_feasibility_07`, `date_accessed = 2026-06-28`. Fields with commas are double-quoted. `used_in_candidate_ids = NA` (standalone run).

```csv
source_id,worker_id,date_accessed,source_title,source_url_or_citation,domain,source_tier,source_type,peer_reviewed_status,impact_quality,publication_date,geography,topic,claim_supported,direct_support,confidence,limitations,count_toward_evidence,used_in_candidate_ids,notes
CN07-001,china_feasibility_07,2026-06-28,"MOFCOM Announcement No. 46 (2024) on Strengthening Export Controls of Dual-Use Items to the US (CSET translation)",https://cset.georgetown.edu/publication/china-rare-earth-export-ban/,cross-domain,Tier1_authoritative_translation,policy_translation,not_peer_reviewed,authoritative_primary_translation,2024-12,China,"China ban on gallium germanium antimony ultra-hard exports to US","China banned export to the US of dual-use items tied to gallium germanium antimony and ultra-hard materials effective 2024-12-03",strong,high,"Think-tank-hosted translation; verify against MOFCOM original for legal use",yes,NA,"Export-control section 5; primary-document translation"
CN07-002,china_feasibility_07,2026-06-28,"Germanium and Gallium: U.S. Trade and Chinese Export Controls",https://www.usitc.gov/publications/332/executive_briefings/ebot_germanium_and_gallium.pdf,semiconductor,Tier1_authoritative_nonarticle,government_report,not_peer_reviewed,authoritative_government,2024,US,"US dependence on Chinese gallium/germanium","US imports significant Ga/Ge from China; controls create supply risk",strong,high,"Executive briefing, summary-level",yes,NA,"Supports commodity/export-control framing"
CN07-003,china_feasibility_07,2026-06-28,"Commerce Strengthens Export Controls to Restrict China's Capability to Produce Advanced Semiconductors",https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military,semiconductor,Tier1_authoritative_nonarticle,government_press_release,not_peer_reviewed,authoritative_government,2024-12,US,"BIS SME and Entity List tightening Dec 2024","BIS added ~140 entities and tightened SME (EUV/DUV) controls",strong,high,"Press release; pair with Federal Register rule text",yes,NA,"Export-control section 5"
CN07-004,china_feasibility_07,2026-06-28,"Additions and Revisions to the Entity List (Final Rule)",https://www.federalregister.gov/documents/2025/09/16/2025-17893/additions-and-revisions-to-the-entity-list,semiconductor,Tier1_authoritative_nonarticle,federal_rule,not_peer_reviewed,authoritative_government,2025-09-16,US,"Sept 2025 Entity List additions incl. Fudan Micro","BIS added 32 entities Sept 2025 including Shanghai Fudan Microelectronics and affiliates",strong,high,"Rule text; affiliates/50% rule interpretation needs counsel",yes,NA,"Export-control section 5"
CN07-005,china_feasibility_07,2026-06-28,"U.S. Export Controls and China: Advanced Semiconductors (CRS R48642)",https://www.congress.gov/crs-product/R48642,semiconductor,Tier1_authoritative_nonarticle,congressional_research,not_peer_reviewed,authoritative_government,2025-08,US,"Scope of US SME and advanced-computing controls","EUV/DUV, etch/deposition/metrology tools and AI-chip controls restrict China advanced nodes",strong,high,"Survey document",yes,NA,"Export-control + semiconductor domain"
CN07-006,china_feasibility_07,2026-06-28,"World Robotics 2025: Global robot demand in factories doubles over 10 years (IFR press release)",https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years,robotics,Tier1_authoritative_nonarticle,industry_association,not_peer_reviewed,authoritative_industry_assoc,2025-09,China,"China share of global robot installs and stock","China = 54% of 2024 global installations (295k units); operational stock >2 million; domestic suppliers 57% of home market",strong,high,"Association press summary; full report paywalled",yes,NA,"Robotics China advantage; verified via WebFetch"
CN07-007,china_feasibility_07,2026-06-28,"World Robotics 2025 China press release (IFR)",https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf,robotics,Tier1_authoritative_nonarticle,industry_association,not_peer_reviewed,authoritative_industry_assoc,2025-09-25,China,"China robot market detail","China largest market; domestic manufacturers outsell foreign for first time",strong,high,"Press release",yes,NA,"Robotics domain corroboration"
CN07-008,china_feasibility_07,2026-06-28,"China Achieves Milestone in Compact Fusion Project (BEST) — CAS",https://english.cas.cn/newsroom/cas_media/202510/t20251010_1088962.shtml,extreme_fusion,Tier1_authoritative_nonarticle,national_academy,not_peer_reviewed,authoritative_national_lab,2025-10,China,"BEST tokamak timeline and HTS magnets","BEST scheduled for completion end-2027; assembly began May 2025; uses superconducting magnets at -269C",strong,high,"Institutional news release",yes,NA,"Extreme/HTS/fusion domain; verified via WebFetch"
CN07-009,china_feasibility_07,2026-06-28,"Chinese 'Artificial Sun' (EAST) sets new record — CAS",https://english.cas.cn/newsroom/cas_media/202501/t20250121_899052.shtml,extreme_fusion,Tier1_authoritative_nonarticle,national_academy,not_peer_reviewed,authoritative_national_lab,2025-01,China,"EAST sustained high-confinement plasma record","EAST achieved a new long-pulse confinement record",strong,medium,"Institutional release; not a journal result",yes,NA,"Fusion ecosystem maturity"
CN07-010,china_feasibility_07,2026-06-28,"China's share in rare earth magnet production, 2024 (IEA chart)",https://www.iea.org/data-and-statistics/charts/china-s-share-in-rare-earth-magnet-production-2024,industrial,Tier1_authoritative_nonarticle,international_agency,not_peer_reviewed,authoritative_international_agency,2024,China,"China NdFeB magnet production dominance","China holds ~85-90% of NdFeB magnet production and dominates separation/refining",strong,high,"Chart with methodology page",yes,NA,"Robotics/actuator + commodity-trap analysis"
CN07-011,china_feasibility_07,2026-06-28,"With new export controls on critical minerals, supply concentration risks become reality (IEA)",https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality,cross-domain,Tier1_authoritative_nonarticle,international_agency,not_peer_reviewed,authoritative_international_agency,2025,China,"China rare-earth/magnet export-control leverage","April 2025 controls cover 7 medium/heavy REEs and Tb/Dy-containing magnets via licensing",strong,high,"Commentary; cites underlying measures",yes,NA,"Export-control section 5"
CN07-012,china_feasibility_07,2026-06-28,"NMPA Announcement No. 30 (2025) on production of imported medical devices in domestic enterprises",https://english.nmpa.gov.cn/2025-06/11/c_1102170.htm,biomedical,Tier1_authoritative_nonarticle,regulator,not_peer_reviewed,authoritative_regulator,2025-06,China,"China policy supporting domestic localization of medical devices","NMPA facilitating domestic production/localization of high-end imported devices",strong,medium,"Policy notice; implementation detail evolving",yes,NA,"Medtech China-first wedge support"
CN07-013,china_feasibility_07,2026-06-28,"China's new energy storage capacity exceeds 70 million kW (gov.cn)",https://english.www.gov.cn/archive/statistics/202501/24/content_WS6793830cc6d0868f4e8ef23f.html,power,Tier1_authoritative_nonarticle,government_statistics,not_peer_reviewed,authoritative_government,2025-01,China,"China new-type storage installed base 2024","Installed new energy storage reached ~73.76 GW end-2024, up >130% YoY",strong,high,"Official statistics summary",yes,NA,"Power domain policy tailwind (W2)"
CN07-014,china_feasibility_07,2026-06-28,"China unveils three-year action plan to boost new-type energy storage (gov.cn)",https://english.www.gov.cn/news/202509/12/content_WS68c3ccbec6d00fa19f7a263f.html,power,Tier1_authoritative_nonarticle,government_policy,not_peer_reviewed,authoritative_government,2025-09,China,"Storage scale-up policy target","Action plan targets large-scale new-type storage expansion (180 GW-class by 2027)",strong,medium,"Policy announcement",yes,NA,"Power domain W2 tailwind"
CN07-015,china_feasibility_07,2026-06-28,"Humanoid Robots (USCC staff report)",https://www.uscc.gov/sites/default/files/2024-10/Humanoid_Robots.pdf,robotics,Tier1_authoritative_nonarticle,government_commission,not_peer_reviewed,authoritative_government,2024-10,US-China,"China humanoid policy and state support","China MIIT humanoid guidance, ~RMB 10B fund, 2025/2027 targets, state-backed ecosystem",strong,high,"Commission analysis; some interpretive",yes,NA,"Robotics policy tailwind + competitive context"
CN07-016,china_feasibility_07,2026-06-28,"The Eastern Data and Western Computing Initiative Contributes to China's Net-Zero Target (Engineering, CAE)",https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.08.010,power,Tier2_peer_reviewed,journal_article,peer_reviewed,Q1_high_impact,2024,China,"East-Data-West-Computing scale, PUE targets, liquid cooling","EDWC drives 8 national hubs, PUE<1.2 goals via liquid cooling, large server-rack buildout",strong,medium,"Policy-analysis article; triangulate exact figures with NDRC",yes,NA,"Power/DC infra tailwind (W1)"
CN07-017,china_feasibility_07,2026-06-28,"Greening China's digital economy: East-West Computing and CO2 reduction (Humanities & Social Sciences Communications)",https://www.nature.com/articles/s41599-024-02963-0,power,Tier2_peer_reviewed,journal_article,peer_reviewed,Q1,2024,China,"EDWC data-center decarbonization","EDWC reallocates compute to renewable-rich western hubs reducing emissions",moderate,medium,"Social-science modeling; macro not customer-pain",yes,NA,"Power domain triangulation"
CN07-018,china_feasibility_07,2026-06-28,"China's HVDC development for large-scale renewable integration: a system-level technology roadmap (Int. J. Electrical Power & Energy Systems)",https://www.sciencedirect.com/science/article/pii/S0142061526003741,power,Tier2_peer_reviewed,journal_article,peer_reviewed,Q1,2026,China,"China UHV/HVDC roadmap and SiC status","SiC benchmarked for UHVDC; press-pack packaging/reliability gaps remain before main-valve use",moderate,medium,"Roadmap article; verify journal issue",yes,NA,"Power-electronics wedge realism (W1)"
CN07-019,china_feasibility_07,2026-06-28,"Status of High-End Performance Packaging 2.5D and 3D (SEMI)",https://www.semi.org/sites/semi.org/files/2025-06/21_Vishal%20Saroha.pdf,semiconductor,Tier1_authoritative_nonarticle,industry_association,not_peer_reviewed,authoritative_industry_assoc,2025-06,Global,"Advanced packaging thermal and integration bottlenecks","2.5D/3D high-end packaging is thermally and integration constrained",moderate,medium,"Conference slide deck",yes,NA,"Semiconductor thermal wedge (W3)"
CN07-020,china_feasibility_07,2026-06-28,"China to launch first commercial SMR Linglong One (ACP100) — World Nuclear News",https://www.world-nuclear-news.org/articles/chinese-smr-completes-non-nuclear-steam-start-up-test,extreme_nuclear,Tier3_journalism,trade_journalism,not_peer_reviewed,trade_press_timing_only,2025-12,China,"China SMR commercialization timing","ACP100 Linglong One targeting commercial operation 2026 in Hainan",moderate,medium,"Trade press; timing only not customer-pain proof",no,NA,"Extreme/nuclear timing signal"
CN07-021,china_feasibility_07,2026-06-28,"China suspends some export controls on dual-use items to US (Global Times)",https://www.globaltimes.cn/page/202511/1347727.shtml,cross-domain,Tier3_journalism,state_media,not_peer_reviewed,journalism_timing_only,2025-11,China,"Nov 2025 suspension of Ga/Ge/Sb ban to US","Ban suspended to 2026-11-27 but not for US military end-use",moderate,low,"State media; corroborate with MOFCOM 72/2025 original",no,NA,"Export-control truce timing"
CN07-022,china_feasibility_07,2026-06-28,"Domestic Chinese TC Bonder completes CoWoS-L test sampling (trade/press release)",globalsmt.net / vendor press release (PrecisioNext Loong series),semiconductor,Tier4_weak_signal,vendor_press_release,not_peer_reviewed,company_claim,2025,China,"China advanced-packaging tool localization progress","A domestic TC-bonder reportedly completed CoWoS-L test sampling",weak,low,"Vendor/press-release claim; not independently verified",no,NA,"WEAK_SIGNAL_ONLY; replace with SEMI/primary before scoring"
CN07-023,china_feasibility_07,2026-06-28,"China humanoid robot mass-production targets (MIIT guidance, via trade coverage)",therobotreport.com / SCMP coverage of MIIT 2023 guidance,robotics,Tier3_journalism,journalism,not_peer_reviewed,journalism_timing_only,2023-11,China,"MIIT humanoid targets 2025/2027","MIIT 2023 guidance set 2025 innovation-system and 2027 growth-engine targets",moderate,medium,"Journalism; corroborated by USCC report CN07-015",no,NA,"Timing; primary policy is MIIT original"
CN07-024,china_feasibility_07,2026-06-28,"China advanced packaging acceleration with HBM/CoWoS amid US restrictions (trade press)",globalsmt.net advanced-packaging coverage,semiconductor,Tier3_journalism,trade_journalism,not_peer_reviewed,journalism_timing_only,2025,China,"China OSAT advanced-packaging push","JCET XDFOI 2.5D in mass production; Tongfu CoWoS cooperation",moderate,low,"Trade press; OEM claims; timing only",no,NA,"WEAK_SIGNAL_ONLY for capacity specifics"
```

---

## Worker self-report

**Labels assigned per domain (dominant posture):**
- **Power / AI data-center infra:** High feasibility — **China-first attractive** (W1, W2), with firmware kept dual-track.
- **Semiconductor / advanced packaging / thermal:** Medium — **China-first possible but dangerous** (W3) and **US-first then China manufacturing** (W4); front-end is a no-go.
- **Biomedical / high-end medtech:** Medium-High — **China-first attractive** for components (W5, W6); keep clinical-data/AI plays US-first.
- **Industrial / robotics / advanced manufacturing:** High at the sensing/controls/thermal layer — **China-first attractive** (W7) but **possible-but-dangerous** at the actuator (W8); joints/frames/reducers are commodity traps.
- **Extreme / HTS / cryo / nuclear / fusion:** Medium — **China-first possible but dangerous** (W9) and **Dual-track from day one** (W10) due to dual-use/export-control exposure.

**Sourcing:** 24 source rows produced. **count_toward_evidence = yes: 19** (authoritative non-article from BIS, Federal Register, CRS, USITC, USCC, IFR, IEA, CAS, NMPA, gov.cn, SEMI; plus 3 peer-reviewed Q1/Q2 journal articles — Engineering/CAE, Nature HSSC, IJEPES). **count_toward_evidence = no / timing or WEAK_SIGNAL_ONLY: 5** (World Nuclear News, Global Times, two trade-press/vendor advanced-packaging claims, MIIT-via-journalism). Two of these (CN07-022, CN07-024) are explicitly flagged WEAK_SIGNAL_ONLY and need primary replacement before any candidate is scored.

**Gaps I could not fully verify:**
- Exact MIIT humanoid-guidance figures (RMB 10B fund, 2025/2027 targets) are corroborated by the USCC report (counts) but the primary MIIT Chinese-language notice was not directly fetched.
- China domestic advanced-packaging *capacity/yield* specifics rest on trade press / vendor claims (WEAK_SIGNAL_ONLY); SEMI deck (CN07-019) anchors only the general thermal-bottleneck claim, not Chinese capacity numbers.
- The two peer-reviewed power articles (CN07-016/017/018) were quality-classified from journal identity and search metadata; final JCR quartile for the 2026 IJEPES roadmap article should be confirmed by the source auditor.
- MOFCOM Announcement 72/2025 (Nov 2025 suspension) was read via CSET/Global Times secondary sources, not the MOFCOM original.
