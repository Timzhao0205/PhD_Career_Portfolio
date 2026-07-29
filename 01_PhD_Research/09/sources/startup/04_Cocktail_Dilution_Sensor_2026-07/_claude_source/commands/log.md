---
description: Append a dated entry to NOTES.md (newest-first)
argument-hint: what happened / what was measured / what's next
---
Append a new dated entry to this project's NOTES.md.

Rules:
- Entries are newest-first: insert the new `## YYYY-MM-DD` section
  immediately after the `---` separator near the top of the file.
- If an entry for today already exists, add bullets to that entry
  instead of creating a duplicate heading.
- Rewrite the raw note below into 1-5 tight bullets, preserving every
  number, unit, and part reference exactly as given. No embellishment.
- Touch nothing else in the file, and show the diff.

Raw note: $ARGUMENTS
