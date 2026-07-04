# G01 — Battery & Storage Manufacturing Beyond the Cell

## Landscape
Scope starts after "the cell exists": grading, tab-to-busbar module welding, module-to-pack or
direct CTP/CTB integration, pack-level EOL test, and — for stationary storage — rack/cable
integration into 20-40ft ISO BESS containers with PCS/BMS/thermal/fire subsystems. China sets
the buyer scale: installed new-type storage was 73.76 GW at end-2024; NDRC/NEA's 2025-2027 plan
targets >180 GW by end-2027 (+100 GW, ~RMB250B direct investment) [G01-01][G01-02]. Buyers are
container integrators (CATL EnerOne, Sungrow, Envision, Tesla, Fluence, and a long tail of
second-tier Chinese assemblers) and, in the US, automakers/JVs (Panasonic, LG, Ford, Tesla) plus
a smaller, capital-constrained ESS-dedicated cohort — not the cell makers themselves.

## Pains & Buyers
Weld/interconnect quality is the recurring failure buyers pay to fix: even deep-learning inline
vision on a real production line hits only 97.9% accuracy, 1.1% miss-alarm, 11.5% false-alarm
(1,268-image dataset), because "material inhomogeneity, residual impurities, and parameter
fluctuations" defeat simple thresholds [G01-04]. Container integrators describe a cruder version:
workers reportedly "kick battery packs into containers by foot" for lack of standardized docking
[G01-09]. Three buyer types pay for fixes: Tier-1 pack integrators needing IATF-16949-class
traceability (weld serialization to VIN/tray, Cpk >=1.33-1.67, 92-96% full-body first-pass yield)
to keep OEM contracts [G01-15]; BESS integrators, where cells/modules are 40-48% of a
$180-295/kWh container and enclosure/BMS/PCS/thermal the rest, needing faster/safer
pack-to-container assembly to protect margin [G01-12]; and second-tier US lines — cancelled 12
GWh KORE Power and 34 GWh FREYR, delayed Kontrolmatik, bankrupt iM3NY — needing cheap retrofits,
not turnkey lines [G01-14].

## Incumbents & Gaps
Line integrators own the top of the stack. Wuxi Lead Intelligent (先导智能) claims #1
global/European lithium-equipment share, >80% line utilization, >65% labor-hour savings, 95%
yield on its PACK/CTP lines, selling to CATL, Tesla, VW, BMW, Stellantis [G01-10]. KUKA supplies
robot cells inside these lines — FAW-Volkswagen's Foshan plant runs ~100 KUKA robots across
welding/gluing/packaging for 300,000 packs/year [G01-08]. Laser vendors (IPG, Trumpf, Laserax)
sell weld heads and in-process monitoring — laser tab welds run ~50ms versus ~100ms ultrasonic,
halving connection count [G01-06]. All of this sells bundled inside multi-million-dollar turnkey
lines; nobody sells a small, bolt-on QC or handling instrument at module/pack/container level.
Cell-level EOL has drawn real but incomplete attention: a UK OPM-quantum-sensor consortium
claimed up to 30% production-cost savings, but its 2020-2023 pilot never reached gigafactory
deployment [G01-03]; Titan AES's ultrasound IonSight is the closest commercial product at
50,000+ cells/line/day, but that is cell-level, outside this lane. Even DOE-side, module
reliability testing (to 10 kW) is still a PNNL research service, not a product — public and
commercial infrastructure both under-invest below the cell level [G01-18].

## 2029 Inflections
Cell format is about to make module/pack welding both easier and higher-stakes. CATL (587Ah, 60
GWh at Jining by Dec-2025), EVE (628Ah), Sunwoda (684Ah), HiTHIUM (to 1,175Ah) are moving
containers from 280-314Ah to 500Ah+ formats specifically to cut "interconnects, weld points,
sensing channels and assembly steps" [G01-11] — fewer, fatter busbar joints, each carrying more
current and more consequence on failure. IEC 62619:2022 already mandates a pack-level
thermal-runaway-propagation test (single-cell trigger, laser ignition, zero propagation over 8h)
[G01-16]; by 2029 that qualification bar plus 500Ah+ joints are table stakes, not
differentiation. US demand is bifurcating toward storage: Panasonic's Kansas line hit 32 GWh
mass production (Jul-2025) while Ford repurposes its Kentucky EV-battery plant for LFP
data-center BESS by 2027, and Form Energy signed a 12 GWh AI-datacenter supply deal (Mar-2026)
[G01-17] — datacenter BESS demand is pulling US pack/container integration onshore faster than
cell capacity.

## China Notes
China defines both the buyer scale (73.76 GW installed, >180 GW by 2027, ~RMB250B capex)
[G01-01][G01-02] and the dominant equipment supplier (Wuxi Lead, plus Yinghe and others)
[G01-10] — a small US team competes there on retrofit/instrument products, not full lines.
Chinese integrators already voice the exact pain a retrofit product would fix: manual
container-loading versus AGV/robotic pitches targeting 3-minute cycles and ~1mm docking
precision [G01-09] — evidence buyers will pay for a faster, cheaper add-on even inside a
Chinese-equipment-dominated line.

## Opportunity Seeds

1. **Bolt-on weld-QC sensor head for existing welders.** Vision + eddy-current retrofit onto
tab/busbar laser welders in module/pack lines, priced as a sub-six-figure add-on rather than a
new line, targeting integrators stuck at today's ~88-98% miss/false-alarm inline rates [G01-04].
Avoids CL-13 (battery/solid-state manufacturing lines, incl. dry-electrode roll-to-roll and
sulfide-film casting) because it never touches a cell, electrode, or electrolyte process — only a
finished weld on an ordinary Li-ion line.

2. **Automated pack-to-container docking/torque-verification cell.** For BESS integration
yards, replacing the manual pack-loading reported at Chinese container lines [G01-09] with
~1mm-class robotic docking and a logged fastener-torque signature — new-pack, first-life
container assembly. Avoids C40/RID-016 (second-life battery grading/repurposing), which regrades
used/returned packs rather than assembling new ones into new containers.

3. **Non-destructive joint-integrity screening instrument.** A standalone bench or inline unit
for the new 500-1,175Ah busbar/cell interconnects, screening the fewer-but-higher-consequence
joints the 500Ah+ transition creates [G01-11]. Avoids C20 (formation systems for new chemistries)
because it never cycles or forms a cell electrochemically, is chemistry-agnostic, and
deliberately skips magnetic current-distribution imaging (PhD-lane) in favor of conventional
4-wire resistance and IR/eddy-current signatures.

4. **Portable field-commissioning test rig.** Certifies insulation resistance, interlock
function, and comms-bus integrity on site-assembled BESS containers pre-energization, for
delayed/cost-constrained US projects lacking in-house commissioning tooling [G01-14]. Avoids
RID-020 (battery thermal-runaway suppression) because it is a pass/fail diagnostic against an
IEC 62619-style checklist [G01-16], with no suppression, venting, or fire-fighting hardware of
its own.

5. **Weld-serialization/traceability retrofit node.** A small data-capture hardware unit plus
software linking every weld's parameters to a tray/container serial number, for legacy or
smaller module/pack lines needing IATF-16949-class traceability (Cpk >=1.33, VIN-linked
serialization) [G01-15] to win OEM or utility contracts without a full line rebuild. Avoids C19
(solid-state-battery isostatic-press cells) because it is a data/software layer bolted onto an
ordinary Li-ion weld station, with zero cleanroom or isostatic-press capex.
