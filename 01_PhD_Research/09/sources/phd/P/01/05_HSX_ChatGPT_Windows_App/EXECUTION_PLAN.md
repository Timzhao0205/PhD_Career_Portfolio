# Resumable execution plan

Run stages in order. A marker is not valid merely because it exists: open it and verify the listed
acceptance condition. Detailed task instructions live in the corresponding file under `prompts/`.

| Stage | Prompt | Required marker | Acceptance condition |
|---|---|---|---|
| 00 inventory | `prompts/00_inventory.md` | `outputs/00_INVENTORY_AND_GAP_MAP.md` | constraints, retained evidence, conflicts, and missing inputs mapped |
| 05 sources | `prompts/05_sources.md` | `outputs/05_EVIDENCE_AND_CLAIM_MATRIX.md` | direct primary-source ledger and claim limitations recorded |
| 10 wirebond | `prompts/10_wirebond.md` | `outputs/10_LCC_WIREBOND_AND_EXTERNAL_JOIN.md` | pad/orientation gates, alternatives, recommended join, drawings, and qualification CSV |
| 20 boards | `prompts/20_boards.md` | `outputs/20_THREE_BOARD_READOUT_ARCHITECTURE.md` | all 12 sensor conductors, control/data flow, grounding, drawings, and pin map resolved |
| 30 package | `prompts/30_package.md` | `outputs/30_REUSABLE_3D_PACKAGE_250C_UHV.md` | three thread-free concepts, envelope/collision math, reuse, drawings, and cost drivers |
| 40 red team | `prompts/40_redteam.md` | `outputs/40_INDEPENDENT_RED_TEAM.md` | independent BLOCKER/MAJOR audit and requirements trace completed |
| 50 synthesis | `prompts/50_synthesis.md` | `outputs/FINAL_RECOMMENDATION_250C_UHV.md` | all three questions answered consistently and final checklist/index written |

## Start and resume algorithm

1. Read `state/PROJECT_STATE.md` and `state/CHECKPOINT_INDEX.md`.
2. Inspect markers in order; treat a missing, empty, obviously truncated, or acceptance-failing
   marker as incomplete.
3. Reconcile state against actual files. Files are authoritative; document any correction.
4. Resume the earliest incomplete stage. Reuse valid prior artifacts and research.
5. Before a stage, mark it `IN_PROGRESS` and checkpoint.
6. Execute its prompt completely, validate every required artifact, then mark it `COMPLETE`.
7. Save stage checkpoint and continue without requesting user confirmation.
8. After synthesis, run a whole-package consistency audit, save the final checkpoint, and provide
   the user a concise completion report.

## Failure behavior

- Retry a transient web/tool failure with a safe alternative or source mirror.
- If a source cannot be reached, record the limitation and continue unless it blocks fabrication.
- If an artifact tool is unavailable, create the most precise supported SVG/table/parametric source
  possible and record the unperformed validation as an open gate.
- If context becomes large, checkpoint immediately, update state, and continue from the saved
  files. Never depend on chat memory to resume.
- Stop and ask the user only for an irreducible, design-changing input or permission outside this
  folder. Record the exact blocker first.

