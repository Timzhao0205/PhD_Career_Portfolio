# G07 — Circular Economy & Critical-Materials Equipment

## Landscape
Circular-economy equipment for critical materials spans four hardware categories: (1) magnet/REE
recycling — demagnetization, hydrogen-decrepitation, solvent-extraction reactors; (2) e-waste
separation — eddy-current, electrostatic, sensor-based (X-ray/NIR/induction) sorters; (3) battery
black-mass/electrolyte recovery — shredding, discharge, powder separation, hydromet feed prep; (4)
urban-mining automation — robotic disassembly/ID. Demand is policy-pulled ahead of market-pulled:
the EU Critical Raw Materials Act mandates >=25% of critical-material consumption from recycling
by 2030, with strategic recycling projects getting a 15-month permitting window [G07-05]; the US
DoW committed $1.4B in loans+equity to ReElement Technologies/Vulcan Elements (Nov 2025) explicitly
to scale recycled-plus-mined REE-to-magnet capacity [G07-13]; China's MIIT tightened
battery-recycling recovery/purity thresholds in Dec 2024 [G07-09]. Feedstock volume (retired
magnets, EVs, e-waste) is only now ramping — this is a build-out-window lane, not a mature one.

## Pains & buyers
Buyers: (a) magnet recyclers (HyProMag, Cyclic Materials, Noveon, ReElement/Vulcan) needing
demag/extraction reactors and feedstock ID; (b) battery-recycling pretreatment plants (156
MIIT-whitelisted Chinese firms plus Western hydromet operators) needing shredding, discharge,
black-mass purity control; (c) WEEE/e-scrap processors needing sorting lines. Pains: (1) feedstock
heterogeneity — magnets sit embedded in disparate form factors (HDDs, motors, wind generators)
with no standard pre-shred ID method, so bulk processing homogenizes high-value heavy-REE (Dy/Tb)
magnets into low-value mixed non-ferrous streams; (2) informal-sector competition — Chinese
licensed recyclers report only ~20-30% of retired batteries reach formal channels because
unregistered workshops skip environmental/tax compliance and simply outbid them [G07-18]; (3)
tightening thresholds (China's 2024 standard: lithium recovery raised 85%->90%, electrode-powder
recovery >=98%, aluminum impurity <1.5% [G07-09]) force capex on inline QC most plants lack; (4)
black-mass handling hazards (combustible fines) require ATEX-rated, inert-atmosphere hardware.

## Incumbents & gaps
Magnet recycling: HyProMag's HPMS hydrogen-decrepitation reactor is still pilot-scale — one
commercial vessel rated up to 5,000 kg/batch, with cumulative output of only 9.2 t of recycled
NdFeB powder (7.4 t shipped to customers) as of April 2026 at its Birmingham site [G07-01][G07-02].
Noveon (Texas) targets >2,000 t/yr magnet output after a $215M Series C (Jan 2026) [G07-10]; Cyclic
Materials (Canada) raised $75M Series C (Jan 2026, $162M cumulative) for hub-and-spoke
magnet-removal sites [G07-08]; ReElement/Vulcan Elements target 10,000 t/yr NdFeB capacity backed
by $620M+$80M DoW loans, $50M DoC equity, and $550M private capital [G07-13]. All are
vertically-integrated recyclers building captive process equipment — none sells a standalone
demag/extraction reactor as a product. Prior art already covers induction-heating demag: UT-Battelle
(ORNL) patent US11250980B2 (granted 2022) claims a >1,000-units/hr line using induction heating to
>=320°C in <5s [G07-16] — but induction-heating demag is charter-excluded for this lane regardless
of assignee.

Battery black-mass mechanical equipment (Metso, ERS, Palamatic, Elcan, Guanma) sells shred/discharge/
airflow lines — mature but instrumentation-poor. China's LFP black mass traded at 2,800-3,000
yuan/%Li in mid-November 2025, moving weekly on lithium-carbonate swings [G07-07] — pricing is
volatile, yet almost no vendor sells inline composition/purity sensing as a standalone product.
Sorting incumbents (Sesotec, SGM Magnetics, TOMRA-class players) are mature, price-opaque (no
public pricing even on primary vendor pages [G07-14][G07-15]) mechanical/optical houses; SGM's ECS
line spans six rotor models (up to 4,800 rpm, separating particles down to 0.2 mm) [G07-14] but
none targets REE-specific magnet identification pre-shred.

Capital-risk lesson: Li-Cycle's $700M-budgeted Rochester Hub, backed by a $475M DOE loan, halted
construction in Sept 2023 and the company filed Chapter 15/CCAA bankruptcy (May 2025), selling to
Glencore on a ~$40M stalking-horse bid for the whole distressed asset package [G07-11][G07-17] —
the vertically-integrated "own-the-hub" model is capital-fragile. Equipment/instrumentation vendors
selling into many recyclers sidestep that commodity-price/capex risk.

## 2029 inflections
(1) EU CRMA's 2030 recycling target and 15-month permitting window [G07-05] starts a recycling
capacity build-out from ~2027. (2) US DoW's $1.4B ReElement/Vulcan commitment targets 10,000 t/yr
NdFeB capacity online ~2027-2028 [G07-13], part of a broader 2026-2029 coordinated domestic-REE
push needing process equipment now, not after plants exist. (3) China's Dec-2024 MIIT standard
[G07-09] forces a retrofit/re-audit cycle across its 156 whitelisted battery recyclers through
~2027. (4) The first big wave of retired Chinese LFP EV packs (2018-2020 vintage, 8-10yr life)
hits scrap volume 2026-2028, straining pretreatment capacity. (5) Post-Li-Cycle, new entrants are
visibly shifting toward capex-light, equipment-buying models rather than Li-Cycle-style vertical
integration [G07-11][G07-17] — good timing for a 2029-launch equipment/instrumentation vendor
rather than another integrated recycler chasing the same capital trap.

## China notes
GEM (格林美) is the clearest domestic magnet-recycling technology leader: >99.9% purity, >90% REE
recovery, >85% non-REE recovery, 57 patents (3 PCT), two recovery centers (Jingmen, Hubei; Fengcheng,
Jiangxi), supplying magnet-maker JL Mag (金力永磁) [G07-12]. On the battery side, 156 MIIT-whitelisted
firms exist, but only ~20-30% of retired-battery flow reaches them — the rest goes to informal
workshops that outbid formal recyclers because they skip environmental and tax compliance [G07-18].
China's Dec-2024 standard [G07-09] is explicitly designed to force consolidation toward the
whitelisted, better-instrumented players. Chinese mechanical-equipment exporters (eddy-current/
magnetic separator makers) compete globally on price, so a US-side team needs genuine sensing/
automation differentiation, not a cheaper ECS clone. The founder's native-Chinese network is a real
edge for OEM-sourcing mechanical subsystems (shredders, conveyors, ECS rotors) from China while
retaining proprietary sensing/automation IP for a dual US+China equipment play.

## Opportunity seeds

**1. Heavy-REE magnetic-signature triage sensor.** A conveyor-mounted magnetometer-array/
field-inversion sensor head — a direct extension of the founder's OPM/current-inversion
instrumentation background — that scans intact magnets/motors pre-shred and classifies NdFeB vs.
ferrite vs. SmCo and high- vs. low-Dy/Tb content, so recyclers route feedstock instead of
homogenizing everything into one low-value eddy-current stream. Sold as a standalone sensor module
to HyProMag/Cyclic/GEM-class recyclers, not as a recycling service. Explicitly avoids C40/RID-016
(classifies dismantled magnets/motors, never battery packs for reuse grading) and stays clear of
HTS (room-temperature array, no superconductors — respects the G6-HTS gate).

**2. Modular non-induction demagnetization/extraction skid.** A containerized hydrogen-decrepitation
reactor plus power-electronics-driven AC (non-induction) demagnetization stage, sold as OEM
equipment to the wave of new magnet recyclers each building captive reactors in-house today (Noveon,
Cyclic, ReElement-class entrants). Targets the gap that no independent vendor sells a turnkey
demag/extraction line. Explicitly avoids C16 (no induction-heating stage — the UT-Battelle/ORNL
incumbent patent path — uses hydrogen decrepitation and AC coil demag instead) and is not an HTS
device.

**3. Compact robotic disassembly cell for magnet-bearing devices.** Leveraging the founder's
precision-automation/machine-building background (built an automated winding machine), a
semi-automated robotic cell extracts intact NdFeB magnets from HDDs, EV drive motors, and
wind-turbine generators without full shredding, preserving magnets for direct reuse or high-purity
HPMS feed. Distinct from the EU's ADIR research demo (2015-2019), which never commercialized
[G07-06]. Explicitly avoids C40/RID-016 (disassembles motors/drives/HDDs for magnet recovery, never
battery packs for second-life grading) and stays outside G01 (no battery-manufacturing-line role).

**4. Retrofit power-electronics + inline sensing kit for eddy-current/electrostatic separators.**
Leveraging the founder's power-electronics background (separator drives, electrostatic HV supplies),
a retrofit variable-frequency rotor-drive plus inline conductivity/eddy-response sensing package
lifts recovery purity/throughput on the large installed base of SGM/Sesotec-class separators at
WEEE and black-mass pretreatment plants, sold as an upgrade kit rather than a full new separator.
Avoids competing on commodity mechanical hardware price; explicitly not a battery-pack product
(avoiding C40/RID-016) and not an induction-heating device (avoiding C16).

**5. Inline black-mass composition/purity QC sensor.** A non-optical (XRF/eddy-response fusion)
inline sensor for shredded black-mass powder streams verifies Li/Co/Ni content and aluminum
impurity in real time against China's tightened MIIT thresholds (Al <1.5%, electrode-powder
recovery >=98% [G07-09]) before hydrometallurgical feed, sold to any black-mass processor.
Explicitly stays outside G01 (post-scrap recycling-feedstock QC, not battery-manufacturing-line QC)
and outside C40/RID-016 (analyzes shredded powder chemistry only — no pack-level reuse/second-life
grading decision involved).
