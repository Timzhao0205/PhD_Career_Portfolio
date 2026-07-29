# TECH CLUSTERS — Patent-search charters P01-P10

Each cluster = one patent-scout run. CPC codes below are **candidate entry points — fetch and
verify each class definition during the run** (playbook §2.3); correct or extend in the PL
file. ZH seeds are mandatory passes. "Linked themes" point at the unsolved-problem areas the
whitespace hypotheses should test against (final U-### ids come from Phase 1).

---

## C12 side (Wave 1)

**P01 — SC-tape winding tension & placement control.**
Scope: closed-loop tension control for REBCO/HTS tape winding; turn placement metrology;
laser/vision alignment of tape during coil winding; tension-profile programming; twist/camber
control; kilometer-spool payoff.
EN seeds: "superconducting tape winding tension", "REBCO coil winding apparatus", "HTS coil
winding machine", "tape tension control coil", "winding tension feedback superconduct".
ZH seeds: 超导 带材 绕制 张力; 高温超导 线圈 绕线机; 张力控制 超导; REBCO 绕制; 带材 排线.
CPC candidates: H01F 41/06 (+subgroups), H01F 41/04, H01F 6/06, B65H 23/00, B65H 59/38,
G05B 19/4155, H10N 60/20.
Assignee seeds: CAS Hefei institutes (incl. re-fetch US11581133B2), MIT, NHMFL/Florida State,
KIT, Tokamak Energy/Ridgway, Broomfield, SuNAM, SuperPower/Furukawa, Fujikura, Shanghai
Superconductor 上海超导, Energy Singularity 能量奇点.
Linked themes: recipe-is-the-design (tension→Rc), first-pass yield, non-planar handling.

**P02 — NI/MI coil architecture & contact-resistance engineering.**
Scope: no-insulation / metal-insulation / partial-insulation coil constructions; co-winding
(stainless/copper) arrangements; turn-to-turn contact resistance control (surface treatment,
oxide layers, interleaves); charging-delay mitigation; 干式绕线 (dry winding) processes;
screening-current strain mitigation via winding parameters.
EN seeds: "no-insulation coil", "metal insulation REBCO", "no insulation superconducting
magnet", "contact resistance turn-to-turn", "partial insulation HTS coil", "co-wound tape".
ZH seeds: 无绝缘 线圈; 金属绝缘 超导; 无绝缘 超导磁体; 匝间 接触电阻; 干式绕线; 屏蔽电流.
CPC candidates: H01F 6/06, H01F 6/02, H01F 41/04, H10N 60/20, Y02E 40/60.
Assignee seeds: MIT, Korea (SuNAM, KERI, Seoul National Univ), FSU/NHMFL (incl. the active-
feedback charging-delay work referenced in the corpus), ASIPP 中科院等离子体所, CFS, 健信超导.
Linked themes: predictable Rc, MI variants, delamination avoidance.

**P03 — HTS joints & in-situ joint-resistance verification.**
Scope: REBCO-REBCO soldered/bridged joints; joint fixtures; nano-ohm measurement of joints
(in-situ or in-process); superconducting joint fabrication for coils/cables; joint QC.
EN seeds: "REBCO joint resistance", "superconducting tape joint apparatus", "HTS splice",
"nano-ohm joint measurement", "superconducting joint solder fixture".
ZH seeds: 超导 接头 电阻; 高温超导 焊接 接头; 接头 测量 纳欧; 超导带材 连接.
CPC candidates: H01R 4/68, H10N 60/20, H01F 6/06, G01R 27/(low-resistance measurement —
verify exact subgroup), H01B 12/00.
Assignee seeds: MIT/CFS (VIPER lineage), Fujikura, Furukawa, SuNAM, KERI, ASIPP, Shanghai
Superconductor, Samri?/discover.
Linked themes: production joint yield at nΩ, in-process verification vs post-test scrap.

**P04 — Inline coil/tape QC, defect-map-aware manufacturing & traceability (C33 space).**
Scope: continuous Ic/defect mapping of HTS tape (TapeStar-class); during-winding QC sensing
(Hall arrays, voltage taps, acoustic, optical); defect-map-synchronized feed control;
per-coil digital traceability / birth-certificate records; post-wind coil qualification
instruments; fiber-optic sensing embedded at winding.
EN seeds: "critical current mapping tape", "HTS tape quality inspection", "coil winding
quality monitoring", "in-situ magnet quality control", "fiber optic sensing superconducting
coil", "manufacturing traceability coil".
ZH seeds: 临界电流 检测 带材; 超导带材 缺陷 检测; 绕制 过程 监测; 质量追溯 线圈; 光纤 传感 超导.
CPC candidates: G01R 33/12 (magnetic material testing — verify), G01N 27/00, H01F 41/06,
G05B 19/418, G01R 31/00.
Assignee seeds: THEVA, tape vendors' QC filings (SuperPower/Furukawa, Fujikura, SuNAM, 上海超导),
KIT, national labs; mandate: establish whether ANYONE claims during-winding Rc/defect QC.
Linked themes: the C33 module thesis — "coil with predicted Rc ±20% and logged joint
resistance" as an output spec.

**P05 — Non-planar / robotic winding & coil-forming machinery.**
Scope: robot-cell winding of non-planar coils; winding trajectory generation; end-effectors
for tape laying on 3D formers; D-shape/saddle/stellarator coil winding tooling; inter-layer
transition forming; coil impregnation/handling automation adjacent to winding.
EN seeds: "robotic coil winding superconducting", "non-planar coil winding", "stellarator
coil manufacturing", "winding trajectory tape", "coil former winding apparatus".
ZH seeds: 机器人 绕制 线圈; 非平面 线圈; 仿星器 线圈 制造; 绕制 轨迹; 线圈骨架.
CPC candidates: H01F 41/06, B25J 9/16, H01F 41/098 (verify), B65H 54/00, H01F 7/00.
Assignee seeds: KIT (2025 robot cell), CAS Hefei, Aumann/Marsilli-class winder OEMs, Thea
Energy (planar-array manufacturing), Proxima, Type One/discover.
Linked themes: 6-axis option pack, KIT-proven architecture, planar-array mass production.

---

## C10 side (Wave 2)

**P06 — Precision current regulation & measurement chain (ppm class).**
Scope: high-stability magnet current sources; DCCT/zero-flux current transducer integration;
ADC/reference chains for ppm regulation; drift/thermal compensation of current measurement;
calibration methods for magnet supplies.
EN seeds: "high stability magnet power supply", "ppm current regulation", "zero flux current
transducer", "DCCT power supply", "precision current source magnet", "current calibration
power converter".
ZH seeds: 高稳定度 电源 磁体; 励磁电源 精密; 零磁通 电流互感器; 直流电流 比较仪; ppm 电流.
CPC candidates: G05F 1/56, G01R 15/18, G01R 19/00, G01R 35/00, H02M 3/155.
Assignee seeds: CERN, Danfysik, CAENels, OCEM, Magna-Power, LEM/Danisense, Hioki?/discover,
中科院近代物理研究所 (IMP), 中国科学院高能物理研究所 (IHEP), 爱科赛博, 英杰电气.
Linked themes: measurement-chain-not-switch reality; catalog ppm above 1 kW.

**P07 — WBG fast-dynamics bipolar/4-quadrant magnet converters.**
Scope: SiC/GaN converter topologies for magnet loads; interleaved multiphase ripple
cancellation; 4-quadrant bipolar output stages; kHz-class closed-loop bandwidth into
inductive loads; EMI/common-mode mitigation in precision converters; active-filter-free
ripple suppression.
EN seeds: "SiC magnet power converter", "four quadrant power supply magnet", "interleaved
converter ripple cancellation", "bipolar power amplifier coil", "high bandwidth current
control inductive load", "common mode EMI precision converter".
ZH seeds: 碳化硅 磁体 电源; 四象限 电源; 交错并联 纹波; 双极性 电源 线圈; 快控电源; 共模 干扰 抑制.
CPC candidates: H02M 3/158, H02M 1/12, H02M 1/44, H02M 7/48, H02M 7/797 (verify), H03F 3/217.
Assignee seeds: CERN (JINST-lineage filings if any), CAENels, 爱科赛博 Actionpower, 荣信汇科,
英杰电气, Toshiba/Mitsubishi/Hitachi (accelerator PS), Nichicon?/discover.
Linked themes: the FastCoil wedge; RMP/fast-control tenders; density 2-4x claim.

**P08 — Modular paralleling, kA scaling & many-coil orchestration.**
Scope: N+1 modular converter paralleling with current sharing to kA; hot-swap module
architectures; distributed/synchronized control of many converters; coil-array drive and
orchestration (per-coil supplies, shaping-by-software); high-bandwidth telemetry of converter
fleets; test-stand assembly from modules.
EN seeds: "modular power converter paralleling current sharing", "coil array power supply",
"synchronized converter control accelerator", "scalable magnet power system", "power supply
telemetry ethernet control".
ZH seeds: 模块化 并联 均流; 线圈 阵列 电源; 多机 同步 控制 电源; 磁体 电源 系统; 遥测.
CPC candidates: H02M 3/1584 (verify interleaved subgroup), H02J 1/10, H02M 1/00, G05B 19/042,
H04L (industrial control — discovery only).
Assignee seeds: Thea Energy (array-drive filings — mandate: check), Vertiv/Delta (datacenter
modular art as prior-art risk), CERN, Magna-Power, 爱科赛博, 许继/南瑞-class SOEs.
Linked themes: converter-count architectures (Thea Canis), ALS-U-scale supply avalanches.

**P09 — Quench detection, protection & energy dump integration (C11 absorber).**
Scope: quench detection for HTS/NI coils (voltage, fiber-optic, RF, acoustic, Hall-array);
protection sequencing; dump resistor/switch integration with the converter; energy extraction;
NI-specific charging/quench management; protection electronics as product.
EN seeds: "quench detection HTS", "no insulation coil quench", "quench protection system
superconducting", "fiber optic quench detection", "energy dump superconducting magnet",
"quench detection Hall sensor array".
ZH seeds: 失超 检测; 失超 保护; 高温超导 失超; 无绝缘 线圈 保护; 能量泄放; 光纤 失超.
CPC candidates: H02H 7/00 (superconducting-apparatus protection subgroup — verify exact code),
H01F 6/02, G01R 31/00, H10N 60/30.
Assignee seeds: CERN, CFS, MIT, Tokamak Energy, ASIPP, KIT, FSU/NHMFL, 聚变新能/BEST ecosystem,
Actionpower; instrument startups (discover).
Linked themes: detection-latency benchmark experiment; converter+protection bundling (CS-H).

**P10 — Converter fleet software, calibration analytics & digital methods.**
Scope: software/method claims around converter calibration & drift analytics; predictive
maintenance of power converters; model-based control tuning for magnet loads; digital twins
of magnet power systems; winding-cell ↔ converter data interfaces (per-coil records driving
drive parameters) — the joint C12×C10 seam.
EN seeds: "power converter calibration method", "predictive maintenance power supply",
"digital twin power converter", "magnet power supply control method", "coil manufacturing
data control parameter".
ZH seeds: 电源 校准 方法; 预测性 维护 电源; 数字孪生 变流器; 磁体 电源 控制 方法.
CPC candidates: G05B 23/02, G06F 30/20 (verify), H02M 1/00 (control details), G05B 13/04.
Assignee seeds: incumbents above + industrial-software filers; mandate: characterize how
crowded generic "digital twin converter" art is vs the magnet-specific seam, and note CN
examination posture on software/method claims (mental-steps/utility framing) as a counsel
question, not a conclusion.
Linked themes: recipe-software subscription moat; trade-secret-vs-patent split (GROUND RULES §5).
