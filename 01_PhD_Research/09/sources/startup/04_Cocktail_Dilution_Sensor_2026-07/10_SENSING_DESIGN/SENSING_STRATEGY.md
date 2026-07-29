# Sensing strategy (locked D-001/D-002)

## Problem
Measure ethanol fraction in water-ethanol at rapidly changing
temperature (25 -> -5 degC) with ice chunks, bubbles, splashing, and
a user who will not stop stirring. Whisky+ice is binary to 99.9 %.

## Architecture
1. PRIMARY — fringing-field interdigitated capacitor near the probe
   tip. eps(water) ~78 vs eps(EtOH) ~24 gives a strong monotone
   signal. Sensing depth ~ pitch: fine pitch (150-300 um) makes the
   interrogation volume a thin skin ice cannot occupy and stirring
   shear keeps refreshed.
2. TEMPERATURE — 10k glass-bead NTC co-located at the tip. Two jobs:
   (a) compensate the ~-0.37 %/degC water permittivity tempco via the
   2-D calibration surface; (b) drive the thermodynamic melt model
   (all chilling comes from 334 J/g ice melt -> dT maps to meltwater
   mass) as an independent dilution estimate.
3. MOTION — IMU classifies smooth stir (valid), ice strike (blank
   50 ms), out-of-glass (invalid). Converts "please pause" into
   "measure during stirring".
4. ESTIMATOR — burst sampling (1-2 s windows), histogram, take the
   mode: bubble outliers are ONE-SIDED (eps -> 1) so mode is unbiased
   where mean/median are not. Fuse capacitive ABV with the melt-model
   dilution; divergence raises a flag instead of silently averaging.
5. SPATIAL REDUNDANCY (Phase 1+) — 3-4 electrode patches along the
   shaft, consensus voting + free immersion-depth detection. Bottom
   of vessel preferred: ice floats, bubbles rise.

## Explicit rejections (v1)
- Ultrasonic ToF: sound speed vs ABV peaks near 20 wt% (ambiguous).
- RI: solid physics, bubble-immune (1 um skin) — kept as the second
  modality for v2 sugar handling.
- Tuning-fork density: fouling + miniaturization.
- Through-tin sensing: grounded metal wall kills the field.
