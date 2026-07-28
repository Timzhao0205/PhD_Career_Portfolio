# Build validation

Build date: 2026-07-27

## Imported data

- Uploaded package SHA-256 verified:
  `9846F5E2B06804690A74A0F57313109B62B7E3ECE0E5238755F7084D1FB578AA`.
- `src\06` contains exactly 419 files.
- All 419 files match `SOURCE_SHA256.json`.
- Frozen counts independently verified:
  - 126 raw ideas / 126 unique IDs;
  - 65 longlist ideas / 65 unique IDs;
  - 1,289 source rows / 1,289 unique IDs / 1,182 accepted;
  - historical completed 24/10 selection and ten deep dives.
- The uploaded package contained no completed top-level rerun output, state, or
  logs to import.

## Fresh implementation

The active scripts, hooks, settings, route, and prompts were rebuilt. The
previous stream-JSON parser, exact text sentinel, stage child launcher, budget
flags, turn caps, and non-persistent sessions are not used.

## Offline tests completed in the build workspace

- Parsed all new JSON configuration and fixture files.
- Verified all frozen source hashes and counts.
- Built deterministic fixtures for every pilot and full stage.
- Verified fixture cardinalities and cross-stage identities:
  65 → 30 → 24 → 10.
- Verified source-pack 20/7/5 quotas.
- Verified ten deep-dive fixtures and actual word counts.
- Verified final 24-row CSV and final PASS audit fixture.
- Checked balanced strings, parentheses, brackets, and braces in every active
  PowerShell script.
- Scanned active launch paths for package-defined monetary, turn, and
  no-persistence flags; none are present.
- Maximum static relative path is 75 characters. Extraction to `C:\AI\F06I`
  leaves substantial Windows path headroom.

## Runtime gates

This build environment is not Windows and cannot execute the user's exact
Windows PowerShell binary or authenticated Claude account. Therefore the
package deliberately performs these gates locally on the user's machine before
the first model call:

1. exact Windows PowerShell 5.1.26100.8875 / Desktop / build / CLR check;
2. native PS5.1 parser check for every active script;
3. package and source SHA-256 verification;
4. all eight stage/pilot fixtures through `VALIDATE.ps1`;
5. SessionStart, status, event, Stop-guard, first-retry, and second-pause hook
   fixtures;
6. Claude Code presence and version display;
7. actual interactive SessionStart model capture and live status effort/
   performance logging.

Claude is not launched if any offline/runtime prerequisite fails. Live research
cannot be pre-executed without the user's Claude authentication and usage
allocation; it is the intended work performed after the one-command gates.

