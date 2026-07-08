# Estimator spec (v0 — refine against P0 data)

## Inputs
- C_k: burst capacitance samples, effective 1-10 kHz, window 1-2 s
- T_k: NTC temperature (10-50 Hz), lag-compensated (tau_NTC from P0-E1)
- IMU: accel magnitude + spectral features at 50-100 Hz

## Pipeline
1. Gate: IMU state in {stir, still} AND immersion detected
   (C above air threshold). Ice-strike spike -> blank +/-50 ms.
2. Robust level: histogram valid C_k over the window (bin width from
   FDC noise floor, P0-E0); take mode; refine by local quadratic fit
   around modal bin. Report n_valid and occlusion fraction.
3. Map: ABV_cap = F_inv(C_mode, T) from the calibrated eps(T, ABV)
   surface (50_ANALYSIS/calibration_fit.py, 2-D poly, order <= 3x3).
4. Melt model: m_melt = (C_p,drink * m_drink * dT) / h_fus integrated
   from pour conditions -> dilution_thermo -> ABV_thermo.
5. Fuse: weighted combination when |ABV_cap - ABV_thermo| < gate;
   else flag DIVERGENT, display ABV_cap, keep sampling.
6. Track: 1-state Kalman on ABV with process noise tied to melt rate;
   convergence cue when posterior sigma < 0.5 % ABV.

## Failure telemetry to record every window
mode, n_valid, occlusion %, T, dT/dt, IMU class, ABV_cap, ABV_thermo,
divergence flag — this is the dataset that tunes v1.

## Open questions -> protocols
- Bubble residence-time distribution on electrode vs pitch (P0-E3)
- Histogram bin width vs FDC2214 noise floor (P0-E0)
- NTC lag constant + compensation residual (P0-E1)
