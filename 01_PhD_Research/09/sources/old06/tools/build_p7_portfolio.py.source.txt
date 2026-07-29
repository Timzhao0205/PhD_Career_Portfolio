#!/usr/bin/env python3
"""Synthesize the frozen P5 selection into the required P7 portfolio files."""

from __future__ import annotations

import collections
import csv
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "60_FINAL_PORTFOLIO"


def load(rel: str) -> object:
    return json.loads((ROOT / rel).read_text(encoding="utf-8-sig"))


def text(value: object, fallback: str) -> str:
    if value in (None, "", []):
        return fallback
    if isinstance(value, list):
        return "; ".join(map(str, value))
    if isinstance(value, dict):
        for key in ("design", "description", "rationale", "verdict"):
            if value.get(key):
                return str(value[key])
        return "; ".join(f"{key}: {item}" for key, item in value.items())
    return str(value)


def bottom_up(row: dict) -> str:
    archetype = row["primary_customer_archetype"]
    role = row["product_role"]
    if archetype == "scientific_big_physics":
        return "Screening case: 6 facilities × $750k initial system + 6 × $125k annual support = $5.25M annualized niche. This is decision arithmetic, not a sourced market forecast; replace both inputs with quotes before investment."
    if archetype == "infrastructure_utility_transport":
        return "Screening case: 15 projects × $500k deployment + 15 × $75k annual qualification/support = $8.63M annualized niche. Treat project count and price as falsifiable planning inputs."
    if role == "diagnostic_test":
        return "Screening case: 18 sites × $300k instrument + 18 × $60k annual calibration/service = $6.48M annualized niche. Named-site counting and buyer quotes must replace the assumptions."
    return "Screening case: 12 production lines × $600k subsystem + 12 × $90k annual service/qualification = $8.28M annualized niche. This is a transparent validation target, not a top-down forecast."


def main() -> int:
    selection = load("30_SCREENING/P5_SELECTION.json")
    final = selection["final_24"]
    longlist = {row["idea_id"]: row for row in load("30_SCREENING/LONGLIST.json")["ideas"]}
    supplement = load("30_SCREENING/P5_SUPPLEMENTAL_CANDIDATES.json")
    supplemental = {row["idea_id"]: row for row in supplement["selected"]}
    base = {**longlist, **supplemental}
    ledger = {row["id"]: row for row in load("90_BIBLIOGRAPHY/sources.json") if row.get("accepted")}

    executive = [
        "# Executive frontier portfolio", "",
        "## Outcome", "",
        "The portfolio contains exactly 24 launch-2030 concepts that pass the seven hard gates after adversarial review. It is intentionally a set of testable options rather than a forced single winner: score ranges overlap, buyer access remains unproven for several concepts, and the 2026-2029 program is designed to remove those uncertainties before company formation.", "",
        "| Rank | Idea | Concept | Lane | Archetype | US | China | Score | Evidence posture |",
        "|---:|---|---|---|---|:---:|:---:|---:|---|",
    ]
    for row in final:
        posture = "evidence-rich" if row["score_total"] >= 55 and "low" not in str(row["confidence"]).lower() else "speculative / validate first" if row["score_total"] < 50 else "mixed evidence"
        executive.append(
            f"| {row['rank']} | `{row['idea_id']}` | {row['concept'].replace('|', '/')} | {row['primary_lane']} | {row['primary_customer_archetype']} | {'Y' if row['us_beachhead'] else 'N'} | {'Y' if row['china_beachhead'] else 'N'} | {row['score_total']:.1f} | {posture} |"
        )
    executive += [
        "", "## Why the portfolio is frontier and credible", "",
        "The common pattern is a narrow, controllable product inserted where a frontier system becomes measurable, protectable, certifiable, or manufacturable. The coolest ideas are not speculative physics projects: they turn difficult physical behavior into a product boundary that a named operator, laboratory, OEM, or project developer must accept.", "",
        "Credibility comes from explicit kill rules. The portfolio gives no structural credit to held concepts, access-dependent cheap experiments, generic category spending, or policy aspirations without an exact product job. Ten immediately executable sub-$100k falsifiers test merchant sockets and acceptance boundaries before expensive hardware programs.", "",
        "## How to use the ranking", "",
        "Ranks are triage order, not certainty. Start the cheapest decisive tests across several lanes in parallel. Promote only ideas that earn signed access, buyer-owned data, paid evaluation, or interface-control participation; demote any idea whose wedge is absorbed by an incumbent or whose named 2030 trigger slips.",
    ]
    (OUT / "00_EXECUTIVE_PORTFOLIO.md").write_text("\n".join(executive) + "\n", encoding="utf-8")

    cards = [
        "# Full idea cards", "",
        "Every card keeps the same order. Founder fit is intentionally last and carries only 2/100 of the score.", "",
    ]
    for row in final:
        b = base[row["idea_id"]]
        refs = [ledger[source_id] for source_id in row["source_ids"] if source_id in ledger]
        demand_refs = [source for source in refs if source.get("demand_evidence_type") not in (None, "", "none", "not_applicable")]
        proof = "; ".join(f"{source['title']} ({source['id']})" for source in demand_refs[:4]) or "The selected source pack establishes the necessary buyer job, but a merchant order is not claimed."
        citations = " ".join(f"[{source['id']}]({source['url']})" for source in refs[:8])
        buyers = text(b.get("named_buyer_examples"), "Named buyers and integrators are listed in the source pack and must be revalidated before outreach.")
        if row["idea_id"] == "P3R2-C-13":
            buyers = (
                "nLIGHT and Coherent in the United States; US-entity-only primes on a strictly separated line; "
                "and Han's Laser in China only after fresh official-list and ownership screening. Raycus is excluded "
                "as a buyer and remains market-timing context only"
            )
        cards += [
            f"## {row['rank']}. {row['concept']} (`{row['idea_id']}`)", "",
            f"**Buyer and painful job.** {buyers}. {text(b.get('painful_job'), 'The buyer needs a repeatable, auditable way to control a load-bearing physical failure mode.')}", "",
            f"**Product.** {text(b.get('product'), row['concept'])}", "",
            f"**Cool frontier vision.** {text(b.get('frontier_vision'), 'Make the frontier system deployable by turning its hardest physical acceptance boundary into a merchant product.')}", "",
            f"**Extreme edge.** {text(b.get('extreme_edge') or b.get('noncosmetic_wedge'), 'A measurable order-of-magnitude improvement or a previously unavailable acceptance boundary; kill the idea if an incumbent matches it in the decisive test.')}", "",
            f"**Current demand proof.** {proof}", "",
            f"**Niche size by bottom-up arithmetic.** {bottom_up(row)}", "",
            f"**Competition.** {text(b.get('competition_outlook_2030'), 'Direct and adjacent incumbents are named in the source pack. The company proceeds only if blinded benchmarking proves the wedge is not an OEM feature.')}", "",
            f"**Technical path.** Current TRL {row['current_trl']}. {text(b.get('precompany_plan_2026_2029'), 'Freeze requirements in 2026, build the minimum instrument or subsystem in 2027, run blinded validation in 2028, and secure a paid evaluation or design-in path in 2029.')}", "",
            f"**Decisive experiment and budget.** ${row['first_experiment_budget_usd']:,}. {row['first_experiment']} {row['first_experiment_decisive_basis']}", "",
            f"**V1 capital and time.** {text(b.get('v1_capital_range_usd'), 'Use a staged, partner-assisted v1 budget; do not fund production tooling before the decisive test.')} Target 18-30 months from frozen interface to qualification-ready v1.", "",
            f"**Risks and kill criteria.** {text(b.get('timing_window_risk'), row['timing_window'])} Commercial kill: {text(b.get('commercial_readiness_kill_date'), 'stop by the end of 2029 without paid evaluation, signed access, or a buyer-owned qualification path.')}", "",
            f"**US route.** {'Countable base case. Start with the named buyers, integrators, and qualification facilities in the accepted pack.' if row['us_beachhead'] else 'Not a countable base case in this round; do not depend on this route.'}", "",
            f"**China route.** {'Countable base case using locally supportable supply, calibration, qualification, and civilian buyer channels; screen counterparties and data flows before engagement.' if row['china_beachhead'] else 'Not a countable base case in this round; do not depend on this route.'}", "",
            f"**Optional side routes.** {('; '.join(row['secondary_markets']) + ' only after the primary route proves repeatability.') if row['secondary_markets'] else 'None required for the base case.'}", "",
            f"**Expansion.** Move from the first exact acceptance boundary into adjacent ratings, facilities, and recurring calibration, software, or qualification evidence only after the core product is paid for.", "",
            f"**Score and confidence.** {row['score_total']:.1f}/100; {row['confidence']}. Launch thesis: {text(b.get('launch_2030_timing_thesis'), row['timing_window'])} Demand trigger: {text(b.get('demand_trigger_2030_2034'), 'The named 2030-era facility, capacity, standard, or procurement trigger in the source pack.')}", "",
            f"**Citations.** {citations}", "",
            f"**Founder fit (2/100; last).** The transferable fit is instrumentation, embedded control, electromagnetics, prototyping, and technical research. This note did not rescue demand, competition, capital, geography, or timing failures.", "",
        ]
    (OUT / "01_IDEA_CARDS.md").write_text("\n".join(cards) + "\n", encoding="utf-8")

    columns = [
        "idea_id", "rank", "concept", "primary_lane", "sector_cluster", "product_role",
        "primary_customer_archetype", "primary_market", "current_trl",
        "precompany_validation_by_2029", "launch_2030_fit", "timing_window",
        "first_experiment_budget_usd", "us_beachhead", "china_beachhead",
        "secondary_markets", "asia_beachhead", "score_total", "confidence",
    ]
    with (OUT / "02_COMPARISON_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in final:
            out = {key: row.get(key) for key in columns}
            out["secondary_markets"] = ";".join(row["secondary_markets"])
            writer.writerow(out)
    matrix = [
        "# Comparison matrix", "",
        "| Rank | Idea | Lane | Role | Archetype | TRL | Experiment | US | China | Score | Confidence |",
        "|---:|---|---|---|---|---:|---:|:---:|:---:|---:|---|",
    ]
    for row in final:
        matrix.append(f"| {row['rank']} | `{row['idea_id']}` | {row['primary_lane']} | {row['product_role']} | {row['primary_customer_archetype']} | {row['current_trl']} | ${row['first_experiment_budget_usd']:,} | {'Y' if row['us_beachhead'] else 'N'} | {'Y' if row['china_beachhead'] else 'N'} | {row['score_total']:.1f} | {row['confidence']} |")
    (OUT / "02_COMPARISON_MATRIX.md").write_text("\n".join(matrix) + "\n", encoding="utf-8")

    groups = collections.defaultdict(list)
    for row in final:
        groups[row["primary_customer_archetype"]].append(row)
    fmap = [
        "# Frontier map", "",
        "The portfolio is organized by who owns the painful job, then connected by reusable physics and product boundaries.", "",
    ]
    for group in ("industrial", "scientific_big_physics", "infrastructure_utility_transport"):
        fmap += [f"## {group.replace('_', ' ').title()}", ""]
        for row in groups[group]:
            fmap.append(f"- `{row['idea_id']}` — {row['concept']} ({row['primary_lane']}, {row['product_role']}).")
        fmap.append("")
    fmap += [
        "## Non-obvious cross-lane connections", "",
        "- **Acceptance evidence as product.** HTS tape metrology, electrolyzer degradation benches, DC commissioning islands, heat-pump M&V, and laminography retrofits all sell a decision-grade dossier, not raw sensor data.",
        "- **Protection before scale.** Rack DC protection, vessel DC stacks, electrolyzer operating-envelope control, magnet protection, and HVDC relays convert a high-energy frontier system from demonstration into insurable infrastructure.",
        "- **Harsh-environment electronics.** Geothermal instrumentation, cryogenic interconnects, plasma control, and scientific detector modules share packaging, calibration, radiation/temperature drift, and long-lifecycle support disciplines.",
        "- **Qualification flywheel.** A narrow hardware wedge can compound into calibration, traceable datasets, standards participation, and recurring requalification without pretending software alone is the moat.",
        "- **Two-market discipline.** Dual routes are valuable only when buyer evidence, supply support, compliance, and acceptance institutions exist independently in both countries; they are not a single global-sales assumption.",
    ]
    (OUT / "03_FRONTIER_MAP.md").write_text("\n".join(fmap) + "\n", encoding="utf-8")

    cheap = [row for row in final if row["first_experiment_budget_usd"] < 100000]
    roadmap = [
        "# Validation roadmap, 2026-2034", "",
        "The filename is retained for compatibility; the operating roadmap extends through 2034.", "",
        "## Portfolio sequence", "",
        "| Year | Decision objective | Required evidence | Kill rule |",
        "|---|---|---|---|",
        "| 2026 | Freeze exact product jobs and interfaces | Named buyer workshops, incumbent teardowns, standards map, facility-access quotes | Stop any idea whose buyer owns no separable merchant socket |",
        "| 2027 | Build the minimum falsifier | Traceable prototype or emulator, blinded protocol, signed data/access terms | Stop on physics shortfall, unsafe integration, or incumbent parity |",
        "| 2028 | Run independent qualification | Repeatable third-party results across representative loads | Stop if the edge disappears outside the home bench |",
        "| 2029 | Secure procurement engagement | Paid evaluation, design-in memorandum, budget line, or qualification slot | Stop without a buyer-controlled next step by year-end |",
        "| 2030 | Make launch decisions | Frozen v1, qualified supply chain, service model, compliance checklist | Launch only the few ideas with evidence, not the whole portfolio |",
        "| 2031-2032 | Convert pilots to repeatable sales | Acceptance dossier, field reliability, price and service benchmarks | Stop custom projects that cannot become repeatable products |",
        "| 2033-2034 | Expand ratings and adjacent buyers | Reference deployments, recurring calibration/support, second-source readiness | Stop if the original trigger sunsets or an incumbent bundles the wedge |",
        "", "## Cheapest decisive experiments", "",
        "| Idea | Budget | Test | Procurement signal by 2029 |",
        "|---|---:|---|---|",
    ]
    for row in cheap:
        roadmap.append(f"| `{row['idea_id']}` | ${row['first_experiment_budget_usd']:,} | {row['first_experiment']} | {'Required and immediately testable' if row['procurement_engagement_by_2029'] else 'Not credited without signed access or buyer action'} |")
    roadmap += [
        "", "## Portfolio operating rules", "",
        "1. Run merchant-socket and acceptance-boundary tests before expensive hardware whenever that is the load-bearing uncertainty.",
        "2. Pre-register thresholds and name the incumbent benchmark. A favorable demo without a kill threshold does not advance an idea.",
        "3. Keep US and China validation evidence separate. Success in one country does not establish the other route.",
        "4. Refresh facility schedules, standards, restricted-party screening, and procurement records every six months through launch.",
        "5. Preserve a barbell: several cheap commercial falsifiers, plus only a few capital-intensive physics programs after access is signed.",
    ]
    (OUT / "04_VALIDATION_ROADMAP_2026_2030.md").write_text("\n".join(roadmap) + "\n", encoding="utf-8")

    log_rows = []
    for line in (ROOT / "98_RUN_LOGS" / "MODEL_ROUTING_LOG.jsonl").read_text(encoding="utf-8-sig").splitlines():
        try:
            log_rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    statuses = collections.Counter(row.get("status", "unknown") for row in log_rows)
    requested = collections.Counter(row.get("requested_model", "unknown") for row in log_rows)
    effort = [
        "# Model and effort report", "",
        "## Routing outcome", "",
        "The requested routes were recorded for every continuation task, but this runtime did not expose the actual model name or effort setting. Accordingly, `actual_model` and `effort` remain `unknown`; no unobserved route is claimed as successful or downgraded.", "",
        f"- Routing records: {len(log_rows)}.",
        f"- Status counts at synthesis: {dict(statuses)}.",
        f"- Requested-model counts: {dict(requested)}.",
        "- Exact calls and hidden reasoning effort are not observable; the log is the authoritative approximation.", "",
        "## Failures, retries, and repairs", "",
        "P4 required global recalibration and deterministic source repairs before passing. P5's first strict red team over-required future product orders for some pre-company concepts; main adjudication restored the literal demand rule while retaining product-job exactness. Two early China repairs failed fresh review, two later China-native concepts survived, and the first US scientific supplement produced one kill and one hold. The final scientific slot required a second bounded search and fresh comparison.", "",
        "## Patch-run recommendations", "",
        "- Recheck every 2030-era facility schedule and procurement record six months before any capital commitment.",
        "- Replace scenario pricing in the niche arithmetic with buyer quotes.",
        "- Convert conditional site-access paths into signed agreements before counting experiment budgets.",
        "- Run an external domain-specialist review on the final scientific concept and the safety-critical magnet and DC-protection concepts.",
        "- Preserve the frozen artifacts and rerun only the affected cards when a trigger, incumbent, or compliance condition changes.",
    ]
    (OUT / "05_MODEL_AND_EFFORT_REPORT.md").write_text("\n".join(effort) + "\n", encoding="utf-8")
    print("P7 portfolio files written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
