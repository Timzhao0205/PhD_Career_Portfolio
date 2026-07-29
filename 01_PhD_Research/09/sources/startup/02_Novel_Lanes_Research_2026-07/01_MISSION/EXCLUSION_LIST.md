# EXCLUSION LIST — concepts already proposed (do NOT regenerate)

**Novelty test (binding):** a candidate is NOVEL only if it differs from every entry below in
buyer segment OR product category, AND is not a re-parameterized variant (same product, new
adjective). Borderline = variant = excluded, unless a written material-difference justification
is included in the candidate's Novelty declaration AND survives red-team verification.
Phase 0 must convert this list + parsed corpus IDs into `05_STATE/exclusion_ledger.json`;
Phase 7 audits every V-candidate against it.

## Round 1 (GEN3) — C01–C40 (final ranking in 00_PRIOR_CORPUS/GEN3/02_FULL_RANKING.md)
C01 MW SiC PEBB / marine-USV power bricks · C02 high-temp WBG packaging platform · C03 MW
marine/off-highway inverters · C04 MCS truck-charging modules · C05 DoD pulsed-power modules ·
C06 800 VDC protection (SSCB and protection-intelligence pivot) · C07 800 V busbar connectors ·
C08 GPU transient buffer / facility ride-through · C09 MV-to-800 VDC power blocks (SST) · C10
precision magnet & scientific power converters · C11 HTS quench protection / MPMU · C12 NI-HTS
coil winding & jointing cells · C13 HTS current leads & joints · C14 HTS cryostats & QC dewars ·
C15 compact HTS magnets / test & background magnets · C16 HTS induction heaters · C17 compact
SMES · C18 HTS MCZ retrofit magnets · C19 SSB isostatic-press cells · C20 formation systems for
new chemistries · C21 WBG wafer-level burn-in · C22 PD/insulation EOL rigs · C23 JEDEC WBG
characterization appliance · C24 HV probe cards · C25 D2W overlay inspection · C26
rad-characterized space WBG modules · C27 downhole/harsh 250–300 °C power platform · C28
COTS-plus rad-tolerant DC-DC · C29 smallsat PPU/PCDU · C30 fast+accurate current sensors · C31
triaxial OPM magnetometers · C32 Rydberg RF probes · C33 cryogenic coil QC instruments · C34
ultra-low-noise SMU · C35 particle-therapy RF cassettes · C36 GaN ablation OEM platform · C37
low-field MRI gradient amplifiers · C38 GFM PCS for compute microgrids · C39 electrolyzer power
modules · C40 second-life battery grading.

## Saturation rows (GEN3/70_SATURATION_CHECK)
N01 SiC SSCB for 800 VDC/MVDC · N02 SSPA klystron replacement · N03 gyrotron/ECRH HV power
systems · N04 subsea inductive power & docking · N05 solid-state RF/microwave process heat ·
N06 cryogenic power electronics · N07 AI-rack transient load-test rigs · N08 industrial pulsed
power / PEF · R1 humanoid/robot actuation drive electronics · R2 near-junction microfluidic
cooling.

## Gen-1 (june25_research.md) — RID top-25
002 supercap DC buffer · 003 SSCB+e-fuse · 008 blind-mate liquid+power connector · 024 GFM
protection relay · 001 800 VDC busway · 030 SiC STATCOM · 053 humanoid rotary actuator · 009
GPU-aware power-orchestration software · 004 MV SiC SST · 029 grid-edge PQ conditioner · 033
45 °C CDU · 034 microfluidic cold plate · 019 LDES GFM controls · 055 cobot SSM safety
controller · 056 PFL force-limiting joint + F/T sensor · 078 microneedle lactate sensor · 111
high-bandwidth piezo actuator · 016 second-life battery repurposing · 100 automated
optical-assembly cell · 102 fusion-magnet HTS components · 015 700 °C thermal-storage module ·
026 hybrid-plant controller · 020 battery thermal-runaway suppression · 040 datacenter
waste-heat recovery · 017 sodium-ion grid module. (Phase 0: parse the file for any RID beyond
the top 25 and add them.)

## Gen-2 (frontier_rank_red_team.md + china_feasibility_deep_dive.md) — CL clusters
CL-02 800 VDC DC-side protection · CL-03 AI-load power-smoothing & GFM buffer · CL-07
chip-package thermal boundary (near-junction fluidics) · CL-08 in-/on-package power delivery
(IVR) · CL-09 CPO optical assembly & test · CL-10 hybrid-bonding process control · CL-12
power-module & WBG packaging/manufacturing · CL-13 battery/solid-state manufacturing · CL-14
robot & surgical actuation · CL-15 force/tactile sensing · CL-18 HTS magnet protection,
charging & control · CL-19 HTS conductor supply chain & qualification · CL-25 energy-based
intervention engines (PFA/histotripsy/FUS) · CL-27 intervention robotics & steerable access ·
CL-29 bio-manufacturing & intervention-decision instruments. (Phase 0: parse both files plus
the five frontier worker files — every PWR-/SEM-/BIO-/IND-/EXT- candidate row and every
06_us_company_radar wedge — into the ledger.)

## Category bans (stronger than per-concept exclusion)
- **HTS / superconductivity anything** — the user allows exactly one HTS idea and the slot is
  held by the incumbent C12 cluster. Gate G6-HTS: any candidate whose core value depends on
  superconductors is ineligible regardless of novelty.
- **Transformer condition monitoring** (Magnefy wall) — absolute.
