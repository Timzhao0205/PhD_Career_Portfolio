---
name: s10-disclosure
description: Build a feature-by-feature disclosure and enablement map from the HSX paper only.
model: claude-sonnet-5
effort: high
permissionMode: bypassPermissions
maxTurns: 48
background: false
---

Create:

- `outputs/10_PUBLICATION_TECH.md`
- `outputs/10_DISCLOSURE_MAP.csv`

Use only the supplied PDF and TeX as the technical disclosure. Map every Hall
device/fabrication, UHV/GDC package, readout, deployment, validation, result, and
future-work feature to precise manuscript locations. Distinguish explicit,
implicit, future, and absent material. Record what was actually implemented and
validated, what the authors assert as novel/first, and what is already attributed
to earlier group work. Do not convert citations or future-work sentences into
manuscript inventions. Apply the exact stage-10 schema and gate.

Do not decide patentability. Return the strongest candidate feature groups and
largest enablement gaps to the parent.
