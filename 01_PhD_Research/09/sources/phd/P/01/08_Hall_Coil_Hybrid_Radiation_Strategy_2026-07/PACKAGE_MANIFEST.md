# Package manifest

## Launchers

- Parent: `..\RUN_HYBRID_RADIATION_ANALYSIS.ps1`
- Mission: `RUN_HYBRID_RADIATION_ANALYSIS.ps1`
- Child process/event flusher: `INVOKE_CLAUDE_CHILD.ps1`
- Live model probe: `TEST_CLAUDE_MODELS.ps1`
- Static/preflight validator: `VALIDATE_PACKAGE.ps1`

## Contracts and policies

- `README_START.md`
- `MISSION.md`
- `AGENTS.md`
- `CLAUDE.md`
- `EXECUTION_PLAN.md`
- `MODEL_POLICY.md`
- `SOURCE_POLICY.md`
- `DECISION_FRAMEWORK.md`
- `CHECKPOINT_PROTOCOL.md`
- `LITERATURE_SEEDS.md`
- `OFFICIAL_SETUP_REFERENCES.md`

## Prompts

Thirteen files under `prompts`: one shared contract and twelve stage prompts.

## Runtime directories

- `evidence`: three source lanes and syntheses.
- `outputs`: decision artifacts.
- `state`: progress, streams/indexes, markers, attempts, checkpoints, logs.
- `logs`: raw run directories and event history.

## Read-only context

- `..\06`
- `..\07_HSX_august2025_results`
- other `01` folders when needed for provenance.

No copy of the large prior evidence is made in folder `08`; the complete
parent package contains it.
