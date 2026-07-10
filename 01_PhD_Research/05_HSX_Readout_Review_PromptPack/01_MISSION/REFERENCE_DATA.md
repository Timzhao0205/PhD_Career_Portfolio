# REFERENCE_DATA — vendor/part facts to seed the review (still re-verify + cite)

This is a starting menu gathered 2026-07-09 so the run is efficient. **Re-fetch each page and
cite it** before using any number in a deliverable (specs change; confirm current stock/spec).

## A. Vacuum feedthrough — Accu-Glass subminiature-D CF family (for ST5)

Baseline (current): **9D-275**, Accu-Glass P/N 100200 — 9-pin sub-D, single connector,
**2.75″ CF**, **500 VDC**, **5 A/pin (max 20 % of pins simultaneously)**, −200…250 °C,
≤ 1×10⁻¹⁰ Torr, stainless + glass-ceramic, male/male.
https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/9d-275

Higher-conductor options in the SAME sub-D CF family (candidate menu for 12 conductors — do
not assume which; evaluate against the 9D-275 ratings and the cube geometry):

| Option | Pins | Connectors | CF flange | URL |
|---|---|---|---|---|
| 15D-450 | 15 | single | 4.5″ | https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d-450 |
| 15D2-450 | 30 (2×15) | dual | 4.5″ | https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/15d2-450 |
| 25D-15D-450 | 40 (25+15) | two | 4.5″ | https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/25d-15d-450 |
| 25D2-450 | 50 (2×25) | dual | 4.5″ | https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/25d2-450 |
| (family index) | — | — | — | https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs |

Things ST5 must verify per candidate: exact voltage/current rating (confirm ≥ 9D-275),
vacuum rating, temperature range, CF size vs the available port on HSX (a 2.75″→4.5″ change
has mechanical consequences — confirm the port/adapter), gender, and the matching in-air and
in-vacuum mating connectors + cables Accu-Glass sells for it.

## B. The v2 sensor connector (for ST2)

**Amphenol D09S33E6GX00LF** — DSUB-9, socket (S), the Digi-Key part now on J1. ST2 must fetch
the Amphenol datasheet and confirm: gender (socket vs pin), standard D-sub pin numbering,
footprint/pinout match to the KiCad symbol used, and that the sensor-side mating connector and
the harness pin convention (p1=1, p3=2, p2=6, p4=7; twisted pairs (1,2)=p1&p3 bias,
(6,7)=p2&p4 sense) are preserved from v1.

## C. Signal-chain datasheets to pull (for ST1 / ST4)

- ADG1209YRUZ (4:1 diff mux): R_on, R_on-flatness, charge injection Q_inj, C_in of logic
  inputs, **continuous current abs-max**, leakage, supply/logic levels.
- ADG5236BRUZ (dual SPDT, latch-up-proof): same set; note the "5000-series" robustness.
- AD8429ARZ (in-amp): e_n (1 nV/√Hz), i_n, CMRR vs G, bandwidth vs G (~1.2 MHz at G=100),
  V_os, supply, temperature (readout is ambient, so this is comfortable).
- Candidate alt in-amp AD8421 (if ST1 considers it): e_n (3.2 nV/√Hz), i_n (~200 fA/√Hz),
  BW (~2 MHz at G=100) — but note the locked constraints may make the incumbent already fine.
- ADA4898-2YRDZ (dual op-amp, present in library, unplaced): decide place-or-not for ST1.
- RS6-2415D (isolated DC/DC ±15 V): ripple/spur spectrum, input range, isolation.
- Raspberry Pi Pico 2 (RP2350) GPIO: drive strength (mA per pin, configurable), and the
  mux/chopper input capacitance × 3 for the ST4 fan-out load estimate.

## C2. Hall-die packaging — Spectrum LCC02046 (for ST7)

Full data + the user's stated wire-bond strategy: `01_MISSION/REFERENCE/PACKAGING_LCC02046.md`.
In brief: 20-pad .350″ hermetic ceramic LCC (Spectrum Semiconductor Materials); octagonal
AlGaN/GaN Hall die with 4 corner contacts p1–p4; user plan = bond the 4 die contacts to the
carrier and route all signals to one side via castellations. ST7 verifies pad geometry against
the Spectrum datasheet (https://www.spectrum-semi.com/products/leadless-chip-carrier) and
comments on the strategy. Attach `LCC02046_datasheet.pdf` + the die image to the session if
available.

## D. Useful priors already in-hand (from the RSI plan; verify, don't assume)

- Harness sizing already contemplated: 12 signal conductors, "DB-15 or 2×DSUB-9" — ST5/ST6
  should reconcile the *board* connector (DSUB-9 per axis) with the *feedthrough* choice.
- One Pico fans a0/a1/a2/EN to 3 boards; each shared line drives 3 CMOS inputs (trivial DC
  load, but ST4 must check capacitive load + edge integrity over the cable run).

## Sources (this file)
- Accu-Glass 9D-275: https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs/9d-275
- Accu-Glass sub-D CF family: https://www.accuglassproducts.com/subminiature-d/cf-feedthroughs
- Accu-Glass 15D-450 / 15D2-450 / 25D-15D-450 / 25D2-450 (URLs in table A)
