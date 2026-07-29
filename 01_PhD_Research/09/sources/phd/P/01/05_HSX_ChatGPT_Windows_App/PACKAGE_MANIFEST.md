# Package manifest

## Active app workflow

- `PASTE_THIS_PROMPT.txt`: the only prompt the user pastes.
- `RESUME_PROMPT.txt`: recovery prompt after an app/computer restart.
- `AGENTS.md`: durable project contract loaded from the folder.
- `EXECUTION_PLAN.md`: ordered stages, markers, acceptance checks, and resume algorithm.
- `CHECKPOINT_PROTOCOL.md`: durable state plus optional local-Git recovery system.
- `APP_MODEL_POLICY.md`: high-end critical work and truthful downgrade logging.
- `DOCUMENTATION_BASIS.md`: official product-documentation rationale.
- `REBUILD_VALIDATION.md`: clean-tree and recovery-system audit.
- `CHECKSUMS.sha256`: active-control-document integrity hashes.
- `prompts/00_inventory.md` through `prompts/50_synthesis.md`: current engineering tasks.

## Retained information

- `inputs/`: authoritative project/reference/CAD/netlist/image sources.
- `previous_results/`: previously processed engineering data, kept read-only by instruction.

## Writable mission data

- `outputs/`: new engineering deliverables.
- `state/`: checkpoint, status, decision, model, and work logs.
- `logs/`: additional tool/runtime logs when useful.

## Explicitly absent

- PowerShell runners and CLI launchers;
- `.claude`, Claude settings/agents, or `CLAUDE.md`;
- project `.codex/config.toml` or other hidden model configuration;
- legacy kickoff and patch-chain automation.
