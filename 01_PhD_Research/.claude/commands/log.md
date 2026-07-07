---
description: Append a dated entry to the active project's NOTES.md
argument-hint: what happened / what was measured / what's next
---
Append a new dated entry to the NOTES.md of the project currently being
worked on (02_HSX_Hall_Sensor_Readout or 03_HSX_Vector_Probe_RSI2026 —
infer from context, ask only if genuinely ambiguous).

Rules:
- Entries are newest-first: insert the new `## YYYY-MM-DD` section
  immediately after the `---` separator near the top of the file.
- If an entry for today already exists, add bullets to that entry
  instead of creating a duplicate heading.
- Rewrite the raw note below into 1–5 tight bullets, preserving every
  number, unit, and part reference exactly as given. No embellishment.
- Touch nothing else in the file, and show the diff.

Raw note: $ARGUMENTS
