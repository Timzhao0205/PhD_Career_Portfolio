# Stage 10B — radiation, temperature, and reliability literature

## Goal

Determine what is actually known about radiation-induced changes in Hall
sensors and every other hybrid measurement-chain element, with conditions
precise enough to support a compensation strategy.

## Evidence layers

1. Direct Hall-device irradiation:
   - neutron spectra and fluence;
   - gamma/TID;
   - proton/electron/heavy-ion evidence;
   - InSb, InAs, GaAs, Si, SOI, GaN/AlGaN/AlN, metallic/ceramic, and other
     justified candidate technologies.
2. Enabling device/material physics:
   - mobility/carrier-density/contact/resistance change;
   - displacement damage, ionization, transmutation, annealing;
   - temperature–radiation interaction.
3. Measurement chain:
   - Hall bias/current source, analog front end, ADC, cabling, packaging;
   - coil conductor/insulation/effective area;
   - integrator and timing/reference electronics.
4. Fusion qualification and calibration practice:
   - ITER/JET/DEMO and long-duration magnetic diagnostics;
   - pre-, in-, and post-irradiation calibration;
   - dose/fluence monitoring and uncertainty.

## Required extraction

For each direct radiation paper, put the following in `claims_supported` or
`notes` when available:

- species/spectrum;
- dose or fluence and units;
- temperature and bias state;
- annealing/time after exposure;
- device material/structure;
- quantity changed and direction/magnitude;
- measurement reference and uncertainty;
- whether the change was reversible, persistent, or not measured.

Do not infer missing conditions. Do not merge proton and neutron behavior.
Distinguish sensitivity, offset, resistance, mobility, noise, linearity,
cross-axis response, hysteresis, and outright failure.

## Outputs

1. `evidence\10B_RADIATION_SOURCES.csv`
   - exact shared ledger header;
   - at least 45 unique verified peer-reviewed rows.
2. `evidence\10B_RADIATION_SYNTHESIS.md`
   - mechanism/condition matrix;
   - material/device comparison;
   - measurement-chain failure pathways;
   - what can be modeled, monitored, calibrated, or only bounded;
   - evidence gaps for fusion-relevant neutron/gamma conditions;
   - source-ID citations.

## Acceptance

- 45 verified peer-reviewed unique sources minimum.
- At least 15 direct Hall-device or Hall-system irradiation/qualification
  sources if the literature permits; if not, document the verified maximum and
  the exact gap rather than padding.
- Radiation species, spectrum, dose/fluence, temperature, and access level are
  not silently conflated.
- Evidence on sensor material is separated from evidence on electronics.
- Contradictory results and plausible causes are retained.
