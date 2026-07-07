# AI_PLAYBOOK — using Claude / ChatGPT in this lab

Core stance: LLMs are a **reasoning and language layer**, not a data source and not an
oracle. They excel at explaining, translating, structuring, and attacking your arguments.
They confidently fabricate numbers, tickers, and citations. Design every workflow so a
hallucinated number cannot survive into a file (see NUMBER TRUTH RULE in CLAUDE.md).

## Good roles (use daily)

1. **Tutor** — concepts on demand, pitched at your background.
2. **Translator** — zh↔en for A-share filings and Chinese financial media; ask it to keep
   figures verbatim and flag ambiguous accounting terms (e.g., 归母净利润, 扣非).
3. **Filing summarizer** — paste filing text IN, get structure out. Never ask it to recall
   a filing from memory.
4. **Red team** — strongest bear case against your thesis; the single highest-value use.
5. **Rumor tracer** — given a claim, have it design the verification plan (candidate
   primary sources + zh/en search queries), then YOU or a web-search-enabled session runs it.
6. **Coder** — screeners, fetch scripts, calibration math (Claude Code missions M1–M4).

## Bad roles (never)

- "What stock should I buy?" — outsources the only skill you're here to build, and the
  answer is untrustworthy anyway.
- Price prediction / forecasting.
- Any number recalled from model memory used as fact.
- Sole source for anything in `10_RESEARCH/` — AI-assisted conclusions get an `[AI]` tag
  in the journal and still need [S###] cites.

## Mechanics

- Use web-search-enabled modes for anything current; ask for URLs; log keepers into
  `90_SOURCES/sources.json` yourself.
- Cross-model check: run load-bearing reasoning past both Claude and ChatGPT; divergence
  = cheap red flag.
- claude.ai: make a Project for this lab and pin `CLAUDE.md` + `SOURCE_STANDARDS.md` as
  project knowledge so every chat inherits the rules. Claude Code (later) reads
  `CLAUDE.md` automatically when run in this folder —
  https://docs.claude.com/en/docs/claude-code/overview

## Copy-paste prompts

**Tutor.** "Explain [EV/EBITDA] to an EE PhD with zero finance background: give the
formula, a systems/circuits analogy, when analysts use it over P/E, and two failure modes
where it misleads. ≤300 words."

**Filing extraction.** "Below is a pasted section of [company]'s FY2025 annual report.
Extract into a table: revenue by segment, YoY %, gross margin, top-5 customer
concentration, capex. Rules: use ONLY numbers present in the pasted text; if a field is
absent write MISSING; quote the exact sentence for customer concentration."

**Red team.** "Here is my draft thesis: [paste]. Write the strongest bear case in 5
bullets, then list 5 falsifiable checks (each: observable event + date + which side it
supports). Do not soften the attack."

**Rumor tracer.** "Claim: [paste rumor]. List, in order of authority, the primary sources
that could confirm or kill it (specific documents, not outlets). Then draft 3 Chinese and
3 English search queries I can run. Do not tell me whether the claim is true."

**Translation.** "Translate this A-share filing excerpt to English. Keep all figures and
units exactly as written; render accounting terms as [zh term] (English gloss); flag any
sentence whose meaning you're <90% sure of."

**Weekly review coach.** "Here are this week's journal notes and prediction outcomes:
[paste]. Draft my weekly review per the template, then ask me the one question I'm most
likely avoiding."
