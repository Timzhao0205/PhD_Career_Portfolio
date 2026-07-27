# Stage 40 — application and collaboration prioritization

## Goal

Determine where the hybrid architecture is worth pursuing and whether/when to
approach another group. Do not send outreach.

## Applications

Evaluate at least:

- tokamak long-pulse/plasma magnetic diagnostics;
- stellarator field mapping, alignment/error field, and coil-current/field
  validation;
- z-pinch/pulsed-power current and field measurements;
- magneto-inertial fusion/plasma-jet experiments;
- superconducting magnets, HTS rotating machinery, motors/generators;
- one additional evidence-supported application.

Use Stage 20 and 30 vetoes. An application with no identifiable calibration
path or no advantage over a simpler sensor cannot win on market size alone.

## Candidate groups

For each serious application, identify current candidate research groups or
facilities from official webpages and directly relevant peer-reviewed work.
Include, when evidence supports them, groups around KSTAR/KFE, ITER/JET/DEMO
magnetics, PPPL/tokamak/stellarator, Sandia pulsed power/Z/Mykonos, LANL
plasma-jet/MIF, and relevant HTS/machine programs. Do not add a famous lab
without a specific technical fit.

Assess:

- what unique capability/data/facility the group has;
- what the user can contribute now;
- minimal low-burden collaboration ask;
- evidence/package needed before approach;
- access/probability uncertainty;
- competition, overlap, IP, safety, export-control, or publication risk;
- whether the relationship advances or dilutes the PhD.

No personal/private contact details. No outreach.

## Outputs

1. `outputs\04_APPLICATION_SCORECARD.csv`
   - columns:
     `application,problem,incumbent_diagnostic,hybrid_value,identifiability_path,radiation_fit,experimental_access,publication_value,collaboration_leverage,prototype_cost,thesis_dilution_risk,technical_score,strategic_score,veto,evidence_ids,rank,recommendation,next_gate`
   - show scoring scale/weights in notes or the collaboration document.
2. `outputs\04_COLLABORATION_STRATEGY.md`
   - ranked application recommendation;
   - approach-now / approach-after-bench-proof / monitor / do-not-prioritize;
   - staged outreach prerequisites and a non-sent outline of the scientific
     ask;
   - risks and fallback path.
3. `outputs\04_COLLABORATOR_CANDIDATES.csv`
   - columns:
     `rank,group_or_facility,institution,application,official_url,relevant_publication_ids,unique_capability,proposed_scientific_ask,prerequisites,access_uncertainty,competition_or_ip_risk,phd_fit,recommendation,notes`

## Acceptance

- All user-named application classes receive evidence-based judgments.
- Scores do not override technical vetoes.
- Candidate status is current and linked to official pages.
- Each approach recommendation has a concrete scientific ask and prerequisite.
- No contact or external write occurs.
