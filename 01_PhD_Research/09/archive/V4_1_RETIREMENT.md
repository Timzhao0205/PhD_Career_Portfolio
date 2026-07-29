# Why the PowerShell runtime was retired

The previous package is retained only as design history, not executable code.

Observed blockers included:

1. a Windows PowerShell 5.1 parse failure caused by a variable immediately
   followed by a colon in `ACCEPT_STAGE.ps1`;
2. a later strict-mode acceptance failure where `CHECKPOINT.ps1` read a
   `stderr` property that the interactive run record intentionally omitted.

The second failure occurred after the A10 pilot itself completed, so it showed
that research success and orchestration correctness were separate concerns.

This rebuild removes the entire error class: no active `.ps1` files, hooks,
launcher probes, archive expansion commands, code validators, or PowerShell
checkpoint objects are used. Acceptance is performed by explicit file rules
plus a fresh independent Fable/xhigh verifier.
