# Stage 30 — Literature-review brief: magnetic-sensor families (commercial + pioneering)

**Status:** citation-carrying research brief, not final prose. The author writes Section 2 from this.
**Citation convention:** `[key]` refers to an entry in `refs_raw/30.jsonl` (this run) or `refs_raw/00_seed.jsonl` (seed anchors, reused keys). Stage 70/80 converts keys to numbered MDPI citations.
**Integrity notes:**
- Every number below traces to a source retrieved this run or in the seed. Where a canonical figure could not be pinned to a retrieved source, the cell/claim says **n/r** (not reported this run) — do not fill from memory at drafting time; re-verify instead.
- Vendor-sourced device facts are tagged `[VENDOR]` and must not be presented as peer-reviewed evidence.
- Claims flagged `(confidence: med)` had their number retrieved from a search-result abstract/snippet rather than the full text; spot-check during drafting.
- The author's own 2023 *IEEE Sensors Letters* AlGaN/GaN Hall paper could **not be located via Crossref/web this run** — [UNVERIFIED]. The author holds the full citation; insert it manually as the fusion-diagnostics example in §1.2 if desired. Do not let anyone else "reconstruct" it.

Cross-family framing anchors for the section lead-in: the classic technology-vs-field-range maps [Lenz1990review; Lenz2006magsensors], updated cross-family surveys [Ripka2010advancesIEEE; MagSensorsReview2021ERX; Tumanski2013modern], and the biomedical-sensitivity comparison [Murzin2020biomedsensors]. Useful organizing axis: detection limit vs bandwidth vs operating conditions (cryogenics, zero-field, vacuum) — every family below is a different corner of that trade space.

---

## 1. Hall effect (Si CMOS; wide-bandgap GaN/2DEG; spinning-current)

### 1.1 Silicon / integrated CMOS Hall
**Principle.** Carriers drifting in a biased semiconductor plate experience the Lorentz force; the resulting transverse charge accumulation produces a Hall voltage V_H ∝ I·B/(n·q·t), linear in the out-of-plane field. Low carrier density (semiconductors, 2DEGs) maximizes sensitivity; the physics, device geometries, and offset mechanisms are treated in the standard monograph [Popovic2004hallbook].

**Performance envelope.**
- Field range: from the ~100 µT class up to multi-tesla fields; Hall is the default above the mT range where xMR saturates [Lenz2006magsensors; Popovic2004hallbook]. Exact usable floor depends on offset handling (below).
- Offset/1/f noise are the limiting non-idealities, not thermal noise. Raw plate offsets correspond to mT-class equivalent fields; spinning-current (connection-commutation) readout separates the Hall signal from offset and 1/f noise in frequency and is the enabling technique for precision Hall ICs [Munter1990spinning; Popovic2004hallbook].
- A 180 nm CMOS implementation with 2 MHz spinning reports 45 µT residual offset, 600 kHz bandwidth, and 32 ppm/°C sensitivity drift (confidence: med — from abstract) [JEET2019lownoisehall].
- A 2025 monolithic 3-axis Si Hall device (inverted-pyramid geometry) applies offset cancellation to all three axes on one die [SiHall3axis2025msn].
- Bandwidth: integrated Hall current sensors reach the hundreds-of-kHz class; architectures and speed/resolution trades reviewed in [Crescentini2022hallcurrent].
- Resolution: nT-class is not native Hall territory; practical integrated devices sit in the µT–sub-µT regime after spinning [JEET2019lownoisehall; SiHall3axis2025msn]. Noise-floor spectral densities in standard units: n/r this run — pull from [Crescentini2022hallcurrent] full text at drafting.

**Strengths.** True dc response; linear over enormous dynamic range; no ferromagnetic material (no hysteresis, no perming); trivially co-integrated with CMOS signal conditioning; lowest unit cost of any family; intrinsically radiation- and temperature-tolerant device physics in wide-bandgap variants [Popovic2004hallbook; Crescentini2022hallcurrent].

**Weaknesses / failure modes.** Low raw sensitivity vs xMR (a GMR bridge yields >50× the signal of a Hall element — vendor claim [VENDOR, Allegro, retrieved via search]); offset and 1/f noise require spinning/chopping, which injects switching ripple and caps bandwidth; piezo-Hall effect — package/die stress shifts sensitivity and offset over life (shear-stress drift of the sensitive axis documented for (100)-Si devices; arXiv record retrieved, version of record n/r — treat as discovery only); temperature coefficient of sensitivity must be actively compensated.

**Commercial maturity.** Mass-market, the volume leader: switches, position/speed, compass, isolated current sensing (Allegro, Infineon, TI, Melexis, ams-Osram among vendors — device families are common knowledge; specific specs, if quoted later, must carry `[VENDOR]` datasheet cites).

### 1.2 GaN / 2DEG Hall (wide-bandgap, harsh-environment)
**Principle.** Same Hall physics, but the conductive layer is the two-dimensional electron gas at an (Al,In)GaN/GaN heterojunction: high mobility, low sheet density, and a 3.4 eV bandgap that suppresses thermal carrier generation at temperatures where Si fails.

**Performance envelope (all from [Alpert2020gan2deg] unless noted).**
- Operation demonstrated room temperature → 576 °C. Voltage-scaled sensitivity falls with temperature (89 → 8.5 mV/V/T for AlGaN/GaN; 53 → 8.3 mV/V/T for InAlN/GaN) tracking mobility, but **current-scaled sensitivity is nearly temperature-flat**: 60.2 V/A/T ± 10.5% (AlGaN/GaN) and 26.3 V/A/T ± 13.1% (InAlN/GaN) across the full range; 12 h soak at 576 °C with near-full recovery.
- Earlier AlGaN/GaN HEMT-structure Hall work: +0.05%/°C Hall-voltage TC near room temperature; 67 V/A/T current-scaled response at 400 °C [GaNHEMThall2012jpcs].

**Strengths.** Only Hall variant qualified by physics for >300 °C ambients; current-bias operation gives a naturally drift-flat transfer; same no-hysteresis/dc advantages as Si Hall.

**Weaknesses.** No monolithic CMOS integration (external readout); offset comparable to Si plates and still needs spinning-current treatment; small supplier base — effectively lab-to-niche, not catalog product.

**Pioneering directions.** Harsh-environment deployment is the active frontier: high-temperature well logging, electric-machine rotors, aerospace, and fusion-plasma diagnostics (in-vessel field measurement) — the author's first-hand area; peer-reviewed in-vessel demonstration exists ([UNVERIFIED] this run — author's own 2023 IEEE Sensors Letters paper, insert manually). Spinning-current offset cancellation applied to AlGaN/GaN plates appears in the preprint literature (arXiv 1812.00363 — discovery only; locate version of record before citing).

**Key refs (family 1):** [Popovic2004hallbook] [Munter1990spinning] [Crescentini2022hallcurrent] [JEET2019lownoisehall] [SiHall3axis2025msn] [Alpert2020gan2deg] [GaNHEMThall2012jpcs] [Lenz2006magsensors]

---

## 2. AMR (anisotropic magnetoresistance)

**Principle.** In a ferromagnetic film (typically permalloy), resistivity depends on the angle between magnetization and current (spin-orbit scattering). "Barber-pole" conductor stripes at 45° linearize the response around zero field; a set/reset field pulse periodically re-magnetizes the easy axis, cancelling offset drift and recovering from magnetic upset [Jogschies2015mrindustrial; Zheng2019mrroadmap].

**Performance envelope.**
- MR ratio: low single-digit percent — the smallest signal of the xMR family [Jogschies2015mrindustrial; Freitas2016spintronic].
- Resolution: nT-class in commercial bridge parts; detailed detectivity spectra per technology are tabulated in the MR roadmap [Zheng2019mrroadmap] — pull exact pT–nT/√Hz values from its tables at drafting time (n/r from this run's snippets).
- Field range: earth-field scale (compassing) up to ~mT full-scale linear parts; saturates and needs reset after overfield exposure [Jogschies2015mrindustrial].
- Bandwidth: dc to ~MHz-class in principle (thin-film resistor); practical parts limited by set/reset cadence — n/r.

**Strengths.** Mature, cheap, radiation-hard thin-film process; excellent linearity after barber-pole biasing; better low-field resolution than Hall without exotic materials; low power; strong track record in compassing and position sensing [Jogschies2015mrindustrial; Treutler2001automotive].

**Weaknesses / failure modes.** Small signal (needs bridge + amplification); flipping/upset when exposed to fields beyond the easy-axis stability margin (hence set/reset circuitry); Barkhausen noise from domain activity in biased designs (retrieved via patent/paper snippets this run); cross-axis sensitivity; limited maximum field before saturation.

**Commercial maturity.** Mass-market: e-compasses, wheel-speed, current sensing (Honeywell HMC-class parts, Sensitec, iSentek — named as common knowledge; cite `[VENDOR]` datasheets only if specs are quoted).

**Pioneering directions.** Barber-pole-free linear AMR via antiferromagnet-stabilized magnetization (IEEE EDL-class work retrieved as a search hit; version-of-record details n/r — verify before citing); AMR in flexible/implantable form factors (La₀.₆₇Sr₀.₃₃MnO₃ implantable AMR, ACS Biomater. Sci. Eng., retrieved as search hit — verify at drafting).

**Key refs:** [Jogschies2015mrindustrial] [Zheng2019mrroadmap] [Treutler2001automotive] [Freitas2016spintronic] [Tumanski2013modern]

---

## 3. GMR (giant magnetoresistance, spin-valve)

**Principle.** Spin-dependent scattering in ferromagnet/non-magnet multilayers: parallel vs antiparallel alignment of a pinned reference layer and a free layer changes resistance by ~5–20% (spin-valve architecture: pinned layer + free layer, linearized by crossed anisotropies) [Freitas2016spintronic; Jogschies2015mrindustrial].

**Performance envelope.**
- MR ratio: an order of magnitude above AMR [Freitas2016spintronic].
- Signal: >50× a Hall element's output for the same field (vendor claim, `[VENDOR]` Allegro application literature — use only as industry color, not as evidence).
- Detectivity: nT-class typical for commercial bridges; optimized lab devices better — exact spectra tabulated in [Zheng2019mrroadmap] (n/r this run).
- Field range/bandwidth: designed-in via free-layer stiffness; automotive speed/angle parts operate at air-gap fields of mT class with dc–100+ kHz response — n/r for exact numbers; [Treutler2001automotive] frames the application envelope.

**Strengths.** Large signal at low cost; wafer-scale back-end integration on CMOS; differential bridge configurations reject common-mode fields and temperature; proven automotive qualification (ABS wheel speed, angle) [Treutler2001automotive; Zheng2019mrroadmap; Freitas2016spintronic].

**Weaknesses / failure modes.** Hysteresis and magnetic noise from the free layer (domain/Barkhausen activity); pinned-layer loss above the antiferromagnet blocking temperature (irreversible if overheated); saturation at modest fields; 1/f noise dominates at low frequency [Freitas2016spintronic; Zheng2019mrroadmap].

**Commercial maturity.** Mass-market: the workhorse of automotive speed/direction sensing and read heads historically; vendors include Allegro, Infineon, Sensitec, MultiDimension [VENDOR-class facts].

**Pioneering directions.** Enhanced-functionality spintronic sensors (multi-axis, wider dynamic range, on-chip diagnostics) surveyed in the 2024 npj Spintronics perspective [Spintronic2024npj]; GMR biosensing arrays (magnetic-bead immunoassay) — covered in stage 40.

**Key refs:** [Freitas2016spintronic] [Zheng2019mrroadmap] [Jogschies2015mrindustrial] [Treutler2001automotive] [Spintronic2024npj]

---

## 4. TMR / MTJ (tunneling magnetoresistance)

**Principle.** Spin-dependent tunneling across a crystalline MgO barrier between ferromagnetic electrodes; coherent Δ1-channel filtering yields TMR ratios of hundreds of percent at room temperature — the largest transfer signal of any magnetoresistive device. Stack engineering, linearization, and fabrication are reviewed in [Zhou2022TMRchapter; Freitas2016spintronic].

**Performance envelope.**
- Detectivity: hybrid MgO-based tunnel sensors reported 97 pT/√Hz at 10 Hz and 2 pT/√Hz at 500 kHz (confidence: med — abstract-level retrieval, primary is a ResearchGate-indexed paper; re-verify or lean on the next two anchors); calculated noise-equivalent fields of 10⁻¹¹–10⁻¹² T/√Hz for optimized junctions and the 1/f-noise obstacle course to get there are laid out in [Egelhoff2009picoteslaMTJ].
- State of the art: sub-pT detectivity TMR aimed at bio-magnetic fields (MCG/MEG), 2025 [TMRsubpT2025APL].
- Series MTJ arrays trade die area for √N noise averaging [SerialMTJ2020sensors].
- Power/size: bridge resistances are high (tunnel junctions), so power can be far below GMR/AMR for equivalent function — n/r for exact figures; [Zhou2022TMRchapter] discusses.

**Strengths.** Highest sensitivity-per-watt of the solid-state room-temperature families; large signal enables simple electronics; scalable to arrays; dc-capable; displacing Hall in current/angle sockets [Zhou2022TMRchapter; Zheng2019mrroadmap].

**Weaknesses / failure modes.** 1/f noise (electronic + magnetic) dominates exactly where biomagnetics needs performance — the central obstacle [Egelhoff2009picoteslaMTJ]; barrier dielectric breakdown (ESD sensitivity); hysteresis; temperature dependence of TMR ratio; tighter process control than GMR (sub-nm barrier uniformity) [Zhou2022TMRchapter].

**Commercial maturity.** Mass-market and growing (angle encoders, current sensors, e-compass; MultiDimension, TDK, Crocus [VENDOR-class]); pT-class biomagnetic TMR is lab-to-pilot.

**Pioneering directions.** Sub-pT room-temperature MCG/MEG arrays as a cryogen-free alternative to SQUID/OPM [TMRsubpT2025APL; Spintronic2024npj]; AC-modulation and flux-concentration schemes to defeat 1/f noise (modulation shown to buy ~an order of magnitude in detectivity — retrieved snippet, confidence: med).

**Key refs:** [Zhou2022TMRchapter] [Freitas2016spintronic] [Egelhoff2009picoteslaMTJ] [TMRsubpT2025APL] [SerialMTJ2020sensors] [Zheng2019mrroadmap] [Spintronic2024npj]

---

## 5. Fluxgate

**Principle.** A soft-magnetic core is driven periodically into saturation by an excitation winding; an external dc field breaks the symmetry of the magnetization waveform, generating even harmonics (classically detected at 2f) in a sense winding proportional to the field. Parallel (ring/race-track) and orthogonal geometries; fundamentals and evolution in [Ripka2003fluxgateadv; Fluxgate2021Sensors].

**Performance envelope.**
- Noise: modern low-noise fluxgates operate at the few-pT/√Hz @ 1 Hz level; fundamental-mode orthogonal fluxgates (dc-biased microwire, coherent-rotation magnetization) reach sub-pT-class white noise — open/closed-loop 1-Hz noise of 0.75/1.5 pT/√Hz and white noise ≤0.3–0.6 pT/√Hz reported across the FM-OFG literature retrieved this run [Dressler2021orthofluxgate; Fluxgate2021Sensors] (specific-figure attribution: confidence med — multiple FM-OFG papers in the retrieved set; verify against [Dressler2021orthofluxgate] full text).
- Range: earth-field scale (±100 µT class) with excellent linearity; observatory/space-grade absolute stability [Fluxgate2021Sensors].
- Bandwidth: dc to ~kHz (excitation-limited) [Ripka2003fluxgateadv].

**Strengths.** Best precision/stability per dollar in the nT–pT dc regime without cryogenics or zero-field shielding; decades of space heritage; vector measurement; radiation-tolerant [Fluxgate2021Sensors; Ripka2003fluxgateadv].

**Weaknesses / failure modes.** Bulky vs solid-state (cored sensor + windings); power for core excitation; perming (offset shift after field shock); core magnetic noise sets the floor; limited bandwidth [Ripka2003fluxgateadv; Fluxgate2021Sensors].

**Commercial maturity.** Mature niche: spacecraft magnetometers, compasses, UXO/geophysics, current transducers (Bartington, Billingsley, Stefan Mayer [VENDOR-class]); PCB/MEMS-integrated fluxgates are emerging [Fluxgate2021Sensors].

**Pioneering directions.** FM-OFG noise reduction toward the sub-pT decade [Dressler2021orthofluxgate]; miniaturized/planar fluxgates for UAV magnetometry and wearables [Fluxgate2021Sensors].

**Key refs:** [Ripka2003fluxgateadv] [Fluxgate2021Sensors] [Dressler2021orthofluxgate] [Ripka2010advancesIEEE]

---

## 6. Search-coil / induction

**Principle.** Faraday induction: voltage across an N-turn coil (usually on a high-permeability core) proportional to dB/dt — inherently ac-only, with sensitivity rising with frequency until core/winding resonance. Design theory (core demagnetization, flux feedback, noise matching) in [Tumanski2007inductioncoil].

**Performance envelope.**
- Noise: 4 fT/√Hz at 6 kHz for a 430 g tri-axis dual-band space instrument [Coillot2010dualband]; ~10 fT/√Hz-class at 1 kHz for optimized cores (JASS 2024 core-comparison paper retrieved: 0.012–0.014 pT/√Hz at 1 kHz — confidence: med, DOI unverified this run); flight instrument for THEMIS documented in [Roux2008themisSCM].
- Range/bandwidth: ~Hz to ~MHz; no dc response by physics [Tumanski2007inductioncoil].

**Strengths.** Unbeatable simplicity and reliability (passive transducer); femtotesla-class ac sensitivity at kHz; huge dynamic range; radiation/temperature robust; the reference sensor for space plasma waves, magnetotellurics, EMC [Tumanski2007inductioncoil; Roux2008themisSCM].

**Weaknesses.** No dc; sensitivity collapses at low frequency (∝ f); physically large for low-frequency performance; microphonics/vibration sensitivity [Tumanski2007inductioncoil].

**Commercial maturity.** Mature niche: geophysics (magnetotellurics), space instruments, EMC antennas, and — in its air-cored guise — every Rogowski coil and current transformer.

**Pioneering directions.** Dual-band and feedback-flattened designs for multi-decade spectral coverage [Coillot2010dualband]; core-material optimization for mass reduction (space).

**Key refs:** [Tumanski2007inductioncoil] [Roux2008themisSCM] [Coillot2010dualband]

---

## 7. GMI (giant magnetoimpedance)

**Principle.** In a soft-magnetic conductor (Co-based amorphous wire/ribbon with near-zero magnetostriction) carrying a MHz ac current, the skin depth depends on transverse permeability, which an external field modulates — impedance changes of >100% per Oe-scale fields. Mechanism, materials, and figure-of-merit landscape in [Phan2008gmiprogress]; magnetometer-level engineering (bias, detection electronics, noise) in [Dolabdjian2016gmichapter].

**Performance envelope.**
- Resolution: pT-class demonstrated with amorphous-wire MI sensors for biomagnetic measurement [Uchiyama2020picoteslaMI]; commercial MI modules sit in the nT decade (Aichi Steel MI parts in smartphones — `[VENDOR]`-class fact, common in the retrieved literature).
- MEMS-integrated GMI: 4.8 V/Oe sensitivity at 60 MHz excitation, 40 nT resolution (confidence: med — abstract-level, PMC-indexed MDPI paper, DOI unverified this run).
- Bandwidth: excitation is MHz-class; demodulated signal bandwidth typically kHz–100 kHz — n/r exact.

**Strengths.** Very high sensitivity-to-power ratio; small (mm wire) and cheap; room temperature; already in consumer e-compasses; pT-level potential without shielding exotica [Phan2008gmiprogress; Uchiyama2020picoteslaMI].

**Weaknesses / failure modes.** Strong nonlinearity and hysteresis of the raw transfer (needs bias-field operating point + feedback — an operating-point self-regulation literature exists); temperature drift of amorphous alloy properties; MHz excitation electronics; wire-contact reliability in MEMS integration [Phan2008gmiprogress; Dolabdjian2016gmichapter].

**Commercial maturity.** Niche-to-mass-market via one dominant vendor path (Aichi Steel MI in phones); scientific/biomedical GMI is lab-stage.

**Pioneering directions.** pT biomagnetics (MCG on unshielded subjects is the stated target of the Nagoya line) [Uchiyama2020picoteslaMI]; GMI meander current sensing (CoFeNiSiB ribbon, contactless — retrieved 2024 PMC paper, confidence: med).

**Key refs:** [Phan2008gmiprogress] [Dolabdjian2016gmichapter] [Uchiyama2020picoteslaMI]

---

## 8. SQUID

**Principle.** Superconducting loop with one (rf) or two (dc) Josephson junctions; flux quantization + Josephson interference make the loop voltage a periodic function of flux with period Φ₀ = h/2e, read out in a flux-locked loop. Instrument physics and system design in [Fagaly2006squidRSI].

**Performance envelope.**
- Noise: few fT/√Hz typical for low-Tc multichannel biomagnetic systems [Clarke2018squidfocus]; SQUIDs measure fT fields in the presence of tesla-scale static fields (dynamic-range statement retrieved from the biomagnetism literature) [Clarke2018squidfocus].
- Context figures: MCG R-peak ~50–100 pT; MEG signals ~2–3 orders below that [Clarke2018squidfocus; Murzin2020biomedsensors] (confidence: med on exact numbers — restate from full text at drafting).
- Bandwidth: dc to ~MHz-class (FLL-limited) — n/r exact; [Fagaly2006squidRSI].

**Strengths.** The sensitivity reference standard for half a century; enormous dynamic range; vector or gradiometric configurations; mature multichannel systems (MEG, MCG, geophysics, NDE, magnetic microscopy) [Fagaly2006squidRSI; Clarke2018squidfocus].

**Weaknesses / failure modes.** Cryogenics (LHe for low-Tc; LN₂ for noisier high-Tc) dominates cost, siting, and maintenance; flux trapping after field transients; needs magnetically shielded rooms for biomagnetics; fixed-helmet geometry wastes standoff on small/moving subjects — the specific weakness OPMs attack [Clarke2018squidfocus; Boto2018wearableMEG].

**Commercial maturity.** Mature niche: clinical MEG installations, geophysical and lab instruments (CTF/MEGIN systems, Tristan, Supracon [VENDOR-class]).

**Pioneering directions.** High-Tc and cryocooled systems; hybrid SQUID/flux-concentrator magnetometers pushing fT under ambient conditions (retrieved 2020 Science Bulletin hit — verify before citing); competition-driven repositioning vs OPM arrays [Clarke2018squidfocus].

**Key refs:** [Fagaly2006squidRSI] [Clarke2018squidfocus] [Murzin2020biomedsensors]

---

## 9. OPM / SERF (optically pumped magnetometers)

**Principle.** Optical pumping polarizes alkali-vapor spins; Larmor precession in the ambient field modulates optical absorption/rotation, read out to infer |B| (scalar) or field components (zero-field variants). In the spin-exchange relaxation-free (SERF) regime — high vapor density, near-zero field — spin-exchange decoherence is suppressed and sensitivity reaches the sub-fT decade [Kominis2003subfemtotesla; Tierney2019OPM].

**Performance envelope.**
- Record class: subfemtotesla multichannel operation, with 0.54 fT/√Hz demonstrated and aT-class projected [Kominis2003subfemtotesla].
- Microfabricated: sub-pT with a chip-scale vapor cell [Shah2007microfabvapor]; miniaturized hybrid-cell SERF at 20 fT/√Hz [SERFhybridcell2024msn]; chip-scale device platform reviewed in [Kitching2018chipscaleatomic].
- Systems: wearable OPM-MEG demonstrated head-motion-tolerant recording; sensor-on-scalp geometry buys 3–5× signal vs fixed SQUID helmets [Boto2018wearableMEG; Tierney2019OPM].
- Bandwidth: SERF channels are ~100 Hz-class (linewidth-limited) — n/r exact; [Tierney2019OPM] discusses.

**Strengths.** SQUID-class (or better) sensitivity with no cryogenics; wearable/conformal arrays; mass-producible MEMS vapor cells; scalar variants are absolute (Larmor frequency ∝ |B| through a fundamental constant) [Tierney2019OPM; Kitching2018chipscaleatomic].

**Weaknesses / failure modes.** SERF works only near zero field (µT-class ambient must be nulled — shielded rooms or active coils); narrow dynamic range and bandwidth; cell heating (~150 °C) and thermal management; cross-talk in dense arrays; gain drift with cell temperature/light power [Tierney2019OPM].

**Commercial maturity.** Commercial niche, scaling fast: QuSpin, FieldLine, Cerca (OPM-MEG systems) [VENDOR-class; peer-reviewed system validation in [Boto2018wearableMEG]]; scalar OPMs long-commercial in geophysics.

**Pioneering directions.** Multi-hundred-channel wearable MEG; wireless OPM-MEG (retrieved 2024 NeuroImage hit); triaxial and closed-loop cells; chip-scale integration [Kitching2018chipscaleatomic; SERFhybridcell2024msn].

**Key refs:** [Kominis2003subfemtotesla] [Shah2007microfabvapor] [Tierney2019OPM] [Boto2018wearableMEG] [SERFhybridcell2024msn] [Kitching2018chipscaleatomic]

---

## 10. NV-diamond (nitrogen-vacancy magnetometry)

**Principle.** The NV⁻ center's ground-state spin triplet has a field-dependent Zeeman splitting read out optically (spin-dependent fluorescence, ODMR) at room temperature; the four NV crystal axes give intrinsic vector capability. Ensemble sensitivity physics and optimization levers (readout fidelity, dephasing, photon collection) are treated in the definitive review [Barry2020NVdiamond].

**Performance envelope.**
- dc sensitivity below 10 pT/√Hz demonstrated (ensemble, (111) diamond), with 0.3 pT resolved after ~10³ s averaging [NVsub10pT2024prapplied].
- Microwave-field sensing at pT level [NVmicrowave2023prapplied].
- Dynamic range: current sensing 0–1000 A with 46 ppm-scale precision and galvanic isolation `[PREPRINT — not peer-reviewed; locate version of record]` [NVcurrentPPM2023].
- Bandwidth: dc to ~MHz protocols exist; portable prototypes report ~10 nT/√Hz-class (retrieved RSI 2024 hit — confidence: med).

**Strengths.** Room-temperature quantum sensor; vector + absolute (frequency-referenced); huge dynamic range (works inside tesla-scale bias fields); solid-state, no consumables; unmatched spatial resolution in microscopy geometries; radiation-hard host [Barry2020NVdiamond].

**Weaknesses / failure modes.** Sensitivity still 2–4 decades off SQUID/SERF at equal averaging; needs green laser + microwave delivery (power, integration); photon-collection efficiency limits practical devices; diamond cost/quality supply chain; fluorescence contrast drift with temperature/laser power [Barry2020NVdiamond].

**Commercial maturity.** Lab-to-startup (Lockheed, Element Six ecosystem, several quantum-sensing startups [VENDOR-class]); no mass-market device yet.

**Pioneering directions.** Biomagnetics push toward sub-pT [NVsub10pT2024prapplied]; EV/battery and power-electronics current sensing [NVcurrentPPM2023, PREPRINT]; integrated photonics + microelectronic readout (retrieved arXiv hits — discovery only); multichannel diamond arrays.

**Key refs:** [Barry2020NVdiamond] [NVsub10pT2024prapplied] [NVmicrowave2023prapplied] [NVcurrentPPM2023 — preprint]

---

## 11. Magnetoelectric (ME) composites

**Principle.** Strain-coupled magnetostrictive + piezoelectric laminate (e.g., Metglas/PZT, Metglas/PVDF): magnetic field strains the magnetostrictive layer, the piezoelectric converts strain to charge — a passive field-to-voltage transducer, resonantly enhanced at the laminate's electromechanical resonance. Reviewed in [Bichurin2021MEreview].

**Performance envelope.**
- Passive laminates: pT-class equivalent magnetic noise at resonance; ~6 pT/√Hz at 1 Hz reported for relaxor-PT single-crystal composites (confidence: med — retrieved review snippet) [Bichurin2021MEreview].
- Quartz-based symmetric laminate: 11 pT detected at 1 Hz; optimized LOD 2.7 pT [QuartzME2022symmetry].
- dc detection via NEMS resonators: picotesla-class dc LOD [Li2017nemsME]; self-biased 215 MHz ME NEMS resonator for dc fields [Nan2013selfbiasME].

**Strengths.** Fully passive (zero-power transduction) options; room temperature; small and cheap materials stack; pT-class at resonance rivals fluxgate in a fraction of the volume [Bichurin2021MEreview].

**Weaknesses / failure modes.** Best performance confined to the (narrow) resonance band; passive types cannot do dc; vibration and acoustic pickup (the strain path is also a microphone); flicker noise at low frequency; aging/creep of bonded laminates; ME coefficient drifts with bias field and temperature [Bichurin2021MEreview].

**Commercial maturity.** Lab-only (no established catalog vendor identified this run).

**Pioneering directions.** ME antennas and dual-use sensor/energy-harvester devices; MEMS/NEMS ME arrays for unshielded biomagnetics [Li2017nemsME; Bichurin2021MEreview].

**Key refs:** [Bichurin2021MEreview] [QuartzME2022symmetry] [Li2017nemsME] [Nan2013selfbiasME]

---

## 12. MEMS Lorentz-force

**Principle.** An ac current at the mechanical resonance of a micromachined structure experiences a Lorentz force in the measured field; the resulting resonant displacement is read capacitively, piezoresistively, or optically. No magnetic material on the die. Family reviewed in [HerreraMay2009memsresonant].

**Performance envelope (collected in/around [HerreraMay2009memsresonant]; individual figures from the retrieved set, confidence: med).**
- Resolutions spanning ~1 nT (capacitive, vacuum-packaged, 35 Hz bandwidth at 2.5 kHz resonance) to ~hundreds of nT (piezoresistive); 0.4 nT with optical readout; pT-class limits claimed in conference work (IEEE, retrieved hit — verify before citing).
- Bandwidth: tens of Hz around resonance (Q-limited) — a defining constraint.

**Strengths.** CMOS-MEMS co-fabrication; no hysteresis or perming (no ferromagnet); 3-axis integration in one process; naturally combines with inertial MEMS in IMU product lines [HerreraMay2009memsresonant].

**Weaknesses / failure modes.** Needs vacuum packaging for useful Q; narrow signal bandwidth; bias-current power vs resolution trade; temperature dependence of resonance (needs tracking/closed loop); stiction/shock fragility standard to MEMS [HerreraMay2009memsresonant].

**Commercial maturity.** Lab-to-niche; magnetometer sockets in consumer IMUs went to AMR/Hall/TMR instead — no volume Lorentz-force product identified this run.

**Pioneering directions.** FM (frequency-modulated) operation for drift immunity; space magnetometry proposals; internal thermal-piezoresistive amplification (retrieved hit, ~10³ gain — verify).

**Key refs:** [HerreraMay2009memsresonant] [MagSensorsReview2021ERX]

---

## 13. Fiber-optic / magneto-optic (brief)

**Principle.** Three retrieved mechanisms [Rostami2023fbgreview]: (i) magnetostrictive composite bonded to an FBG — field-induced strain shifts the Bragg wavelength; (ii) magnetic-fluid cladding — field-dependent refractive index around the fiber/FBG; (iii) Faraday effect — field-induced polarization rotation ∝ Verdet constant (basis of optical current transformers).

**Performance envelope.** Sensitivities quoted as pm/mT-class Bragg shifts (e.g., 9.83 pm/mT for an oriented-domain magnetostrictive composite FBG — confidence: med, retrieved snippet) [Rostami2023fbgreview]; noise floors in tesla units generally n/r — this family is specified by strain/wavelength resolution, not pT/√Hz.

**Strengths.** Total EMI immunity; passive, dielectric sensing head (safe at HV potential — the reason optical current transducers own high-voltage substations); km-scale remote interrogation; multiplexing many sensors on one fiber; intrinsically explosion-safe [Rostami2023fbgreview].

**Weaknesses.** Temperature/strain cross-sensitivity of FBGs (needs referencing); Faraday devices need long interaction lengths or special glass (small Verdet constant) and suffer polarization drift; magnetic-fluid devices have loss/ageing issues; interrogators cost more than the sensor [Rostami2023fbgreview].

**Commercial maturity.** Niche-commercial for optical current transformers in HV metering [VENDOR-class fact]; FBG magnetic sensing is lab-to-pilot.

**Key refs:** [Rostami2023fbgreview]

---

## 14. Resonance magnetometers (proton / Overhauser / CPT) — short treatment

Proton-precession magnetometers polarize protons in a fluid and measure the Larmor frequency (γ_p is a fundamental constant), giving drift-free absolute |B|; the Overhauser variant uses dynamic nuclear polarization via a dissolved radical, allowing continuous, low-power operation [Ge2016overhauser]. Representative commercial performance: 0.2 nT absolute accuracy, 0.022 nT/√Hz sensitivity, 0.01 nT resolution over a 20–120 µT range `[VENDOR — GEM Systems]` [GEMOverhauserVendor]; Overhauser instruments are the de-facto standard in geomagnetic observatories and mineral/UXO surveys [Ge2016overhauser; GEMOverhauserVendor]. Limitations: scalar-only, ~Hz-class update rates, and cycle-time/gradient sensitivity. Coherent-population-trapping (CPT) and related chip-scale atomic magnetometers port the absolute-frequency-readout idea to microfabricated vapor cells, sharing platform technology with chip-scale atomic clocks [Kitching2018chipscaleatomic]. In the review, position these as the *calibration/traceability anchors* of the field — the instruments other magnetometers are checked against — which links Section 2 to the standards/metrology thread of Section 4.

**Key refs:** [Ge2016overhauser] [GEMOverhauserVendor — VENDOR] [Kitching2018chipscaleatomic]

---

## Comparison table

Populated **only** with values sourced above; "n/r" = not reported/verified this run (fill from the cited full texts at drafting, never from memory). Cost tier is an editorial judgment (flagged ~), not a sourced number. Noise figures are best-in-class-reported unless marked "typ."

| Family | Principle | Field range | Resolution / noise | Bandwidth | Size / power | Cost tier~ | Maturity | Typical domains | Key refs |
|---|---|---|---|---|---|---|---|---|---|
| Hall (Si CMOS) | Lorentz V_H ∝ I·B | ~100 µT to multi-T [Lenz2006magsensors] | 45 µT residual offset (spinning, 180 nm) [JEET2019lownoisehall]; nT-class floor n/r | 600 kHz shown [JEET2019lownoisehall] | mm-scale IC; mW | lowest | mass-market | current, position, speed, consumer | Popovic2004hallbook; Crescentini2022hallcurrent |
| Hall (GaN 2DEG) | Hall in 2DEG, wide-bandgap | as Hall; to 576 °C [Alpert2020gan2deg] | 60.2 V/A/T ±10.5% RT–576 °C [Alpert2020gan2deg] | n/r | mm die; external readout | ~low | lab/niche | harsh env., energy, (fusion diagnostics) | Alpert2020gan2deg; GaNHEMThall2012jpcs |
| AMR | anisotropic MR in permalloy | ~nT to mT class [Jogschies2015mrindustrial] | nT-class typ.; spectra in [Zheng2019mrroadmap] n/r | n/r (dc–high) | mm IC; low mW | low | mass-market | compass, position, current | Jogschies2015mrindustrial; Zheng2019mrroadmap |
| GMR (spin-valve) | spin-dependent scattering | µT–mT class n/r | nT-class typ. [Zheng2019mrroadmap] n/r | dc–100 kHz+ n/r | mm IC; mW | low | mass-market | wheel speed, angle, encoders | Freitas2016spintronic; Treutler2001automotive |
| TMR / MTJ | spin-dependent tunneling (MgO) | nT–mT class | sub-pT best [TMRsubpT2025APL]; 10⁻¹¹–10⁻¹² T/√Hz calc. [Egelhoff2009picoteslaMTJ] | 2 pT/√Hz @500 kHz shown (med conf.) | mm IC; sub-mW possible | low–mid | mass-market + pT lab | angle, current, e-compass, biomag (emerging) | Zhou2022TMRchapter; Egelhoff2009picoteslaMTJ |
| Fluxgate | core saturation harmonics | pT to ~mT; ±100 µT typ. [Fluxgate2021Sensors] | few pT/√Hz @1 Hz; ≤0.3–0.75 pT/√Hz FM-OFG (med conf.) [Dressler2021orthofluxgate] | dc–kHz [Ripka2003fluxgateadv] | cm; ~100 mW class n/r | mid | mature niche | space, geophysics, current, navigation | Ripka2003fluxgateadv; Fluxgate2021Sensors |
| Search-coil | Faraday induction | ac only | 4 fT/√Hz @6 kHz [Coillot2010dualband] | ~Hz–MHz [Tumanski2007inductioncoil] | cm–dm; passive | low–mid | mature niche | space waves, MT, EMC, current | Tumanski2007inductioncoil; Roux2008themisSCM |
| GMI | skin-depth/permeability modulation | nT–µT typ.; pT shown [Uchiyama2020picoteslaMI] | pT-class bio demo [Uchiyama2020picoteslaMI]; 40 nT MEMS (med conf.) | kHz–100 kHz n/r | mm wire; low power | low | niche→consumer | e-compass, bio (emerging), NDT | Phan2008gmiprogress; Dolabdjian2016gmichapter |
| SQUID | Josephson/flux quantization | fT to T (with FLL) [Clarke2018squidfocus] | few fT/√Hz [Clarke2018squidfocus] | dc–MHz n/r | rack + cryostat; kW-class facility | very high | mature niche | MEG/MCG, geophysics, NDE, microscopy | Fagaly2006squidRSI; Clarke2018squidfocus |
| OPM / SERF | optically pumped alkali spins | near-zero field (SERF); µT scalar | 0.54 fT/√Hz [Kominis2003subfemtotesla]; 20 fT/√Hz mini [SERFhybridcell2024msn] | ~100 Hz SERF n/r | cm sensor; W-class heater | mid–high | commercial niche, scaling | wearable MEG/MCG, geophysics | Tierney2019OPM; Boto2018wearableMEG |
| NV-diamond | ODMR of NV⁻ spins | pT to T-scale bias fields | <10 pT/√Hz dc [NVsub10pT2024prapplied] | dc–MHz protocols n/r | benchtop→cm modules; W | high (falling) | lab/startup | current sensing, microscopy, bio (emerging) | Barry2020NVdiamond; NVsub10pT2024prapplied |
| Magnetoelectric | magnetostrictive+piezo laminate | pT–µT at resonance | 2.7–11 pT LOD [QuartzME2022symmetry]; ~6 pT/√Hz @1 Hz (med conf.) [Bichurin2021MEreview] | narrow, near resonance | mm–cm; passive option | low | lab-only | biomag candidates, ME antennas | Bichurin2021MEreview; Li2017nemsME |
| MEMS Lorentz | resonant Lorentz displacement | nT–mT n/r | ~1 nT best (vacuum, med conf.) [HerreraMay2009memsresonant] | tens of Hz (Q-limited) | µm–mm; mW | low | lab/niche | IMU-adjacent, space proposals | HerreraMay2009memsresonant |
| Fiber-optic / magneto-optic | FBG strain / Faraday rotation | µT–T (current xducers) n/r | 9.83 pm/mT (med conf.) [Rostami2023fbgreview] | n/r | fiber + interrogator | mid | niche (HV current) | HV metering, EMI-hostile plants | Rostami2023fbgreview |
| Proton/Overhauser | nuclear Larmor precession (absolute) | 20–120 µT [GEMOverhauserVendor, VENDOR] | 0.2 nT absolute; 0.022 nT/√Hz [GEMOverhauserVendor, VENDOR] | ~Hz update | dm probe; portable | mid | mature niche | observatories, survey, UXO | Ge2016overhauser; Kitching2018chipscaleatomic |

---

## Gaps to close before/while drafting Section 2 (carried to stage 80)
1. **AMR/GMR detectivity spectra** — pull exact pT–nT/√Hz numbers from [Zheng2019mrroadmap] full text; this brief only has qualitative "nT-class".
2. **Hall noise floor in T/√Hz** and current-sensor bandwidth numbers from [Crescentini2022hallcurrent] full text.
3. **SERF bandwidth and dynamic-range figures** — [Tierney2019OPM] full text.
4. Med-confidence snippet numbers to re-verify against full texts: 45 µT/600 kHz Hall [JEET2019lownoisehall]; FM-OFG 0.3–0.75 pT/√Hz attribution [Dressler2021orthofluxgate]; MCG 50–100 pT [Clarke2018squidfocus]; ME 6 pT/√Hz [Bichurin2021MEreview]; MEMS ~1 nT [HerreraMay2009memsresonant]; FBG 9.83 pm/mT [Rostami2023fbgreview].
5. **Author self-citation** (2023 IEEE Sensors Letters, AlGaN/GaN Hall in HSX) — [UNVERIFIED] this run; author inserts the exact record.
6. Preprints used for discovery only, to be replaced by versions of record if kept: NV current sensing [NVcurrentPPM2023]; GaN spinning-current arXiv 1812.00363.
7. No catalog vendor found for ME composites — if one exists by drafting time, add with `[VENDOR]` tag; otherwise keep "lab-only".
