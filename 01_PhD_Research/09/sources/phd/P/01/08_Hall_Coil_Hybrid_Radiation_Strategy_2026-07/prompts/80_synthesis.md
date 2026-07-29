# Stage 80 — Fable final synthesis and audit

## Goal

Give the user a concise, direct, evidence-traceable decision package after
applying every red-team correction. Fable 5 must personally read the critical
artifacts and produce the accepted final main response.

## Questions to answer explicitly

1. Is the user's understanding of option 2 correct: Hall validation first,
   hybrid coil second, module/simulation third? What exact refinement or
   reorder is recommended?
2. Can coil output calibrate radiation-induced Hall sensitivity or bias? Can
   Hall output calibrate coil/integrator behavior? Which parts are feasible,
   conditional, or impossible without an external reference?
3. What is the recommended minimum architecture and why?
4. Which application/research-group direction should be prioritized, which
   should wait, and which should not be pursued now?
5. What are the hybrid architecture's decisive limitations and potential
   relative to alternatives?
6. What is the lowest-cost next experiment, its reference, metric, and
   pass/fail decision?
7. What is the balanced budget path, and what evidence triggers higher-cost
   radiation work?
8. What should remain out of the current first-author HSX critical path?

## Outputs

1. `outputs\FINAL_EXECUTIVE_DECISION.md`
   - one-page-style verdict first;
   - evidence-backed answers to all eight questions;
   - recommended claim, architecture, application, collaboration timing,
     budget tier, and kill criteria;
   - confidence and top unknowns;
   - source-ID citations.
2. `outputs\FINAL_PLAIN_LANGUAGE_GUIDE.md`
   - explain the Hall/coil idea, observability problem, radiation caveat, and
     recommended sequence without assuming estimator expertise.
3. `outputs\FINAL_ACTION_PLAN.md`
   - next 2 weeks, 2 months, 6 months, and later conditional work;
   - owner/inputs/output/gate/checkpoint for each action;
   - exact documents/data to bring to an advisor or collaborator.
4. `outputs\FINAL_DELIVERABLE_INDEX.md`
   - every output, purpose, stage/model, status, key dependencies, and reading
     order;
   - link model/effort/performance logs and resume files.
5. `outputs\FINAL_AUDIT.md`
   - requirements trace;
   - source and new-source/topic counts;
   - model/effort integrity summary;
   - performance-log completeness;
   - red-team corrections;
   - file/schema checks;
   - unresolved limitations;
   - the final line must be exactly:

`FINAL STATUS: PASS`

Only use that terminal line if every mandatory gate passes. Otherwise stop
before completing the stage, preserve a checkpoint, and report the exact
failing gate.

## Acceptance

- Direct answers lead each document; process history does not obscure them.
- No new uncited technical fact appears in final synthesis.
- The mutual-calibration verdict matches the formal Stage 20 analysis.
- The research plan matches the limitations, application score, and red team.
- All final ledger gates and output checks pass.
- Fable 5 produces the accepted final main response.
