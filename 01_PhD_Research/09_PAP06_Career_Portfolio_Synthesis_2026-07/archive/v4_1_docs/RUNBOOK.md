# Interactive runbook

## Runtime architecture

`START.ps1` opens one visible `pap06-controller` session on Fable 5/xhigh with
`bypassPermissions`. It does not run research outside the interface and does
not launch `claude -p`.

For each route item, the controller:

1. asks `NEXT.ps1` for the exact next stage/mode;
2. runs `PREP_STAGE.ps1`, which verifies package/input/source hashes,
   prerequisites, partial state, route model/effort, and target path;
3. invokes the exact fresh named agent:
   `pap06-fable-xhigh` or `pap06-sonnet-high`;
4. waits in the interface while that foreground agent writes and validates;
5. runs `ACCEPT_STAGE.ps1`, which checks the hook record, actual transcript
   model evidence, effort when exposed, schema, and file hashes;
6. creates an immutable pilot/full checkpoint and advances.

Accepted checkpoints are revalidated and skipped in future controller sessions.
Partial attempts are moved under `quarantine`.

## Global order

`ROUTE.json` defines 15 stages. Each stage has two sequential calls:

1. live pilot under `pilot/<stage>`;
2. full run under `outputs/<stage>`.

Operation B is locked on valid full checkpoints for A10, A20, and A30 plus
`state/OP_A_COMPLETE.json`.

## Analysis principles

- Historical provenance and fresh agreement are separate. Agreement never
  proves which model generated a historical file.
- A10 reads only the score-free `blind` pool and selects 24/10 without seeing
  old/new rankings.
- A20 audits old Folder 06 logs/state and prior chat, labeling claims proven,
  inferred, missing, or contradictory.
- A30 unblinds and compares old, new, and blind results, including overlap,
  rank changes, additions/removals, reasons, uncertainty, and current web
  checks.
- B20 calculates PhD→startup and startup→PhD separately; the user's expected
  direction is a hypothesis.
- B12 retains 60–100 screened publications, at least 48 verified peer-reviewed
  core journal papers, and coverage for all four technical streams. It creates
  evidence tables but no final judgment.
- B15 independently adjudicates the literature with Fable 5/xhigh, including
  contradictions, gaps, retraction/correction checks, and applicability.
- B25 analyzes at least 18 specialized converter/power-electronics/power-supply
  directions and maps PhD support, missing skills, safety, certification,
  manufacturing, and bridge experiments.
- B40 ranks exactly 24 combined directions.
- B60 attacks all earlier claims.
- B80 passes only with zero unresolved critical or major issues.

## Final release

B80 builds candidate canonical artifacts. `COMPLETE.ps1` revalidates every
pilot/full checkpoint and source/package hash, builds `outputs/FINAL`, writes
model/performance evidence, seals release hashes, and creates
`state/RUN_COMPLETE.json`.
