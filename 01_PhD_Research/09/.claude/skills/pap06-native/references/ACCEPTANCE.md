# Acceptance rules

Every pilot and full candidate must:

- contain every filename required by `workflow/ROUTE.json`;
- include non-empty `RUN_META.md` and `SELF_CHECK.md`;
- use the exact task target and leave immutable areas unchanged;
- follow the relevant stage specification and scope boundary;
- distinguish direct evidence, inference, uncertainty, and unknowns;
- map material current claims to opened sources;
- contain no fabricated citation, DOI, model observation, count, quote,
  measurement, market fact, or historical provenance claim;
- preserve stable idea IDs and paper IDs;
- disclose inaccessible or contradictory evidence;
- be internally consistent across Markdown, JSON, and CSV artifacts.

Pilot candidates must also:

- use only the deterministic sample defined by the stage;
- exercise all methods and output types that the full stage will require;
- label every artifact `PILOT SAMPLE — NOT FINAL`;
- demonstrate that the full stage can be completed without a structural error.

Full candidates must not contain pilot labels and require an independent
`pap06-verifier` PASS.

Stage-specific counts and controlled values in the stage specification are
hard gates. A plausible narrative cannot compensate for missing rows, wrong
IDs, weak source status, inconsistent counts, or absent required files.

The controller must never accept its own judgment as the full-stage verifier.
