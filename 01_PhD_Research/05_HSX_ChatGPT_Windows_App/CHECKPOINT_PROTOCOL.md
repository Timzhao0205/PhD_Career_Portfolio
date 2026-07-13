# Checkpoint protocol

## Durable records

- `state/PROJECT_STATE.md`: canonical stage status, current action, next action, blockers, timestamp.
- `state/WORKLOG.md`: short chronological progress entries with files created and checks run.
- `state/DECISION_LOG.md`: design decisions, alternatives rejected, evidence, and reversal trigger.
- `state/MODEL_EFFORT_LOG.md`: actual model/effort by task and any downgrade/control limitation.
- `state/CHECKPOINT_INDEX.md`: checkpoint ID, stage, timestamp, artifact list, validation, Git commit.
- `state/checkpoints/CP_<stage>_<sequence>.md`: self-contained recovery snapshot.

## When to checkpoint

Checkpoint:

1. before the first edit;
2. at stage start and stage completion;
3. after significant web research or source-ledger expansion;
4. after finalizing a pad map, circuit topology, package concept, dimension ledger, or CAD model;
5. before and after red-team corrections;
6. before context compression, a long tool run, or any risky transformation;
7. immediately before the final response.

## Required snapshot contents

Every checkpoint file must state:

- checkpoint ID and UTC/local timestamp;
- current stage and status;
- objective and verified work completed;
- exact files created or changed;
- validation performed and result;
- unresolved blockers/open gates;
- next deterministic action;
- actual model/effort or `MODEL_CONTROL_UNAVAILABLE`;
- Git commit hash if one exists.

Write checkpoints atomically when possible: write a complete temporary file, verify it is nonempty,
then rename it to its final checkpoint name. Update the index only after the snapshot is durable.

## Local Git safety layer

At the first checkpoint, test whether Git is available. If it is:

1. initialize a repository only if this folder is not already in one;
2. set repository-local identity only when needed (`ChatGPT Checkpoint`, local placeholder email);
3. create a baseline commit before changing engineering content;
4. commit after every completed stage with message `checkpoint: <stage> complete`;
5. never push, add a remote, rewrite history, delete branches, or modify files outside this folder.

If Git is absent or a commit fails, record `FILE_CHECKPOINT_ONLY` and continue. Git is redundant
protection, not a prerequisite.

## Recovery test

After each completed stage, pretend chat context is gone. Using only `PROJECT_STATE.md`, the latest
checkpoint, the stage marker, and the index, verify that another agent could identify what was
done, what was checked, and the exact next action. If not, improve the checkpoint before continuing.

