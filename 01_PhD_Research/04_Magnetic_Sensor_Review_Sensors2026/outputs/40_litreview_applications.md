# Stage 40 — Literature-review brief: current applications across four domains

**Status:** citation-carrying research brief, not final prose. The author writes the applications tail of Section 2 from this.
**Citation convention:** `[key]` refers to an entry in `refs_raw/40.jsonl` (new this stage), `refs_raw/30.jsonl` (sensor-family anchors, reused keys), or `refs_raw/00_seed.jsonl` (seed). Stage 70/80 converts keys to numbered MDPI citations.
**Integrity notes:**
- Every quantitative claim traces to a source retrieved this run or in the seed/stage-30 logs. Numbers taken from a vendor page carry `[VENDOR]` and must never be presented as peer-reviewed evidence. Numbers from market-research firms carry `[MARKET]` and are framing, not measured facts — treat the spread across firms as the honest uncertainty.
- "Widely deployed" vs "demonstrated in research" is called out per deployment; do not upgrade a research demo to a product in drafting.
- Sensor-family device facts (noise floors, MR ratios, maturity) are NOT re-derived here — see stage 30. This brief maps families → uses and gives the *application-side* requirement each must meet.

Framing anchor for the section lead-in: magnetic sensors reach an application when a **field-range / resolution / bandwidth** requirement meets a hard **cost, isolation, size, or temperature** constraint that a competing (shunt, optical, mechanical) transducer cannot satisfy simultaneously. Each domain below is organized around that collision.

---

## A. Energy

**Framing.** The dominant energy use is *current sensing by proxy*: measure the magnetic field a conductor produces rather than break the circuit with a shunt. This buys galvanic isolation "for free," which is the decisive advantage at battery-pack, inverter-DC-link, and grid voltages. Requirements are set by the power-electronics switching edge (bandwidth), by billing/SoC accuracy (offset & drift), and by the environment (temperature, isolation voltage).

### A.1 Power-electronics & traction-inverter current sensing
- **Incumbent:** open-/closed-loop **Hall** current sensors (cored and coreless), the volume default for isolated DC/AC current in drives and inverters; principles and integrated-Hall architectures reviewed in [Crescentini2022hallcurrent]. Fluxgate-based closed-loop transducers occupy the high-accuracy tier of the same market (excellent linearity, wide bandwidth) — noted in the EV-current-sensor engineering literature `[VENDOR-adjacent]` [LEMbatterycurrentVendor].
- **Disruptive challenger:** **TMR** coreless current sensors. Vendor devices claim ~10× faster response and ~4× lower noise than comparable Hall parts; the Allegro XtremeSense TMR family (e.g., ACS37xxx) advertises a 10 MHz bandwidth, ~50 ns response, and −40…150 °C operation, targeted explicitly at fast-switching **SiC/GaN** inverters where the Hall bandwidth is marginal `[VENDOR]` [AllegroTMRcurrentVendor; InfineonCurrentSensorVendor]. This is a genuine socket-by-socket displacement, not just research: Infineon and Allegro ship both Hall and TMR current-sensor lines for automotive traction inverters and onboard chargers `[VENDOR]`.
- **Quantitative requirement:** bandwidth ≳ (5–10)× the PWM/switching fundamental (hundreds of kHz–MHz for wide-bandgap), isolation to the DC-link potential (hundreds of V to >1 kV), and TC-compensated sensitivity across −40…150 °C automotive-grade range [Crescentini2022hallcurrent; AllegroTMRcurrentVendor].
- **Maturity:** widely deployed (Hall, mass-market; TMR, rapidly scaling into new designs). A traction-inverter current-sensor market note puts Hall at ~48.5 % share in 2025 with TMR the fastest-growing challenger `[MARKET]` — treat the exact share as indicative only.

### A.2 EV battery management (pack current, SoC/SoH)
- **Incumbent:** **Hall** and **fluxgate** open-loop/closed-loop current sensors on the pack bus bar; the BMS integrates current over time (coulomb counting) so **offset and gain drift dominate the SoC error budget**, which is why fluxgate (superior linearity/offset) is chosen where range estimation accuracy is paramount `[VENDOR]` [LEMbatterycurrentVendor].
- **Requirement:** wide dynamic range (idle-µA to hundreds-of-A charge/discharge), low temperature drift over pack thermal range, and isolation at pack voltage; ppm-class stability is the aspiration for reliable range readout [LEMbatterycurrentVendor].
- **Maturity:** widely deployed (Hall/fluxgate). NV-diamond current sensing (galvanically isolated, 0–1000 A, ~46 ppm) is a research-stage challenger for high-accuracy battery/pack current — `[PREPRINT — not peer-reviewed]` [NVcurrentPPM2023]; do not present as productized.

### A.3 Smart-grid, substation & transmission-line monitoring
- **Contactless overhead-line monitoring:** ground- or tower-level **magnetoresistive (AMR/GMR/TMR) sensor arrays** measure the field emanating from conductors and *reconstruct* phase current, conductor sag/clearance, and wind-induced motion — no line contact, no outage for install [Khawaja2017overheadlines; Chen2024contactlessOHL]. Chosen for cost, non-intrusive install, and sensitivity [Chen2024contactlessOHL].
- **Weak-current metrology:** high-precision **TMR** current sensors are being pushed for accurate weak-current measurement in grid applications [Xu2025TMRsmartgrid].
- **Digital substations / HV metering:** **fiber-optic Faraday-effect optical current sensors (OCS/OCT)** own the highest-voltage tier — dielectric sensing head, EMI immunity, no saturation/ferroresonance, DC-to-transient capability; deployed by ABB and integrated to IEC 61850-9-2 digital substations, with fiber OCS demonstrated to ~600 kA DC [Silva2012opticalcurrent; Rostami2023fbgreview]. Rogowski coils (air-cored search coils) serve the AC side for metering/protection where saturation-free wide-range AC is needed (see stage 30, search-coil family).
- **Requirement:** for contactless MR arrays, resolve conductor field (µT-scale at standoff) against Earth's field and cross-talk from adjacent phases; for OCS, HV isolation (tens–hundreds of kV) and metering-class accuracy (0.2 %/0.2S class) [Silva2012opticalcurrent; Khawaja2017overheadlines].
- **Maturity:** OCS/OCT — deployed niche (HV substations); MR contactless line monitoring — mostly demonstrated/pilot, growing.

### A.4 Renewables condition monitoring
- Magnetic sensing enters wind/generator health mainly via **stray-flux and current-signature** analysis of the generator (see A.5/Industrial B.2), and via **oil-debris/magnetic-particle** detection of gearbox wear; note honestly that vibration, acoustic-emission, and oil analysis remain the primary CM modalities, with magnetic-field methods complementary rather than dominant [Mazaheri2022strayflux].

### A.5 Contactless DC metering
- Coreless **Hall/TMR** field-to-current sensors provide contactless DC measurement where a shunt's insertion loss/isolation is unacceptable; same device basis as A.1 [Crescentini2022hallcurrent; AllegroTMRcurrentVendor].

**Energy — incumbent vs challenger:** incumbent = Hall (+ fluxgate for accuracy, optical for HV); challenger = TMR (coreless, wide-bandgap-ready) and, at research stage, NV-diamond for isolated high-accuracy current.

---

## B. Transportation (automotive-dominant)

**Framing.** The highest-volume magnetic-sensor domain. Almost every use is **position, angle, or speed** read magnetically because a magnetic interface is contactless, dust/oil/water-immune, and cheap — plus **isolated current sensing** for the traction inverter (shared with Energy A.1). Functional-safety (ASIL) drives redundancy and diagnostics (standards → stage 60).

### B.1 Position / angle / speed
- **Angle & rotary position** (steering, throttle/pedal, motor commutation, rotor position): migrating **Hall → AMR/GMR → TMR**. TMR angle sensors are the current high-accuracy choice — e.g. MDT TMR308x: dual-bridge, ±0.6° over 360°, −40…150 °C, AEC-Q100, ~600 mV/V output (no external amplification) `[VENDOR]` [MDTangleVendor]. Application envelope and the Hall/AMR/GMR/TMR trade for automotive angle sensing framed in the classic survey [Treutler2001automotive] and the MR roadmap [Zheng2019mrroadmap].
- **Wheel-speed / ABS & transmission speed:** **back-biased Hall** (and GMR) gear-tooth / ring-magnet sensors producing clean digital pulses; chosen for true-zero-speed capability and robustness to contamination; e.g. Allegro A1688-class ABS ICs `[VENDOR]` [AllegroABSVendor]. Widely deployed, safety-critical.
- **Requirement:** angular accuracy <1° over −40…150 °C and life; air-gap tolerance (mm-scale) at the target field; EMC and stray-field immunity (ISO 11452 / functional-safety, → stage 60) [MDTangleVendor; Treutler2001automotive].
- **Maturity:** mass-market, mature (Hall/AMR/GMR), with TMR ascendant in new high-accuracy designs.

### B.2 Traction-inverter current sensing
- Shared with A.1: Hall incumbent, TMR challenger for SiC/GaN drives [Crescentini2022hallcurrent; AllegroTMRcurrentVendor].

### B.3 E-compass / navigation
- Three-axis **AMR / Hall / TMR / GMI** magnetometers for tilt-compensated heading in phones and vehicles; GMI (amorphous-wire) modules serve the consumer e-compass niche (see stage 30 GMI family) [Phan2008gmiprogress; Uchiyama2020picoteslaMI]. Requirement: resolve Earth-field heading (~25–65 µT) after hard/soft-iron calibration; main failure mode is local magnetic interference `[VENDOR]` [STeCompassVendor].
- **Maturity:** mass-market, mature.

### B.4 Aerospace / space magnetometry
- **Fluxgate** is the vector workhorse for spacecraft/CubeSat field measurement — decades of heritage, radiation tolerance, absolute stability. Miniaturized science-grade digital fluxgates now fly on CubeSats: 150–200 pT/√Hz at 1 Hz, ~400 mW, 121 g on a 60 cm deployable boom (Ex-Alta-1 / constellation-class instruments) [Miles2016fluxgateCubeSat; Fluxgate2021Sensors]. **Search-coil** magnetometers cover AC/plasma-wave fields (THEMIS-class, ~fT/√Hz at kHz) [Roux2008themisSCM; Coillot2010dualband].
- **Maturity:** mature niche (space-qualified fluxgate/search-coil).

**Transportation — incumbent vs challenger:** incumbent = Hall + AMR/GMR (position/speed), Hall (current); challenger = TMR (angle accuracy, coreless current); fluxgate/search-coil remain the space standard.

---

## C. Industrial & manufacturing

**Framing.** Two big buckets: **NDT/inspection** (find a defect via its leakage or eddy-current field) and **condition monitoring / motion** (encoders, and machine-health via stray flux). MR-sensor arrays win where spatial resolution + low-field sensitivity + array integration beat a single coil.

### C.1 Non-destructive testing — MFL & eddy current
- **Magnetic Flux Leakage (MFL):** the oldest, most-used in-line-inspection (ILI) method for ferromagnetic pipelines; magnetize wall to near-saturation, scan leakage with **Hall / GMR / TMR** sensor arrays to size corrosion/metal-loss. High-resolution GMR/TMR arrays add spatial resolution and lift-off tolerance vs coils [Rifai2016GMReddyreview] (family survey) and MFL practice (widely deployed, mature).
- **Eddy-current testing (ECT):** **GMR** array probes exploit very low 1/f noise → low excitation frequency → deeper penetration; used for cracks in aircraft structure, rebar, PCBs, bridges, and corrosion-under-insulation (e.g., 300 A pipe-encircling excitation, 5–200 Hz, imaging wall loss without removing insulation) [Rifai2016GMReddyreview; Bailey2017eddyCUI].
- **Requirement:** sub-mm defect localization, lift-off tolerance, and array pitch fine enough to resolve pitting; sensitivity at low field to allow low-frequency (deep) inspection [Bailey2017eddyCUI; Rifai2016GMReddyreview].
- **Maturity:** MFL — mass-deployed (pipeline ILI); GMR/TMR-array ECT — deployed→growing in aerospace/CUI niches.

### C.2 Motor & bearing condition monitoring / predictive maintenance
- **Stray-flux (external leakage field)** monitoring of electrical machines detects bearing, rotor-bar, eccentricity, and winding faults, complementing motor-current-signature analysis; bearing faults are ~40 % of machine failures, so this is a high-value target [Mazaheri2022strayflux]. Search-coils and Hall/MR sensors pick up the external flux; note that Hall sensitivity can be marginal for the low-amplitude stray-flux signature, favoring coils/MR.
- **Maturity:** demonstrated→early-deployed; predictive-maintenance analytics (→ stage 50) are the growth lever.

### C.3 Encoders, robotics, proximity/position
- **Magnetic rotary/linear encoders** (Hall/AMR/GMR/**TMR**) for servo drives, robot joints, and motion control; TMR encoder ICs claim 23-bit absolute output, up to 4096 PPR, 40 000 rpm, and <0.05° temperature drift, with on-/off-axis flexibility for humanoid/collaborative-robot joints `[VENDOR]` [MDTencoderVendor]. Requirement: absolute angular resolution + high-speed update + robustness vs optical encoders in dirty environments.
- **Maturity:** mass-market (magnetic encoders), with TMR pushing precision/robotics sockets.

**Industrial — incumbent vs challenger:** incumbent = Hall + search-coil (NDT, CM) and Hall/AMR/GMR (encoders); challenger = GMR/TMR arrays (higher-resolution NDT, precision encoders).

---

## D. Biomedical

**Framing.** Split by signal amplitude. **Biomagnetism** (MEG ~fT, MCG ~pT) needs the most sensitive families and fights ambient noise; **biosensing / tracking / imaging** trade absolute sensitivity for room-temperature, low-cost, array-friendly operation. Ultrasensitive-family vs biomagnetic-signal amplitudes are tabulated in [Murzin2020biomedsensors].

### D.1 MEG (magnetoencephalography)
- **Incumbent:** cryogenic **SQUID** helmet arrays — few fT/√Hz, the clinical standard for decades [Fagaly2006squidRSI; Clarke2018squidfocus].
- **Disruptive challenger:** wearable **OPM (SERF)** on-scalp MEG — no cryogenics, sensors sit on the scalp (3–5× closer → higher signal), motion-tolerant. A 50-channel OPM system has matched/surpassed a 275-channel cryogenic MEG in reported studies; OPM-MEG detects a majority of deep (mesiotemporal) epileptic discharges and enables naturalistic/ambulatory recording [Boto2018wearableMEG; Tierney2019OPM; Brickwedde2024OPMMEG; Pedersen2022OPMepilepsy].
- **Requirement:** sub-10 fT/√Hz per channel, operation in µT-nulled shielded/active-compensated environment (SERF needs near-zero field), whole-head channel count [Tierney2019OPM; Kominis2003subfemtotesla].
- **Maturity:** SQUID — mature clinical; OPM-MEG — commercial-niche, scaling fast (epilepsy, translational neuroscience).

### D.2 MCG (magnetocardiography)
- **Incumbent:** SQUID (shielded). **Challengers:** room-temperature **TMR** arrays and **OPM** for *unshielded* MCG — the clinical prize is a compact, shielding-free cardiac magnetometer. Microfabricated TMR arrays report ~14.1 pT_rms over 0.2–100 Hz and have yielded diagnostically useful ventricular de/repolarization signals in an unshielded office (atrial fields still challenging) [Brisinda2023clinicalMCG]. Scalar OPM sensor arrays demonstrate bedside/unshielded MCG [Iwata2024bedsideMCG]. Sub-pT TMR for biomagnetics is the active device frontier [TMRsubpT2025APL].
- **Requirement:** ~pT resolution across ~0.1–100 Hz with ambient-noise rejection (gradiometry/adaptive cancellation) without a shielded room [Brisinda2023clinicalMCG; Iwata2024bedsideMCG].
- **Maturity:** research→early-clinical (unshielded MCG); SQUID-MCG mature but installation-limited.

### D.3 GMR/TMR biosensors & lab-on-chip
- **GMR/TMR** magnetoresistive biosensors detect magnetic-nanoparticle labels bound to target biomarkers (sandwich immunoassay) → resistance change; integrated with microfluidics and CMOS front-ends for point-of-care. Concrete demos: portable GMR platforms with smartphone readout; GMR microfluidic immunoassay (e.g., cardiac myoglobin); TMR magnetic-immunoassay bacterial detection to ~100 CFU/mL *E. coli* in ~5 h [Wang2024magbiosensorPOCT]. TMR offers higher sensitivity than GMR for this transduction [Wang2024magbiosensorPOCT; Zhou2022TMRchapter].
- **Requirement:** resolve single-particle / low-copy label fields at room temperature, multiplexed array, low-cost disposable cartridge [Wang2024magbiosensorPOCT].
- **Maturity:** research→pilot POC; not yet mass-clinical.

### D.4 Magnetic particle imaging (MPI)
- Tomographic imaging of injected superparamagnetic-iron-oxide tracer via its nonlinear magnetization; radiation-free, zero tissue attenuation, quantitative. Preclinical scanners are commercial (rat-scale); spatial resolution ~1 mm with 6.3–7 T/m selection fields; human brain systems in development [Wu2019MPIneuro].
- **Maturity:** preclinical-commercial; clinical translation ongoing.

### D.5 Catheter / instrument tracking & wearables
- **Electromagnetic tracking systems (EMTS):** a field generator plus small **magnetic sensors** in the instrument give real-time 5–6-DoF pose without line-of-sight — used for catheters, endoscopes, capsule robots, and surgical navigation; enables non-ionizing endovascular guidance [He2025EMtracking]. Requirement: mm-scale position accuracy in the working volume, tolerance to metal distortion.
- **Maturity:** deployed (commercial surgical-navigation systems); micro-scale robotic-catheter tracking is research→early.

**Biomedical — incumbent vs challenger:** incumbent = SQUID (MEG/MCG), EM-tracking coils (navigation); challenger = OPM & TMR arrays (cryogen-free, unshielded biomagnetism), GMR/TMR biosensors (POC diagnostics).

---

## E. Domain × sensor-family fit matrix

Legend: ● primary/dominant · ◐ used/secondary or emerging · ○ niche/research-only · (blank) not a fit. "Why" = the deciding property.

| Family | Energy | Transportation | Industrial | Biomedical | Deciding property (why it wins where it does) |
|---|:--:|:--:|:--:|:--:|---|
| Hall (Si CMOS) | ● | ● | ◐ | ○ | Lowest cost, isolated DC current, position/speed; bandwidth caps it for wide-bandgap [Crescentini2022hallcurrent] |
| Hall (GaN 2DEG) | ◐ | ○ | ○ | — | Only Hall for >300 °C / harsh env. (well-logging, machine rotors) [Alpert2020gan2deg] |
| AMR | ◐ | ● | ◐ | — | Cheap low-field position/compass; set/reset needed [Zheng2019mrroadmap] |
| GMR | ◐ | ● | ● | ◐ | Big signal + array integration → NDT arrays, speed/angle, biosensors [Rifai2016GMReddyreview; Wang2024magbiosensorPOCT] |
| TMR | ● | ● | ● | ◐ | Highest sensitivity-per-watt → coreless current, angle accuracy, encoders, pT biomag [AllegroTMRcurrentVendor; MDTangleVendor; TMRsubpT2025APL] |
| Fluxgate | ◐ | ◐ | ◐ | — | Best pT-nT DC accuracy w/o cryo → precise pack/inverter current, space, CM [Fluxgate2021Sensors; Miles2016fluxgateCubeSat] |
| Search-coil | ◐ | ◐ | ● | — | Passive AC field → Rogowski metering, stray-flux CM, space waves [Roux2008themisSCM; Mazaheri2022strayflux] |
| GMI | ○ | ◐ | ○ | ○ | High sensitivity/size ratio → consumer e-compass; bio emerging [Phan2008gmiprogress] |
| SQUID | — | — | ◐ | ● | Ultimate sensitivity → MEG/MCG, magnetic microscopy/NDE (cryo cost) [Clarke2018squidfocus] |
| OPM / SERF | — | ○ | — | ● | fT w/o cryo, wearable → on-scalp MEG, unshielded MCG [Boto2018wearableMEG; Iwata2024bedsideMCG] |
| NV-diamond | ○ | ○ | ○ | ○ | Room-T vector/absolute, huge dynamic range → isolated current (research), microscopy [NVcurrentPPM2023 PREPRINT] |
| Magnetoelectric | ○ | — | ○ | ○ | Passive pT-at-resonance → biomag/ME-antenna candidates (lab) [Bichurin2021MEreview] |
| Fiber-optic / magneto-optic | ● | ○ | ◐ | — | Dielectric, EMI-immune, HV-safe → optical current transformers in HV substations [Silva2012opticalcurrent] |

(Fusion-plasma / harsh-environment field measurement is the GaN-Hall pioneering frontier from stage 30; it sits outside the four survey domains and is mentioned there, not scored here.)

---

## F. Cross-cutting observations for drafting

1. **TMR is the common challenger across all four domains** — coreless current (energy/transport), precision angle/encoders (transport/industrial), and pT biomagnetics (biomedical). This is the single strongest "where the field is heading" thread linking Section 2 to Section 3.
2. **Isolation is the recurring "why."** Field-proxy current sensing wins in energy/transport specifically because it is galvanically isolated; optical (Faraday) sensing extends the same logic to HV where even a semiconductor's isolation fails.
3. **Cryogen-free is the biomedical inflection** — OPM and TMR arrays are dismantling the SQUID's shielded-room/cryostat moat for MEG/MCG.
4. **"Deployed" vs "demonstrated" honesty:** mass-deployed = Hall/AMR/GMR position-speed-current, MFL ILI, magnetic encoders, EM surgical navigation, SQUID-MEG. Research/pilot = unshielded MCG, GMR/TMR POC biosensors, NV current sensing, contactless OHL current arrays. Keep this line sharp in prose.

## G. Market framing (label as estimate, not measurement)
- Magnetic-sensor market sized at roughly **USD 3–5.5 billion in 2024** depending on firm/scope, growing at ~**6–8 % CAGR**; **automotive is the largest segment**, driven by ADAS + EV position/current/speed sensing `[MARKET]` [GVRmagsensormarket; MRFRautomotivemarket]. The wide inter-firm spread is itself the honest takeaway — cite as orientation, and separate clearly from sourced device facts. Deeper TRL/standards/market treatment → stage 60.

## H. Gaps to close before/while drafting
1. Replace the traction-inverter "48.5 % Hall share" `[MARKET]` figure with a peer-reviewed or primary-industry source if one exists by drafting; otherwise keep the qualitative "Hall dominant, TMR fastest-growing."
2. NV current sensing rests on a **preprint** [NVcurrentPPM2023] — locate the version of record before asserting the 46 ppm / 0–1000 A number in final prose.
3. Vendor performance numbers (TMR current-sensor 10 MHz/50 ns; angle ±0.6°; encoder 23-bit) are `[VENDOR]` — keep tagged; do not present as independent measurement.
4. Renewables/wind CM: magnetic-field methods are complementary to vibration/oil analysis — resist overstating; the stray-flux review [Mazaheri2022strayflux] is the defensible anchor.
5. GMR-biosensor concrete detection-limit examples (E. coli 100 CFU/mL; myoglobin platform) are carried through the review [Wang2024magbiosensorPOCT]; pull the primary papers if a specific LOD is quoted in final text.
