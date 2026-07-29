# Stage 70 — Fable adversarial red team and source audit

## Goal

Attempt to disprove the emerging recommendation before final synthesis.
Fable 5 must produce the accepted final main response.

## Attacks

1. **Novelty:** Does direct 2007/2022/2025 prior art already cover the broad
   Hall+coil, drift correction, embedded actuation, or hybrid claim?
2. **Identifiability:** Are any unobservable parameters hidden behind filter
   assumptions or priors? Reproduce at least one rank/confounding check.
3. **Radiation extrapolation:** Are proton, neutron, gamma, temperature, or
   material results improperly combined?
4. **Reference integrity:** Can the coil, integrator, field model, current
   source, dosimeter, or calibration winding degrade in the same environment?
5. **Uncertainty:** Do accuracy claims include calibration/reference
   uncertainty, timing, geometry, cross-axis, and device variation?
6. **Alternatives:** Does a simpler Hall, coil, fluxgate, optical, or other
   system meet the selected use case?
7. **Application reality:** Are field/bandwidth/environment/access
   requirements sourced? Is the proposed group actually current?
8. **Budget/scope:** Could radiation qualification or software expansion
   consume the PhD without a decisive result?
9. **Source integrity:** Are DOI/title/venue/peer-review/access claims valid?
10. **Claims:** Are simulated or inferred results phrased as observed?

Independently inspect primary/publisher records for at least 30 claims/sources,
including every direct hybrid source, every source supporting the chosen
radiation mechanism, and every source supporting the top application.

Correct source records and downstream outputs when the evidence clearly
requires it. Do not hide corrections. If a correction changes the decision,
update all affected artifacts and explain.

## Outputs

1. `outputs\07_RED_TEAM_FINDINGS.md`
   - attack, evidence, severity, disposition, residual risk, and decision
     impact.
2. `outputs\07_SOURCE_AUDIT.csv`
   - at least 30 rows;
   - columns:
     `audit_id,source_id,claim_or_field,verification_url,verification_level,result,issue,severity,correction,downstream_files,reviewer_note`
3. `outputs\07_CORRECTION_LOG.md`
   - every changed claim/source/decision with before, after, reason, evidence,
     and files updated;
   - include “none” explicitly if no correction survives.

## Acceptance

- At least 30 audit rows and all critical direct sources covered.
- At least one serious non-identifiability or prior-art counterargument is
  developed to its strongest form.
- Failures are corrected or remain visible as unresolved blockers.
- Source-count and topic gates still pass after correction.
- No conclusion is protected merely because earlier Fable stages produced it.
