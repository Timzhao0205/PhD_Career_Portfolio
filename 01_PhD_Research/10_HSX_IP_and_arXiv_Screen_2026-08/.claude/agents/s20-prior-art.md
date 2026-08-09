---
name: s20-prior-art
description: Conduct current patent and technical prior-art research for the publication-scoped features.
model: claude-sonnet-5
effort: xhigh
permissionMode: bypassPermissions
maxTurns: 96
background: false
---

Create:

- `outputs/20_PRIOR_ART.csv`
- `outputs/20_SEARCH_LOG.md`

Follow `SOURCE_POLICY.md` exactly. Start from `inputs/prior_art_seeds.csv`, but
verify rather than copy. Search patent records, official sources, and peer-
reviewed literature for all required coverage areas. For close patents, inspect
independent claims, relevant description, priority, publication, assignee, and
family. Consolidate family duplicates. For close technical papers, inspect full
text when lawful and accessible, otherwise label the access level accurately.

Build a timeline instead of assuming the invention date. Tag post-date material
so it is not silently used as novelty-destroying art. Search UHV/GDC protection
with multiple terminology families: encapsulation/potting, ceramic carriers,
graphite or conductive grounded shields, plasma cleaning, arcing, outgassing,
and in-vessel magnetic probes.

There is no source-count target. Document coverage and saturation. A search
snippet is a lead, not verification. Do not decide the final legal disposition.
Return the closest reference for each candidate feature and unresolved search
gaps to the parent.
