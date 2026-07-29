# PL_P05 — Non-planar / robotic winding & coil-forming machinery

Run 2026-07-04. All 22 cited numbers fetched this run at their Google Patents pages
(PL_P05_patents.json, `verified:"fetched"`). Landscape read only — NOT an FTO or
patentability opinion; legal-status lines are as displayed on GP, indicative.

## Method & saturation

All five playbook passes run. (1) EN keywords: robotic coil winding superconducting /
non-planar coil winding / stellarator coil manufacturing / winding trajectory / saddle coil
winding machine / coil former winding apparatus. (2) Assignees: Tokamak Energy(+Ridgway),
Thea/Princeton, Type One, Proxima, MIT/CFS, KIT, CAS Hefei (HFIPS/ASIPP), Aumann, Marsilli,
Nittoku, 北京原力辰超导, 合肥曦合超导, 星环聚能, 能量奇点. (3) CPC definitions fetched from
USPTO CPC scheme (corrections below). (4) ZH pass: 机器人 绕制 线圈 / 非平面 线圈 / 仿星器
线圈 制造 / 绕制 轨迹 / 线圈骨架 / 三维 绕线机 / 双饼 绕制 / 托卡马克 绕制 装置 — utility
models captured (2 in ledger). (5) Citation chase one hop from US9105396B2, WO2023234913A2,
US11289253B2, CN108461277B, CN101719408A. Saturation: last 5 fetches (EP4672265A1,
CN101719408A, CN202861073U, CN107481854A, CN114551083A) added new assignees but zero new
claim themes — CN side repeats planar pancake-winder tension mechanics; Western side repeats
the 2024+ stellarator conductor/plate wave. GP assignee-search pages for 原力辰 returned a
JS shell (limitation logged); zh site-index queries surfaced no filings under 原力辰 / 曦合 /
星环聚能 names.

## CPC verification (charter corrections)

Fetched H01F scheme: **H01F41/098 = "Mandrels; Formers"** — charter flag resolved: it is the
winding-tooling subgroup under H01F41/06 (Coil winding), correct entry for former/mandrel
claims (Zenergy-class art), not a machine-cell code. Verified siblings worth using:
H01F41/082 (guiding/positioning the winding material), /094 (tensioning or braking),
/096 (dispensing/feeding), /09 (machines with 2+ work holders), /071 (coils of special
form). **Add H01F41/048 "{Superconductive coils}"** — the most consistent code on fetched SC
docs (TE, HFIPS, Type One, Proxima, Argonne, Siemens). **Drop H01F7/00** (Magnets — device
class, not machinery). B65H54/22 + B65H59/385 confirmed in the wild on CN108292544B;
H02K55/04 carries saddle-former art (US8058764B2); G21B1/055 carries stellarator device art.
B25J9/16 (robot program control) appeared on none of the 22 fetched records — the
robotics×SC-winding cross-class is empty in everything fetched.

## Landscape read

**Assignee × year.** Three distinct strata. (a) 2005-2012 EU device-makers: Siemens saddle
re-forming (US7741944B2, priority 2005, KR/RU/CN family) and Zenergy former tooling
(US8058764B2, 2007) — both display as fee-lapsed. (b) 2010-2022 CN planar-machinery stratum:
Tsinghua constant-tension winder (CN101719408A, 2010, lapsed 2019), Hefei Keye R-bend die UM
(CN202861073U, 2012, withdrawn), Guangdong Power Grid EPRI dual-tape DP winder (CN107481854A,
2017, granted), HFIPS inter-layer transition forming machine (US11581133B2, CN sibling
CN108461277B, 2018/2019, active to ~2041/2038), Henan/Newrich "intelligent" winder
(CN114551083A, 2022, granted). (c) 2018-2024 fusion-startup method wave: Tokamak Energy is
the **densest single assignee** (US11289253B2 2018 shunted-turn coils, active to 2039;
CN115485868A/B 2020 PI-by-edge-machining granted in CN; WO2023083956A1 2021 shingle-overlap
winding, displays Ceased), then MIT/CFS non-planar cable/former techniques (WO2023234913A2,
2021, displays Ceased), Princeton/Thea planar-coil stellarator device (US12100520B2, 2022,
active to 2043), and the 2024 stellarator-manufacturing surge: Type One (WO2025221339A3,
priority 2024-02, published 2026-01, pending, TW sibling) and Proxima (EP4672267A1 +
EP4672265A1, priority 2024-06, published 2025-12, pending).

**Dense vs empty.** Dense: planar pancake/DP winder mechanics with tension feedback (CN);
coil-architecture and PI/NI construction claims (TE); since 2024, stellarator conductor
forming and plate-channel routes (Type One, Proxima, MIT/CFS lineage). Empty in everything
searched: robot-trajectory generation coupled to tape tension/orientation; tape-laying
end-effector apparatus; any winding-cell claim containing QC/traceability/process-recipe
elements; planar-array coil mass-production tooling. The e-mobility OEM estates checked
(Marsilli US20170229947A1/US10348171B2 needle winder; Aumann hits were wire-bobbin devices)
claim **round-wire** guiding structures — fetched claim language does not read on band/tape
conductors, though their generic mechanics remain prior art against machine claims.

**CN vs US center of gravity.** Non-planar HTS *method* claims center in US/WO/EP (fusion
startups + MIT); CN-origin filings found are planar machinery, CICC bend tooling, and
design-method art (SWJTU CN114444337B for CFQS-class modular coils). Western families are
entering CN (TE CN115485868B granted; Siemens CN101164124B historic; US-origin CN108292544B).
The reverse flow is absent: **no CN-origin non-planar/robotic HTS winding-machine publication
was located** despite 原力辰's merchant 3D stellarator winder delivered to USTC and 曦合's
首台套 CICC winder award — bounded by GP zh indexing and the 18-month publication lag.

**Expiry horizon (indicative only).** The foundational saddle/former art displays as already
lapsed: Siemens US7741944B2 "Expired - Fee Related" (2005 priority; displayed expiry 2022),
Zenergy US8058764B2 lapsed 2015, NECOA robotic-cell US5263639A (1992) term-expired, Tsinghua
CN101719408A lapsed 2019. Each "displays as expired — verify before reliance." The active
fence is young: nothing blocking-relevant expires before US9105396B2 (~2033); TE/HFIPS
machinery-adjacent grants run to ~2038-2041; the 2024 stellarator wave, if granted, to ~2044.

## Blocking table (independent-claim depth)

| Doc [fetched] | Assignee | Priority | Status (displayed) | Independent-claim gist | Risk |
|---|---|---|---|---|---|
| WO2025221339A3 | Type One Energy Group | 2024-02-06 | Pending (TW sibling) | Forming stellarator coils: cable bent to tapered helical shape; independent bobbins dispense layers; thin spine+strut stabilization structures for HTS tape | **high** — pending, claims can grow, directly on non-planar coil forming |
| EP4672267A1 | Proxima Fusion | 2024-06-28 | Pending | Stellarator with non-planar plates having non-circular recesses whose orientation changes continuously along winding path to align HTS cable; method steps incl. provision/alignment/fixing | **high** — fences the plate-channel route to non-planar coils |
| US9105396B2 | Takayasu (DOE license noted) | 2012-10-05 | Active, exp ~2033-12-11 | Fabricating coils from stacked-tape cable: bend at corners without twist, twist about longitudinal axis along straight portions (STTW), enabling 3D/saddle geometries | **high** — method reads on twist-managed 3D tape-stack winding practice |
| WO2023234913A2 | MIT + CFS | 2021-05-20 | Ceased (national phases not located this run — verify) | HTS cable: former channels holding tape stacks, both twisted with twist pitch smaller than local bend radius; two-step twist + anneal manufacturing | med — status uncertain; disclosure is strong prior art regardless |
| CN115485868A/B | Tokamak Energy | 2020-05-04 | Granted CN, active | Manufacture HTS field coil by winding tapes about axis then removing material from axial tape edges to control turn-to-turn resistance | med — blocks PI-by-edge-machining inside a CN cell offering |
| US11581133B2 (CN108461277B) | HFIPS, CAS | 2019-08-27 (CN sibling shows 2018-02-01) | Active, exp ~2041 (CN ~2038) | Inter-layer transition forming machine: perpendicular vertical+horizontal hydraulic forming mechanisms, positive/negative-thread wedge clamps, reference-line positioning | med — specific mechanism; design-around plausible but sits exactly in P05 scope |
| US12100520B2 | Princeton (Thea-licensed) | 2022-03-14 | Active, exp ~2043 | Stellarator of planar shaping coils on mounting elements + planar encircling coils; shaping coils individually non-encircling, collectively encircling; no interlocking | med — blocks the planar-array *architecture*, not winding machinery |
| EP4672265A1 | Proxima Fusion | 2024-06-28 | Pending | Non-planar coil cable with inner/outer sections whose cross-section orientations change relative to each other along cable length (pre-adjusted layered SC material) | med — pairs with EP4672267A1 to fence cable-orientation management |

Also monitored: US11289253B2 (TE shunted-turn coils, med, architecture-side);
WO2023083956A1 (TE shingle-overlap winding, displays Ceased, med pending verification);
CN108292544B (Electric Chaos closed-loop tension winding in CN, med); US10249420B2
(Argonne grooved-core continuous winding, med for array-route analogies).

## Whitespace hypotheses (bounded absence — hypotheses only, not patentability conclusions)

**WH-P05-1 — Robot trajectory × tension co-control for non-planar HTS winding.** Searched EN
("robotic coil winding superconducting", "winding trajectory" coil robot) and ZH (机器人 绕制
线圈; 绕线 机器人 轨迹 规划); B25J9/16 cross-hits checked: no US/CN/EP family found claiming
6-axis trajectory generation synchronized with tape tension/orientation for superconducting
coil winding. Nearest art: US5263639A (robot only transfers bobbins between stations;
term-expired), CN108292544B (closed-loop tension, spool-to-spool, no trajectory), WO2025221339A3
(cable forming, no robot claims). KIT's dual-robot cell (SUST 2025-12) has no located filing —
filings after ~2024-12 could still be unpublished. Serves U-003, U-005, U-006.

**WH-P05-2 — Winding-cell process layer (recipe-grade tension profiles + per-coil QC/
traceability) for NI/REBCO non-planar cells.** Searched EN+ZH machine claims for QC/
traceability/recipe elements: none found. Nearest art: CN114551083A ("intelligent" device =
mechanical adaptive pressing only — fetched claim contains no QC/data/robot elements),
CN107481854A (constant tension + length encoder only), US11581133B2 (single-function forming
bench). Serves U-002, U-006 — and confirms the U-002 absence holds in patent space, not just
product space.

**WH-P05-3 — Tape-laying end-effector apparatus for 3D formers (twist/camber/hard-way-bend
management in the head).** Searched "end effector" tape winding, saddle winding machine, ZH
线圈骨架/绕制 轨迹: no apparatus claims on a tape head for non-planar SC laying found. Nearest:
US9105396B2 (twist-wind method, no head apparatus), WO2023234913A2 / EP4672267A1 /
EP4672265A1 (former-channel and cable-orientation claims — the workpiece, not the tool),
Marsilli US20170229947A1 (needle head claims recite round wire). Serves U-003.

**WH-P05-4 — In-line (on-the-fly) inter-layer / inter-pancake transition forming during
continuous winding.** Searched transition/joggle forming claims: only offline bench tooling
found. Nearest: US11581133B2 / CN108461277B (standalone hydraulic transition former),
CN202861073U (hydraulic R-bend die UM, withdrawn). A cell that forms transitions in the
winding path without demounting was not found claimed. Serves U-002, U-006.

**WH-P05-5 — Planar-array mass-production tooling (Thea route).** Searched planar coil
stellarator manufacturing/winding claims across the Princeton/Thea family and assignee pass:
US12100520B2 family claims device configuration only — no located claims on array coil
production lines, batch winding, or array assembly automation. Nearest process analog:
US10249420B2 (grooved-core jointless continuous winding for undulators). Serves U-003 (via
the architecture that substitutes for non-planar winding), U-002.

**WH-P05-6 — CN-origin 3D/non-planar HTS winding machinery (incl. utility models).** ZH
passes (仿星器 线圈 绕制; 三维 绕线机 超导; D形 线圈 绕制 装置; 托卡马克 线圈 绕制 装置; UM
capture on) located zero CN-origin filings claiming non-planar HTS winding machines — nearest
CN art is planar DP winders (CN107481854A), CICC bend dies (CN202861073U), and design methods
(CN114444337B) — despite 原力辰's merchant USTC stellarator winder and 曦合's 首台套 award.
Bounded by GP zh index coverage, JS-shell assignee search, and 18-month lag; a 2025-2026
CN-first filing could surface any month — pre-empting it argues for early CN-inclusive filing
of WH-1/-2/-3 subject matter. Serves U-006, U-003, U-005.

Ledger: 22 records (9 US, 8 CN, 3 WO, 2 EP); families carry KR/RU/TW/GB/DE/EP siblings.
