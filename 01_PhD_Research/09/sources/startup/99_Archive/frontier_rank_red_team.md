# Prompt 10/12 — Frontier Ranking & Red-Team (Scorer / Red-Team Reviewer Deliverable)

**Date:** 2026-06-29
**Role:** Red-team reviewer / scorer. Executes `prompts/10_rank_red_team_frontier.md` under the binding rules of `merge_outputs/10E_premerge_package_for_ranking.md` §3.
**Posture:** Skeptic. Scores are NOT inflated for excitement. Anti-patterns (generic AI dashboard, monitoring-only, TAM-only, China-clone-without-wedge, cleanroom-heavy-no-outsourcing, regulatory speculation, company-claim-as-evidence) are explicitly penalized per `CLAUDE.md`.

---

## Provenance note (binding scope)

- **Scoring is restricted to the 29 CLEARED / CLEARED_WITH_WEAKNESS eligible clusters** from 10E §1: **CL-01…CL-23 and CL-25…CL-30**. Unit of ranking = the cluster; each scored row's `candidate_id` = the cluster id, with the cluster name.
- **Excluded from scoring (watchlist appendix only):** **CL-24 / EXT-17** (Cryo-CMOS Quantum Control — source-blocked at 10C, may_proceed=no); **SEM-24** (UCIe at-speed test — WEAK_SIGNAL_ONLY, individually excluded from CL-10's clearing evidence); **IND-01's headline 18–22 Nm/kg continuous-torque-density metric** (HOLD — no peer-reviewed anchor). CL-14 itself is eligible and is scored on its other members (IND-21/04/02/20/22), without using the IND-01 headline metric as clearing evidence.
- **Source_status is treated as a confidence ceiling.** A CLEARED_WITH_WEAKNESS cluster cannot earn a near-perfect evidence-dependent score; PREPRINT / COMPANY / JOURNALISM / MARKET / CONSORTIUM sources are timing/triangulation only and do not boost any score. (Confirmed: the highest-scoring CWW cluster is CL-29 at 77; every score ≥78 belongs to a CLEARED cluster.)
- **Open repairs are carried forward, not waived** (CL-01/04/08 re-anchors; CL-07 drop S07; CL-22 drop S36/S38; CL-15 IEEE Sensors Journal; CL-25 drop PACE S-04) — each is reflected as a penalty in the relevant sub-scores and flagged in notes.
- **No new candidate/wedge was introduced.** Every cluster, China posture, and track is taken from 10E §1 / `frontier_merge_cluster_map.csv` / `frontier_track_assignment.csv`.

---

## Rubric and scoring method (100 points; caps respected exactly)

| Sub-score | Cap | Scoring logic (skeptic) |
|---|---|---|
| Boundary-shift magnitude | 20 | How hard a system/physics boundary is moved (Hinetics-like). CWW ceiling applied. |
| System-unlock potential | 15 | Does it unlock a whole frontier system (the engine layer)? |
| Pain intensity & WTP | 12 | Acute, quantified, named buyer, demonstrated willingness to pay. |
| Prototype path 2026–2028 | 10 | Bench→pilot inside the window; high for founder-pilotable, low for moonshot/clinical/megafacility. |
| HW/SW/control integration depth | 8 | Depth of multi-domain HW + SW + actuating control loop. |
| Defensibility | 8 | Process IP + qualification data + lock-in vs commodity risk. |
| China-first wedge | 7 | Strength of a **defensible** China-first wedge. NOT_CHINA_FIRST scores low here by design; CHINA_FIRST_DANGEROUS penalized when the wedge is "China clone." |
| US expansion path | 6 | Clarity/strength of the US market. |
| Reg/export risk (INVERTED) | 6 | **Higher = lower risk.** Heavy ITAR/NRC/aviation-cert/export-controlled/Class-III score LOW. |
| Capital efficiency | 4 | $30–100M cleanroom/test-facility = low; sub-$15M founder rig = high. |
| Founder-fit after unbiased search | 4 | Engine-layer clarity + pilotability, not hype. |

Every sub-score ≤ its cap; `total = Σ sub-scores` (arithmetic re-verified per row).

---

# Deliverable 1 — Ranked table of all 29 cleared clusters

Sub-score column keys: **BS**/20 · **SU**/15 · **PW**/12 · **PP**/10 · **HW**/8 · **DEF**/8 · **CN**/7 · **US**/6 · **RG**/6 (inverted) · **CE**/4 · **FF**/4.

| Rank | Cluster | Name | Domain | Evidence | Total | BS | SU | PW | PP | HW | DEF | CN | US | RG | CE | FF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CL-07 | Chip-Package Thermal Boundary Shift | Semiconductor | CLEARED | **84** | 18 | 13 | 10 | 8 | 7 | 5 | 6 | 5 | 5 | 3 | 4 |
| 2 | CL-18 | HTS Magnet Protection, Charging & Control | Extreme | CLEARED | **83** | 17 | 13 | 11 | 8 | 8 | 6 | 4 | 5 | 4 | 3 | 4 |
| 3 | CL-10 | Hybrid-Bonding & Adv-Packaging Process-Control | Semiconductor | CLEARED | **82** | 17 | 14 | 11 | 7 | 8 | 7 | 3 | 5 | 3 | 3 | 4 |
| 4 | CL-12 | Power-Module & WBG Packaging/Manufacturing | Industrial | CLEARED | **82** | 16 | 12 | 10 | 8 | 7 | 6 | 6 | 5 | 5 | 3 | 4 |
| 5 | CL-15 | Force / Tactile Sensing Engine | Industrial | CLEARED | **80** | 16 | 12 | 9 | 8 | 7 | 5 | 5 | 5 | 5 | 4 | 4 |
| 6 | CL-09 | CPO Optical Assembly & Test | Semiconductor | CLEARED | **79** | 16 | 13 | 10 | 8 | 7 | 5 | 4 | 5 | 4 | 3 | 4 |
| 7 | CL-02 | 800VDC DC-Side Protection | Power | CLEARED | **78** | 17 | 11 | 10 | 8 | 7 | 6 | 3 | 5 | 4 | 3 | 4 |
| 8 | CL-25 | Energy-Based Intervention Engines | Biomedical | CLEARED | **77** | 17 | 13 | 11 | 6 | 7 | 6 | 4 | 5 | 3 | 2 | 3 |
| 9 | CL-13 | Battery / Solid-State Manufacturing | Industrial | CLEARED | **77** | 16 | 12 | 10 | 7 | 6 | 5 | 5 | 5 | 5 | 2 | 4 |
| 10 | CL-29 | Bio-Manufacturing & Intervention-Decision Instruments | Biomedical | CLEARED_WITH_WEAKNESS | **77** | 15 | 12 | 10 | 7 | 7 | 6 | 4 | 5 | 4 | 3 | 4 |
| 11 | CL-19 | HTS Conductor Supply Chain & Qualification | Extreme | CLEARED | **76** | 16 | 13 | 10 | 7 | 7 | 6 | 3 | 5 | 3 | 2 | 4 |
| 12 | CL-08 | In-/On-Package Power Delivery | Semiconductor | CLEARED | **75** | 16 | 12 | 10 | 7 | 7 | 5 | 3 | 5 | 4 | 2 | 4 |
| 13 | CL-03 | AI-Load Power-Smoothing & GFM Buffer | Power | CLEARED | **75** | 15 | 11 | 10 | 8 | 7 | 5 | 3 | 5 | 4 | 3 | 4 |
| 14 | CL-14 | Robot & Surgical Actuation Engine | Industrial | CLEARED_WITH_WEAKNESS | **75** | 14 | 12 | 9 | 8 | 7 | 5 | 3 | 5 | 4 | 4 | 4 |
| 15 | CL-27 | Intervention Robotics & Steerable Access | Biomedical | CLEARED | **74** | 16 | 12 | 10 | 6 | 7 | 5 | 4 | 5 | 3 | 3 | 3 |
| 16 | CL-01 | AI-Factory MV-to-800VDC Power Core | Power | CLEARED_WITH_WEAKNESS | **73** | 16 | 13 | 10 | 6 | 7 | 6 | 3 | 5 | 3 | 2 | 2 |
| 17 | CL-21 | Superconducting Power Delivery & Fault Limiting | Power | CLEARED | **72** | 18 | 14 | 9 | 4 | 7 | 6 | 4 | 5 | 2 | 1 | 2 |
| 18 | CL-28 | Implantable Therapeutic Delivery & Closed-Loop Devices | Biomedical | CLEARED | **72** | 16 | 12 | 11 | 5 | 7 | 6 | 4 | 5 | 2 | 2 | 2 |
| 19 | CL-20 | Cryogenic Power Electronics & Cryo Balance-of-Plant | Extreme | CLEARED | **71** | 15 | 12 | 9 | 6 | 7 | 6 | 4 | 5 | 3 | 2 | 2 |
| 20 | CL-04 | Grid Interconnection & BTM Prime Power | Power | CLEARED_WITH_WEAKNESS | **71** | 15 | 13 | 11 | 6 | 6 | 5 | 3 | 5 | 3 | 2 | 2 |
| 21 | CL-17 | Embodied-AI Data-Capture Engine | Industrial | CLEARED_WITH_WEAKNESS | **71** | 13 | 10 | 8 | 9 | 6 | 4 | 3 | 5 | 6 | 4 | 3 |
| 22 | CL-26 | Neural Interface & Implant Engine | Biomedical | CLEARED | **70** | 16 | 13 | 10 | 5 | 7 | 6 | 3 | 5 | 2 | 1 | 2 |
| 23 | CL-16 | Precision Mfg & In-Process Quality Cells | Industrial | CLEARED_WITH_WEAKNESS | **70** | 14 | 11 | 10 | 7 | 7 | 6 | 1 | 6 | 2 | 2 | 4 |
| 24 | CL-11 | Advanced Substrate Manufacturing | Semiconductor | CLEARED_WITH_WEAKNESS | **70** | 14 | 12 | 10 | 5 | 7 | 6 | 4 | 5 | 4 | 1 | 2 |
| 25 | CL-06 | Vehicle & Defense Electrified Power + SS Protection | Power | CLEARED | **65** | 16 | 11 | 9 | 5 | 7 | 6 | 1 | 5 | 1 | 2 | 2 |
| 26 | CL-22 | Harsh-Environment SiC/GaN Electronics & Sensing | Extreme | CLEARED_WITH_WEAKNESS | **64** | 15 | 11 | 9 | 5 | 7 | 6 | 1 | 5 | 1 | 2 | 2 |
| 27 | CL-05 | LDES & Hybrid-Plant Power Conversion | Power | CLEARED_WITH_WEAKNESS | **63** | 13 | 10 | 8 | 6 | 6 | 5 | 3 | 4 | 4 | 2 | 2 |
| 28 | CL-23 | Fusion Plasma-Facing & Liquid-Metal Subsystems | Extreme | CLEARED_WITH_WEAKNESS | **62** | 14 | 10 | 7 | 4 | 7 | 5 | 4 | 4 | 3 | 2 | 2 |
| 29 | CL-30 | Cryogen-Free Medical Imaging Magnet | Biomedical | CLEARED_WITH_WEAKNESS | **62** | 14 | 10 | 9 | 4 | 6 | 5 | 5 | 4 | 3 | 1 | 1 |

*Tie-breaks applied: (1) CLEARED outranks CLEARED_WITH_WEAKNESS; (2) higher boundary-shift; (3) higher founder-fit. (CL-10>CL-12 at 82; CL-25>CL-13>CL-29 at 77; CL-08>CL-03>CL-14 at 75; CL-21>CL-28 at 72; CL-20>CL-04>CL-17 at 71; CL-26>CL-16>CL-11 at 70; CL-23>CL-30 at 62.)*

---

# Deliverable 2 — Top 25 frontier candidates

Ranks 1–25 above. The four clusters **not** in the Top 25: CL-22 (26), CL-05 (27), CL-23 (28), CL-30 (29).

### Top-25 portfolio quota tally (binding 10E rule 4)

| Domain bucket | Count in Top 25 | Min required | Status |
|---|---|---|---|
| Power | 5 (CL-02, CL-03, CL-01, CL-21, CL-04) | ≥3 | PASS |
| Semiconductor | 5 (CL-07, CL-10, CL-09, CL-08, CL-11) | ≥3 | PASS |
| Biomedical | 5 (CL-25, CL-29, CL-27, CL-28, CL-26) | ≥3 | PASS |
| Industrial | 6 (CL-12, CL-15, CL-13, CL-14, CL-17, CL-16) | ≥3 | PASS |
| Extreme | 3 (CL-18, CL-19, CL-20) | ≥3 | PASS (exactly at minimum) |
| **Data-center-only (strict)** | **2 (CL-03, CL-08)** | ≤8 | **PASS** |

> **Final Top-25 tally: Power 6 (CL-01/02/03/04/06/21) · Semiconductor 5 · Biomedical 5 · Industrial 6 · Extreme 3 · data-center-only 2 (≤8)** = 6+5+5+6+3 = 25. ✔ All five domain minima (≥3) met; DC-only well under the cap. The natural score ranking satisfied the quota with **no weak idea forced in** — Extreme lands exactly at its floor of 3, so CL-22/CL-23 (the next Extreme clusters) were correctly left out on merit, not quota.
>
> **DC-leaning treatment:** CL-01/02/07/09/21 are data-center-leaning-with-adjacency; each is ranked on its non-DC-exclusive framing (CL-02 EV/microgrid DC; CL-07 RF/defense diamond; CL-09 broader optics/telecom; CL-01 MCS charging via PWR-12; CL-21 SFCL grid/shipboard), so per rule 4 they are **not** counted against the DC-only cap. Strict DC-only stays = 2.

---

# Deliverable 3 — Top 12 deep-dive candidates

| Rank | Cluster | Name | Domain | Track | Total | Why it is a deep-dive priority |
|---|---|---|---|---|---|---|
| 1 | CL-07 | Chip-Package Thermal Boundary Shift | Semiconductor | FOUNDER_PILOTABLE | 84 | Near-junction fluidics gates every >2 kW accelerator package; unregulated thermal HW, $5–20M, OSAT co-dev. |
| 2 | CL-18 | HTS Magnet Protection, Charging & Control | Extreme | FOUNDER_PILOTABLE | 83 | Detection-to-actuation quench loop every HTS magnet needs; clearest extreme-lane engine; IOP SUST/Nuclear Fusion Q1. |
| 3 | CL-10 | Hybrid-Bonding & Adv-Packaging Process-Control | Semiconductor | FOUNDER_PILOTABLE | 82 | Closed-loop metrology that actuates the bonder; deepest control loop in the pool; gates 3D-IC/HBM yield. |
| 4 | CL-12 | Power-Module & WBG Packaging/Manufacturing | Industrial | FOUNDER_PILOTABLE | 82 | Void-controlled sinter + feed-forward yield engine; genuine China-first process-IP wedge; $8–20M. |
| 5 | CL-15 | Force / Tactile Sensing Engine | Industrial | FOUNDER_PILOTABLE | 80 | Full-hand tactile + impulse-tolerant 6-axis F/T; dexterity gate; low capex; surgical crossover (BIO-002). |
| 6 | CL-09 | CPO Optical Assembly & Test | Semiconductor | FOUNDER_PILOTABLE | 79 | Owns the CPO fiber-attach bottleneck; instrumented active-alignment cell; Frontiers of Optoelectronics Q1. |
| 7 | CL-02 | 800VDC DC-Side Protection | Power | FOUNDER_PILOTABLE | 78 | µs SiC breaker/e-fuse; hard physics gate (no DC current zero); buildable by a small team. |
| 8 | CL-25 | Energy-Based Intervention Engines | Biomedical | PARTNER_ONLY_FLAGSHIP | 77 | PFA/histotripsy/FUS energy-as-intervention; PFA generator is founder-pilotable; Nature Medicine/Circulation Q1. |
| 9 | CL-13 | Battery / Solid-State Manufacturing | Industrial | FOUNDER_PILOTABLE | 77 | Dry-electrode R2R + sulfide SE film lines; removes costliest cell step; process-IP wedge. |
| 10 | CL-29 | Bio-Manufacturing & Intervention-Decision Instruments | Biomedical | FOUNDER_PILOTABLE | 77 | Parallelized LNP + decentralized CAR-T engines (clearing anchors); founder-pilotable with partners. |
| 11 | CL-19 | HTS Conductor Supply Chain & Qualification | Extreme | FOUNDER_PILOTABLE | 76 | In-line REBCO Jc/defect QC + joints + cabling + test; throat of the HTS supply chain for the fusion magnet boom. |
| 12 | CL-08 | In-/On-Package Power Delivery | Semiconductor | FOUNDER_PILOTABLE | 75 | Vertical IVR chiplet under the die; the only way to feed kW packages without IR/area collapse. |

---

# Deliverable 4 — Top 5 R&D pilot tracks

All five are FOUNDER_PILOTABLE with a credible bench→pilot path inside 2026–2028 and sub-$30M capex — the strongest "build it now" R&D bets.

1. **PILOT-1 · Near-junction fluidic cooling cell (CL-07).** 2026 2 kW test vehicle → 2027 accelerator qual with an OSAT → 2028 pilot line. Capex $5–20M (Si etch outsourceable). KPI: <0.05 K/W across mm die-height step on a real 2 kW GPU + 35 W HBM stack. *Carry-forward repair: drop S07 (Functional Diamond) before DB build.*
2. **PILOT-2 · Fiber-optic quench detection-to-actuation loop for HTS magnets (CL-18).** 2026 77 K pancake → 2027 4.2 K REBCO coil → 2028 closed-loop dump/heater fire on a customer coil. KPI: sub-second, <1 cm-resolution normal-zone localization in tokamak EM noise that **fires protection** (not monitoring).
3. **PILOT-3 · Inline hybrid-bond metrology with closed-loop APC (CL-10).** 2026 standalone inline head → 2027 closed-loop with a bonder OEM → 2028 integrated. KPI: 100% wafer void/overlay/Cu-recess inspection writing a corrective bonder recipe at throughput. *Do not admit SEM-24 (UCIe) as clearing evidence; export-control both legs.*
4. **PILOT-4 · Silver-sinter die-attach cell with inline void metrology (CL-12).** 2026 void spec on >2400 mm² die → 2027 line integration → 2028 power-cycle qual. KPI: closed-loop void control on large-area joints with reliability data. *Keep SEM-12 SiC-defect PL as feed-forward control, not diagnostics-only.*
5. **PILOT-5 · Full-hand e-skin + overload-tolerant 6-axis F/T sensing engine (CL-15).** 2026 palm+finger patch / sensor drift+drop tests → 2027 full-hand + foot/wrist integration → 2028 volume qual. KPI: >60,000 mm² coverage at <3.5 mm super-resolution; F/T temp drift ~0.2% FS surviving impulse overload. *Cite IND-12 to IEEE Sensors Journal (resolved).*

---

# Deliverable 5 — Red-team failure case for each Top 12

Each is the most credible "how this dies" path, drawn from the cluster's own kill criteria and the carry-forward weaknesses.

1. **CL-07 (84).** *Boundary collapses to a cheaper substitute.* If lidless **direct-die** cold plates reach <0.05 K/W, or HBM is moved **off-package** (optical/CXL memory disaggregation), the near-junction fluidic boundary shift evaporates and the product becomes a premium cooler in a commoditizing cold-plate market. Leak risk near live silicon at rack scale is an existential reliability tail. *Skeptic adjustment: defensibility held to 5 for this reason.*
2. **CL-18 (83).** *The pain is real but the buyer count is tiny and timeline-fragile.* If conventional **voltage-tap + inductive compensation** reaches adequate trip latency at scale by 2028, the optical loop becomes a nice-to-have; and if private-fusion magnet build rates slip (CFS/Type One/Tokamak Energy schedule risk), the served market is a handful of programs that may in-source (CFS/MIT already do quench R&D). Fusion dual-use export adds friction.
3. **CL-10 (82).** *Incumbent bundling + export-control vise.* KLA/Onto/Bruker bundle closed-loop APC into their metrology, or hybrid bonding ramps slower than HBM4 roadmaps assume — either removes the wedge. The cluster is **export-controlled both ways**, so the "China-mfg second leg" is largely foreclosed, capping the addressable market to US/Korea fabs. IND-19 (D2W placement) cannot reach economics without fab co-development it may never get.
4. **CL-12 (82).** *China commodity trap if the IP is just a press.* Silver-sinter presses are sold by ASMPT et al.; if **sampled offline C-SAM stays "good enough"** and paste chemistry advances trivialize void control, the differentiator collapses to a metrology add-on. CHINA_FIRST_ATTRACTIVE only survives because the wedge is inline-metrology + closed-loop process IP, **not** the press — lose that and it is a localization clone with no moat. SEM-12 must stay feed-forward control or it degrades to diagnostics-only.
5. **CL-15 (80).** *Sensing gets designed out.* If **vision + joint-current torque estimation** proves adequate for humanoid manipulation, OEMs accept sparse fingertip sensing and the full-hand e-skin/F/T engine is a cost adder. Abrasion/wash durability is unproven; e-skin that cannot survive contact cycles is dead on arrival. China manufacturability means commoditization pressure unless the super-resolution + sensor-fusion IP holds.
6. **CL-09 (79).** *Passive alignment reaches parity.* If **photonic wire bonding / passive (V-groove) alignment** hits volume yield, the sub-100nm active-alignment cell is over-engineered. SEM-22 (optical KGD) is on the monitoring-loop WATCH — if wafer-level optical test **cannot predict post-assembly yield**, it stays monitoring-only and cannot lift the cluster. ficonTEC/PI already sell alignment platforms.
7. **CL-02 (78).** *800VDC adoption stalls.* If hyperscalers stay at **400VDC with conventional protection**, the µs DC breaker has no native bus to protect. UL489-DC / IEC arc-fault standards are still settling; a slow standard delays every design-in, and ABB (SACE Infinitus)/Eaton/Littelfuse are validating competing approaches. Physics gate is real but the market is timing-dependent.
8. **CL-25 (77).** *Incumbent generator lock-out + clinical failure.* Boston Scientific (Farapulse)/Medtronic/J&J make integrated PFA generators standard and **refuse merchant supply**, leaving only weak long-tail OEMs; or porcine durability parity fails by 2027. BIO-018 (steerable tcFUS) carries an explicit **efficacy-vs-sham HOLD** (clinical) and must not be treated as proven; PACE S-04 dropped. Histotripsy capex ($25–50M) and Class III trials slow the non-PFA members.
9. **CL-13 (77).** *Patent wall + China margin trap.* Tesla/Maxwell-lineage **dry-electrode IP** blocks freedom-to-operate, or fibrillation uniformity fails at web scale. CHINA_FIRST_ATTRACTIVE risks a commodity localization play unless the process IP is genuinely defensible; the solid-state (sulfide SE) leg is earlier-TRL and leans US/EU-first, so the near-term China thesis rests mainly on dry-electrode.
10. **CL-29 (77, CWW).** *Incumbents close the scale-up gap; WATCH members can't carry it.* Precision NanoSystems/Cytiva close the LNP scale-transfer gap and lock CDMOs, or allogeneic CAR-T removes per-patient manufacturing (killing the bedside instrument). The cluster's exciting instruments — **OPM-MEG (BIO-017, monitoring-only bar), nanopore protein seq (BIO-020), spatial multi-omics (BIO-025)** — are WATCH and **must not lift the score** until they actuate a decision / prove engine-purity vs ONT/10x/Bruker. CWW ceiling applied.
11. **CL-19 (76).** *Architecture obviates the engine + dual-use export.* If magnets move to **jointless winding** or tape Jc uniformity improves enough that defect mapping commoditizes, the QC engine loses its reason to exist. HTS is **dual-use export-exposed** (CHINA_FIRST_DANGEROUS — the China leg cannot be a clone), and EXT-13 (SULTAN-class test bed) is very-high capex that drags capital efficiency. Demand is fusion-timeline-coupled.
12. **CL-08 (75).** *Foundry/board-PDN substitution.* If board VRMs + better PDN suffice, or a foundry **bundles IVR** into the package offering, the vertical power-delivery chiplet is absorbed by the incumbent stack. The PWR-20 "last-inch loss" metric was a company claim and **must be re-anchored** (folds into SEM-09). Strict data-center-only exposure concentrates the risk on the AI-accelerator cycle.

---

# Deliverable 6 — Watchlist appendix (high-upside, weak-evidence / blocked / conditional)

These are **not scored** as clearing rows. They are tracked for re-entry once the stated repair lands.

### 6a. Source-blocked / individually excluded (must be repaired before scoring)

| Item | Parent | Status | What it would take to admit |
|---|---|---|---|
| **CL-24 / EXT-17** Cryo-CMOS Quantum Control | — (whole cluster) | BLOCKED (may_proceed=no) | Sole anchor APL Quantum is unrankable/CANNOT_VERIFY + IBM (company) + unpinned ISSCC. Cite a ranked Q1/Q2 journal **or** a specific accepted ISSCC/JSSC/VLSI cryo-CMOS controller paper → becomes a WATCH-eligible moonshot. High upside (qubit-count chokepoint) but crowded/contested market + advanced-node & quantum export controls. **Not scored.** |
| **SEM-24** Chiplet at-speed UCIe test | CL-10 | WEAK_SIGNAL_ONLY (excluded) | UCIe is a consortium spec with **no peer-reviewed anchor**. Secure a Q1/flagship (or top-conference) anchor **and** confirm a binning **feed-forward** action. CL-10 was scored on SEM-05 only; SEM-24 contributed nothing to CL-10's score. |
| **IND-01 headline 18–22 Nm/kg** continuous torque density | CL-14 | HOLD (metric excluded) | No peer-reviewed home (blogs/preprints). Ground in a peer-reviewed actuator review/measurement. CL-14 was scored on IND-21/04/02/20/22; the headline metric was **not** used as clearing evidence. |

### 6b. Moonshot WATCH — scored but flagged (>2030 / >$25M / dual-use)

| Cluster | Rank | Watch reason |
|---|---|---|
| **CL-21** Superconducting Power Delivery & Fault Limiting | 17 (Top 25) | Very-high-capex SC busway; HTS/cryo dual-use + novel MVDC approval. Ranks high on impact (BS 18 / SU 14) but PP 4 / CE 1 / RG 2 reflect the moonshot reality. Keep WATCH. |
| **CL-23** Fusion Plasma-Facing & Liquid-Metal Subsystems | 28 (not Top 25) | Programmatic pull, research-only risk past 2030; both members (EXT-08/EXT-18) WATCH. CWW. |
| **CL-30** Cryogen-Free Medical Imaging Magnet | 29 (not Top 25) | $40–100M; multicenter uptime/homogeneity pending; single SuST Q2 anchor. CWW. Genuine China helium-importer wedge but capital-prohibitive solo. |

### 6c. Monitoring-loop WATCH — may only count if they actuate/control/qualify/change treatment

Per 10E rule 6, these were **held to the loop bar** and did not lift their parent cluster's score until the loop is demonstrated:

- **SEM-22** (CL-09) — optical KGD must drive **feed-forward die disposition**, else it is monitoring-only.
- **EXT-11** (CL-22) — hypersonic TPS sensing must feed **flight/thermal control**, not post-flight inspection.
- **BIO-017** (CL-29) — OPM-MEG must tie to **epileptogenic-zone localization** (change the surgical plan), else monitoring-only.

### 6d. Engine-purity / long-horizon WATCH members

- **IND-14** (CL-17) — engine-layer purity: hardware rig vs **data-as-a-service** anti-pattern; replace non-ICLR preprints. (Parent scored, capped at 71.)
- **BIO-020 / BIO-025** (CL-29) — nanopore protein seq / spatial multi-omics: engine-purity vs ONT / 10x / Bruker / Vizgen incumbents; high capex.
- **BIO-016** (CL-26) — cortical visual prosthesis: long clinical horizon (revenue WATCH).
- **EXT-08 / EXT-18** (CL-23) — programmatic fusion moonshots.
- **IND-19** (CL-10) — D2W hybrid-bond placement: non-source HOLD (fab co-dev path / capex / export); did not boost CL-10.
- **BIO-018** (CL-25) — steerable tcFUS: clinical efficacy-vs-sham HOLD; did not boost CL-25.

### 6e. Open repairs to resolve before the database build (carried forward, not waived)

CL-01/04/08 company-claim metric re-anchors (ISS-017/027/018); CL-07 drop S07; CL-22 drop S36/S38, re-cite S37/RPR-06; CL-15 replace IND-12 arXiv with IEEE Sensors Journal; CL-25 drop PACE S-04. Each is reflected as a penalty in the affected sub-scores.

---

# Deliverable 7 — CSV-ready rows for `frontier_scored_database.csv`

> These rows are provided as text only. The master `08_frontier_research/frontier_scored_database.csv` is **NOT** modified by this pass. `candidate_id` = cluster id. `evidence_status` = cluster source_status. `decision` ∈ {TOP12, TOP25, RANKED, WATCHLIST}.

```csv
rank,candidate_id,candidate_name,total_score,boundary_shift_score,system_unlock_score,pain_wtp_score,prototype_path_score,hw_sw_depth_score,defensibility_score,china_wedge_score,us_expansion_score,reg_export_inverse_score,capital_efficiency_score,founder_fit_score,evidence_status,decision,notes
1,CL-07,Chip-Package Thermal Boundary Shift,84,18,13,10,8,7,5,6,5,5,3,4,CLEARED,TOP12,"Near-junction fluidics gates >2kW packages; founder-pilotable $5-20M; drop S07; risk=lidless direct-die or HBM off-package"
2,CL-18,"HTS Magnet Protection, Charging & Control",83,17,13,11,8,8,6,4,5,4,3,4,CLEARED,TOP12,"Detection-to-actuation quench loop; clearest extreme engine; risk=voltage-tap latency catches up + tiny fusion buyer set"
3,CL-10,Hybrid-Bonding & Advanced-Packaging Process-Control,82,17,14,11,7,8,7,3,5,3,3,4,CLEARED,TOP12,"Closed-loop metrology actuates bonder; SEM-24 excluded; export-controlled both ways; risk=KLA/Onto bundle APC"
4,CL-12,Power-Module & WBG Packaging/Manufacturing,82,16,12,10,8,7,6,6,5,5,3,4,CLEARED,TOP12,"Void-controlled sinter + feed-forward yield; genuine China process-IP wedge; risk=offline C-SAM stays adequate"
5,CL-15,Force / Tactile Sensing Engine,80,16,12,9,8,7,5,5,5,5,4,4,CLEARED,TOP12,"Full-hand tactile + impulse-tolerant 6-axis F/T; cite IEEE Sensors Journal; risk=vision+current-estimation displaces F/T"
6,CL-09,CPO Optical Assembly & Test,79,16,13,10,8,7,5,4,5,4,3,4,CLEARED,TOP12,"Owns CPO fiber-attach bottleneck; SEM-22 KGD must feed-forward; risk=passive/photonic-wire-bond alignment parity"
7,CL-02,800VDC DC-Side Protection,78,17,11,10,8,7,6,3,5,4,3,4,CLEARED,TOP12,"us SiC breaker/e-fuse; hard physics gate; founder-pilotable; risk=hyperscalers stay 400VDC; UL489-DC slips"
8,CL-25,Energy-Based Intervention Engines,77,17,13,11,6,7,6,4,5,3,2,3,CLEARED,TOP12,"PFA/histotripsy/FUS; PFA generator founder-pilotable; BIO-018 efficacy-vs-sham HOLD; drop PACE S-04; risk=incumbent generator lockout"
9,CL-13,Battery / Solid-State Manufacturing,77,16,12,10,7,6,5,5,5,5,2,4,CLEARED,TOP12,"Dry-electrode R2R + sulfide SE film; process-IP wedge; risk=Tesla/Maxwell IP wall + China margin trap"
10,CL-29,Bio-Manufacturing & Intervention-Decision Instruments,77,15,12,10,7,7,6,4,5,4,3,4,CLEARED_WITH_WEAKNESS,TOP12,"LNP/CAR-T clearing anchors; BIO-017/020/025 WATCH did not lift score; CWW ceiling; risk=incumbents close scale-up gap"
11,CL-19,HTS Conductor Supply Chain & Qualification,76,16,13,10,7,7,6,3,5,3,2,4,CLEARED,TOP12,"In-line REBCO Jc QC + joints + cabling + test; HTS dual-use export; CHINA_FIRST_DANGEROUS wedge penalized; risk=jointless winding"
12,CL-08,In-/On-Package Power Delivery,75,16,12,10,7,7,5,3,5,4,2,4,CLEARED,TOP12,"Vertical IVR chiplet under die; strict DC-only; PWR-20 metric re-anchor; risk=foundry bundles IVR or board PDN suffices"
13,CL-03,AI-Load Power-Smoothing & GFM Buffer,75,15,11,10,8,7,5,3,5,4,3,4,CLEARED,TOP25,"Rack buffer founder-pilotable; strict DC-only; PWR-18 must actuate not monitor; risk=GPU vendors solve in firmware"
14,CL-14,Robot & Surgical Actuation Engine,75,14,12,9,8,7,5,3,5,4,4,4,CLEARED_WITH_WEAKNESS,TOP25,"IND-01 18-22 Nm/kg metric EXCLUDED; cleared on IND-21/04/02; CHINA_FIRST_DANGEROUS wedge penalized; commodity-actuator trap risk"
15,CL-27,Intervention Robotics & Steerable Access,74,16,12,10,6,7,5,4,5,3,3,3,CLEARED,TOP25,"Steerable/robotic access modules; Magbot=timing only; shares actuation core CL-14/15; risk=steerable guidewires undercut"
16,CL-01,AI-Factory MV-to-800VDC Power Core,73,16,13,10,6,7,6,3,5,3,2,2,CLEARED_WITH_WEAKNESS,TOP25,"AI-factory power chokepoint; 800VDC arch=company/timing re-anchor; partner-only low pilotability; CWW ceiling"
17,CL-21,Superconducting Power Delivery & Fault Limiting,72,18,14,9,4,7,6,4,5,2,1,2,CLEARED,TOP25,"MOONSHOT WATCH-flagged; very-high capex SC busway + SFCL; HTS/cryo dual-use; high impact but PP/CE/RG low"
18,CL-28,Implantable Therapeutic Delivery & Closed-Loop Devices,72,16,12,11,5,7,6,4,5,2,2,2,CLEARED,TOP25,"Leadless pacing + micropump + RDN endpoint; strongest clinical anchors (NEJM/Heart Rhythm); Class III + high capex limit"
19,CL-20,Cryogenic Power Electronics & Cryo Balance-of-Plant,71,15,12,9,6,7,6,4,5,3,2,2,CLEARED,TOP25,"Cryo SiC/GaN module + cryo BOP picks-and-shovels; partner-led; program-dependent demand"
20,CL-04,Grid Interconnection & BTM Prime Power,71,15,13,11,6,6,5,3,5,3,2,2,CLEARED_WITH_WEAKNESS,TOP25,"Speed-to-power microgrid; #1 interconnect-queue pain; BTM scale on journalism re-anchor; partner-gated; CWW ceiling"
21,CL-17,Embodied-AI Data-Capture Engine,71,13,10,8,9,6,4,3,5,6,4,3,CLEARED_WITH_WEAKNESS,TOP25,"Lowest-capex rig $1-5M; engine-purity WATCH (hardware vs data-SaaS); replace non-ICLR preprints; risk=OEMs build rigs in-house"
22,CL-26,Neural Interface & Implant Engine,70,16,13,10,5,7,6,3,5,2,1,2,CLEARED,TOP25,"Hermetic package/ASIC/power engine for BCI wave; NEO/policy=timing only; high cleanroom/capex; long clinical horizon"
23,CL-16,Precision Mfg & In-Process Quality Cells,70,14,11,10,7,7,6,1,6,2,2,4,CLEARED_WITH_WEAKNESS,TOP25,"Qualify-as-you-build in-process remediation; NOT_CHINA_FIRST (ITAR moat); cite PR control papers; ITAR reg risk; CWW ceiling"
24,CL-11,Advanced Substrate Manufacturing,70,14,12,10,5,7,6,4,5,4,1,2,CLEARED_WITH_WEAKNESS,TOP25,"Glass-core/panel RDL yield engine; $30-80M panel cleanroom (capital-eff=1); confirm partner path; CWW ceiling"
25,CL-06,Vehicle & Defense Electrified Power + SS Protection,65,16,11,9,5,7,6,1,5,1,2,2,CLEARED,TOP25,"MVDC ship + eVTOL HV protection; NOT_CHINA_FIRST; heavy ITAR/aviation-cert (reg=1); eVTOL timing uncertain"
26,CL-22,Harsh-Environment SiC/GaN Electronics & Sensing,64,15,11,9,5,7,6,1,5,1,2,2,CLEARED_WITH_WEAKNESS,RANKED,"SiC/GaN past 175C Si wall; NOT_CHINA_FIRST; EXT-11 monitoring WATCH; drop S36/S38; heavy ITAR/NRC (reg=1); CWW ceiling"
27,CL-05,LDES & Hybrid-Plant Power Conversion,63,13,10,8,6,6,5,3,4,4,2,2,CLEARED_WITH_WEAKNESS,RANKED,"Power-layer-optimized PCS+BOP; commercial LDES early; BOP-cost-driver partly inferred; partner-only; CWW ceiling"
28,CL-23,Fusion Plasma-Facing & Liquid-Metal Subsystems,62,14,10,7,4,7,5,4,4,3,2,2,CLEARED_WITH_WEAKNESS,WATCHLIST,"MOONSHOT WATCH; LM PFC flow-control + HHF test bed; research-only risk past 2030; both members WATCH; CWW ceiling"
29,CL-30,Cryogen-Free Medical Imaging Magnet,62,14,10,9,4,6,5,5,4,3,1,1,CLEARED_WITH_WEAKNESS,WATCHLIST,"MOONSHOT WATCH; helium-free 1.5T magnet; $40-100M (capital-eff=1); single SuST Q2 anchor; uptime data pending; CWW ceiling"
```

---

## Compliance check (10E §3 rules)

1. **Eligibility binding** — only the 29 eligible clusters scored; no new candidate/wedge introduced. ✔
2. **Blocked items not admitted** — CL-24 not scored; SEM-24 and IND-01's headline metric not used as clearing evidence (watchlist only). ✔
3. **Source policy strict / confidence ceiling** — no CWW cluster scores ≥78; the top 9 are all CLEARED; company/journalism/market/consortium sources used as timing only. ✔
4. **Portfolio quota honored** — Top 25 = Power 6 / Semi 5 / Bio 5 / Industrial 6 / Extreme 3 (all ≥3); DC-only 2 (≤8). ✔
5. **Tracks respected** — moonshots (CL-21/23/30) ranked on impact but WATCH-flagged; FOUNDER/PARTNER/MOONSHOT not used as a quality order. ✔
6. **Monitoring-loop bar enforced** — SEM-22 / EXT-11 / BIO-017 held to the actuation bar; did not lift parent scores. ✔
7. **Open repairs carried forward** — CL-01/04/08 re-anchors, CL-07 S07, CL-22 S36/S38, CL-15 IEEE Sensors Journal, CL-25 PACE S-04 all penalized and flagged, not waived. ✔
8. **China posture binding** — NOT_CHINA_FIRST (CL-06/16/22) scored low on china-wedge (1) and not paired with a China-first thesis; CHINA_FIRST_DANGEROUS (CL-14/17/19) penalized to china-wedge 3 absent a clone-proof wedge. ✔

```text
RANK_RED_TEAM_COMPLETE = YES
CLUSTERS_SCORED = 29
MASTER_CSVS_MODIFIED = NONE
```
