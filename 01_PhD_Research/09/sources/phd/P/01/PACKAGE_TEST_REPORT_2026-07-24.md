# Package test report — 2026-07-24

## Source and restart state

- Source ZIP: `PHD (2)(2).zip`
- Source ZIP SHA-256:
  `035d6cf698c8119846f43c959e110a6581af8faa8b4fa4ad1bc790db7c977363`
- Source ZIP integrity: PASS, 845 entries.
- Active mission state: `READY_TO_START_FROM_BEGINNING`.
- Active progress: 0 of 12 stages complete.
- First active stage: `00_inventory`, global attempt 1.
- Active markers, sessions, attempts, checkpoints, outputs, and evidence:
  empty except for placeholder files.
- The 102 prior runtime files are preserved under `_history\r0` for audit only.
- The prior stage-00 marker remains in that history with SHA-256
  `b1272429d2896003a86d6a013d410dd366f4a264347465db6e502ac031535f12`;
  it is not active completion evidence.
- All publication files, prior-project folders, supplied inputs, and HSX data
  compare byte-for-byte with the uploaded source ZIP: PASS.

## Static, state, and policy validation

- Seven active PowerShell files parsed with the PowerShell tree-sitter grammar:
  PASS, zero syntax errors.
- Windows PowerShell 5.1 validation hotfix: PASS. The two Fable-policy source
  assertions now use PowerShell-native regex escaping (`\(` rather than
  `\\(`). Both assertions match their exact runner/event-logger targets.
- Formerly failing policy/event-logger assertions: 9 of 9 passed.
- Scoped hotfix, clean-state, checksum, routing, runtime-exclusion, and Windows
  extraction checks: 12 of 12 passed.
- Required files, JSON, active JSONL, and active log CSV structure: PASS.
- Every immutable hash in `INPUT_CHECKSUMS.sha256`: PASS.
- Manuscript source and 230-file HSX input tree: PASS.
- Exact 12-stage routing: PASS.
  - Fable 5 / Extra High: 7 critical stages.
  - Sonnet 5 / Extra High: 3 literature-search stages.
  - Sonnet 5 / High: 2 administrative/assembly stages.
- No active Codex, MCP-server, or alternate-provider execution route: PASS.
- User-scoped MCP tools are denied for Claude calls and connection probes:
  PASS.
- Per-event durable flushing and final-result model recording: PASS.
- Clean full-restart state at `00_inventory`: PASS.
- Windows-safe names and path lengths when extracted to `D:\PHD`: PASS;
  longest resulting path is 195 characters.
- Independent package/state/policy checks: 17 of 17 passed.

## Fable final-result policy tests

The built-in `-SelfTest` covers these cases:

1. Sonnet main work plus auxiliary Haiku: allowed and logged.
2. Fable main work plus auxiliary Opus: allowed and logged.
3. Temporary direct Opus work followed by a Fable final response: allowed,
   with Opus recorded as transient.
4. Fable initialization followed by a security-classifier notice and an Opus
   final response: rejected as a Fable final-result failure.
5. First Fable final-result failure: quarantine, regenerated engineering
   prompt, fresh Fable retry with `--safe-mode`.
6. Second Fable final-result failure: durable ChatGPT Windows handoff.
7. A completion marker for a Fable-assigned stage cannot be written unless
   the recorded final result model is Fable.

The launcher waits until an attempt finishes before applying this policy. It
does not stop merely because a temporary or auxiliary non-Fable model appears.

## Expected first run transition

1. The launcher validates the package and parses the active PowerShell files
   with the native Windows PowerShell parser.
2. Small Sonnet 5 and Fable 5 access probes run.
3. `00_inventory` begins as attempt 1 in a fresh Claude session.
4. Each streamed event, model, effort, progress transition, flag, and output
   path is flushed to durable state.
5. Later Fable-assigned stages are accepted only when Fable produces the final
   validated result.

## Runtime boundary

No paid Claude research stage was started while rebuilding this archive.
The one-command launcher performs the live model probes and research run on
the user's Windows machine. The local rebuild validated syntax, structure,
state, routing, hashes, policy wiring, and extraction compatibility.

The user's first Windows launch of the preceding archive completed both live
Claude model probes, then stopped in preflight because two validator regexes
were over-escaped. No research stage ran. This release corrects those validator
expressions without changing the Fable final-result policy or stage routing.
