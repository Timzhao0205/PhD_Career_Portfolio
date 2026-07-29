# Calibration protocol (standards + surface fit)

## Gravimetric standards (fresh each session)
1. Tare jar on 0.01 g balance. Add m_e grams 190-proof (92.4 % v/v,
   verify bottle), then m_w grams DI to hit target ABV.
2. Compute the EXACT wt% from masses (`abw_from_masses()`), convert
   to % v/v for the label via `abv_from_abw()` (tabulated, handles
   the ~3 % mixing contraction). Never prepare or label standards
   from ideal volume additivity. Prefer parameterizing the surface
   in wt% — it is what the balance gives exactly.
3. Label: ABV, date, time. Cap tightly. Discard after the session.

## Temperature sweep per standard
Seal probe in jar -> salt-ice bath (~-8 degC): log C + T continuously
from 25 degC to below 0 degC (~20-30 min). Stir bath, not sample
(sample sealed). One trace per standard populates the whole T axis.

## Fit + acceptance
`python 50_ANALYSIS/calibration_fit.py --fit data/cal_*.csv`
- Surface: poly order <= 3 in T, <= 3 in ABV; report residual map.
- Accept: max |residual| <= 1.0 % ABV; T-comp residual <= 0.5 % ABV.
- Write coefficients to 10_SENSING_DESIGN/cal_coeffs.json and log the
  fit hash in the run log. Coefficients are versioned, never edited.

## Cross-checks
- Hydrometer on 2 standards at 15.6 degC (Tralle reference temp).
- Refractometer on 3 aliquots, temp-corrected.
- Any disagreement > 1 % ABV between methods -> stop, find out why.
