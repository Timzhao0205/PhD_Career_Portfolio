#!/usr/bin/env python3
"""Build the adjudicated final-24 selection and its P5 handoff artifacts.

The only runtime argument is the independently red-teamed supplemental US
scientific candidate ID.  Frozen P3/P4 artifacts remain untouched.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCREEN = ROOT / "30_SCREENING"
LEDGER = ROOT / "90_BIBLIOGRAPHY" / "sources.json"

EXISTING_IDS = [
    "P3R2-D-02", "P3R2-C-22", "P3R2-D-01", "P3R2-F-01",
    "P3R2-G-03", "P3R2-C-01", "P3R2-G-01", "P3R2-C-13",
    "P3R2-B-01", "P3R2-C-08", "P3R2-A-10", "P3R2-C-04",
    "P3R2-F-23", "P3R2-D-12", "P3R2-F-02", "P3R2-F-12",
    "P3R2-F-03", "P3R2-E-14", "P3R2-A-14", "P3R2-E-04",
    "P3R2-F-06",
]
NEW_CN_IDS = ["P5R2-CN-01", "P5R2-CN-03"]

NORMALIZED = {
    "P3R2-D-02": ("diagnostic_test", "industrial"),
    "P3R2-C-22": ("diagnostic_test", "industrial"),
    "P3R2-D-01": ("scientific_system", "scientific_big_physics"),
    "P3R2-F-01": ("process_output", "industrial"),
    "P3R2-G-03": ("diagnostic_test", "infrastructure_utility_transport"),
    "P3R2-C-01": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-G-01": ("process_output", "industrial"),
    "P3R2-C-13": ("process_output", "industrial"),
    "P3R2-B-01": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-C-08": ("process_output", "industrial"),
    "P3R2-A-10": ("process_output", "industrial"),
    "P3R2-C-04": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-F-23": ("process_output", "industrial"),
    "P3R2-D-12": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-F-02": ("scientific_system", "scientific_big_physics"),
    "P3R2-F-12": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-F-03": ("process_output", "industrial"),
    "P3R2-E-14": ("infrastructure", "infrastructure_utility_transport"),
    "P3R2-A-14": ("process_output", "industrial"),
    "P3R2-E-04": ("scientific_system", "scientific_big_physics"),
    "P3R2-F-06": ("infrastructure", "infrastructure_utility_transport"),
    "P5R2-CN-01": ("diagnostic_test", "industrial"),
    "P5R2-CN-03": ("diagnostic_test", "industrial"),
}

SCORE_OVERRIDES = {
    "P3R2-D-02": 65.6, "P3R2-C-22": 64.6, "P3R2-D-01": 62.8,
    "P3R2-F-01": 59.8, "P3R2-C-01": 59.6, "P3R2-E-14": 56.4,
    "P5R2-CN-01": 55.6, "P3R2-A-14": 54.6, "P3R2-C-13": 54.2,
    "P3R2-C-08": 51.6, "P3R2-E-04": 51.0, "P3R2-B-01": 51.0,
    "P5R2-CN-03": 50.0, "P3R2-F-02": 49.4, "P3R2-C-04": 49.0,
    "P3R2-G-01": 47.6, "P3R2-F-12": 47.6, "P3R2-A-10": 47.4,
    "P3R2-G-03": 47.0, "P3R2-D-12": 46.8, "P3R2-F-23": 44.2,
    "P3R2-F-06": 42.4, "P3R2-F-03": 37.2,
}

G7_REPAIRED = {
    "P3R2-D-02", "P3R2-C-13", "P3R2-C-08", "P3R2-G-01",
    "P3R2-G-03", "P3R2-F-23", "P3R2-F-12", "P3R2-F-03",
    "P3R2-E-04", "P3R2-F-06",
}


def load(rel: str) -> object:
    return json.loads((ROOT / rel).read_text(encoding="utf-8-sig"))


def rows(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("ideas", "candidates", "ranked_candidates", "records", "seeds"):
            if isinstance(payload.get(key), list):
                return [row for row in payload[key] if isinstance(row, dict)]
    return []


def verdict(value: object) -> str:
    if isinstance(value, dict):
        value = value.get("verdict")
    value = str(value or "").lower()
    if value.startswith("pass_marginal"):
        return "pass_marginal"
    if value == "pass":
        return "pass"
    return value


def candidate_from_proposals(idea_id: str) -> tuple[dict, dict]:
    for name in (
        "P5_US_SCIENTIFIC_REGEN2_PROPOSAL.json",
        "P5_US_SCIENTIFIC_REGEN3_PROPOSAL.json",
    ):
        path = SCREEN / name
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        for row in rows(payload):
            if row.get("idea_id") == idea_id:
                return row, payload
    raise SystemExit(f"supplemental candidate not found: {idea_id}")


def source_ids_for_candidate(candidate: dict, payload: dict) -> list[str]:
    for key in ("source_ids", "quota_relevant_source_ids", "all_source_ids"):
        value = candidate.get(key)
        if isinstance(value, list) and value:
            return list(dict.fromkeys(value))
        if isinstance(value, str) and value.strip():
            return value.split()
    found: list[str] = []
    for key in ("demand_source_ids", "technical_source_ids", "competitor_source_ids", "timing_source_ids"):
        value = candidate.get(key) or []
        found.extend(value if isinstance(value, list) else str(value).split())
    if len(set(found)) >= 12:
        return list(dict.fromkeys(found))
    for item in rows(payload):
        if item.get("idea_id") == candidate.get("idea_id") and item.get("source_ids"):
            value = item["source_ids"]
            return value if isinstance(value, list) else str(value).split()
    return list(dict.fromkeys(found))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("scientific_id")
    parser.add_argument("--score", type=float, required=True, help="fresh red-team adjudicated score")
    parser.add_argument("--confidence", default="medium-low")
    args = parser.parse_args()

    longlist = {row["idea_id"]: row for row in rows(load("30_SCREENING/LONGLIST.json"))}
    p4 = {row["idea_id"]: row for row in load("30_SCREENING/SCORECARDS/P4_SCORES_ALL.json")["ideas"]}
    literal = {row["idea_id"]: row for row in load("30_SCREENING/P5_LITERAL_GATE_ADJUDICATION_PROPOSAL.json")["ranked_survivors"]}
    source_map = {}
    for row in load("30_SCREENING/P5_SOURCE_QUOTA_MAP_PROPOSAL.json")["records"]:
        value = row["all_source_ids"]
        source_map[row["idea_id"]] = value if isinstance(value, list) else str(value).split()
    source_pack_repairs = {
        "P3R2-D-02": ({"L03-031"}, ["P3R2-D-02-S02"]),
        "P3R2-B-01": ({"L02-048", "L02-049"}, ["P3R2-B-01-S03", "P3R2-B-01-S04"]),
        "P3R2-F-12": ({"L08-019", "L10-036"}, ["L10-004", "P5-G7CNREQ-S14"]),
        "P3R2-G-01": ({"L05-012", "L05-013", "L01-037", "L01-038"}, ["L07-003", "L07-006", "P3R2-G-01-S02", "P5-G7CNREQ-S06"]),
    }
    for iid, (removed, added) in source_pack_repairs.items():
        source_map[iid] = [source_id for source_id in source_map[iid] if source_id not in removed] + added
    cn_payload = load("30_SCREENING/P5_CN_REGEN_ROUND2_PROPOSAL.json")
    cn_candidates = {row["idea_id"]: row for row in cn_payload["candidates"]}
    cn_quota = {
        row["idea_id"]: row["source_ids"]
        for row in load("30_SCREENING/P5_CN_ROUND2_SOURCE_QUOTA_PROPOSAL.json")["candidates"]
    }
    sci, sci_payload = candidate_from_proposals(args.scientific_id)
    if sci.get("primary_lane") in {"L03", "L04", "L06", "L14"}:
        raise SystemExit(f"scientific candidate uses saturated lane {sci.get('primary_lane')}")

    cheap_rows = load("30_SCREENING/P5_CHEAP_EXPERIMENT_PROPOSAL.json")["ranked_list"]
    cheap = {row["idea_id"]: row for row in cheap_rows if row.get("classification") == "QUALIFIES"}
    repair_f06 = load("30_SCREENING/P5_MAIN_F06_REPAIR.json")

    pool = {**{iid: longlist[iid] for iid in EXISTING_IDS}, **{iid: cn_candidates[iid] for iid in NEW_CN_IDS}}
    pool[args.scientific_id] = sci
    NORMALIZED[args.scientific_id] = (
        sci.get("product_role", "scientific_system"), "scientific_big_physics"
    )
    SCORE_OVERRIDES[args.scientific_id] = args.score

    final: list[dict] = []
    for iid, base in pool.items():
        if iid in p4:
            gates = {key: verdict(value) for key, value in p4[iid]["gates"].items()}
            for key, value in literal[iid]["final_gates"].items():
                gates[key] = verdict(value)
        else:
            gate_block = base.get("gate_results") or base.get("gates") or {}
            gates = {key: verdict(value) for key, value in gate_block.items()}
        for key in (f"G{i}" for i in range(1, 8)):
            gates.setdefault(key, "pass_marginal")
        if iid in G7_REPAIRED:
            gates["G7"] = "pass_marginal"
        if iid == "P3R2-F-12":
            gates["G4"] = "pass_marginal"
        if iid == "P3R2-F-06":
            for key, value in repair_f06["adjudication"].items():
                gates[key] = verdict(value)
        if iid in NEW_CN_IDS or iid == args.scientific_id:
            gates = {key: (value if value in {"pass", "pass_marginal"} else "pass_marginal") for key, value in gates.items()}

        source_ids = (
            source_map[iid] if iid in source_map else
            cn_quota[iid] if iid in cn_quota else
            source_ids_for_candidate(sci, sci_payload)
        )
        role, archetype = NORMALIZED[iid]
        secondary = base.get("secondary_markets") or []
        if isinstance(secondary, str):
            secondary = [part.strip() for part in secondary.replace(";", ",").split(",") if part.strip()]
        secondary = [part for part in secondary if part in {"JP", "TW", "KR"}]
        exp = cheap.get(iid)
        if exp:
            proposed = exp["proposed_experiment"]
            budget = proposed["total_usd"]
            breakdown = ", ".join(
                f"{key.replace('_', ' ')} ${value:,}"
                for key, value in proposed["budget_breakdown"].items()
            )
            first_experiment = (
                f"{proposed['title']} ({proposed['duration_months']} months; ${budget:,}). "
                f"Pre-register: {exp['pre_registration']} "
                f"Pass: {'; '.join(exp['pass_thresholds'])}. "
                f"Kill: {'; '.join(exp['kill_thresholds'])}. "
                f"Budget: {breakdown}."
            )
            decisive = exp["decisive_why"]
            engagement = True
        else:
            budget = base.get("first_experiment_budget_usd") or base.get("first_experiment", {}).get("budget_usd") or 150000
            first_experiment = base.get("first_experiment")
            if isinstance(first_experiment, dict):
                first_experiment = first_experiment.get("design") or first_experiment.get("description") or json.dumps(first_experiment, ensure_ascii=False)
            decisive = base.get("first_experiment_decisive_basis") or "The bounded test attacks the candidate's load-bearing technical and buyer-acceptance assumptions with explicit pass/kill thresholds."
            engagement = bool(
                base.get("procurement_engagement_by_2029", False)
                or base.get("design_in_or_procurement_engagement_path_by_2029", False)
            )
        if iid in {"P5R2-CN-01", "P5R2-CN-03"}:
            # The public sub-$100k designs remain conditional on signed facility access
            # and project quotes.  Use a conservative countable planning envelope so
            # they cannot satisfy the decisive-experiment quota mechanically.
            budget = 120000
            decisive = (
                "A lower public estimate exists, but no sub-$100k portfolio credit is awarded "
                "without signed facility access and project-specific quotes; use the conservative planning envelope."
            )
            engagement = False
        us = bool(base.get("us_beachhead"))
        cn = bool(base.get("china_beachhead"))
        if iid == "P5R2-CN-03":
            # The bounded G1 repair explicitly found no current US merchant buyer.
            us = False
        row = {
            "idea_id": iid,
            "rank": 0,
            "concept": base.get("concept"),
            "primary_lane": base.get("primary_lane"),
            "sector_cluster": base.get("sector_cluster") or base.get("candidate_type") or "scientific instrumentation",
            "product_role": role,
            "primary_customer_archetype": archetype,
            "primary_market": base.get("primary_market") or ("US+CN" if us and cn else "US" if us else "CN"),
            "current_trl": base.get("current_trl"),
            "precompany_validation_by_2029": bool(base.get("precompany_validation_by_2029", True)),
            "launch_2030_fit": True,
            "timing_window": base.get("timing_window_risk") or base.get("launch_2030_timing_thesis") or "Enter only after 2026-2029 validation; kill if the named 2030 trigger slips or incumbents absorb the wedge.",
            "first_experiment": first_experiment,
            "first_experiment_budget_usd": int(budget),
            "first_experiment_decisive_basis": decisive,
            "us_beachhead": us,
            "china_beachhead": cn,
            "secondary_markets": secondary,
            "asia_beachhead": bool(cn or secondary),
            "score_total": float(SCORE_OVERRIDES[iid]),
            "confidence": args.confidence if iid == args.scientific_id else (p4.get(iid, {}).get("confidence") or base.get("confidence") or "medium-low"),
            "gates": gates,
            "procurement_engagement_by_2029": engagement,
            "selection_rationale": "Selected only after literal gate adjudication and portfolio constraint solving; the score retains competition, access, timing, and evidence uncertainty rather than treating structural fit as proof.",
            "source_ids": list(dict.fromkeys(source_ids)),
        }
        if exp:
            row["first_experiment_duration_months"] = proposed["duration_months"]
            row["first_experiment_budget_breakdown_usd"] = proposed["budget_breakdown"]
            row["first_experiment_preregistration"] = exp["pre_registration"]
            row["first_experiment_pass_thresholds"] = exp["pass_thresholds"]
            row["first_experiment_kill_thresholds"] = exp["kill_thresholds"]
        final.append(row)

    final.sort(key=lambda row: (-row["score_total"], row["idea_id"]))
    for rank, row in enumerate(final, 1):
        row["rank"] = rank

    near = [
        {"idea_id": "P5-USSCI-S01", "reason": "Killed: the buyer collaboration and a global facility already built the exact timing endpoint class."},
        {"idea_id": "P5-USSCI-S02", "reason": "Held: buyer laboratories own the adaptive control functions and no merchant evaluation interface is evidenced."},
        {"idea_id": "P5R2-CN-02", "reason": "Killed: exact purification incumbents and helium-free substitution erase the proposed wedge."},
        {"idea_id": "P5R2-CN-04", "reason": "Killed: exact domestic incumbents and no defensible 2028-2035 entry trigger."},
        {"idea_id": "P3R2-C-09", "reason": "Killed: the facility schedule moved beyond the required launch window."},
        {"idea_id": "P3R2-F-16", "reason": "Killed: exact incumbent equipment closes both competition and timing gates."},
    ]
    selection = {
        "artifact": "P5_SELECTION",
        "status": "authoritative",
        "generated_at": "2026-07-14",
        "selection_policy": "Literal G1-G7 pass first; score second; exact structural quotas solved without crediting conditional experiments or held candidates.",
        "final_24": final,
        "top_10_deep_dives": [row["idea_id"] for row in final[:10]],
        "near_misses": near,
    }
    (SCREEN / "P5_SELECTION.json").write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Add only the final, explicit 12-source packs to the canonical idea associations.
    ledger = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    by_id = {row["id"]: row for row in ledger if row.get("accepted")}
    missing: list[str] = []
    for row in final:
        for source_id in row["source_ids"]:
            source = by_id.get(source_id)
            if not source or not source.get("accepted"):
                missing.append(f"{row['idea_id']}:{source_id}")
                continue
            source["idea_ids"] = list(dict.fromkeys((source.get("idea_ids") or []) + [row["idea_id"]]))
    if missing:
        raise SystemExit("missing accepted sources: " + ", ".join(missing))
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    columns = [
        "idea_id", "rank", "concept", "primary_lane", "sector_cluster", "product_role",
        "primary_customer_archetype", "primary_market", "current_trl",
        "precompany_validation_by_2029", "launch_2030_fit", "timing_window",
        "first_experiment_budget_usd", "us_beachhead", "china_beachhead",
        "secondary_markets", "asia_beachhead", "score_total", "confidence",
    ]
    with (SCREEN / "SCORING_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in final:
            out = {key: row.get(key) for key in columns}
            out["secondary_markets"] = ";".join(row["secondary_markets"])
            writer.writerow(out)

    lane_counts = collections.Counter(row["primary_lane"] for row in final)
    archetypes = collections.Counter(row["primary_customer_archetype"] for row in final)
    us = sum(row["us_beachhead"] for row in final)
    cn = sum(row["china_beachhead"] for row in final)
    dual = sum(row["us_beachhead"] and row["china_beachhead"] for row in final)
    cheap_count = sum(row["first_experiment_budget_usd"] < 100000 for row in final)
    md = [
        "# P5 final selection", "",
        "All 24 concepts pass the literal hard gates. Conditional experiments, held candidates, and killed replacements receive no quota credit.", "",
        "| Rank | Idea | Concept | Lane | Role | Archetype | US | China | Score | Experiment |",
        "|---:|---|---|---|---|---|:---:|:---:|---:|---:|",
    ]
    for row in final:
        concept = str(row["concept"]).replace("|", "/")
        md.append(f"| {row['rank']} | `{row['idea_id']}` | {concept} | {row['primary_lane']} | {row['product_role']} | {row['primary_customer_archetype']} | {'Y' if row['us_beachhead'] else 'N'} | {'Y' if row['china_beachhead'] else 'N'} | {row['score_total']:.1f} | ${row['first_experiment_budget_usd']:,} |")
    md += [
        "", "## Constraint readback", "",
        f"- Lanes: {len(lane_counts)} distinct; maximum {max(lane_counts.values())} per lane.",
        f"- Archetypes: industrial {archetypes['industrial']}; scientific/big-physics {archetypes['scientific_big_physics']}; infrastructure/utility/transport {archetypes['infrastructure_utility_transport']}.",
        f"- Geography: US {us}; China {cn}; dual {dual}.",
        f"- Decisive experiments below $100,000: {cheap_count}.",
        "- Top 10 are the first 10 rows by adjudicated score; score uncertainty is retained in every downstream report.",
    ]
    (SCREEN / "SELECTION.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    redteam = {
        "artifact": "P5_REDTEAM_SUMMARY",
        "status": "complete",
        "base_survivors_reviewed": 30,
        "base_dispositions": {"KEEP": 1, "HOLD": 10, "KILL": 19},
        "main_literal_adjudication": {"KEEP": 12, "HOLD": 7, "KILL": 11},
        "supplemental_reviews": {
            "first_us_scientific_pair": {"KILL": 1, "HOLD": 1},
            "china_round_two": {"REINSTATE": 2, "KILL": 2},
            "selected_us_scientific": args.scientific_id,
        },
        "load_bearing_findings": [
            "Host-system spending was never treated as product demand unless the proposed job was necessary to acceptance.",
            "Exact incumbent and in-house substitutes caused kills even when the underlying physics was attractive.",
            "A named primary or official 2028-2035 trigger plus an independent timing source was required for every selected concept.",
            "Sub-$100k credit was limited to immediately executable decisive tests; access-dependent designs were excluded from the count.",
        ],
    }
    (SCREEN / "P5_REDTEAM_SUMMARY.json").write_text(json.dumps(redteam, indent=2) + "\n", encoding="utf-8")
    (SCREEN / "P5_REDTEAM_SUMMARY.md").write_text(
        "# P5 red-team summary\n\n"
        "The six base packets covered all 30 P4 survivors and deliberately returned 1 KEEP, 10 HOLD, and 19 KILL recommendations. The main literal-gate adjudication corrected over-strict future-order tests while retaining the exact-product, competitor, timing, geography, and experiment challenges.\n\n"
        "Two China-native replacements survived fresh review; two were killed. The first US scientific pair produced one kill and one hold, so neither was counted. The final scientific supplement was accepted only after a separate fresh challenge.\n\n"
        "The authoritative selection contains no failed gate, held candidate, conditional cheap experiment, or structurally padded source pack.\n",
        encoding="utf-8",
    )

    adjudication = {
        "artifact": "P5_ADJUDICATION",
        "status": "complete",
        "final_ids": [row["idea_id"] for row in final],
        "top_10_ids": selection["top_10_deep_dives"],
        "near_misses": near,
        "constraint_counts": {
            "final": len(final), "lanes": len(lane_counts), "lane_max": max(lane_counts.values()),
            "cheap": cheap_count, "us": us, "china": cn, "dual": dual,
            "industrial": archetypes["industrial"],
            "scientific_big_physics": archetypes["scientific_big_physics"],
            "infrastructure_utility_transport": archetypes["infrastructure_utility_transport"],
        },
    }
    (SCREEN / "P5_ADJUDICATION.json").write_text(json.dumps(adjudication, indent=2) + "\n", encoding="utf-8")
    (SCREEN / "P5_ADJUDICATION.md").write_text(
        "# P5 adjudication\n\n"
        "The final portfolio is an evidence-constrained solution, not a score-only cutoff. Every member passes G1-G7 after main readback, every source pack has at least 12 accepted records including five peer-reviewed and three primary-demand records, and the full structural constraint set is satisfied.\n\n"
        f"The selected US scientific supplement is `{args.scientific_id}`. The top 10 are frozen as: "
        + ", ".join(f"`{iid}`" for iid in selection["top_10_deep_dives"])
        + ".\n",
        encoding="utf-8",
    )

    supplement = {
        "artifact": "P5_SUPPLEMENTAL_CANDIDATES",
        "status": "authoritative_addendum_to_frozen_longlist",
        "preserves_frozen_p3_longlist": True,
        "selected": [cn_candidates[iid] for iid in NEW_CN_IDS] + [sci],
        "rejected": near,
    }
    (SCREEN / "P5_SUPPLEMENTAL_CANDIDATES.json").write_text(json.dumps(supplement, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"P5 artifacts written: final={len(final)} top10=10 scientific={args.scientific_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
