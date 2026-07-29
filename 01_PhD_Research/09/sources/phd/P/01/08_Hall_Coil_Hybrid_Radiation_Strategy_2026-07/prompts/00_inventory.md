# Stage 00 — inventory, hypothesis, and requirements trace

## Goal

Reconstruct exactly what the user is asking, what option 2 in folder `06`
actually proposed, and which prior conclusions or scope rules constrain this
new analysis.

## Work

Inspect:

- all policies and prompts in this mission;
- folder `06` final strategy, action plan, research-direction decision,
  literature review, source coverage, roadmap, red team, and final audit;
- folder `06` CLAUDE/mission scope;
- folder `07` at file/inventory level, opening only the most relevant context;
- parent launchers and root instructions for conflicts.

Do not modify any inspected sibling file.

Explicitly test the user's interpretation:

1. Hall sensor/device validation and metrology first.
2. Hybridization with an inductive coil second.
3. Reusable module and simulation package third.

Record whether folder `06` stated that sequence, merely implied it, or left it
ambiguous. Separate reconstruction from the new recommendation, which later
stages will make.

Identify every requirement in the current user request:

- additional hybrid literature;
- radiation sensitivity/bias/compensation;
- bidirectional calibration hypothesis;
- application/group strategy;
- limitations and comparison;
- accuracy/budget;
- model/effort routing;
- performance logs;
- two-strike Fable behavior;
- checkpoints, run/resume, and full package.

## Outputs

1. `outputs\00_INPUT_INVENTORY.md`
   - inspected paths and purpose;
   - option-2 reconstruction with quotations kept short;
   - existing evidence and missing evidence;
   - read-only/write boundary;
   - scope caveat: no claim of radiation testing.
2. `outputs\00_REQUIREMENTS_TRACE.csv`
   - columns:
     `requirement_id,user_requirement,interpretation,stage,deliverable,acceptance_test,status,notes`
   - one or more rows for every requirement above.
3. `outputs\00_CONFLICT_LEDGER.md`
   - conflicts among root instructions, folder `06`, current request, source
     policies, and practical constraints;
   - resolution and rationale for each.

## Acceptance

- No sibling file changed.
- The option-2 interpretation is classified as confirmed, partly confirmed,
  or not confirmed, with file evidence.
- All current requirements trace to a later output and objective test.
- No new technical conclusion is asserted without labeling it preliminary.
