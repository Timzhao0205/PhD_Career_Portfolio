#!/usr/bin/env python3
"""Validate P5 final-24 and top-10 portfolio constraints."""

from __future__ import annotations

import collections
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "30_SCREENING" / "P5_SELECTION.json"
BANNED = re.compile(r"\b(?:India|Indian|Singapore)\b", re.I)
PASSING_GATES = {"pass", "pass_marginal"}
DIRECT_ROLES = {"process_output", "infrastructure", "scientific_system"}


def truthy(value: object) -> bool:
    return value is True or str(value).lower() in {"true", "1", "yes", "y"}


def main() -> int:
    errors: list[str] = []
    if not PATH.exists():
        print("P5 SELECTION VALIDATION FAIL")
        print(f"- missing {PATH.relative_to(ROOT).as_posix()}")
        return 1

    try:
        payload = json.loads(PATH.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        print("P5 SELECTION VALIDATION FAIL")
        print(f"- invalid JSON: {exc}")
        return 1

    final = payload.get("final_24", [])
    top = payload.get("top_10_deep_dives", [])
    near = payload.get("near_misses", [])
    final_ids = [row.get("idea_id") for row in final]
    top_ids = [row if isinstance(row, str) else row.get("idea_id") for row in top]

    if len(final) != 24:
        errors.append(f"final_24 count {len(final)} != 24")
    if len(set(final_ids)) != len(final_ids):
        errors.append("final_24 contains duplicate IDs")
    if len(top_ids) != 10 or len(set(top_ids)) != 10:
        errors.append(f"top_10_deep_dives must contain 10 unique IDs, got {len(set(top_ids))}")
    if not set(top_ids).issubset(set(final_ids)):
        errors.append(f"top-10 IDs outside final-24: {sorted(set(top_ids) - set(final_ids))}")
    if BANNED.search(json.dumps(payload, ensure_ascii=False)):
        errors.append("selection contains excluded-market references")

    required = {
        "idea_id", "rank", "concept", "primary_lane", "sector_cluster", "product_role",
        "primary_customer_archetype", "primary_market", "current_trl",
        "precompany_validation_by_2029", "launch_2030_fit", "timing_window",
        "first_experiment", "first_experiment_budget_usd", "first_experiment_decisive_basis",
        "us_beachhead",
        "china_beachhead", "secondary_markets", "asia_beachhead", "score_total",
        "confidence", "gates", "procurement_engagement_by_2029", "selection_rationale",
        "source_ids",
    }
    for row in final:
        iid = row.get("idea_id", "<missing>")
        missing = [key for key in required if row.get(key) in (None, "")]
        if missing:
            errors.append(f"{iid} missing fields {sorted(missing)}")
        gates = row.get("gates", {})
        for gate in (f"G{i}" for i in range(1, 8)):
            verdict = gates.get(gate)
            if isinstance(verdict, dict):
                verdict = verdict.get("verdict")
            if verdict not in PASSING_GATES:
                errors.append(f"{iid} has non-passing {gate} verdict {verdict!r}")
        if not truthy(row.get("launch_2030_fit")):
            errors.append(f"{iid} does not pass launch_2030_fit")

    source_path = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
    sources = json.loads(source_path.read_text(encoding="utf-8-sig"))
    source_by_id = {source.get("id"): source for source in sources if source.get("accepted")}
    primary_demand = {
        "buyer_tender", "buyer_specification", "procurement_award", "company_filing",
        "earnings_transcript", "official_project_award", "direct_customer_documentation",
    }
    for row in final:
        iid = row.get("idea_id", "<missing>")
        ids = list(dict.fromkeys(row.get("source_ids") or []))
        refs = [source_by_id[source_id] for source_id in ids if source_id in source_by_id]
        peer = sum(source.get("source_type") == "academic_peer_reviewed" for source in refs)
        demand = sum(source.get("demand_evidence_type") in primary_demand for source in refs)
        if len(refs) < 12 or peer < 5 or demand < 3:
            errors.append(
                f"{iid} selection source quota total={len(refs)} peer={peer} demand={demand}"
            )

    lanes = collections.Counter(row.get("primary_lane") for row in final)
    if len(lanes) < 12:
        errors.append(f"lane diversity {len(lanes)} < 12")
    over = {lane: count for lane, count in lanes.items() if count > 3}
    if over:
        errors.append(f"lane cap exceeded {over}")
    hts = sum(
        "superconduct" in str(row.get("sector_cluster", "")).lower()
        or "hts" in str(row.get("sector_cluster", "")).lower()
        for row in final
    )
    if hts > 4:
        errors.append(f"superconductivity/HTS count {hts} > 4")
    diagnostics = sum(row.get("product_role") == "diagnostic_test" for row in final)
    if diagnostics > 6:
        errors.append(f"diagnostic/test count {diagnostics} > 6")
    direct = sum(row.get("product_role") in DIRECT_ROLES for row in final)
    if direct < 14:
        errors.append(f"direct-value count {direct} < 14")
    cheap = sum(float(row.get("first_experiment_budget_usd", 1e99)) < 100_000 for row in final)
    if cheap < 8:
        errors.append(f"sub-$100k decisive experiments {cheap} < 8")

    archetypes = collections.Counter(row.get("primary_customer_archetype") for row in final)
    for archetype, minimum in {
        "industrial": 8,
        "scientific_big_physics": 4,
        "infrastructure_utility_transport": 4,
    }.items():
        if archetypes[archetype] < minimum:
            errors.append(f"{archetype} count {archetypes[archetype]} < {minimum}")

    us = sum(truthy(row.get("us_beachhead")) for row in final)
    cn = sum(truthy(row.get("china_beachhead")) for row in final)
    dual = sum(
        truthy(row.get("us_beachhead")) and truthy(row.get("china_beachhead"))
        for row in final
    )
    if us < 18:
        errors.append(f"US beachheads {us} < 18")
    if cn < 18:
        errors.append(f"China beachheads {cn} < 18")
    if dual < 12:
        errors.append(f"dual beachheads {dual} < 12")
    side = sum(str(row.get("primary_market", "")).upper() in {"JP", "TW", "KR"} for row in final)
    if side > 4:
        errors.append(f"side-market-primary count {side} > 4")
    precompany = sum(truthy(row.get("precompany_validation_by_2029")) for row in final)
    if precompany < 12:
        errors.append(f"pre-company validation count {precompany} < 12")
    engagement = sum(truthy(row.get("procurement_engagement_by_2029")) for row in final)
    if engagement < 8:
        errors.append(f"procurement/design-in paths by 2029 {engagement} < 8")

    near_ids = [row.get("idea_id") for row in near if isinstance(row, dict)]
    if len(set(near_ids)) != len(near_ids):
        errors.append("near_misses contains duplicate IDs")
    for row in near:
        if not isinstance(row, dict) or not row.get("idea_id") or not row.get("reason"):
            errors.append("every near miss needs idea_id and reason")

    if errors:
        print("P5 SELECTION VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("P5 SELECTION VALIDATION PASS")
    print(
        f"- final={len(final)} top10={len(top_ids)} lanes={len(lanes)} "
        f"cheap={cheap} us={us} cn={cn} dual={dual} direct={direct}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
