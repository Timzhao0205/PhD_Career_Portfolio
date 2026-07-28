#!/usr/bin/env python3
"""Apply the main-agent P4 calibration adjudication and render candidate outputs."""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SC = ROOT / "30_SCREENING" / "SCORECARDS"

WEIGHTS = {
    "demonstrated_demand": 16,
    "frontier_coolness_vision": 15,
    "high_end_niche_quality": 10,
    "competition_whitespace": 9,
    "reachable_validation_budget": 9,
    "technical_elegance_controllability": 11,
    "tenx_technical_edge": 7,
    "us_china_dual_market_leverage": 10,
    "launch_window_fit_2030": 8,
    "expansion_economics": 3,
    "founder_skill_transfer": 2,
}

# Main-agent decisions after reading the all-65 independent audit. These are deliberately
# bounded to the clearest cross-batch inconsistencies; red-team work remains responsible for
# resolving the conditional hard-gate cases in P5.
RAW_ADJUSTMENTS = {
    "P3R2-A-05": {
        "competition_whitespace": 3,
        "reachable_validation_budget": 3,
    },
    "P3R2-A-14": {
        "tenx_technical_edge": 3,
        "launch_window_fit_2030": 4,
        "expansion_economics": 3,
    },
    "P3R2-B-01": {"reachable_validation_budget": 3},
    "P3R2-C-01": {
        "demonstrated_demand": 3,
        "high_end_niche_quality": 3,
        "expansion_economics": 3,
    },
    "P3R2-C-04": {
        "demonstrated_demand": 3,
        "launch_window_fit_2030": 4,
        "expansion_economics": 3,
    },
    "P3R2-C-22": {"demonstrated_demand": 3},
    "P3R2-D-01": {"reachable_validation_budget": 3},
    "P3R2-D-02": {
        "competition_whitespace": 2,
        "launch_window_fit_2030": 4,
    },
    "P3R2-D-12": {"reachable_validation_budget": 3},
    "P3R2-D-13": {
        "demonstrated_demand": 3,
        "tenx_technical_edge": 3,
    },
    "P3R2-E-02": {"reachable_validation_budget": 3},
    "P3R2-E-14": {
        "demonstrated_demand": 3,
        "us_china_dual_market_leverage": 2,
    },
    "P3R2-G-01": {"competition_whitespace": 3},
}

GATE_ADJUSTMENTS = {
    "P3R2-C-22": {
        "gate": "G1",
        "verdict": "pass_marginal",
        "note": (
            " Main-agent global calibration: the cited projects and supplier records prove "
            "electrolyzer spending, but not a booked merchant degradation-emulation bench. "
            "Carry only as a marginal pass into P5; flip to fail without a paid OEM, developer, "
            "or financier evaluation."
        ),
    },
    "P3R2-D-13": {
        "gate": "G1",
        "verdict": "pass_marginal",
        "note": (
            " Main-agent global calibration: directed-energy awards prove funded system demand, "
            "not a thermal-magazine purchase. Carry only as a marginal pass; flip to fail unless "
            "a prime or subsystem integrator confirms the burst-thermal socket."
        ),
    },
    "P3R2-E-14": {
        "gate": "G1",
        "verdict": "pass_marginal",
        "note": (
            " Main-agent global calibration: transmission projects and compliance deadlines prove "
            "protection work, but no merchant relay/HIL order is cited. Carry only as a marginal "
            "pass; P5 must find a utility, EPC, or OEM design-in for the product."
        ),
    },
}

RATIONALES = {
    "P3R2-A-05": "Negative-search whitespace and a ceiling-budget experiment were each one point too generous.",
    "P3R2-A-14": "A 300 C capability class is not itself a demonstrated 10x buyer metric; timing and expansion remain strong but not maximum.",
    "P3R2-B-01": "The $250k experiment fits the band, but the $3M-$8M v1 range crosses the rubric's under-$5M preference.",
    "P3R2-C-01": "Buyer specifications establish the protection gap, not a booked product; platform-owner absorption also narrows the niche and expansion score.",
    "P3R2-C-04": "Liquid-cooling demand is stronger than demand for the PFAS-free two-phase premium, and the $10M-$25M v1 path limits launch/expansion confidence.",
    "P3R2-C-22": "Underlying hydrogen spending is not direct proof of a merchant bankability bench; G1 and demand are therefore marginal pending paid product evidence.",
    "P3R2-D-01": "A $250k experiment at the band ceiling plus a v1 range above $5M does not support a raw-4 budget score.",
    "P3R2-D-02": "THEVA/TAPESTAR is a direct incumbent and capacity growth does not guarantee a new entrant's 2030 design win.",
    "P3R2-D-12": "The experiment is reachable, but the sellable-v1 path and external licensing burden make raw 4 too generous.",
    "P3R2-D-13": "System awards do not directly purchase the thermal magazine, and the 10x SWaP claim remains a brassboard target.",
    "P3R2-E-02": "A ceiling-budget experiment and v1 range above $5M warrant a middle budget score.",
    "P3R2-E-14": "Project spending does not directly buy the merchant relay/HIL product; the frozen record is US-led and does not justify raw-4 dual-market leverage.",
    "P3R2-G-01": "Absence of an integrated competitor in a search does not by itself justify raw-4 whitespace.",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def gate_map(record):
    return {name: value["verdict"] for name, value in record["gates"].items()}


def snapshot(record):
    return {
        "gates": gate_map(record),
        "eliminated": record["eliminated"],
        "score_total": record.get("score_total"),
    }


def md(text) -> str:
    return str(text or "").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def render_batch(batch: str, ideas: list[dict], concepts: dict[str, dict]) -> str:
    lines = [
        f"# P4 score batch {batch} — globally calibrated",
        "",
        "This batch is a deterministic split of the authoritative global calibration candidate.",
        "Original pre-calibration files are preserved under the ChatGPT handoff backup and generated-file checkpoints.",
        "",
        "| Idea | Gate result | Score | Confidence | Concept |",
        "|---|---|---:|---|---|",
    ]
    for item in ideas:
        result = "ELIMINATED" if item["eliminated"] else "SURVIVES"
        lines.append(
            f"| {item['idea_id']} | {result} | {item['score_total']:.1f} | "
            f"{item['confidence']} | {md(concepts[item['idea_id']]['concept'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    proposed = load(SC / "P4_SCORES_ALL_PROPOSED.json")
    longlist = load(ROOT / "30_SCREENING" / "LONGLIST.json")["ideas"]
    concepts = {item["idea_id"]: item for item in longlist}

    raw_index = {}
    for batch in ("S1", "S2", "S3", "S4"):
        for item in load(SC / f"P4_SCORES_{batch}.json")["ideas"]:
            raw_index[item["idea_id"]] = item

    final = copy.deepcopy(proposed)
    final["artifact"] = "P4 globally calibrated scorecards"
    final["status"] = "candidate_pending_mechanical_promotion"
    final["generated_at"] = datetime.now(timezone.utc).isoformat()
    final["provenance"]["main_adjudication"] = {
        "requested_model": "GPT-5.6 Sol",
        "requested_effort": "extra_high_or_higher",
        "actual_model": "unknown",
        "actual_effort": "unknown",
        "basis": "65-idea proposal plus independent cross-batch audit and deterministic repair plan",
    }

    by_id = {item["idea_id"]: item for item in final["ideas"]}
    changes = {item["idea_id"]: item for item in final.get("calibration_changes", [])}

    for idea_id, score_changes in RAW_ADJUSTMENTS.items():
        item = by_id[idea_id]
        changed_fields = []
        for criterion, new_raw in score_changes.items():
            score = item["scores"][criterion]
            old_raw = score["raw"]
            if old_raw == new_raw:
                continue
            score["raw"] = new_raw
            score["weighted"] = round(new_raw * WEIGHTS[criterion] / 5, 1)
            changed_fields.extend(
                [f"scores.{criterion}.raw", f"scores.{criterion}.weighted"]
            )

        gate_change = GATE_ADJUSTMENTS.get(idea_id)
        if gate_change:
            gate = item["gates"][gate_change["gate"]]
            if gate["verdict"] != gate_change["verdict"]:
                gate["verdict"] = gate_change["verdict"]
                changed_fields.append(f"gates.{gate_change['gate']}.verdict")
            if gate_change["note"].strip() not in gate["rationale"]:
                gate["rationale"] += gate_change["note"]
                changed_fields.append(f"gates.{gate_change['gate']}.rationale")
            flag = gate_change["note"].strip()
            if flag not in item["redteam_flags_for_p5"]:
                item["redteam_flags_for_p5"].append(flag)
                changed_fields.append("redteam_flags_for_p5")

        old_total = item["score_total"]
        item["score_total"] = round(sum(s["weighted"] for s in item["scores"].values()), 1)
        if item["score_total"] != old_total:
            changed_fields.append("score_total")
        low, high = item["score_range"]
        if not low <= item["score_total"] <= high:
            item["score_range"] = [
                max(0, int(item["score_total"] - 8)),
                min(100, int(item["score_total"] + 8)),
            ]
            changed_fields.append("score_range")

        entry = changes.get(idea_id)
        if entry is None:
            entry = {
                "idea_id": idea_id,
                "before": snapshot(raw_index[idea_id]),
                "after": snapshot(item),
                "changed_fields": [],
                "rationale": "",
            }
            final["calibration_changes"].append(entry)
            changes[idea_id] = entry
        entry["after"] = snapshot(item)
        entry["changed_fields"] = sorted(set(entry.get("changed_fields", []) + changed_fields))
        prefix = "Main adjudication after independent cross-batch audit: " + RATIONALES[idea_id]
        if prefix not in entry.get("rationale", ""):
            entry["rationale"] = (entry.get("rationale", "").rstrip() + " " + prefix).strip()

    survivors = [item for item in final["ideas"] if not item["eliminated"]]
    eliminated = [item for item in final["ideas"] if item["eliminated"]]
    final["summary"].update(
        {
            "ideas": 65,
            "survivors": len(survivors),
            "eliminated": len(eliminated),
            "main_adjudication_adjusted_ideas": len(RAW_ADJUSTMENTS),
            "status": "candidate_pending_mechanical_promotion",
        }
    )

    # Write the consolidated candidate first; promotion to P4_SCORES_ALL.json is a separate,
    # hash-checked action after batch-mode validation succeeds.
    dump(SC / "P4_SCORES_ALL_CANDIDATE.json", final)

    subset_map = {}
    for batch in ("S1", "S2", "S3", "S4"):
        subset = load(SC / f"_subset_{batch}.json")
        subset_map[batch] = [item["idea_id"] for item in subset]
        batch_ideas = [by_id[idea_id] for idea_id in subset_map[batch]]
        payload = {
            "batch": batch,
            "model_self_report": "chatgpt-continuation global calibration; actual runtime model unknown",
            "scored_at": final["generated_at"],
            "ideas": batch_ideas,
            "batch_summary": {
                "ideas": len(batch_ideas),
                "survivors": sum(not item["eliminated"] for item in batch_ideas),
                "eliminated": sum(item["eliminated"] for item in batch_ideas),
                "source": "P4_SCORES_ALL_CANDIDATE.json",
            },
        }
        dump(SC / f"P4_SCORES_{batch}.json", payload)
        (SC / f"P4_SCORES_{batch}.md").write_text(
            render_batch(batch, batch_ideas, concepts), encoding="utf-8"
        )

    ranked = sorted(survivors, key=lambda item: item["score_total"], reverse=True)
    lines = [
        "# P4 globally calibrated scores",
        "",
        f"Status: candidate pending mechanical promotion. Ideas: 65; survivors: {len(survivors)}; eliminated: {len(eliminated)}.",
        "",
        "Hard-gate failure controls survival regardless of numeric score. `pass_marginal` records carry explicit P5 flip conditions.",
        "The exact runtime ChatGPT model/effort was not exposed and is recorded as unknown; no identity is inferred.",
        "",
        "## Ranked survivors",
        "",
        "| Rank | Idea | Lane | Score | Range | Confidence | Concept |",
        "|---:|---|---|---:|---|---|---|",
    ]
    for rank, item in enumerate(ranked, 1):
        meta = concepts[item["idea_id"]]
        lines.append(
            f"| {rank} | {item['idea_id']} | {meta['primary_lane']} | {item['score_total']:.1f} | "
            f"{item['score_range'][0]}–{item['score_range'][1]} | {item['confidence']} | {md(meta['concept'])} |"
        )
    lines.extend(
        [
            "",
            "## Eliminated ideas",
            "",
            "| Idea | Score | Failed gates | Reason |",
            "|---|---:|---|---|",
        ]
    )
    for item in sorted(eliminated, key=lambda value: value["score_total"], reverse=True):
        failed = ", ".join(
            gate for gate, value in item["gates"].items() if value["verdict"] in {"fail", "blocked"}
        )
        lines.append(
            f"| {item['idea_id']} | {item['score_total']:.1f} | {failed} | {md(item['elimination_reason'])} |"
        )
    lines.extend(
        [
            "",
            "## Calibration interpretation",
            "",
            "- The survivor count is below 32, so P5 must red-team every survivor and document the shortfall.",
            "- Current survivors do not by themselves satisfy the final China-beachhead or sub-$100k-experiment gates; P5 must perform targeted evidence/experiment repair without weakening hard gates.",
            "- Scores are comparative judgments, not forecasts. Overlapping ranges should not be forced into false precision.",
            "",
        ]
    )
    (SC / "P4_SCORES_ALL.md").write_text("\n".join(lines), encoding="utf-8")

    log_lines = [
        "# P4 global calibration log",
        "",
        "This log preserves every proposal/schema/citation repair and main-agent substantive adjustment.",
        "Original batch files are preserved in the ChatGPT handoff backup or generated-file checkpoints.",
        "",
    ]
    for change in sorted(final["calibration_changes"], key=lambda item: item["idea_id"]):
        log_lines.extend(
            [
                f"## {change['idea_id']}",
                "",
                f"- Before: eliminated={change['before']['eliminated']}; score={change['before']['score_total']}; gates={change['before']['gates']}",
                f"- After: eliminated={change['after']['eliminated']}; score={change['after']['score_total']}; gates={change['after']['gates']}",
                f"- Changed fields: {', '.join(change.get('changed_fields', []))}",
                f"- Rationale: {change['rationale']}",
                "",
            ]
        )
    (SC / "P4_GLOBAL_CALIBRATION_LOG.md").write_text(
        "\n".join(log_lines), encoding="utf-8"
    )

    print(
        f"P4 candidate rendered: ideas=65 survivors={len(survivors)} "
        f"eliminated={len(eliminated)} main_adjusted={len(RAW_ADJUSTMENTS)}"
    )


if __name__ == "__main__":
    main()
