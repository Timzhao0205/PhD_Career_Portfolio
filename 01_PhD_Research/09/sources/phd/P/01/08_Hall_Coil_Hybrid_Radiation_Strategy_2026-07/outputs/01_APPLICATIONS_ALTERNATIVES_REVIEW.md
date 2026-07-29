# Applications and alternatives — final review (stage 10D)

Source IDs cite `outputs\01_SOURCE_LEDGER.csv`; claim IDs cite
`outputs\01_EVIDENCE_MAP.csv`. Labels per `CLAUDE.md`. Per the stage scope,
this review characterizes application needs and incumbent/alternative
evidence **without finalizing outreach priority** — collaboration scoring
belongs to stage 40.

## 1. Application requirements (Observed)

| Lane | Field / dynamics | Duty cycle | Environment drivers |
|---|---|---|---|
| Tokamak long-pulse (ITER/WEST/JT-60SA/EAST) | ~0.01–1 T poloidal; DC-dominant + MHD AC | ~1000 s now (P004), hours targeted | In-vessel neutron/gamma + heat + EM loads; remote handling only (P001, P002); DEMO-class coils qualified ≥500 °C (P009); JT-60SA 200 °C/9 MGy figures secondary-sourced (P006, unconfirmed) |
| Stellarator mapping (W7-X/LHD/TJ-II/HIDRA/CNT) | sub-0.1 T commissioning to 2.75 T | Infrequent commissioning campaigns | ~1e-4 relative coil-accuracy criterion (P016); error fields correctable with ~5 % trim-coil current (P013); no environmental-qualification literature surfaced (gap) |
| Z-pinch/pulsed power (Z, MAGPIE, LTDs) | sub-T bias to >100 T; 100–240 ns rise | Single-shot | Extreme EMI/blast/debris (P021, P022); burst not cumulative radiation |
| Plasma-jet/MIF (PLX, ZaP, MagLIF) | sub-T jets to tens of T loads | Single-shot (0.2 Hz exception, P037) | MagLIF has real neutron yield ~1e12 (P030); probes excluded from pinch core (P032) |
| Superconducting/HTS magnets & machines | T-class to 17.7 T trapped (P040, P041) | Persistent DC; ms magnetization pulse | Cryogenic (4–77 K); temperature, not radiation, dominates; Hall temp-coefficients to 0.001 %/K by doping (P050, P051) |
| Accelerator magnets (CERN/FNAL/HIAF) | multi-T, ppm precision (P054, figures unconfirmed) | Controlled test campaigns | Bench metrology; radiation is background context, not a qualification driver |

## 2. Incumbents and the hybrid question, per lane (Observed/Derived)

- **Tokamak long-pulse — the one documented "promising" fit.** Incumbents:
  Mirnov/Rogowski/flux loops with drift-limited integrators. ITER's OVSS
  already pairs a bismuth-Hall DC channel with inductive sensors to correct
  coil drift — the strongest real-machine precedent in this mission (P003)
  (C27). It is a *system-level pairing of separate heads*, not a co-located
  hybrid, and **no tokamak source demonstrates the reverse direction** (coil
  identifying Hall drift). Cross-machine algorithm validation paths exist
  (JT-60SA→ITER, P010; Bayesian sensor-placement, P011). Steady-state DC
  sensing is a stated *requirement* (H065; P009; P004) (C33).
- **Stellarator mapping — open niche, zero prior art.** Incumbent is
  electron-beam flux-surface mapping (vacuum-only, commissioning-only:
  P018–P020) plus trim-coil correction validated against it (P012–P014).
  **No Hall+coil hybrid literature exists for stellarator mapping** (C32).
  For the user's HSX context this is an open niche with no validation base —
  the absence cuts both ways.
- **Z-pinch/pulsed power — documented poor fit.** The community solved
  redundancy by fusing two *inductive* sensors (B-dot + Rogowski, ±13–15 %,
  P025), bypassing Hall; Hall EMI susceptibility is documented in power
  electronics (P028 — extrapolation to z-pinch explicitly an inference);
  ns–µs timescales leave no DC baseline for a Hall anchor (C30).
- **Plasma-jet/MIF — mostly out of scope.** Where conditions are worst the
  field abandoned magnetic probes for optical PDV (P031) or Zeeman
  spectroscopy (P032) (C35); boundary-probe niches are plausible but
  undemonstrated (Unknown).
- **Persistent-mode SC/HTS magnets — structurally poor fit.** A coil is
  blind to a static trapped field (no dB/dt); the field's own precision
  reference is NMR (>2-year persistent NMR magnet at ~3e-5 ppm/h drift,
  P042, full text) with Hall arrays for mapping (P038, P043, P045) (C28).
  Coils appear only during the magnetization transient (P039, P049).
- **Accelerator magnets — mature prior art, novelty risk.** Hall + rotating
  coil + NMR combination is decades-old production practice, including
  in-situ rotating-coil calibration against a reference magnet (P052, P054,
  P057; NMR references P055, P058) (C29). Any novelty must rest on the
  radiation/in-situ/embedded-calibration angle, not the sensor combination.

## 3. Alternative technologies (seven families; Observed)

1. **Fluxgate** (P060, P061): DC-capable; thermal-*gradient* offset
   sensitivity mirrors the Hall offset problem; no new radiation source found
   (gap).
2. **AMR/GMR/TMR/planar Hall** (P062–P065): best-evidenced competitor
   family. TMR spans DC-to-broadband in a single channel (P064) and showed no
   key-parameter degradation to 5 Mrad(Si) gamma/X-ray under bias (P063,
   upgraded to verified at 10D); AMR tolerated 200 krad(Si) with front-end
   electronics as the weak link (P062). **Gamma/X-ray only — no neutron
   displacement data** (C31). TMR is the sharpest single-channel challenge to
   the Hall+coil value proposition.
3. **Fiber-optic/Faraday (FOCS)** (P066, P067; R063; H029, H030): EMI-immune,
   integrator-free, DC-capable current sensing; validated through JET D-T
   (C20); accuracy limited by Faraday-mirror imperfections with a published
   compensation route (P066). Competes on *enclosed current*, not local field
   mapping (C34).
4. **NMR** (P055, P058, P059, P068): the absolute-reference gold standard
   (to ~1e-12 relative, cryogenic ³He, P068) but DC/quasi-static and
   homogeneity-limited — a calibration reference, not a plasma diagnostic.
5. **SQUID** (P069, P070): fT-class sensitivity, mandatory cryogenics, narrow
   dynamic range; no peer-reviewed source directly documents fusion/radiation
   unsuitability — that remains an inference (flagged honestly).
6. **NV-center/quantum** (P071, P072): weakest-evidenced; no peer-reviewed
   radiation-tolerance or tokamak-deployment source exists (2026 preprint
   excluded by policy).
7. **Standalone Hall / coil baseline** (P073 anchor review; extensive 06
   coverage): the incumbent baseline both channels must beat individually.

## 4. Synthesis for later stages (Derived; no outreach priority set here)

- The only application lane where the evidence base *documents* both the need
  (steady-state DC + AC in one radiation environment) and a working precedent
  for half the architecture is the long-pulse tokamak lane (C27, C33).
- The stellarator-mapping niche is open but evidence-free (C32) — attractive
  for the user's HSX access, risky for validation burden.
- Three lanes carry documented vetoes or mature prior art (z-pinch C30,
  persistent-mode SC C28, accelerator C29) that stage 40's scoring must treat
  as vetoes/novelty risks, not just low scores.
- The competitive frontier is not "Hall vs coil" but Hall+coil vs TMR
  (single-channel DC-broadband, C31) and vs FOCS (current measurement, C34);
  neither competitor has neutron displacement-damage evidence — a gap that
  cuts in *both* directions.
- Group landscape (documented from official pages in the 10C synthesis §4;
  official pages are not peer-reviewed evidence and are not ledger rows):
  radiation-hard fusion Hall sensing is a small, mature EU-centered network
  (Prague/Lviv/Italy JET-RHP line) plus KFE (Kalman fusion) and the
  ITER OVSS program; pulsed-power and accelerator/HTS groups are active in
  adjacent metrology. Outreach sequencing is deferred to stage 40.
