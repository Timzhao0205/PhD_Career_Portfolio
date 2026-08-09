---
name: s70-final
description: Produce the accepted Fable 5 executive decision, OTL brief, and model audit.
model: fable
effort: xhigh
permissionMode: bypassPermissions
maxTurns: 88
background: false
---

Create:

- `outputs/70_FINAL_OTL_BRIEF.md`
- `outputs/70_EXEC_SUMMARY.md`
- `outputs/70_MODEL_REPORT.md`

Synthesize all accepted stages and verified evidence. Resolve conflicts rather
than averaging them. Lead the final brief with exactly one decision label from
the stage-70 gate and a one-paragraph rationale. Directly answer:

1. Can the disclosed AlGaN/GaN Hall sensor itself plausibly be patented now?
2. Does using it as a stellarator/fusion magnetic diagnostic support a meaningful
   new-use case?
3. Is the epoxy/bake/ceramic/grounded-graphite UHV/GDC module worth OTL review or
   likely too routine/thin?

Rank concepts as strong, conditional, weak, or excluded. Give 48-hour and
one-week actions, an evidence request list, inventorship/sponsor questions, and
the exact arXiv hold/release condition. Separate patentability triage from FTO,
ownership, and filing decisions. Use citations near claims and state search
limitations.

The model report must reconcile `MODEL_PLAN.md`, `state/MODEL_LOG.csv`, debug or
status evidence, and every fallback event. Do not upgrade requested configuration
into observed fact. Apply all final gates. This accepted synthesis must be
substantively authored by Fable 5/xhigh.
