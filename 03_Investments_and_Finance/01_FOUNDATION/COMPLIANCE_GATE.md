# COMPLIANCE_GATE.md — must pass before any real-money action

> Purpose: turn legal/tax unknowns into a checklist. Items marked ⚠️ are hard gates.
> This file states issues to resolve, not legal advice — confirm §1–§2 outcomes with a
> qualified professional (Stanford's international student tax resources / Bechtel
> International Center are the cheap first stop).

## §0. Scope — what is and isn't restricted (owner declaration 2026-07-05)

Research, reading filings, price tracking, prediction journaling, and paper/simulated
trading are **not** regulated transactions: they are lawful for any name, including
sanctioned issuers. The rules below attach to *real* purchases and sales of securities
— and of derivatives or funds *designed to provide exposure* to a listed name, so an
ETF or swap is not a workaround. Sanctions liability is strict: "learning intent" is
not a defense once real money moves. Bright line: **paper = unrestricted; real = this
gate, in full, every time.** Separately, the owner has declared sanctioned issuers
permanently no-buy regardless of gate outcomes; they remain in the research universe
as study-only names.

## §1. Determine my US tax status (do once, re-check each January)

- [ ] Am I a **US citizen or green-card holder**? If yes → resident; skip to §2.
- [ ] If on F-1: count "exempt individual" years (typically first 5 calendar years on
      F/J student status — undergrad years count) and then apply the substantial
      presence test. Outcome: **resident alien** or **nonresident alien (NRA)** for tax.
      My status: `[FILL]` — verified with: `[FILL: advisor/tool, date]`.
- [ ] Consequences to confirm for my status: correct broker tax form (**W-9** for
      resident vs **W-8BEN** for NRA), dividend withholding and any treaty rate,
      capital-gains treatment, correct return (1040 vs 1040-NR), state (CA) treatment.
- [ ] Roth IRA eligibility & whether stipend/fellowship income counts as compensation
      for my situation: `[FILL]`.

## §2. ⚠️ OFAC NS-CMIC screen (applies to persons IN the US, regardless of citizenship)

Executive Orders 13959/14032 prohibit "US persons" — a term that includes anyone
physically in the United States — from purchasing or selling publicly traded securities
(and derivatives/ETFs designed to give exposure) of companies on Treasury's **NS-CMIC
list**. Penalties are strict-liability. Therefore:

- [ ] Locate the current NS-CMIC list on the OFAC/Treasury sanctions site
      (ofac.treasury.gov → sanctions lists → NS-CMIC). Save a dated copy to
      `90_SOURCES/inbox/`.
- [ ] **Screen every ticker** on WATCHLIST.md against it before status can be
      `actionable`. Record `pass/FAIL + date` in the watchlist compliance column.
- [ ] Known flag from the 2026-07-05 session: **SMIC (中芯国际, 688981.SH / 0981.HK)
      has been on this list for years — treat as prohibited unless a fresh dated check
      shows otherwise.** Telecom operators (China Mobile etc.) have also appeared
      historically; check before touching any state-linked name.
- [ ] Note: the Commerce **Entity List** (export controls, where Huawei itself sits)
      does NOT itself bar owning securities — do not confuse the two lists; only the
      OFAC list is the investment gate.
- [ ] Treasury's Outbound Investment Security Program (31 CFR 850, in force since
      Jan 2025) targets certain US-person investments in Chinese semiconductor/AI
      entities; publicly traded securities have had exceptions — verify current scope
      before any non-listed/PE-style investment. Date checked: `[FILL]`.

## §3. Market access mechanics

- [ ] Which of my available brokers offer **Shanghai/Shenzhen Stock Connect** A-share
      trading to my account type? (IBKR historically does; availability varies by
      residency/account.) Broker chosen: `[FILL]`. Note eligible boards — STAR Market
      (688xxx) access via Connect has extra eligibility rules; confirm per ticker.
- [ ] Alternative exposure routes if a ticker is inaccessible: H-share twin, or a
      China-tech ETF — but ⚠️ for **NRA/PFIC** reasons, if I am a US tax resident,
      non-US-domiciled funds can trigger punitive PFIC taxation; if NRA, US-domiciled
      funds have estate-tax quirks. Resolve per §1 status: `[FILL]`.
- [ ] FX: funding CNH/HKD trades, conversion costs, and repatriation path understood.

## §4. Per-ticker gate (copy into each thesis)

| Check | Result | Date |
|---|---|---|
| OFAC NS-CMIC screen (incl. subsidiaries/aliases) | | |
| Other sanctions/EO exposure noted in filings | | |
| Broker can actually execute (board + Connect eligibility) | | |
| Tax form/withholding implications understood | | |

## §5. Visa-conduct note

Passive investing is generally uncontroversial on a student visa; a pattern of
high-frequency trading that resembles running a business is a gray zone worth avoiding
on prudence grounds alone — which the IPS already forbids for financial reasons.
