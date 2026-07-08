# SPECS — Cocktail Dilution Sensor quick reference
One page. If a number is here, don't re-derive it. If the bench
disagrees, flag in NOTES.md — don't edit silently.

## Physics constants (25 °C unless noted)
| Quantity | Value | Note |
|---|---|---|
| εr water | ≈ 78.4 | tempco ≈ −0.37 %/°C |
| εr ethanol | ≈ 24.3 | |
| ρ water | 0.997 g/mL | |
| ρ ethanol | 0.789 g/mL | |
| nD water / EtOH | 1.333 / 1.361 | RI backup modality |
| Ice melt enthalpy | 334 J/g | thermodynamic dilution model |
| Sound speed vs ABV | NON-monotonic, peak ≈ 20 wt% | why ultrasonic alone fails |

## Scenario envelope (whisky + ice, v1)
| Quantity | Value |
|---|---|
| ABV range at pour | 40–45 % v/v |
| ABV at full melt-in | ~20–28 % v/v |
| Liquid temp trajectory | +25 °C → ≈ −5 °C |
| Calibration grid | 0–60 % ABV, −8 to +30 °C |
| Typical pour / ice | 60 mL spirit + ~150 g ice |

## Product targets (v1, from REQUIREMENTS.md)
| Metric | Target |
|---|---|
| ABV accuracy | ±1.5 % v/v (stretch ±1.0) |
| Dilution accuracy | ±3 % of total volume |
| Convergence | ≤ 2 s of immersed time, no deliberate pause |
| Update rate (live) | ≥ 2 Hz displayed |
| Environment | splashes, ice strikes, −10 to +40 °C liquid contact |
| Drift budget | < 0.5 % ABV-equivalent over a 4 h shift |

## Sensing chain (locked for Phase 0/1 — DECISIONS.md D-001)
| Element | Choice |
|---|---|
| Primary | Interdigitated capacitive (fringing field) |
| Electrode pitch coupons | 150 / 200 / 300 µm (6/8/12 mil), ENIG, guard ring |
| Sensing depth rule | ≈ 1 × electrode pitch |
| Passivation | Parylene-C (SNF benchtop only — replace before productization); backup MG 422B silicone |
| Readout | TI FDC2214 (4 ch, 28-bit, I²C); fallback EVAL-AD7746 (±4 pF range — needs guard scheme) |
| Temp | 10 kΩ glass-bead epoxy NTC, divider into MCU ADC; DS18B20 = slow sanity ch only (750 ms) |
| Motion | LSM6DS3 IMU (on XIAO Sense) — stir/strike/immersion gating |
| MCU | Seeed XIAO nRF52840 Sense, I²C to FDC2214, BLE/USB stream |
| Wiring | sensor→chip < 10 cm, shielded twisted pair |

## Estimator (see ESTIMATOR_SPEC.md)
| Element | Choice |
|---|---|
| Sampling | burst 1–10 kHz effective, 1–2 s windows |
| Robust statistic | mode-of-histogram (bubble outliers are ONE-SIDED, ε→1) |
| Strike handling | IMU spike → blank 50 ms |
| Fusion | capacitive ABV vs. thermodynamic melt model; divergence flag |
| Calibration form | 2-D low-order polynomial ε(T, ABV), inverted to ABV(ε, T) |

## Ground truth
| Method | Use |
|---|---|
| Gravimetric standards (0.01 g balance, 190-proof + DI) | static calibration |
| Strain-and-weigh surviving ice | exact dilution for dynamic runs |
| Proof & Tralle hydrometer | endpoint ABV check |
| 0–80 % v/v refractometer | binary-mix aliquot check (temp-corrected) |

## Budget bands
Phase 0 (dipstick) ≤ $400 · Phase 1 (clip-on probe) ≤ $1.5 K cumulative.
Core kit actual: see 20_HARDWARE/BOM.csv (~$250–400).
