# Requirements — v1 (whisky + ice)

R-01 ABV accuracy: ±1.5 % v/v (stretch ±1.0) over 15–50 % ABV,
     −5 to +25 °C liquid, after convergence.
R-02 Dilution accuracy: ±3 % of total volume, same envelope.
R-03 Convergence: valid reading within ≤2 s of cumulative immersed,
     wetted time, WITHOUT requiring the user to stop stirring.
R-04 Live update: ≥2 Hz display rate once converged; monotone melt
     tracking without >1 %-ABV jumps between updates.
R-05 Chaos immunity: meets R-01/R-02 with ≤40 % of burst samples
     corrupted by bubbles, and with ice strikes at ≤2 Hz (IMU-blanked).
R-06 Temperature compensation: residual error from T-comp ≤0.5 % ABV
     across the −5 to +25 °C sweep, including a 20 °C/min transient.
R-07 Drift: ≤0.5 % ABV-equivalent over 4 h continuous wet operation
     (passivation quality gate).
R-08 Wetted-end sealing: survives full immersion to 10 cm and bar-sink
     rinsing (Phase 1+: target IP67 for the probe end).
R-09 Power (Phase 1+): ≥1 shift (6 h) per charge on a coin cell or
     small LiPo; charging without exposed contacts preferred.
R-10 Cleanability: wetted surfaces smooth, no crevices; benchtop units
     are explicitly NOT food-safe (label-and-dump rule).
R-11 Interface: single gesture to zero/tare in neat spirit; LED or
     haptic "converged" cue; BLE stream for logging.
R-12 Cost: Phase-0 kit ≤$400; Phase-1 probe BOM ≤$40 at qty 1.

Out of scope for v1: sugared cocktails (needs 2nd modality), carbonated
drinks (continuous bubble load exceeds R-05 assumption), metal-tin
through-wall sensing.
