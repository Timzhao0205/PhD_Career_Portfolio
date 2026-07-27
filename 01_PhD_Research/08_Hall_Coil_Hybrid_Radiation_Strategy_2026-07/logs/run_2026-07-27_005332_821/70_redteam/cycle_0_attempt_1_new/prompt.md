# Shared research contract

You are executing one stage of the Hall + inductive-coil hybrid/radiation
strategy. Work autonomously until every acceptance gate in the current stage
is satisfied or a real blocker is documented.

## Read before work

Read `AGENTS.md`, `CLAUDE.md`, `MISSION.md`, `SOURCE_POLICY.md`,
`DECISION_FRAMEWORK.md`, `CHECKPOINT_PROTOCOL.md`, and
`LITERATURE_SEEDS.md`. Inspect `state\PROJECT_STATE.md`, `state\WORKLOG.md`,
the current attempt state, and existing stage files before deciding whether to
resume or start.

Folder `06` and all siblings are read-only context. Write only inside this
folder. Do not edit the runner, validator, policy files, model logs,
completion markers, or rejected-attempt archives.

## Method

1. Convert the current stage requirements into a private checklist.
2. Reuse valid checkpointed work; do not repeat completed searches.
3. Use web search/fetch for current, primary, and publisher verification.
4. Verify rather than infer citation metadata. Search snippets are discovery,
   not full-text evidence.
5. Track claims as observed, derived, inferred, proposed, or unknown.
6. Record counterevidence, assumptions, conflicts, and access limitations.
7. Use equations, units, conditions, and uncertainty where relevant.
8. Never equate different radiation species/spectra or simulate unobserved
   experimental results.
9. Never make a novelty claim without direct prior-art analysis.
10. Check every required output before returning.

You may use local analysis scripts for calculations and CSV checks, but leave
only reusable scripts that materially help future work. Do not manufacture
data. Do not contact groups or change external resources.

## Source IDs and traceability

Use stable source IDs. Technical claims in narrative outputs cite one or more
IDs from the lane/final ledgers. If a statement is your inference or proposal,
label it and cite the premises. If evidence is insufficient, say unknown.

The exact ledger header is:

`source_id,citation,title,authors,year,venue,doi,url,source_type,peer_review_status,quality_tier,topic_tags,claims_supported,verification_basis,access_level,notes`

Do not count preprints, patents, theses, standards, books, talks, vendor pages,
or webpages as verified peer-reviewed rows.

## Checkpoint and closeout

After each major milestone, update `state\PROJECT_STATE.md`, append a dated
entry to `state\WORKLOG.md`, and create a concise
`state\checkpoints\CP_<stage>_<timestamp>.md`. Include counts and exact next
action.

Before the final main response:

- confirm all named outputs exist and are nontrivial;
- parse all CSV files;
- verify required headers/counts;
- inspect for duplicate DOI/title and unsupported claims;
- state unresolved limitations honestly.

The final main response must be produced by the stage's assigned model and
briefly report files, gates, corrections, and remaining uncertainty.


===== CURRENT STAGE =====

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

