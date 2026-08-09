# Source de-duplication map

The old Folder 06 content occurred three times:

1. the standalone old Folder 06 attachment;
2. `src/06` inside the recent completed Folder 06 package;
3. `06_Frontier_Idea_Research_2026-07` inside the startup archive.

All 419 files in each repeated tree matched the standalone copy by relative
path and SHA-256 before packaging. They are represented once at
`sources/old06`.

The recent package's outputs, logs, state, audits, prompts, and documentation
remain at `sources/new06`. The startup archive's other research folders remain
at `sources/startup`.

This avoids duplicate counting and saves space without discarding unique
evidence.
