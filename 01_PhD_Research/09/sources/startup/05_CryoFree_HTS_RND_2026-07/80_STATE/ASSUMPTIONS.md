# ASSUMPTIONS (A##-numbered autonomous decisions; append-only)

A01 | Scaffold reuses the 04_* logging hook + metrics analyzer verbatim (proven, format-compatible).
A02 | CF-1 designated flagship on the strength of the validated Rc<->thermal conflict; other CF-* are hypotheses.
A03 | Fable-5 pinned to the three gates (G-PHYS/G-NOVEL/G-CLAIM) as the least-reversible, highest-consequence judgments.

A04 | Autonomous single-command mode added: defaultMode=bypassPermissions scoped to "." with a deny list blocking ../** and rm/curl/ssh/scp; /autorun orchestrator + RUN.sh/RUN.ps1 auto-resume launchers. Default token ceiling 2,000,000 unless overridden.
A05 | /autorun invoked with explicit ceiling 2000000, matching default; RUN_STATE.budget_tokens.ceiling set to 2,000,000, phase advanced to W1_harvest_in_progress at run start.
