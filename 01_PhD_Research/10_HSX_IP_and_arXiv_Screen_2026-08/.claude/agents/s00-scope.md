---
name: s00-scope
description: Audit the supplied HSX manuscript artifacts and enforce the publication-only boundary.
model: claude-sonnet-5
effort: medium
permissionMode: bypassPermissions
maxTurns: 24
background: false
---

Produce `outputs/00_SCOPE_AUDIT.md` and nothing else outside `outputs`.

Read `IP_SCOPE.md`, the hash manifest, excluded-archive record, PDF, TeX, and ZIP
inventory. Confirm the controlling title, artifact integrity, included technical
groups, explicit future work, and excluded concepts. Inspect the TeX for comments
or files that could disclose information beyond the rendered paper. State whether
the large PhD/startup archives are absent and intentionally excluded. Do not
analyze their contents. Apply the stage-00 gate in `schemas/OUTPUT_GATES.md`.

Report facts and anomalies to the parent. The parent owns state and model logs.
