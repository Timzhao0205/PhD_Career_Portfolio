# Rebuild and preservation record

## V4.1 rebuild boundary

The active V4.1 launcher and orchestration were rebuilt around Claude Code's
interactive main-agent/named-subagent design. No prior runtime `state`, `logs`,
`pilot`, `outputs`, session transcript, compacted context, or completion marker
is carried into the package.

The reviewed research prompts, strong stage validators, checkpoint/release
rules, literature policy, model route, blind pool, and immutable inputs were
retained because they are specifications/evidence rather than failed runtime
state.

## Preserved material

1. All five current input files, byte-for-byte.
2. Old and new Folder 06 research, PhD/Opt2 work, complete startup corpus, and
   prior chat contained in those inputs.
3. The 126-row score-free blind pool.
4. The V2 outer SHA-256 and all 69 V2 member hashes.
5. The compact inactive V2 reference containing 64 non-input members.
6. The retired V3 START/RUN/CHILD/MODEL_CHECK/session-policy/settings/hook
   files under `legacy/V3_RUNTIME`.

No file beneath `legacy` executes. It is immutable audit evidence.

## Hash hierarchy

- `INPUT_SHA256.json`: five user inputs
- `LEGACY_SHA256.json`: V2 reference and original member ledger
- `PACKAGE_SHA256.json`: active V4.1 runtime, prompts, policies, docs, blind pool,
  and inactive V3 runtime reference
- `state\SOURCE_FILES.json`: every safely expanded source file
- `state\agent_runs`: named-agent transcript identity/performance summaries
- pilot/full checkpoints: every accepted output file hash
- `outputs\FINAL\RELEASE.json`: canonical final release
- `state\RUN_COMPLETE.json`: final completion anchor

This separates immutable evidence, controller code, partial attempts, accepted
work, and the audited final release.
