# Patch and recovery playbook

Normal recovery is one command:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume
```

The launcher starts a fresh non-interactive Claude session, but the mission state and all evidence
remain on disk. Claude resumes the first incomplete phase rather than repeating completed waves.

This build's first incomplete phase is P2A. If usage stops during the 12 source-origin batches,
run `-Resume` again; completed batch ledgers remain checkpoints. Do not manually advance state to
P3. P3 is unlocked only after every accepted source has a passing `india_origin_audit`, all source
gates pass, the atlas is repaired, and Fable 5/xhigh writes a P2A PASS.

## Where to diagnose a weak or stopped run

1. `05_STATE/MASTER_STATE.json`: last completed phase, counters, and next action.
2. `05_STATE/PROGRESS_LOG.md`: wave history.
3. `98_RUN_LOGS/LAUNCHER_LOG.md`: versions, configured models, exit codes.
4. Latest `98_RUN_LOGS/claude_*.jsonl`: raw tool/agent transcript.
5. `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`: intended/actual model, effort, retries, downgrade flag.
6. `99_AUDIT/MECHANICAL_AUDIT.md` and `FABLE_ADJUDICATION.md`: exact failures.

## Targeted patch prompt

If repeated resume runs do not repair a specific failure, open Claude Code in this folder with
Fable 5/xhigh and paste:

```text
Read CLAUDE.md, MASTER_STATE.json, the latest mechanical audit, Fable adjudication, and launcher
log. Repair only the numbered unresolved failures. Preserve accepted evidence and completed
analysis. Log model/effort and every changed file. Rerun both validators, then continue the mission
brief's P8 completion protocol. Do not ask questions and do not lower thresholds.
```

## Intentional model changes

Use launcher parameters; do not hand-edit agent files. Example:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume -CriticalModel claude-fable-5 -ScoutModel claude-sonnet-5
```

The launcher rewrites source-agent frontmatter to the requested scout model and records the
override. A critical model other than Fable 5, or critical effort below xhigh, is logged as a
downgrade. No unavailable model is silently replaced.
