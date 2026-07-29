# Prompt 11 — China Feasibility Deep Dive (China-Feasibility-Analyst Deliverable)

**Date:** 2026-06-29
**Role:** China-feasibility analyst. Executes `prompts/11_china_feasibility_deep_dive.md` under the binding rules of `merge_outputs/10E_premerge_package_for_ranking.md` §3 (rule 8: China posture is candidate-specific and binding) and `CLAUDE.md` anti-patterns.

---

## Provenance note (binding scope)

- **Scope = the TOP 15 ranked clusters** taken from `merge_outputs/frontier_rank_red_team.md`, Deliverable 1, ranks 1–15. The Top 15 in this file were re-confirmed against that ranking; no other candidate is introduced.
- **Unit = the cluster** (`candidate_id` = cluster id). The 10 deliverables per cluster are built from the member-candidate rows in `merge_outputs/parallel_merge.md` (`china_wedge`, `us_wedge`, `cleanroom_dependency`, `capex_band`, `reg_export_risk`, `competitors`, `defensibility`, `customer_pain`/`first_customer`/`buyer_title`), the cluster definitions + `china_posture` + notes in `merge_outputs/frontier_merge_cluster_map.csv`, and the ranking notes/red-team failure cases.
- **Labels are consistent with the binding 10E `china_posture`.** Posture→label mapping: CHINA_FIRST_ATTRACTIVE → "China-first attractive"; DUAL_TRACK → "Dual-track from day one"; US_FIRST_THEN_CHINA_MFG → "US-first then China manufacturing"; CHINA_FIRST_DANGEROUS → "China-first possible but dangerous". **No deviations from the binding posture are proposed in this pass** (any deviation would be flagged explicitly; none was warranted).
- **Source discipline:** company sources = claims only; market reports = triangulation only; journalism = timing/triangulation only. None is treated as customer-pain proof. Supply-chain/copycat/partner detail mined from `worker_outputs/07_china_analogue_feasibility.md` is used as triangulation only and admitted **no new candidate**. Customer-pain anchors rest on the peer-reviewed/authoritative-non-article evidence each cluster cleared on (10C/10E).
- **"No direct company-copy" rule (prompt 11) honored:** every candidate is given an *adjacent, defensible subsystem/engine-layer wedge*, not a clone of Hinetics or any named company. The two CHINA_FIRST_DANGEROUS clusters (CL-19, CL-14) each carry an explicit adjacent wedge plus a copycat-survival argument in deliverables 5 and 7.
- **Penalties applied per task:** over-cleanroom-with-no-outsourcing, commodity/margin traps, regulatory speculation-as-fact, and "China clone without a wedge" are called out where they bite.

---

# Candidate deep-dives (15)

---

## 1. CL-07 — Chip-Package Thermal Boundary Shift (Semiconductor)

**Binding posture:** CHINA_FIRST_ATTRACTIVE · Rank 1 (score 84) · members SEM-01/03/08/16/18.
**Adjacent defensible wedge:** a **die-height-compensating, in-package near-junction microfluidic cooling engine** co-developed with an OSAT (topology-matched Si/Cu manifold + leak-safe rack fluidic interface + anti-pump-out LM TIM), sold as a co-design service. This is the engine layer, **not** a commodity copper cold plate (which is an explicit China trap).

1. **China-first attractiveness — HIGH.** Thermal is the gating bottleneck for every >2 kW accelerator package and is *unregulated* hardware that front-end tool controls do not touch. China has OSAT depth and a thermal-hardware manufacturing base, and domestic AI-chip buyers actively want de-Americanized cooling. Capex is low ($5–20M; Si etch outsourceable), founder-pilotable. Pain is anchored to peer-reviewed thermal limits (IEEE TCPMT 2025; imec IEDM 2025), not vendor claims.
2. **First Chinese customer segment.** OSAT advanced-packaging lines (2.5D/3D R&D directors) and domestic fabless AI-accelerator thermal leads — buyers who own a junction-temperature ceiling on CoWoS-class parts and would co-develop an embedded-cooling interposer. Buyer title: Director 2.5D/3D R&D / VP Hardware-Thermal.
3. **First US customer segment.** AI-accelerator vendors and US-ops OSATs (VP Advanced Packaging / Director Thermal) co-developing a >2 kW package; secondary hyperscaler liquid-cooling integrators for the rack fluidic-interconnect/quick-disconnect layer (SEM-18).
4. **Supply-chain advantage in China.** Etched-Si/skived-Cu manifold fabrication, OSAT co-integration, and gallium supply for the LM TIM (SEM-16) are all domestically dense. China leads gallium supply and LM-TIM research — a genuine materials edge unavailable to a US founder.
5. **Commodity/copycat risk in China — MODERATE, manageable.** Generic copper/aluminum cold plates are a price-war trap; the *manifold geometry* alone is copyable. Survives because the moat is **per-SKU thermo-mechanical reliability/qualification data + bonding-compatible process flow co-owned with the OSAT** (designed-in lock-in), not a CAD file. SEM-16 anti-pump-out barrier-metallization chemistry adds a process moat.
6. **Regulatory/export-control risk — MIXED by sub-engine.** The core microfluidic cooler is low/EAR99-class. But two members carry real exposure: SEM-03 GaN-on-diamond is export-controlled GaN RF (defense, HIGH) and is itself DUAL_TRACK; SEM-08 backside-power couples to leading-edge nodes (export-controlled). SEM-16 depends on gallium, which sits under MOFCOM Ga/Ge/Sb outbound controls (Dec 2024 ban; Nov 2025 MOFCOM 72/2025 suspension to 2026-11-27 but **not** for US military end-use) — a switch Beijing can flip. Treat the gallium-LM and GaN-diamond arms as conditional, not the headline.
7. **IP strategy.** Trade-secret the manifold/flow recipe and barrier-metallization chemistry; lock reliability/qual datasets into the OSAT spec-of-record (switching cost). Keep the GaN-on-diamond bonding know-how in an allied entity (defense/export). Do not rely on a single cooling-geometry patent.
8. **Local partner requirement — REQUIRED.** An OSAT co-development partner is the wedge (designed-in lock-in and the outsourcing path for Si etch). Without an OSAT design-in, this degrades to a cold-plate vendor.
9. **US expansion path.** Sell the manifold + leak-safe QD as a co-design to US accelerator vendors/OSATs; the rack fluidic-interconnect standard (SEM-18) is the cleanest US entry (no export friction). Keep GaN-diamond US-only.
10. **Go/no-go — GO (China-first), with the GaN-diamond/gallium arms hedged.**

**Label: China-first attractive**

---

## 2. CL-18 — HTS Magnet Protection, Charging & Control (Extreme)

**Binding posture:** DUAL_TRACK · Rank 2 (score 83) · members EXT-01/04/09/19.
**Adjacent defensible wedge:** a **distributed fiber-optic quench detection-to-actuation loop** (co-wound OFDR + FPGA trip to dump/heaters) plus model-based charging/ramp control — the safety/control engine every high-field HTS magnet needs. Detection-to-actuation, **not** monitoring; **not** a magnet clone.

1. **China-first attractiveness — MEDIUM (hence dual-track, not China-first).** The pain is real and engine-layer-clear, and China has a concentrated, fast-iterating fusion-magnet customer base (ASIPP/CAS EAST/BEST, Energy Singularity, Startorus, ENN). But HTS is classic dual-use with the highest two-sided listing exposure, and the allied fusion ecosystem (CFS/Tokamak Energy/Type One) is equally important and cannot be reached from a China-only entity. Two entities from day one is the only structure that keeps both ecosystems reachable.
2. **First Chinese customer segment.** National + commercial fusion magnet programs — Head of Magnets / Magnet Systems Lead at ASIPP (EAST/BEST), Energy Singularity, Startorus, ENN. Pain: an undetected quench destroys a multi-million-dollar coil; voltage-tap detection is too slow/noisy in tokamak EM noise.
3. **First US customer segment.** Private fusion magnet developers (CFS, Tokamak Energy, Type One) — Head of Magnet Engineering / Diagnostics & Control Lead; secondarily NHMFL-class high-field science magnets for the charging/ramp controller (EXT-04/19).
4. **Supply-chain advantage in China.** Domestic fiber, optics, and FPGA supply; ASIPP cryogenics/charging heritage (CHMFL 45T-class). Co-location with domestic REBCO scale-up shortens iteration loops.
5. **Commodity/copycat risk in China — LOW-MODERATE.** Few players, but high talent mobility in a small field. Survives on **calibration datasets across REBCO geometries + trip-latency IP + a safety track record** (qualification-data moat) — expensive to reproduce and becomes the magnet builder's spec of record.
6. **Regulatory/export-control risk — HIGH (dual-use), the gating reason for dual-track.** HTS/cryogenics/fusion magnets are export-radioactive on both sides: US Entity List/BIS exposure and China's Export Control Law + dual-use catalog. Fusion procurement is nationalistic both ways. This is structural, not speculative.
7. **IP strategy.** Two legal entities, two data vaults. Keep the trip-logic firmware and calibration datasets partitioned per jurisdiction; license the *interface* (sensor+trip spec) rather than the geometry. Patents are secondary to qualification data.
8. **Local partner requirement — REQUIRED on both sides.** A magnet-program co-development partner in each ecosystem (one PRC, one allied) is needed to qualify across coil designs.
9. **US expansion path.** Direct: qualification + integration sold to US private fusion via the allied entity. Clean because the value is safety qualification, not a controlled component (the interrogator can be allied-sourced).
10. **Go/no-go — GO, but only with the two-entity dual-track from inception.** Red-team risk: voltage-tap + inductive compensation reaching adequate latency by 2028, and a tiny/in-sourcing buyer set.

**Label: Dual-track from day one**

---

## 3. CL-10 — Hybrid-Bonding & Advanced-Packaging Process-Control (Semiconductor)

**Binding posture:** US_FIRST_THEN_CHINA_MFG · Rank 3 (score 82) · members SEM-05/15/20, IND-13/19 (SEM-24 excluded, SEM-19 absorbed).
**Adjacent defensible wedge:** a **closed-loop inline hybrid-bond metrology head that actuates the bonder** (100% wafer IR-void + sub-50nm overlay + Cu-recess → corrective bonder recipe at throughput). Engine-layer APC, **not** a metrology clone of KLA/Onto.

1. **China-first attractiveness — LOW-to-MEDIUM (US-first by posture).** Back-end metrology is China's weakest localized layer (an import-substitution pull exists), but the cluster is **export-controlled both ways**: US SME controls (CRS R48642) are creeping toward advanced-packaging TC-bonders, which largely forecloses the China-manufacturing second leg and caps the addressable market to US/Korea fabs. Anchor IP in the US/allied jurisdiction; treat China as a later contract-manufacturing leg only.
2. **First Chinese customer segment (later leg).** Domestic HBM/3D-IC and OSAT process/yield managers seeking de-Americanized back-end metrology — but only reachable once the tool-export posture is navigated. Not the launch market.
3. **First US customer segment.** US/Korea HBM/3D-IC makers and OSATs ramping hybrid bonding (Director Packaging Process / Yield Eng Mgr), with a bonder-OEM co-integration partner. EM-screening (SEM-15) and wafer-thinning/handling (SEM-20) are adjacent reliability gates.
4. **Supply-chain advantage in China.** Real but largely inaccessible for the launch product because of tool-export controls; the OSAT density that helps CL-07 does not rescue an export-controlled metrology/placement tool.
5. **Commodity/copycat risk in China — secondary to the export wall.** The moat is **closed-loop APC algorithms + bonder co-integration + a defect-data network** (a moving target that improves with deployment), not the camera. IND-19 (D2W placement) is the highest-risk member: it cannot reach economics without fab co-development it may never get, and is the most export-exposed.
6. **Regulatory/export-control risk — HIGH, both directions.** US SME/advanced-packaging-tool controls outbound; China inbound restrictions. This is the binding reason the cluster is US-first, not a speculation.
7. **IP strategy.** US/allied entity owns the APC control IP and bonder-co-integration; build a defect-classification data flywheel as the durable moat. Do not export the corrective-recipe engine into a PRC entity.
8. **Local partner requirement.** A bonder OEM (allied) co-integration partner is essential — the metrology must write the bonder recipe. A PRC fab partner is relevant only for a much-later, carefully-scoped manufacturing leg.
9. **US expansion path — the primary path.** Standalone inline head (2026) → closed-loop with a bonder OEM (2027) → integrated (2028), selling into US/Korea HBM/3D-IC ramps. Red-team: KLA/Onto/Bruker bundle APC into their metrology, or hybrid bonding ramps slower than HBM4 roadmaps.
10. **Go/no-go — GO US-first; China manufacturing leg only post-traction and post-export-clearance.**

**Label: US-first then China manufacturing**

---

## 4. CL-12 — Power-Module & WBG Packaging/Manufacturing (Industrial)

**Binding posture:** CHINA_FIRST_ATTRACTIVE · Rank 4 (score 82) · members IND-08, SEM-10/12/17/23.
**Adjacent defensible wedge:** a **silver-sinter die-attach cell with INLINE acoustic void metrology + closed-loop process control**, paired with SiC inline-PL feed-forward yield control (SEM-12). The wedge is the inline-metrology + closed-loop process IP, **explicitly not the sinter press** (presses are sold by ASMPT et al. — a localization clone with no moat).

1. **China-first attractiveness — HIGH.** China's SiC/GaN build-out is the largest, capex is modest ($8–20M), founder-pilotable, and the pain (voids degrading large-area joint reliability) is anchored to peer-reviewed large-area-sinter studies. A genuine China-first process-IP wedge, not a clone.
2. **First Chinese customer segment.** SiC/GaN power-module makers for EV-traction and grid converters — Director Power-Module Packaging / Process Eng (StarPower, BYD Semiconductor, JingHe class). They own the void/reliability pain on large die.
3. **First US customer segment.** US/EU SiC fabs and EV/grid module makers wanting non-China high-reliability modules (Wolfspeed, onsemi, Coherent for SEM-12 defect feed-forward; Denso/Bosch-class for SEM-10 double-sided modules).
4. **Supply-chain advantage in China.** Deep SiC/sintered-Ag and ceramic (Si3N4 AMB, SEM-23) capacity; localization of AMB substrate is a stated priority. China leads SiC + sintered-Ag volume.
5. **Commodity/copycat risk in China — HIGH if mis-scoped, defused by the wedge.** If sampled offline C-SAM stays "good enough" and paste chemistry trivializes void control, the differentiator collapses to a metrology add-on and it becomes a press-localization clone. Survives ONLY because the wedge is **inline void metrology + closed-loop control + large-area reliability/power-cycle data** (process + qualification moat). SEM-12 must stay *feed-forward control*, not diagnostics-only, or it degrades to the commodity-inspection trap.
6. **Regulatory/export-control risk — LOW-MODERATE.** Power modules are largely EAR99/low; SiC *fab/inline tools* carry some sensitivity, and gallium (for the GaN member SEM-17) sits under MOFCOM outbound controls. No clinical/ITAR exposure.
7. **IP strategy.** Trade-secret the acoustic void-map analytics + closed-loop drying/pressure recipe and the SiC-PL classifier; build a per-joint reliability database as the spec-of-record. Avoid relying on the press hardware (commodity).
8. **Local partner requirement — RECOMMENDED, not gating.** A module-maker design-in partner accelerates qualification; the cell itself is founder-buildable.
9. **US expansion path.** Sell the inline-metrology + control engine (tool-in-customer-fab model) to US/EU SiC makers as a resilience play; SEM-12 defect feed-forward is the cleanest US entry.
10. **Go/no-go — GO (China-first), conditioned on holding the inline-metrology/closed-loop moat (not the press).**

**Label: China-first attractive**

---

## 5. CL-15 — Force / Tactile Sensing Engine (Industrial)

**Binding posture:** CHINA_FIRST_ATTRACTIVE · Rank 5 (score 80) · members IND-03, IND-12, IND-23, BIO-002.
**Adjacent defensible wedge:** a **contact-sensing engine** — full-hand super-resolution e-skin (IND-03) + overload-tolerant self-compensating 6-axis F/T (IND-12) with on-sensor fusion firmware. Win at the sensing/representation layer where vision fails; **do not** clone joints/frames (the commodity trap) or LiDAR (price-war).

1. **China-first attractiveness — HIGH.** Tactile is the gating bottleneck for embodied-AI dexterity, and China has 54% of global robot installs (IFR triangulation), a humanoid action plan + RMB-10B-class fund (USCC triangulation), and dozens of domestic humanoid OEMs needing hands that work. Lowest capex in the pool ($4–15M).
2. **First Chinese customer segment.** Humanoid OEMs — VP Hardware / Hand Lead at UBTech, Unitree, AgiBot (Zhiyuan), Fourier — for the e-skin and 6-axis F/T; the buyer's pain is contact-rich tasks failing for lack of tactile sensing.
3. **First US customer segment.** US humanoid OEMs wanting robust non-China critical sensing (Figure, Apptronik, Agility, Tesla Optimus). BIO-002 (FBG force-sensing catheter tip) is the surgical crossover and is candidate-specific **US-first** (robotic/EP catheter OEMs).
4. **Supply-chain advantage in China.** Flex-electronics/MEMS foundry access (outsourceable), robotics-component supplier density, and a local humanoid customer base for fast deployment-data loops.
5. **Commodity/copycat risk in China — MODERATE.** Manufacturable, so commoditization pressure is real if an OEM open-sources a "good-enough" skin. Survives on **super-resolution reconstruction + multimodal-fusion firmware that improves with deployment data + overload-tolerant mechanics/thermal-comp algorithm** (moving-target + cost-at-volume moat). Durability (abrasion/wash) is the unproven risk that must be designed in.
6. **Regulatory/export-control risk — LOW for robotics tactile; MEDIUM trust-tax in the US.** Sensors are low-export. The US barrier is the connected-firmware/country-of-origin "trust tax" on robot hardware, not an export ban. BIO-002 carries Class II/III medical validation (low export).
7. **IP strategy.** Trade-secret the super-res + fusion algorithms and the overload-tolerance + GRU temp-comp (IEEE Sensors Journal-anchored); build a tactile-representation dataset flywheel. Avoid a single-sensor-geometry patent (copied in quarters).
8. **Local partner requirement — RECOMMENDED.** Co-develop the full-hand stack with a humanoid OEM to integrate into their control loop and lock in.
9. **US expansion path.** License the sensing module + fusion firmware to US humanoid OEMs as a differentiated non-China subsystem; enter surgical via BIO-002 (US-first FDA path).
10. **Go/no-go — GO (China-first) at the sensing layer; keep the surgical (BIO-002) arm US-first.**

**Label: China-first attractive**

---

## 6. CL-09 — CPO Optical Assembly & Test (Semiconductor)

**Binding posture:** US_FIRST_THEN_CHINA_MFG · Rank 6 (score 79) · members SEM-06, SEM-07, SEM-22 (WATCH), IND-06 absorbed.
**Adjacent defensible wedge:** an **instrumented sub-100nm active-alignment fiber-attach (FAU) assembly cell** plus left-shifted wafer-level optical KGD that feeds forward die disposition. The engine that owns the CPO fiber-attach bottleneck — **not** a clone of ficonTEC/PI alignment platforms.

1. **China-first attractiveness — LOW-MEDIUM (US-first by posture).** Domestic Si-photonics needs home-grown assembly tools, but the assembly-tool/photonics adjacency (high-power lasers, ATE test) leans US/allied-first; the value is in alignment algorithms + yield correlation, cleaner to anchor in an allied entity, then volume-manufacture later.
2. **First Chinese customer segment (later leg).** Domestic CPO/optical-engine makers and photonics OSATs once the cell is proven — Director Photonics Packaging. Not the launch market.
3. **First US customer segment.** CPO switch/optical-engine makers and US photonics fabs/OSATs (VP Optical Engineering) running hyperscaler CPO programs; the fiber-attach yield/throughput bottleneck dominates PIC cost.
4. **Supply-chain advantage in China.** Photonics assembly labor and module localization (SEM-07 detachable connector / remote laser) are real, but the launch wedge depends on alignment IP, not assembly labor.
5. **Commodity/copycat risk in China — MODERATE.** If photonic-wire-bonding / passive (V-groove) alignment reaches volume parity, the active-alignment cell is over-engineered. Survives on **alignment-optimization algorithms + throughput/yield data + fixturing IP**; SEM-22 (optical KGD) must drive *feed-forward die disposition* (it is on the monitoring-loop WATCH) or it cannot lift the cluster.
6. **Regulatory/export-control risk — LOW-MEDIUM.** Photonics assembly is low; SEM-07's high-power lasers carry medium export sensitivity; wafer-level optical KGD touches ATE export scrutiny. No ITAR/clinical.
7. **IP strategy.** Allied entity owns the alignment algorithms + KGD methodology + assembly-yield correlation dataset; license the cell. Keep high-power-laser module specifics allied.
8. **Local partner requirement.** A CPO OSAT / photonics-fab pilot partner (allied first) to validate the cell at volume and prove KGD-to-assembly-yield correlation.
9. **US expansion path — the primary path.** Single-cell demo (2026) → pilot at a CPO OSAT (2027) → multi-cell line (2028) into US photonics programs.
10. **Go/no-go — GO US-first; China manufacturing leg after the cell and KGD feed-forward are proven.**

**Label: US-first then China manufacturing**

---

## 7. CL-02 — 800VDC DC-Side Protection (Power)

**Binding posture:** DUAL_TRACK · Rank 7 (score 78) · member PWR-02.
**Adjacent defensible wedge:** a **µs bidirectional SiC/GaN solid-state DC breaker / e-fuse with energy-absorption + selective-coordination firmware** for 800–1000VDC busways. The defensible layer is the protection/selectivity firmware + qualification data, **not** the SiC silicon (a commodity wafer trap).

1. **China-first attractiveness — MEDIUM (dual-track).** Hard physics gate (no DC current zero) and a real standards-driven pull from China's data-center buildout (East-Data-West-Computing, PUE mandates). But the value lives in connected protection/controls firmware, which faces US connected-hardware bans — so the firmware/controls must be dual-tracked while the power hardware can localize.
2. **First Chinese customer segment.** 800VDC busway/power-shelf OEMs and hyperscaler facilities — Director Power Distribution Engineering at Inspur/H3C/Sugon-class OEMs and Alibaba/Tencent/ByteDance DC infra. Pain: 800VDC faults arc before AC-side breakers react.
3. **First US customer segment.** 800VDC busway OEMs and hyperscaler facilities (Director Power Distribution Engineering); the 800VDC safety/standards gap is an explicit design-in blocker.
4. **Supply-chain advantage in China.** Domestic SiC device localization and AI-DC DC-standardization pull; deepest power-hardware manufacturing base.
5. **Commodity/copycat risk in China — MODERATE.** The SiC array is copyable; survives on **energy-absorption + selective-coordination firmware + UL/IEC qualification data**. Treat the silicon as a bought-in input inside a higher-integration, firmware-defined breaker.
6. **Regulatory/export-control risk — MEDIUM, plus a standards-timing dependency (flagged as timing, not fact).** SiC export sensitivity on the device side; the binding US risk is the connected grid/DC-controls "trust tax" (NDAA 889, FCC Covered List, proposed connected-hardware rules). UL489-DC / IEC arc-fault standards are still settling — this is a *timing* risk that delays design-in, explicitly not treated as a regulatory certainty.
7. **IP strategy.** Two firmware code-bases / two entities; protection-coordination algorithms and qual datasets partitioned by jurisdiction. The qualification dossier (UL/IEC) is the durable moat.
8. **Local partner requirement.** A busway/power-shelf OEM design-in partner in each ecosystem to embed the breaker into the bus architecture.
9. **US expansion path.** Direct design-in to US 800VDC busway OEMs via the allied entity; UL489-DC product (2028). Red-team: hyperscalers stay at 400VDC with conventional protection.
10. **Go/no-go — GO dual-track; gate the US firmware behind an allied entity.**

**Label: Dual-track from day one**

---

## 8. CL-25 — Energy-Based Intervention Engines (Biomedical)

**Binding posture:** US_FIRST_THEN_CHINA_MFG · Rank 8 (score 77) · members BIO-001, BIO-005, BIO-018, BIO-021.
**Adjacent defensible wedge:** a **merchant multi-kV biphasic PFA pulse/field-shaping generator engine** (waveform library + per-electrode field solver + contact closed loop), licensed to EP device OEMs. The differentiator moves from the catheter to the programmable energy engine — **not** a clone of an integrated Farapulse/Varipulse system.

1. **China-first attractiveness — LOW-MEDIUM (US-first by posture).** Class III clinical evidence and FDA/IEC 60601 are time-and-trust moats that anchor design + IDE in the US; clinical data built on China cohorts is often re-required for FDA. The PFA generator itself is founder-pilotable, but the regulated clinical use forces a US-first structure.
2. **First Chinese customer segment (later leg).** Mid-tier/emerging domestic EP device companies entering volume-based procurement (VBP) and the NMPA innovative ("green channel") pathway — VP R&D Cardiac Ablation. Reached after US clinical anchoring.
3. **First US customer segment.** Mid-tier and emerging US EP device companies that cannot build safe multi-kV pulse engines (VP R&D / Chief Engineer Cardiac Ablation); IR/oncology centers for histotripsy (BIO-005); neuro-oncology for FUS BBB-opening (BIO-021).
4. **Supply-chain advantage in China.** HV-electronics and phased-array (HIFU) manufacturing base for a later localization leg; not the launch advantage.
5. **Commodity/copycat risk in China — MODERATE, gated by clinical evidence.** Incumbents making integrated generators standard and refusing merchant supply is the bigger threat than copycats. Survives on **waveform + field-shaping IP + porcine/clinical durability datasets + IEC-60601 multi-kV engineering + OEM lock-in.**
6. **Regulatory/export-control risk — clinical burden dominates; export modest.** Class III generator (FDA PMA/IDE, IEC 60601, HV/EMC); export is modest. BIO-018 (steerable tcFUS) carries an explicit **efficacy-vs-sham HOLD** — a clinical risk that must not be treated as proven. (PACE S-04 dropped per carry-forward repair.) No speculation admitted as fact.
7. **IP strategy.** US entity owns waveform/field-shaping IP and the clinical/durability dataset; license the generator to OEMs. China leg is contract-manufacturing under the US design master.
8. **Local partner requirement.** A catheter/EP OEM partner (US-first) to host the generator; a domestic manufacturing partner only for the later China leg.
9. **US expansion path — the primary path.** Benchtop multi-kV + phantom (2026) → porcine durability (2027) → GLP + OEM/IDE (2028); FDA Breakthrough/TCET. Red-team: incumbent generator lock-out + porcine parity failure by 2027.
10. **Go/no-go — GO US-first; China manufacturing/NMPA leg post-FDA. Histotripsy (BIO-005, $25–50M Class III) and FUS arms are slower/capital-heavier.**

**Label: US-first then China manufacturing**

---

## 9. CL-13 — Battery / Solid-State Manufacturing (Industrial)

**Binding posture:** CHINA_FIRST_ATTRACTIVE · Rank 9 (score 77) · members IND-15, IND-16.
**Adjacent defensible wedge:** a **solvent-free dry-electrode roll-to-roll process engine** (fibrillation/dry-spray + inline thickness/uniformity closed loop) that removes the costliest cell step. Process-IP play — **not** a commodity LFP cell/pack/BESS integrator (an explicit China overcapacity trap).

1. **China-first attractiveness — HIGH.** China has the world's deepest battery manufacturing base and the dry-electrode pain is anchored to peer-reviewed reviews (Advanced Energy Materials; Nature Comms ultrahigh-loading). Capex modest ($15–40M dry room). Process-IP wedge avoids the cell-commodity trap.
2. **First Chinese customer segment.** Battery cell makers / solid-state developers — VP Manufacturing / Process Development Lead (CATL/Sungrow/Envision-class and solid-state startups). Pain: wet-slurry drying is the costliest, most energy-intensive step and caps loading.
3. **First US customer segment.** US/EU cell + solid-state programs seeking cost/energy and a non-China process; defense-energy suppliers. The sulfide SE thin-film line (IND-16) leans US/EU/JP-KR-first (materials-IP heavy, earlier TRL).
4. **Supply-chain advantage in China.** Electrode-equipment and battery-materials supplier density; the largest installed cell-manufacturing capacity to design-in against.
5. **Commodity/copycat risk in China — HIGH at the cell, defused at the process.** Cells/packs/BESS are razor-margin overcapacity. Survives only because the wedge is **fibrillation/dry-spray process IP + uniformity control + solid-state compatibility** (process know-how, not the cell). Red-team: Tesla/Maxwell-lineage dry-electrode IP could block freedom-to-operate, and fibrillation uniformity may fail at web scale — the near-term China thesis rests mainly on dry-electrode.
6. **Regulatory/export-control risk — LOW.** Battery process equipment is low-export; some UL/transport for storage. No ITAR/clinical. (Cross-lane note: power/energy-lane overlap flagged to the power lane — not double-counted.)
7. **IP strategy.** Freedom-to-operate clearance against Tesla/Maxwell dry-electrode patents is the first gate; then trade-secret the fibrillation/dry-spray recipe + inline-uniformity control and build a thick-electrode uniformity dataset. Solid-state film IP anchored US/EU.
8. **Local partner requirement — RECOMMENDED.** A cell-maker pilot-line partner to validate at web scale and lock the process spec.
9. **US expansion path.** Sell the dry-electrode line as a cost/energy + non-China-process resilience play to US/EU cell makers; lead with the solid-state SE film line (US/EU-first) for the frontier-cell segment.
10. **Go/no-go — GO (China-first) on dry-electrode contingent on FTO clearance; solid-state leg US/EU-first.**

**Label: China-first attractive**

---

## 10. CL-29 — Bio-Manufacturing & Intervention-Decision Instruments (Biomedical)

**Binding posture:** US_FIRST_THEN_CHINA_MFG · Rank 10 (score 77, CLEARED_WITH_WEAKNESS) · members BIO-006/009/010/013 + WATCH BIO-017/020/025.
**Adjacent defensible wedge:** a **parallelized microfluidic LNP production engine with closed-loop CQA control + a scale-transfer model** (and a decentralized closed-loop CAR-T "manufacturing-in-a-box" instrument). Engine that conserves nanoscale attributes from 1 mL to GMP — **not** a clone of Precision NanoSystems / Lonza Cocoon.

1. **China-first attractiveness — LOW-MEDIUM (US-first by posture).** GMP regulatory complexity, CMC datasets, and (for any genomic/health data) PIPL + Human Genetic Resources outbound rules anchor the regulatory moat in the US. The instruments are founder-pilotable, but the value is regulatory-acceptance + scale-transfer data — cleaner US-first.
2. **First Chinese customer segment (later leg).** Domestic RNA-therapeutics firms/CDMOs under biopharma self-sufficiency, and cost-constrained cancer centers for decentralized CAR-T. Reached after US CMC anchoring.
3. **First US customer segment.** RNA-therapeutics companies and CDMOs (Head of Drug Product / CMC) for LNP; NCI/academic cell-therapy units (Director of Cellular Therapy) for bedside CAR-T; pharma tox groups for the organ-on-chip NAM platform (BIO-006).
4. **Supply-chain advantage in China.** Microfluidic-chip and instrument manufacturing for a later localization leg; large patient volume for CAR-T demand — but not the launch advantage.
5. **Commodity/copycat risk in China — MODERATE, gated by regulatory data.** Incumbents closing the scale-up gap and locking CDMOs is the bigger threat than copycats. Survives on **parallelized-mixer geometry + scale-transfer control + PAT + CMC datasets** (qualification + data-network moat). The exciting WATCH members (OPM-MEG BIO-017, nanopore protein seq BIO-020, spatial multi-omics BIO-025) are **monitoring-/engine-purity WATCH** and must not be leaned on until they actuate a decision / prove engine purity vs ONT/10x/Bruker/Vizgen.
6. **Regulatory/export-control risk — manufacturing-equipment low; data/clinical complexity high.** LNP/CAR-T equipment is low device burden (dual-use watch); point-of-care CAR-T carries GMP/release-testing regulatory complexity. Any genomic-data play hits PIPL/HGR outbound + US Biosecure-style inbound scrutiny.
7. **IP strategy.** US entity owns the closed-loop CQA control + scale-transfer model + CMC regulatory templates; license/sell the engine. Keep any patient-data analytics US-side. China leg = instrument manufacturing under the US design master.
8. **Local partner requirement.** A CDMO (LNP) and an NCI/academic cell-therapy site (CAR-T) as US-first co-development partners; site network effects are the durable advantage.
9. **US expansion path — the primary path.** Attribute-matching (2026) → GMP single-skid / engineering runs (2027) → CDMO tech-transfer / IND-enabling POC (2028).
10. **Go/no-go — GO US-first (LNP + decentralized CAR-T as the clearing anchors); China manufacturing leg later. CWW ceiling applied — do not over-claim on the WATCH instruments.**

**Label: US-first then China manufacturing**

---

## 11. CL-19 — HTS Conductor Supply Chain & Qualification (Extreme)

**Binding posture:** CHINA_FIRST_DANGEROUS · Rank 11 (score 76) · members EXT-03 (anchor), EXT-02, EXT-13, EXT-15.
**Adjacent defensible wedge (explicit, non-clone):** an **in-line REBCO tape Jc/defect-mapping platform whose differentiator is IN-FIELD (high-B) Jc correlation**, bundled with a **qualified low-resistance joint process** and a per-tape/per-joint "passport" dataset. The wedge is the *qualification-data + process moat that the magnet builder's acceptance spec depends on* — explicitly **not** a REBCO tape clone, and explicitly more than the 77 K self-field scanners (THEVA/Bruker TapeStar class) that fail to predict in-field magnet performance.

1. **China-first attractiveness — present but DANGEROUS, not "attractive."** China is aggressively scaling 2G REBCO tape (Shanghai Superconductor, Shanghai Creative) for BEST/EAST and commercial fusion — a real demand pull. But HTS is the single most export-radioactive domain (dual-use, two-sided listing), so this is *possible but dangerous*, deliberately not upgraded to attractive. (China-wedge sub-score held to 3 in the ranking by design.)
2. **First Chinese customer segment.** REBCO tape makers and fusion magnet winders — VP Manufacturing / Quality Director at Shanghai Superconductor / Shanghai Creative; magnet programs at ASIPP (BEST/EAST), Energy Singularity, Startorus, ENN. Pain: Jc non-uniformity + slitting defects are the largest magnet-performance risk, and 77 K self-field Jc poorly predicts in-field performance.
3. **First US customer segment.** Allied REBCO tape makers (MetOx, Faraday Factory, SuperPower) and US fusion magnet builders (CFS, Tokamak Energy, Type One) needing acceptance QC and qualified joints.
4. **Supply-chain advantage in China.** Domestic 2G HTS tape capacity being built, co-location with CICC/cabling for EAST/BEST/CFETR, and ASIPP/CHMFL test infrastructure heritage.
5. **Commodity/copycat risk in China — and why the wedge survives fast-following.** The launch risk is a tape maker *internalizing* metrology/jointing, plus rapid copy of any geometry-based tool. The wedge survives because its moat is **process IP + an in-field Jc-correlation dataset that becomes the buyer's qualification spec of record** — expensive to reproduce, improves with every qualified reel/joint, and is not a mechanical CAD file. A pure 77 K self-field scanner clone would be fast-followed and is *not* the recommended product. EXT-13 (SULTAN-class test bed) is very-high-capex and drags capital efficiency — keep it as a later qualification-as-a-service arm, not the entry product. Architecture risk: jointless winding or improved tape Jc uniformity could obviate the engine.
6. **Regulatory/export-control risk — HIGHEST in the pool, both directions.** HTS/cryogenics are classic dual-use: US Entity List/BIS exposure (and the Sept-2025 50% affiliates rule widening contamination of any PRC supply you depend on) and China's Export Control Law + dual-use catalog. A China-first HTS entity can be cut off from the allied fusion market entirely. This is the binding reason it is "dangerous," not speculation.
7. **IP strategy (must defeat fast-following).** Trade-secret the EM-inversion algorithms + in-field-correlation methodology and grow the tape/joint passport database as the durable, copy-resistant moat; license the *acceptance spec*, not the scanner. Partition data per jurisdiction; assume any PRC-entity tooling is non-exportable to allied customers. Do **not** rely on a single metrology patent — in HTS's small, high-mobility talent pool it would be designed around in quarters.
8. **Local partner requirement.** A tape maker + a magnet program as co-development partners; without an integrator dependent on your passport data, the metrology commoditizes.
9. **US expansion path.** Allied QC + joint qualification sold to MetOx/Faraday/SuperPower and CFS/Type One via an allied entity that relieves dependence on the single European (SULTAN) test facility. Export posture makes a clean PRC→US transfer largely foreclosed — structure allied from inception for the US leg.
10. **Go/no-go — CONDITIONAL GO, dangerous: pursue the in-field-correlation + qualified-joint wedge only with a deliberate two-jurisdiction structure and the qualification-data moat front and center; do NOT enter as a tape/scanner clone.**

**Label: China-first possible but dangerous**

---

## 12. CL-08 — In-/On-Package Power Delivery (Semiconductor)

**Binding posture:** DUAL_TRACK · Rank 12 (score 75) · member SEM-09 (PWR-20 absorbed).
**Adjacent defensible wedge:** a **vertical in-package IVR power-delivery chiplet** (GaN/Si power-stage + in-package inductors/IPDs + fast digital control loop) co-designed with the compute die — the only way to feed kW packages without IR/area collapse. Engine-layer power delivery, **not** a clone of Empower/MPS board VRMs.

1. **China-first attractiveness — MEDIUM (dual-track).** Couples to domestic GaN + advanced packaging, but the strict data-center-only exposure ties it to the AI-accelerator cycle, and GaN + advanced-packaging adjacency carries two-sided export exposure — so the control IP and any advanced-packaging steps are dual-tracked.
2. **First Chinese customer segment.** Domestic AI-accelerator / HPC SoC vendors wanting vertical power delivery (Cambricon, Biren, Moore Threads, Ascend) — Director Power Delivery / SoC Power Architect.
3. **First US customer segment.** US AI-accelerator and HPC SoC vendors (NVIDIA/AMD/Broadcom-class) — Director Power Delivery; vertical-power-delivery (VPD) roadmaps.
4. **Supply-chain advantage in China.** Domestic GaN device localization + advanced-packaging assembly for the chiplet (chiplet fab outsourceable).
5. **Commodity/copycat risk in China — MODERATE.** Risk that board VRMs + better PDN suffice, or a foundry bundles IVR into the package, absorbing the chiplet. Survives on **power-density + transient-response IP co-designed with the compute die** (designed-in lock-in). Note the PWR-20 "last-inch loss" metric was a company claim and is re-anchored (ISS-018) — not used as proof.
6. **Regulatory/export-control risk — MEDIUM-HIGH.** GaN device export sensitivity; advanced-packaging tool-control creep; advanced-computing/AI-chip controls (2024–25) shape which accelerators can even be deployed in China — directly affecting the served market on the China side.
7. **IP strategy.** Two entities; the fast digital control loop + co-design methodology held per jurisdiction; license the IVR interface to compute-die vendors. Reliability/transient datasets as the moat.
8. **Local partner requirement.** A compute-die (SoC) co-design partner in each ecosystem — the chiplet is worthless without die co-design.
9. **US expansion path.** VR chiplet on test SoP (2026) → customer SoC (2027) → product (2028) into US accelerator vendors via the allied entity.
10. **Go/no-go — GO dual-track; gate advanced-packaging/control IP behind an allied entity. Capital efficiency and DC-cycle concentration are the watch-items.**

**Label: Dual-track from day one**

---

## 13. CL-03 — AI-Load Power-Smoothing & GFM Buffer (Power)

**Binding posture:** DUAL_TRACK · Rank 13 (score 75) · members PWR-03, PWR-04, PWR-10, PWR-16 (PWR-18 absorbed).
**Adjacent defensible wedge:** a **predictive rack/campus power-shaping buffer** (hybrid supercap/film-cap + bidirectional SiC DC-DC + grid-forming converter) whose moat is **feed-forward control co-designed to GPU telemetry + grid-forming control validated on real AI dynamics** — the active power-shaping layer. Controls/firmware moat, **not** a commodity BESS container (an explicit China trap).

1. **China-first attractiveness — MEDIUM (dual-track).** Strong market signals exist in China (74 GW/168 GWh storage installed 2024, 180-GW-by-2027 target, capacity-price floor — gov.cn triangulation), and the rack buffer is founder-pilotable. But the value is connected grid/controls firmware, which faces US connected-hardware bans, and the cells/containers are commodity — so dual-track the firmware, treat storage hardware as a bought-in input.
2. **First Chinese customer segment.** GPU rack/power-shelf OEMs (Inspur/H3C/Sugon) for the rack buffer (Chief Engineer Rack Power), and AI-DC developers/State Grid for the campus grid-hiding buffer (Head of Grid Interconnection).
3. **First US customer segment.** GPU rack/power-shelf OEMs (rack buffer) and AI-DC developers/utilities (campus GFM buffer); the buyer pain is utilities throttling/delaying interconnect due to volatile AI load + oscillations (DOE/PNNL/NERC + FERC Dec-2025 PJM order anchors).
4. **Supply-chain advantage in China.** Domestic supercap + film-cap + SiC + storage manufacturing at AI-DC scale; world-largest storage manufacturing base.
5. **Commodity/copycat risk in China — HIGH at the box, defused at the controls.** LFP cells/BESS containers are razor-margin. Survives only because the wedge is **predictive feed-forward control co-designed with GPU telemetry + GFM control validated on real AI dynamics + utility certification** (moving-target firmware moat). PWR-18 (oscillation damper, absorbed) must *actuate*, not monitor (ISS-012), or it fails the monitoring-only bar. High-temp film-cap (PWR-16) adds a material-IP moat.
6. **Regulatory/export-control risk — MEDIUM + grid-rules-in-flux (flagged as timing).** SiC/grid-control export sensitivity; the binding US risk is connected grid-firmware bans (NDAA 889, FCC, connected-hardware rules) and Buy-American/domestic-content (IRA/BABA) favoring domestic hardware. Interconnection rules are in flux — a timing risk, not treated as settled fact.
7. **IP strategy.** Two firmware code-bases / two entities; GPU-telemetry feed-forward and GFM dispatch algorithms + utility-certification data partitioned per jurisdiction. Avoid relying on the storage hardware.
8. **Local partner requirement.** A GPU rack OEM (rack buffer) and a utility/ISO (campus GFM) co-development partner in each ecosystem.
9. **US expansion path.** Shelf demo (2026) → full-rack ODM (2027) → hall pilot with grid verification (2028) via the allied entity; IEEE 1547/1741 grid-interactive listing. Red-team: GPU vendors solve smoothing in firmware / on-package caps.
10. **Go/no-go — GO dual-track; firmware behind an allied entity, storage hardware localized.**

**Label: Dual-track from day one**

---

## 14. CL-14 — Robot & Surgical Actuation Engine (Industrial)

**Binding posture:** CHINA_FIRST_DANGEROUS · Rank 14 (score 75, CLEARED_WITH_WEAKNESS) · members IND-01 (anchor; headline 18–22 Nm/kg metric EXCLUDED), IND-02 (NOT_CHINA_FIRST), IND-04, IND-20, IND-21, IND-22.
**Adjacent defensible wedge (explicit, non-clone):** a **continuous-duty, thermally-managed actuation engine** — axial-flux + low-ratio stage + phase-change/conductive cooling + thermal-state observer + learned torque estimation, qualified for hours-long duty cycles (the humanoid endurance wall) — plus the **friction-compensated dexterous-hand module** (IND-04). The wedge is *thermal + control + sensing integration and continuous-duty qualification data*, explicitly **NOT** the joint/reducer/servo (commodity traps) and **NOT** a "whole humanoid" clone.

1. **China-first attractiveness — present but DANGEROUS, not "attractive."** China has the supplier density, an 85–90% NdFeB magnet position (IEA triangulation — a genuine cost input edge), and an aggressive humanoid customer base. But reducers, servos, frames, and "whole humanoid" clones are all commoditizing fast — the joint layer is a race to the bottom. The defensible move is the continuous-duty thermal/control engine, deliberately not upgraded to attractive. (China-wedge sub-score held to 3 by design; IND-01's headline torque-density metric is HOLD/excluded — the cluster clears on IND-21/04/02.)
2. **First Chinese customer segment.** Domestic humanoid/legged OEMs — VP Hardware / Chief Actuation Engineer at UBTech, Unitree, AgiBot (Zhiyuan), Fourier, Galbot, LimX. Pain: actuator endurance (thermal) at work duty cycles, not peak torque.
3. **First US customer segment.** US/EU humanoid OEMs wanting non-China actuation (Figure, Apptronik, Agility, Tesla Optimus) — and surgical-robot makers for the backdrivable micro-actuator (IND-20) and dexterous-hand crossover (IND-04). Note IND-02 (rare-earth-free servo) is candidate-specific **NOT_CHINA_FIRST** (US/EU/defense-first) and must not be paired with a China-first thesis.
4. **Supply-chain advantage in China.** NdFeB magnet cost/availability (use as a cost input *inside* a higher-integration actuator, never as the product), robotics-component supplier density, and a local humanoid deployment base.
5. **Commodity/copycat risk in China — HIGH; why the wedge survives fast-following.** Mechanical subsystems are copied in quarters; a commodity joint margin-compresses below qualification-cost recovery. The wedge survives because its moat is **magnetics+thermal+control co-design + continuous-duty qualification data** (expensive to reproduce, becomes the OEM's spec of record) and the **friction/hysteresis-compensation firmware that improves with deployment data** — not a CAD file or a single patent. Kill discipline: if integrated-joint margin compresses below qualification-cost recovery within ~18 months, exit. A pure joint/reducer clone is the anti-pattern and is rejected.
6. **Regulatory/export-control risk — MEDIUM, asymmetric.** China's April-2025 rare-earth controls license Tb/Dy-containing NdFeB/SmCo magnets (light-REE-only magnets remain free) — a lever that helps a China-side actuator (local magnets) but is a US-side supply risk and feeds US 1260H/connected-robot trust concerns. Embodied-AI compute carries some export exposure. The surgical arms (IND-04/20) carry FDA burden.
7. **IP strategy (must defeat fast-following).** Trade-secret the thermal-state observer + FOC/torque-estimation firmware and grow continuous-duty qualification datasets as the durable moat; build the dexterous-hand compensation as a deployment-data flywheel. Do **not** patent-gate a magnet geometry or gearbox. Keep the rare-earth-free servo (IND-02) and surgical micro-actuator (IND-20) in an allied/US entity.
8. **Local partner requirement.** A humanoid OEM co-development partner to embed the actuator in the control stack and generate continuous-duty data; without it, the engine commoditizes.
9. **US expansion path.** License the thermal/control-integrated actuation engine + dexterous-hand module to US/EU humanoid OEMs as a non-China, continuous-duty-qualified subsystem; enter surgical via IND-04/20 (US-first FDA). IND-02 is the explicitly allied-first arm.
10. **Go/no-go — CONDITIONAL GO, dangerous: pursue ONLY the continuous-duty thermal/control + dexterous-hand wedge with the qualification-data moat; do NOT clone the joint/reducer/servo or the whole robot.**

**Label: China-first possible but dangerous**

---

## 15. CL-27 — Intervention Robotics & Steerable Access (Biomedical)

**Binding posture:** US_FIRST_THEN_CHINA_MFG · Rank 15 (score 74) · members BIO-004 (anchor), BIO-011, BIO-022.
**Adjacent defensible wedge:** a **steerable / variable-stiffness access module** — magnetic soft-tip steering + external field control + navigation autopilot (BIO-004), with the transparenchymal steerable-needle (BIO-011) and tremor-filtering subretinal micromanipulator (BIO-022) as adjacent access modules — sold as a licensable subsystem. **Not** a clone of Magbot/Stereotaxis robotic catheters.

1. **China-first attractiveness — LOW-MEDIUM (US-first by posture).** Class II/III surgical-robot regulation, FDA, and clinical/hospital trust anchor the design in the US; the China-wedge for BIO-004 leans on Magbot company/journalism (timing-only) and cannot be treated as customer-pain proof. Component localization for domestic OEMs is a later leg.
2. **First Chinese customer segment (later leg).** Domestic neurovascular/endovascular-robotics OEMs riding the stroke push and Magbot magnetic-nav precedent (timing-only) — Director Neurointerventional. Reached after US clinical anchoring.
3. **First US customer segment.** Neurovascular/stroke programs and endovascular-robotics OEMs (Director Neurointerventional / Endovascular Robotics) for the steering module; interventional pulmonology (BIO-011) and vitreoretinal surgery + gene-therapy developers (BIO-022).
4. **Supply-chain advantage in China.** Catheter/microcatheter and surgical-instrument manufacturing for a later localization leg; large patient volume — not the launch advantage.
5. **Commodity/copycat risk in China — MODERATE, gated by clinical evidence.** Risk that steerable guidewires/robotic catheters reach the same vessels more cheaply, or incumbents internalize steerable needles. Survives on **magnetic soft-robot tip + field-control IP + navigation datasets + OEM integration** and clinical-delivery data (for BIO-022, gene-therapy partnerships).
6. **Regulatory/export-control risk — clinical burden dominates; export moderate.** Class II/III surgical robot (FDA), magnetic-field safety; export moderate. The shared actuation/sensing core with CL-14/15 means it inherits those sensing/control moats but adds clinical-trust gates that force US-first.
7. **IP strategy.** US entity owns the field-control + navigation-autopilot IP and clinical-delivery datasets; license the access module to robotic-platform OEMs. China leg = manufacturing under the US design master.
8. **Local partner requirement.** A robotic-platform OEM (US-first — e.g., endovascular-robotics, robotic-bronchoscopy, ophthalmic-robot integrators) to host the module; gene-therapy developer partnerships for BIO-022.
9. **US expansion path — the primary path.** Phantom navigation (2026) → in-vivo reach (2027) → GLP + first-in-human design (2028); license to US endovascular-robotics entrants.
10. **Go/no-go — GO US-first; China manufacturing/component leg post-FDA. The China wedge rests on timing-only signals and must not be over-weighted.**

**Label: US-first then China manufacturing**

---

# Final summary table

| candidate_id | cluster_name | domain | binding_posture (10E) | deep_dive_label | go/no-go | one-line adjacent wedge |
|---|---|---|---|---|---|---|
| CL-07 | Chip-Package Thermal Boundary Shift | Semiconductor | CHINA_FIRST_ATTRACTIVE | China-first attractive | GO (China-first) | OSAT-co-designed die-height-compensating in-package microfluidic cooling engine (not a cold plate) |
| CL-18 | HTS Magnet Protection, Charging & Control | Extreme | DUAL_TRACK | Dual-track from day one | GO (two entities) | Fiber-optic quench detection-to-actuation + charging/ramp control loop (not a magnet) |
| CL-10 | Hybrid-Bonding & Adv-Packaging Process-Control | Semiconductor | US_FIRST_THEN_CHINA_MFG | US-first then China manufacturing | GO (US-first) | Closed-loop inline hybrid-bond metrology that actuates the bonder (not a KLA clone) |
| CL-12 | Power-Module & WBG Packaging/Manufacturing | Industrial | CHINA_FIRST_ATTRACTIVE | China-first attractive | GO (China-first) | Silver-sinter cell with inline void metrology + closed-loop control (the IP, not the press) |
| CL-15 | Force / Tactile Sensing Engine | Industrial | CHINA_FIRST_ATTRACTIVE | China-first attractive | GO (China-first) | Full-hand super-res e-skin + overload-tolerant 6-axis F/T with fusion firmware (not LiDAR/joints) |
| CL-09 | CPO Optical Assembly & Test | Semiconductor | US_FIRST_THEN_CHINA_MFG | US-first then China manufacturing | GO (US-first) | Sub-100nm active-alignment fiber-attach cell + feed-forward optical KGD (not a ficonTEC clone) |
| CL-02 | 800VDC DC-Side Protection | Power | DUAL_TRACK | Dual-track from day one | GO (firmware dual-track) | µs SiC/GaN DC breaker with selective-coordination firmware (the firmware, not the silicon) |
| CL-25 | Energy-Based Intervention Engines | Biomedical | US_FIRST_THEN_CHINA_MFG | US-first then China manufacturing | GO (US-first) | Merchant multi-kV biphasic PFA pulse/field-shaping generator engine (not an integrated catheter) |
| CL-13 | Battery / Solid-State Manufacturing | Industrial | CHINA_FIRST_ATTRACTIVE | China-first attractive | GO (China-first, FTO-gated) | Solvent-free dry-electrode R2R process engine (process IP, not commodity cells) |
| CL-29 | Bio-Manufacturing & Intervention-Decision Instruments | Biomedical | US_FIRST_THEN_CHINA_MFG | US-first then China manufacturing | GO (US-first) | Parallelized LNP production engine + decentralized closed-loop CAR-T instrument (not a NanoSystems clone) |
| CL-19 | HTS Conductor Supply Chain & Qualification | Extreme | CHINA_FIRST_DANGEROUS | China-first possible but dangerous | CONDITIONAL GO | In-field-correlated REBCO Jc/defect mapping + qualified joints + passport data (not a tape/scanner clone) |
| CL-08 | In-/On-Package Power Delivery | Semiconductor | DUAL_TRACK | Dual-track from day one | GO (controls dual-track) | Vertical in-package IVR chiplet co-designed with the die (not a board-VRM clone) |
| CL-03 | AI-Load Power-Smoothing & GFM Buffer | Power | DUAL_TRACK | Dual-track from day one | GO (firmware dual-track) | Predictive rack/campus power-shaping buffer with GPU-telemetry/GFM control (not a BESS container) |
| CL-14 | Robot & Surgical Actuation Engine | Industrial | CHINA_FIRST_DANGEROUS | China-first possible but dangerous | CONDITIONAL GO | Continuous-duty thermal/control-integrated actuation + dexterous-hand module (not a joint/reducer clone) |
| CL-27 | Intervention Robotics & Steerable Access | Biomedical | US_FIRST_THEN_CHINA_MFG | US-first then China manufacturing | GO (US-first) | Steerable/variable-stiffness access module + field-control/nav autopilot (not a Magbot/Stereotaxis clone) |

**Deviations from binding posture:** NONE. All 15 deep-dive labels are consistent with the binding 10E/cluster-map `china_posture` (CHINA_FIRST_ATTRACTIVE→"China-first attractive"; DUAL_TRACK→"Dual-track from day one"; US_FIRST_THEN_CHINA_MFG→"US-first then China manufacturing"; CHINA_FIRST_DANGEROUS→"China-first possible but dangerous"). The two dangerous clusters (CL-19, CL-14) were held at "possible but dangerous" — not upgraded to "attractive" — with an explicit adjacent wedge and a copycat-survival argument in deliverables 5 and 7, per the binding rule.

**Wedge / no-clone confirmation:** Every one of the 15 candidates is assigned an adjacent, defensible subsystem/engine-layer wedge (column above); none recommends copying Hinetics or any specific company. No new candidate, worker idea, company-radar wedge, or China-feasibility wedge outside the Top-15 cluster membership was introduced.

```text
CHINA_FEASIBILITY_DEEP_DIVE_COMPLETE = YES
CANDIDATES_ASSESSED = 15
LABEL_DEVIATIONS_FROM_BINDING_POSTURE = 0
MASTER_CSVS_MODIFIED = NONE
```
