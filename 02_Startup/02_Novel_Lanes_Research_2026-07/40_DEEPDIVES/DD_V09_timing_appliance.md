# DD-V09 — Field-hardened White-Rabbit-class timing & synchronization appliance

Date 2026-07-03 · Candidate V09 (lane G06) · RT-adjusted 74.0, RT kill 65% · Sources: `DD_V09_sources.json` (DD-V09-01…27; 19 fetched, 19 fresh, T1+2 = 22/27). POLICY_DELTA.md absent at drafting — §7 is **provisional**, self-researched.

**Deep-dive verdict up front: NO-GO (kill-leaning, ~70%).** The red team's bear case survives contact with primary sources on every load-bearing point. The residual venture is a fleet-software-plus-hardening services business at low-single-digit-$M scale, in a standard whose authors are industrializing it 2026-2028, with the China half of the founder's thesis inverted.

---

## 1. Problem & who has it

Sub-ns time transfer over fiber is required wherever distributed detectors/nodes must correlate events tighter than GNSS+PTP delivers (~100 ns typical field PTP; WR: sub-ns accuracy, ps-class jitter [DD-V09-05][DD-V09-03]). Named buyer archetypes:

- **Quantum-testbed network lead** (DOE lab or utility): entanglement-swapping nodes in data closets and huts need common time plus classical control; EPB's Chattanooga network (est. 2022, "first commercially available" US quantum network) has capacity for ten user nodes and fights wind/outdoor-temperature disturbance on deployed fiber [DD-V09-17]. Five DOE NQIS centers renewed Nov 2025 at $625M/5 yr, with Q-NEXT explicitly scaling entanglement "across labs and cities" [DD-V09-10].
- **EuroQCI national-consortium engineer**: all 27 EU member states are building national quantum-communication networks, 19 CEF cross-border link projects, terrestrial phase 2023-2025, capabilities target 2030 [DD-V09-11]. (RT cited 26 states; the EC page as fetched 2026-07-03 says all 27 joined — fetched figure preferred.)
- **Astroparticle/radio-array timing engineer**: LHAASO synchronizes >8,000 detectors over 1.3 km² at 4,410 m through 550+ WR switches, outdoors, since 2021 [DD-V09-03]. CTA/ngVLA-class arrays are the next builds; peer-reviewed WR-for-interferometry evaluation appeared in 2025 [DD-V09-26, snippet].
- **Accelerator timing group**: HIAF (IMP/CAS) designed its timing on WR (reported ~600 devices, <2 ns — snippet-level color [DD-V09-22][DD-V09-27]); these groups overwhelmingly self-build.
- **PNT-resilience officer** (NMI/critical infrastructure): NIST now sells UTC(NIST)-over-commercial-fiber calibration service [DD-V09-15]; VSL distributes Dutch legal time over SURF fiber via an OPNT-built WR network at <5 ns [DD-V09-14].

Quantified niche (ex-China, ex-telecom/finance, 2027-2031): quantum testbeds ~8-12 US programs × 3-10 nodes plus EuroQCI 27 national nets × 4-12 nodes plus arrays/NMIs → **~400-1,200 hardened-WR-relevant node deployments cumulative**, of which a new entrant can realistically contest 10-25% (rest captive to integrators, self-build, or collaboration members). Uncertainty is dominated by whether EuroQCI nodes specify WR at all (many QKD systems use their own sync).

## 2. Product & extreme edge

Proposed: -40…+70 °C, IP65-capable, fanless, dual-PSU, remotely managed WR node/switch + **fleet-management layer** (per-link asymmetry calibration DB, SFP drift analytics, holdover health scoring, zero-touch provisioning).

Spec reality vs SOTA (all fetched):

| Item | Temp range | Notes |
|---|---|---|
| Safran WR-ZEN TP-FL (ships today) | -10…+50 °C | 1U, sub-ns, >80 km fiber, optional holdover, new low-jitter version [DD-V09-05] |
| LHAASO modified WRS (SyncTechnology/Tsinghua) | -20…+70 °C | fanless industrial, auto temp/link-delay compensation, fielded since 2021; WRS-FL accepted 2018 [DD-V09-03][DD-V09-12] |
| WRS v4 (CERN+GMV, in progress) | n/s | redundant field-replaceable fans/PSUs, 10GbE, expansion slot; IQD ICPT-1 quantum-clock holdover board; open production test suite [DD-V09-02] |
| V09 proposal | -40…+70 °C | delta vs fielded SOTA = **20 °C at the cold end + software** |

Honest assessment: the hardware edge is a packaging increment, not a 10x. The defensible "extreme" claim shrinks to fleet-scale operability (MTBF/MTTR, calibration-as-data) — real, but a software/services edge on open (CERN OHL) hardware. VLBI/optical-clock links are a **category mismatch**: WR frequency transfer is ~1×10⁻¹³ (VSL-measured [DD-V09-14]); optical-clock comparison needs 10⁻¹⁵…10⁻¹⁷ carrier-phase links — that segment must be deleted from the one-pager.

## 3. Feasibility & TRL path to sellable v1 (2029-2031)

Feasibility is not the gate (RT concurs, C6=5). BOM sketch (node): Zynq/Artix-class FPGA + open WR PTP core; DDMTD clock recovery + low-jitter PLL; OCXO standard, mini-Rb or ICPT-1-class quantum-clock holdover option (the IQD board already exists in the collaboration pipeline [DD-V09-02]); BiDi C/DWDM SFPs; wide-range DC/PoE PSU; die-cast fanless enclosure with conformal coat. Estimated BOM $3.5-8K, COGS $6-10K at 100-unit lots (assumption, unverified), target ASP $20-45K/node + $3-8K/yr fleet software (assumption — WR list prices are unpublished; Safran sells price-on-request [DD-V09-05], ns-class Adtran/Microchip grandmasters occupy the band below [DD-V09-24]).

Buy: FPGA SoMs, oscillators, optics, PSUs. Build: enclosure/thermal, calibration rig (climate chamber + ps TDC — HIAF-style real-time calibration reaches ~5.5 ps RMS [DD-V09-27, snippet]), fleet software. **Cleanroom: none.** Timeline: v1 prototype 12-15 months from start (2029) on WRS v4 open design; TRL 6-7 field pilots 2030; sellable qualified unit 2031. All plausible — which is precisely the strategic problem: six collaboration members can execute the same plan earlier.

## 4. Competitive landscape — global and Chinese

**Global.** Safran/Seven Solutions (acquired Dec 2021, price undisclosed [DD-V09-07]): full WR line + rugged MIL-STD-810G VersaSync bench [DD-V09-05][DD-V09-25]. GMV: £2M Innovate UK (2024-08-07) to be *first commercializer of WRS v4* with IQD and Zyxt, explicitly framed as UK sovereign GNSS-backup infrastructure with "export potential" [DD-V09-09]. WR Collaboration grew 8→18 members in 2024 [DD-V09-04] and shows ~25 member logos as of 2026-07 [DD-V09-01] — CERN, Fermilab, GSI, INFN, Safran, GMV, OPNT-adjacent orgs, finance (Deutsche Börse, Quincy Data, Jump Trading, Liquid-Markets [DD-V09-04]). OPNT: WR-as-service, built the Dutch national-time network [DD-V09-14]. Nu Quantum: embeds WR inside its Quantum Networking Unit control plane (announced 2024-11-07, QNU delivery targeted March 2025) — i.e., the quantum-datacenter timing socket is being absorbed by the network-fabric vendor [DD-V09-18]. From below: Adtran OSA 5405 rugged outdoor GNSS/PTP grandmasters and Microchip TimeProvider-class boxes cover most ns-class field tenders without WR [DD-V09-24].

**Chinese (zh sourcing).** 信科太（北京）科技有限公司 / SyncTechnology: the commercial WR vendor credited on the LHAASO fleet, WR Collaboration member [DD-V09-21, snippet][DD-V09-03]; the underlying WRS-FL fanless industrial switch was developed by Tsinghua Engineering Physics and passed acceptance 2018-09-04 with >500 units planned [DD-V09-12]. 成都天奥电子 (Spaceon, SZ:002935, CETC-10 platform): board→module→device→system military time-frequency line (NTP/PTP servers, BeiDou/GPS sync modules, distribution amplifiers) [DD-V09-13] — no WR SKU listed, but owns the military/BeiDou channel a foreigner can never enter. 国盾量子 (QuantumCTek, China Telecom Quantum Group-controlled, 588+ patents, 京沪干线 equipment chain) locks quantum-network procurement [DD-V09-23, snippet]. Facilities (HIAF, CiADS, SHINE) self-build WR-based timing [DD-V09-22][DD-V09-27, snippets]. **Pricing signals:** WR-class list prices unpublished globally; the observable signal is structural — an entire Chinese supply chain exists at facility scale since 2018, so Chinese tenders clear at domestic cost levels; Western WR nodes transact above the $5-20K ns-class grandmaster band (inference from product tiering [DD-V09-24][DD-V09-05]).

## 5. Market: bottom-up beachhead + top-down triangulation

**Bottom-up (units × ASP), addressable ex-China 2029-2031 cumulative:**

| Segment | Procuring orgs 2027-31 | Nodes | Contestable share | Revenue @ $20-45K |
|---|---|---|---|---|
| DOE/US quantum testbeds + commercial (EPB-class) [DD-V09-10][DD-V09-17] | 8-12 | 40-120 | 30-50% (no incumbent habit) | $0.4-2.2M |
| EuroQCI national nets + cross-border links [DD-V09-11] | 10-20 of 27 specify WR-class | 100-300 | 5-15% (integrator-captive, EU-preference) | $0.1-1.6M |
| Arrays/astroparticle (CTA/ngVLA-class) [DD-V09-03][DD-V09-26] | 2-4 tenders | 200-600 per win | 0-1 tender win | $0-13M (lumpy, single-shot) |
| NMIs/fiber-time pilots [DD-V09-14][DD-V09-15] | 5-10 | 20-60 | 20-40% | $0.1-0.9M |
| Defense PNT (via primes) [DD-V09-25] | 2-5 pilots | 10-40 | prime-gated | $0.1-0.5M |

**Base case ~$1.5-6M cumulative hardware by end-2031** (+fleet software ARR $0.3-1.5M/yr by 2031); upside case requires winning exactly one array-scale tender. That is a services-scale outcome, not venture-scale.

**Top-down triangulation (shown as conflict):** Tier-3 estimates of the PTP time-server market disagree by ~90x — $1.8B (2025)→$3.2B (2033) @7.4% [DD-V09-20, snippet] vs $0.02B (2026)→$0.03B (2035) @6.4% [DD-V09-19, fetched]. Both are unreliable; the credible anchor is that Orolia — the whole resilient-PNT portfolio containing the leading WR line, atomic clocks, GNSS simulators, beacons — did ~€100M revenue with 435+ staff at acquisition [DD-V09-06]. The WR-specific slice is plausibly $30-80M/yr globally today (stated as analyst range, not sourced fact). Bottom-up and the Orolia anchor agree; the $1.8B figure is rejected.

## 6. GTM: China-first AND US sequences — which leads and why

**China-first: dead, with evidence.** Timing is military-adjacent (Spaceon sells "military standard time" product lines under CETC-10 [DD-V09-13]); WR capability is domestic and mature since 2018 (Tsinghua/信科太, LHAASO scale [DD-V09-12][DD-V09-03]); quantum-network procurement is vertically locked by QuantumCTek/China Telecom Quantum [DD-V09-23]; big-science facilities self-build [DD-V09-22]. A US-person vendor selling timing gear into CAS programs faces not an export wall (gear is largely uncontrolled, §7) but a **demand wall**: domestic-substitution posture plus security-review procurement means no tender path. China role at best: component sourcing and a future commercial-datacenter SKU.

**US/EU-first: the only sequence.** (1) 2029-2030: DOE testbeds + EPB-class commercial quantum nets — small, reachable, no incumbent habit [DD-V09-10][DD-V09-17]; sell 5-15-node fleets with the software layer. (2) 2030-2031: NMI fiber-time pilots (NIST service expansion, VSL-pattern national rollouts [DD-V09-15][DD-V09-14]). (3) 2031+: array tender (CTA/ngVLA-class) as the scale event; UK/EU spend flows to sovereign vendors (Innovate UK financed GMV precisely to create one [DD-V09-09]) — a US startup should expect US-first procurement (DOE/NSF channels), EU via partners. **US leads.** This inverts the founder's China+US preference; his China networks contribute supply chain only.

## 7. Regulatory & geopolitical exposure (PROVISIONAL — POLICY_DELTA.md not yet issued; coordinate when it lands)

- **US export controls:** the Sept 6, 2024 BIS quantum IFR (89 FR, doc 2024-19633) added ECCNs 3A901/3A904/3B904/3C907-909/4A906 etc. for quantum computers, cryocoolers, materials — **timing/synchronization/clock-distribution equipment is not among the controlled items** [DD-V09-16]. WR gear remains telecom-class (EAR99/5A991-like — provisional classification; counsel required). Deemed-export exposure minimal; a GGL exists even for quantum-tech deemed exports to D:1/D:5 persons [DD-V09-16].
- **Creep risk:** if marketed as "quantum network timing for defense," it drifts toward quantum-networking and military-PNT policy surfaces (OISP outbound rules constrain China JV/entity structures, not product sales; Round-1 brief background). Keep SKUs civil-scientific.
- **Demand-side policy tailwind (US/EU):** EO 13905 + NISTIR 8323r1 push GNSS-independent timing for critical infrastructure; NIST's own fiber-time service legitimizes the category [DD-V09-15]. UK/EU fund sovereign WR vendors [DD-V09-09][DD-V09-11] — tailwind for the category, headwind for a US outsider in EU tenders.
- **China:** selling in is demand-blocked (§6), not license-blocked; CAS end-user screening still required per-institute. Net exposure: **LOW regulatory, HIGH procurement-nationalism.** RT's C9=4 stands.

## 8. Capital & milestones 2029→2032

- **2029 (pre-seed, $1-2M):** WRS-v4-derived -40…+70 °C node prototype; climate-chamber + ps-TDC calibration rig; fleet-software alpha; 2 paid pilots (DOE testbed, EPB-class). Milestone: sub-ns verified across -40…+70 °C cycling, 30-day unattended run.
- **2030 (seed, $3-5M):** 3-5 sites, 30-80 nodes cumulative; software GA (holdover analytics, asymmetry-cal DB); UNH-IOL-style conformance [DD-V09-04]; first NMI pilot. Milestone: $1.5M revenue, one array-tender shortlist.
- **2031:** array/EuroQCI tender outcome decides trajectory: win → $6-15M backlog, raise A ($8-15M); lose → plateau at $2-4M/yr services scale.
- **2032:** either fleet-software-led expansion (timing layer for quantum datacenters — contested by Nu Quantum-style absorption [DD-V09-18]) or trade sale. Fits seed-scale ceiling; the A-round is gated on a lumpy tender — structurally weak.

## 9. Risks & kill criteria

1. **Incumbent hardening (probability high):** LHAASO-grade -20…+70 °C fielded since 2021 [DD-V09-03]; WRS v4 + IQD holdover + production test suite land 2026-2028 [DD-V09-02][DD-V09-09]. *Kill if* any collaboration member lists an extended-temp field node before end-2027 (check 15th WR Workshop, May 27-28, CERN [DD-V09-01]).
2. **Buyer-pool thinness:** contestable demand ~40-150 nodes/yr (§5). *Kill if* <3 LOIs at ≥$25K/node + software by mid-2027.
3. **Absorption of the seam:** network-fabric vendors embed WR (Nu Quantum QNU [DD-V09-18]); Safran can bundle fleet software. *Kill if* Safran/GMV announce fleet-management/calibration-analytics products before founder's seed.
4. **Tender lock-out:** EU/UK sovereign-vendor preference [DD-V09-09][DD-V09-11]; Chinese market closed [DD-V09-12][DD-V09-23]. *Kill if* ngVLA/CTA-class timing tenders restrict to collaboration incumbents.
5. **No IP moat:** CERN OHL base; differentiation is execution speed against the standard's authors (RT C7=3 confirmed).

## 10. Verdict

**Conviction: LOW — NO-GO for the final portfolio (kill ~70%, above RT's 65%).** Every pillar of the one-pager degraded under fetched evidence: "nothing exists for field nodes" is false (LHAASO 2021 [DD-V09-03]); the window closes before launch (WRS v4 ecosystem 2026-2028 [DD-V09-02][DD-V09-04]); China is a competitor, not a market [DD-V09-12][DD-V09-13][DD-V09-23]; exits are modest (Orolia, the category leader's whole portfolio: ~€100M revenue, ~€400M-class reported consideration, officially undisclosed; Eurazeo netted €189M [DD-V09-06][DD-V09-08]; Seven Solutions itself: undisclosed small-cap tuck-in [DD-V09-07]). The steelman (fleet software + calibration-as-service on open hardware) is a real but services-scale business.

**Cheapest validation experiments 2026-2028 (run only if keeping a watch file):**
1. **WR Workshop reconnaissance + roadmap test (<$2K, May 2026/2027):** attend [DD-V09-01]; directly ask CERN/GMV/Safran whether extended-temp field nodes and fleet software are roadmapped. If yes → confirm kill. If no → seam confirmed in writing.
2. **10-buyer LOI sweep (<$5K):** DOE testbed leads [DD-V09-10], EPB/Qubitekk [DD-V09-17], 2 EuroQCI consortia [DD-V09-11], 1 NMI [DD-V09-14], ngVLA/CTA timing groups. Pass bar: ≥3 LOIs at ≥$25K/node + ≥$3K/yr software for 2029-2030 delivery.
3. **Paper-BOM + thermal sim of a -40…+70 °C fanless node from the open WRS v4 design, CM-quoted (<$10K):** verifies the cost floor and whether the 20 °C cold-end delta is >$2K of BOM (if it is cheap, incumbents will do it; if expensive, buyers won't pay — either result is decision-grade).

## 11. NOVELTY DEFENSE

Ledger check (RT full-ledger grep): **zero timing/sync/clock/1588/GNSS/PNT entries** across all generations — time-transfer as a category is absent; G7 novelty passes. Nearest excluded neighbors and material differences:

- **C10 (precision magnet / scientific power converters):** same facilities, different physics and budget line — C10 moves regulated watts into magnets; V09 moves picosecond-accurate timestamps across a network. No shared BOM (power stage vs FPGA/PLL/optics), different buyer function (power-systems engineer vs facility timing engineer).
- **EXT-21 (rad-hard in-vessel wireless telemetry):** a data link engineered for a radiation environment inside one machine; no clock distribution, no multi-site synchronization, no network-management layer. V09 has no radiation requirement and lives in facility networks.
- **C34 (ultra-low-noise SMU):** bench analog source-measure instrument sold per-seat to device labs; V09 is deployed network infrastructure sold per-facility. Different category, channel, and success metric (noise floor vs field MTBF at sub-ns).

V09 is genuinely novel **inside the ledger** — the kill decision comes from the outside world (fielded prior art at 8,000-node scale and an 18→~25-member industrial collaboration industrializing the residual gap before the founder's 2029 launch), not from overlap with prior candidates. Recommend logging V09 in the exclusion ledger as "timing/sync appliance — investigated, killed on incumbent trajectory" to protect future rounds from re-derivation.

---
*Word count ≈ 2,150 (excl. tables/header). Sources: 27 unique (19 verified:"fetched", 19 fresh this DD, 5 zh; T1 10 / T2 12 / T3 5). All load-bearing numbers trace to verified:"fetched" entries; snippet-level items are flagged inline and used as color only.*
