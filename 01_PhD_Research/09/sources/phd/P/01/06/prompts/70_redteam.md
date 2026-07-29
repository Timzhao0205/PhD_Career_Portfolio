# Stage 70 — Claude Fable 5 red team and corrections

Act as a skeptical committee comprising a fusion diagnostic instrumentation
reviewer, Hall-sensor/metrology reviewer, PhD-program scheduler,
reproducibility auditor, startup-translation skeptic, and cautious
pre-publication IP reviewer.

This package intentionally keeps the PowerShell route Claude-only. Perform an
adversarial Fable 5 audit that is independent from the earlier reasoning in
method and evidence sampling, while clearly recording that provider-level
independence is not claimed.

Audit all completed outputs. You may patch earlier mission outputs when a
finding is proven, but do not create later final-synthesis files.

Required checks:

- deterministic source-ledger schema/count/duplicate/type checks;
- stratified manual verification of at least 30 source rows across all topic
  groups, years, tiers, and access levels;
- spot-check inline claims against source rows and available evidence;
- novelty overclaiming and unsupported “first” claims;
- manuscript/reviewer coverage completeness;
- experiment feasibility, calibration traceability, statistical units,
  uncertainty, data availability, and hidden cleanroom burden;
- 24-month schedule critical-path realism and missing buffers;
- contradictions among direction, publication, experiment, startup, and IP
  recommendations;
- legal/ownership/patentability overstatement;
- model/effort and checkpoint audit.

Create `outputs/07_SOURCE_AUDIT.csv` with header:

```text
audit_id,source_id,audit_type,field_checked,claimed_value,verified_value,verification_url,result,severity,required_correction,notes
```

Create `outputs/07_RED_TEAM.md` with findings ordered by severity, evidence,
impact, and disposition.

Create `outputs/07_CORRECTION_LOG.md` listing every earlier file changed,
before/after claim summary, reason, and validation. If a material issue cannot
be corrected, convert it into an explicit open gate rather than hiding it.

The stage passes only when there are no unresolved critical defects in the
source count, recommendation logic, or safety/legal wording.

Next stage: `80_synthesis`.
