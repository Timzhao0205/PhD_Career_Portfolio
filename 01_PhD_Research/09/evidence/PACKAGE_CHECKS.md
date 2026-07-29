# Build validation

Status: **PASS**

Validated before distribution:

- every active JSON configuration, route, state file, and blind-pool shard
  parses;
- exactly 15 ordered stages are defined;
- all 15 stages require pilot before full;
- 12 stage types route to Fable 5/xhigh and three bounded support stages route
  to Sonnet 5/high;
- all 15 full stages route to a fresh Fable 5/xhigh verifier;
- controller, skill, workers, verifier, settings, and one-command flags agree;
- 2,344 included source files match their build-time byte sizes and SHA-256;
- all four input ZIPs passed full CRC checks;
- both omitted old-Folder-06 duplicate trees matched 419/419 files by relative
  path and SHA-256;
- the blind pool contains 126 rows with 126 unique IDs;
- there are no active `.ps1`, `.py`, `.js`, `.bat`, `.cmd`, `.sh`, nested
  `.claude`, nested `CLAUDE.md`, nested `AGENTS.md`, or nested `SKILL.md` files;
- Windows-invalid names and case collisions are absent;
- the longest installed path under `C:\AI\PAP06N` is 181 characters;
- the launch command is interactive native Claude Code, not `claude -p` and
  not a PowerShell workflow.

This is build-time validation. Provider availability, live web access, and
organization-side model execution can only be observed at run time and must be
logged honestly.
