# Seed references (verified anchors)

These are hand-checked, mostly peer-reviewed anchors that bootstrap the review so
the pipeline starts from real sources instead of inventing them. The machine-
readable version the pipeline actually consumes is `../refs_raw/00_seed.jsonl`;
Stage 70 verifies every DOI and merges these with what the lit-review stages find.

## Sensor-type reviews (Section 2 backbone)
- **Lenz & Edelstein, "Magnetic Sensors and Their Applications," *IEEE Sensors
  Journal* 6(3):631-649, 2006.** The standard cross-technology comparison.
- **Lenz, "A Review of Magnetic Sensors," *Proc. IEEE* 78(6):973-989, 1990.**
  Classic taxonomy of eleven sensing technologies.
- **"Magnetic sensors - A review and recent technologies," *Eng. Res. Express*
  3:022005, 2021** (DOI 10.1088/2631-8695/ac0838). Recent broad survey.
- **"Recent Progress of Fluxgate Magnetic Sensors," *Sensors* 21:1500, 2021**
  (DOI 10.3390/s21041500). In-journal example; weak-field, high-accuracy family.
- **Freitas, Ferreira & Cardoso, "Spintronic Sensors," *Proc. IEEE*
  104(10):1894-1918, 2016.** GMR/TMR authority.
- **"Enhanced performance and functionality in spintronic sensors," *npj
  Spintronics* 2, 2024** (DOI 10.1038/s44306-024-00058-9). Recent perspective.
- **Zhou, Zhang & Leng, "Tunneling Magnetoresistance (TMR) Materials and Devices
  for Magnetic Sensors," in *Spintronics* (Wiley), ch.3, 2022**
  (DOI 10.1002/9781119698968.ch3).
- **Barry et al., "Sensitivity optimization for NV-diamond magnetometry," *Rev.
  Mod. Phys.* 92:015004, 2020.** Pioneering room-temperature quantum magnetometry.

## Biomedical / pioneering
- **Tierney et al., "Optically pumped magnetometers: From quantum origins to
  multi-channel MEG," *NeuroImage* 199:598-608, 2019.** Wearable-MEG basis.
- **"TMR sensors with sub-pT detectivity for detecting bio-magnetic fields,"
  *Appl. Phys. Lett.* 126:160503, 2025.** MCG/MEG with solid-state sensors.
- **Tumanski, "Modern magnetic field sensors - a review," *Przeglad
  Elektrotechniczny* 89(10):1-12, 2013.** (peer-reviewed, lower impact.)

## Applications lead (to expand in Stage 40)
- **NV open-loop current sensing, ppm precision (arXiv:2304.07998, 2023)** -
  *preprint, discovery only*; the pipeline must find the version of record.

## Standards (Section 4 backbone)
- **ISO 26262** (automotive functional safety), **IEC 61508** (parent),
  **ISO/PAS 21448 / SOTIF** (2022). Cite the standards bodies directly.
- **Salay, Queiroz & Czarnecki, "An Analysis of ISO 26262: Using Machine Learning
  Safely in Automotive Software" (arXiv:1709.02435; find the SAE version).**
