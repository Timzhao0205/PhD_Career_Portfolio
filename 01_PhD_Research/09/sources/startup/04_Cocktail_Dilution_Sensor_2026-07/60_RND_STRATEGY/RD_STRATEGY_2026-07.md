# R&D Strategy - Cocktail Dilution Sensor

Date: 2026-07-09

## Executive Decision

Use Phase 0 to prove the measurement physics before spending effort on a
product-form PCB. The fastest credible path is:

1. FDC2214EVM + IDE coupon panel + co-located NTC, logging to CSV.
2. Python reference estimator against controlled static and dynamic data.
3. Custom KiCad coupon/readout board only after P0-E0/P0-E1 pass.
4. XIAO nRF52840 Sense as the default Phase 1 controller because it already
   includes BLE and an onboard 6-axis IMU for stir/strike gating.

Raspberry Pi Pico / Pico 2 W is a valid bench-controller alternative, but it
does not remove the need for an external IMU and has less direct wearable BLE
product precedent in this folder. Use Pico only if the project needs more
compute, Wi-Fi logging, or a MicroPython-first demo.

## Product Hypothesis

For whisky + ice, dilution and ABV can be measured in real time from a
fringing-field capacitive electrode plus temperature, with the estimator
rejecting bubbles and ice strikes by using burst sampling, mode estimation,
and IMU blanking.

Pass/fail claim for v1:

- ABV within +/-1.5 % v/v after convergence.
- Dilution within +/-3 % total volume.
- Valid reading within 2 s of immersed time while stirring.
- Drift below 0.5 % ABV-equivalent over a 4 h wet-use window.

## Phase Plan

| Phase | Goal | Build | Decision Gate |
|---|---|---|---|
| P0-A | Confirm readout chain | FDC2214EVM, three IDE coupons, NTC, guarded wiring | Air/DI/IPA separation, drift, hand-parasitic suppression |
| P0-B | Build calibration surface | Gravimetric ethanol/water standards, -8 to +30 C sweep | Static residual <=1.0 % ABV; T-comp residual <=0.5 % ABV |
| P0-C | Prove live dilution tracking | Stirred whisky + weighed ice, strain-and-weigh endpoint | Final ABV within +/-1.5 % on >=4/5 runs |
| P0-D | Abuse the estimator | Bubble load, ice strikes, half-immersion, hand/glass parasitics | Recovers within 2 s with <=40 % corrupted samples |
| P1 | Clip-on probe electronics | Custom KiCad readout board near electrodes, XIAO nRF52840 Sense | BLE/USB live stream, IMU gating, sealed wet end |
| P2 | Barspoon prototype | Flexible or narrow rigid-flex electrode shaft, potted handle | Usability, cleanability, one-gesture tare, repeatability |

## LTspice / Simulation Strategy

Do not try to fully simulate the FDC2214 internal digital converter in
LTspice. The useful simulations are the parts around it:

1. NTC divider and ADC input
   - Simulate 10 k NTC + precision divider + optional RC filter.
   - Sweep -8 to +30 C using the NTC Beta equation.
   - Output: ADC code sensitivity in counts/degC and filter time constant.

2. LC tank sensitivity
   - Model the FDC channel externally as L in parallel/series with sensor
     capacitance and parasitic capacitance.
   - Sweep sensor capacitance over the measured air/DI/IPA range from P0-E0.
   - Output: resonant frequency shift, margin to FDC2214 frequency limits,
     and sensitivity loss from cable parasitics.

3. Cable and guard parasitics
   - Model sensor capacitance, cable capacitance, leakage resistance, and
     shield/guard coupling as lumped elements.
   - Sweep lead length and leakage to set a hard rule for sensor-to-IC
     distance in the KiCad board.

4. Power integrity for Phase 1
   - Simulate LiPo/LDO or buck/LDO transient response only after the readout
     board architecture is selected.

Simulation output standard:

- Every simulation gets a one-page note with schematic screenshot, netlist
  parameters, sweep table, and the design decision it changes.
- If a model parameter comes from a datasheet, cite it.
- If a parameter is guessed, label it "bench-fit required" and create a test.

## KiCad Layout Strategy

### P0 Coupon Panel

Keep the first KiCad job simple and manufacturable:

- Three IDE pitches: 150, 200, and 300 um.
- Two replicates per pitch.
- Active area around 8 x 12 mm.
- ENIG finish.
- Ground guard ring around each coupon.
- Back-side ground pour stitched to guard.
- Connector pads at the dry end, sensing area at the wet end.
- One through-glass pad-pair coupon as a stretch test.

Layout risks to control:

- Bare ENIG will drift in ethanol/water, so every real test coupon needs
  passivation except the intentional bare-control coupon.
- Do not route long high-impedance sensor traces across the board.
- Keep wet-end geometry smooth enough to coat and clean.

### P1 Readout Board

Only start this after P0-A/P0-B pass. Put the FDC2214 close to the electrodes:

- FDC2214 or equivalent CDC near the wet-end connector.
- XIAO nRF52840 Sense socket/header for firmware speed.
- I2C pullups sized for the actual bus length.
- NTC divider close to the tip connector.
- Test pads for I2C, power, FDC channels, NTC ADC, and ground.
- Guard/shield net clearly named and separated from noisy digital return.
- Optional battery/charger section only if the clip-on form factor is being
  tested; otherwise power by USB during development.

Bring-up checklist:

- ERC/DRC clean.
- Known-good I2C scan.
- Air/DI/IPA response matches EVM within expected parasitic offset.
- Guard ring hand-wave rejection measured before sealing.
- Coating process recorded with before/after capacitance drift.

## Microcontroller Decision

| Option | Strength | Weakness | Recommendation |
|---|---|---|---|
| XIAO nRF52840 Sense | BLE, compact, onboard LSM6DS3 IMU, low-power wearable path | Less raw compute than Pico 2 W, Arduino/PlatformIO choice needed | Default for P1/P2 |
| Raspberry Pi Pico W | Cheap, MicroPython/C SDK, official Bluetooth support | No onboard IMU, older RP2040, product BLE workflow less integrated | Bench alternative |
| Raspberry Pi Pico 2 W | Faster RP2350, more SRAM, Wi-Fi + Bluetooth 5.2 | No onboard IMU, larger board, more than needed for P1 | Use if Wi-Fi logging or extra compute matters |

Decision rule:

- If the priority is product-like BLE + motion gating, stay with XIAO
  nRF52840 Sense.
- If the priority is bench automation and cheap scripting, use Pico 2 W.
- If both are used, keep the wire protocol and CSV schema identical so the
  estimator does not care which MCU produced the data.

## Firmware Strategy

Firmware should port the validated Python reference, not invent new math.

1. P0 firmware scope
   - None required for first data: TI GUI CSV is acceptable.
   - Optional: XIAO or Pico reads NTC/IMU only, timestamp-aligned to FDC CSV.

2. P1 firmware scope
   - FDC2214 I2C driver, 4-channel continuous read.
   - NTC ADC at 20-50 Hz.
   - IMU at 104 Hz or similar, enough for strike detection.
   - USB serial binary frames during development.
   - BLE UART/NUS stream after USB stream is stable.

3. P1 estimator scope
   - Immersion detection.
   - IMU strike blanking.
   - 1-2 s histogram mode.
   - ABV lookup using coefficients generated by Python.
   - Divergence flag between capacitive estimate and melt model.

4. Firmware acceptance
   - Device and Python replay produce the same ABV from the same captured data
     within numerical tolerance.
   - No unexplained display jumps >1 % ABV after convergence.
   - Every frame includes timestamp, channel values, temperature, IMU class,
     validity flags, and estimator version.

## Experiment Setup

The existing P0 experiment plan is strong. Add these operational details:

### Bench Fixture

- Acrylic or 3D-printed dipstick holder with fixed immersion depth.
- Ring stand and clamp for repeatability.
- FDC2214EVM within 10 cm of the coupon.
- Shielded twisted pair or short coax for sensor leads.
- NTC physically co-located with the active IDE area.
- Salt-ice bath for -8 C calibration points.
- Separate labeled vessels for standards; all samples dumped after testing.

### Data Schema

Each run should log:

- `run_id`
- `timestamp_ms`
- `coupon_id`
- `pitch_um`
- `coating`
- `liquid_label`
- `target_abv_vv`
- `temperature_c`
- `fdc_ch0_raw` ... `fdc_ch3_raw`
- `capacitance_or_frequency`
- `ntc_adc`
- `imu_ax_g`, `imu_ay_g`, `imu_az_g`
- `imu_class`
- `valid_sample`
- `notes`

### Extra Tests To Add

1. Coating before/after test
   - Measure air/DI/IPA before coating and after coating.
   - Decision: coating thickness may reduce sensitivity but must reduce drift.

2. Electrode memory test
   - Alternate high-ABV and DI samples.
   - Decision: checks adsorption, wetting, and slow recovery.

3. Stir-rate matrix
   - Still, gentle stir, realistic stir, abuse stir.
   - Decision: separates physics noise from motion noise.

4. Ice-contact false event test
   - Touch ice directly to passivated coupon at known intervals.
   - Decision: sets IMU blanking and capacitance outlier rules.

5. Vessel parasitic test
   - Same liquid in glass, metal tin, hand-near-glass, wet-glass cases.
   - Decision: validates product scope and through-wall rejection.

## Source-Grounded Facts Checked 2026-07-09

- TI positions FDC2214/FDC2x1x as high-resolution multichannel capacitance to
  digital converters using an LC resonator architecture.
- TI's FDC2214EVM is designed for flexible capacitive sensing prototyping.
- Seeed's XIAO nRF52840 Sense includes BLE and a 6-DOF IMU.
- Raspberry Pi Pico 2 W provides RP2350, Wi-Fi, and Bluetooth 5.2, but not an
  onboard IMU.
- KiCad supports schematic/PCB workflow with integrated SPICE simulation.
- LTspice is a free SPICE simulator with schematic capture and waveform viewer.

Detailed links are in `SOURCE_NOTES.md`.

## Next 10 Work Packages

| ID | Work Package | Owner Mode | Exit Criteria |
|---|---|---|---|
| WP-01 | Order/verify P0 BOM | sourcing | All P0 parts available under budget |
| WP-02 | KiCad coupon panel | CAD | Gerbers pass DRC and fab constraints |
| WP-03 | LTspice NTC model | simulation | ADC sensitivity and tau budget known |
| WP-04 | LC tank sensitivity model | simulation | Frequency shift vs parasitic C table |
| WP-05 | P0-E0 data capture | lab | Pitch/coating selected or killed |
| WP-06 | Calibration standards | lab | 0-60 % ABV grid with run logs |
| WP-07 | Python calibration fit | analysis | Residual plots and coefficients saved |
| WP-08 | Dynamic dilution runs | lab | Mass-balance truth compared to live estimate |
| WP-09 | Firmware skeleton | embedded | Timestamped USB frames from MCU |
| WP-10 | P1 schematic decision | design review | Go/no-go for custom readout PCB |

## Kill Criteria

Kill or pivot the v1 approach if any of these remain true after one iteration:

- Passivated electrodes drift above 0.5 % ABV-equivalent over 4 h.
- Static calibration cannot reach +/-1.0 % ABV residual over the target grid.
- Bubble/ice corruption is not one-sided or not recoverable by mode estimation.
- Required electrode geometry cannot be made cleanable and sealable.
- The value proposition requires sugared/citrus drinks before the binary
  whisky+ice case works.

