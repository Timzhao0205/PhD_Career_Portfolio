"""Build deterministic offline fixtures for the PowerShell stage validators.

This script is a package-build aid. Runtime PILOT.ps1 consumes the generated
files and does not require Python.
"""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"
OUT = FIX / "outputs"
PILOT = FIX / "pilot"


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def result(stage: str, names: list[str]) -> dict[str, object]:
    return {
        "stage": stage,
        "status": "COMPLETE",
        "outputs": names,
        "checks": {"fixture": True},
    }


if FIX.exists():
    shutil.rmtree(FIX)
OUT.mkdir(parents=True)
PILOT.mkdir(parents=True)

longlist = json.loads(
    (ROOT / "src" / "06" / "30_SCREENING" / "LONGLIST.json").read_text(
        encoding="utf-8"
    )
)
ids = [row["idea_id"] for row in longlist["ideas"]]
survivors = ids[:30]
final24 = ids[:24]
top10 = ids[:10]

for stage in (
    "10_refresh",
    "20_p4",
    "30_redteam",
    "40_select",
    "45_packs",
    "50_deep",
    "60_synth",
    "70_audit",
):
    dump(
        PILOT / stage / "PILOT.json",
        {
            "stage": stage,
            "status": "PASS",
            "sample_ids": ids[:3],
            "paths_tested": ["read", "write", "validate"],
            "checks": {"schema": True, "paths": True},
            "errors": [],
            "lessons": ["fixture"],
        },
    )
    text(PILOT / stage / "PILOT.md", f"# {stage} fixture pilot\n\nPASS\n")

# 10_refresh
d = OUT / "10_refresh"
dump(
    d / "REFRESH.json",
    {
        "artifact": "fixture",
        "as_of": "2026-07-27",
        "items": [
            {
                "idea_id": idea_id,
                "refresh_status": "no_material_change",
                "checked_claims": [{"claim": "fixture", "source_ids": []}],
                "new_source_ids": [],
                "stale_claims": [],
                "confidence": "fixture",
            }
            for idea_id in ids
        ],
    },
)
dump(d / "SOURCES.json", [])
text(d / "REFRESH.md", "# Fixture refresh\n")
dump(
    d / "RESULT.json",
    result("10_refresh", ["REFRESH.json", "SOURCES.json", "REFRESH.md"]),
)

# 20_p4
criteria_names = (
    "demonstrated_demand",
    "frontier_vision",
    "high_end_niche",
    "competition_whitespace",
    "reachable_validation_budget",
    "technical_elegance",
    "ten_x_edge",
    "us_china_leverage",
    "launch_2030_fit",
    "expansion_economics",
    "founder_skill_transfer",
)
d = OUT / "20_p4"
score_rows = []
for position, idea_id in enumerate(ids, 1):
    gates = {
        f"G{number}": {
            "pass": True,
            "rationale": "fixture",
            "source_ids": [],
        }
        for number in range(1, 8)
    }
    criteria = {
        name: {
            "score_0_5": 3,
            "weighted_points": 5,
            "rationale": "fixture",
            "source_ids": [],
        }
        for name in criteria_names
    }
    score_rows.append(
        {
            "idea_id": idea_id,
            "hard_gates": gates,
            "criteria": criteria,
            "total_100": 55,
            "confidence": "fixture",
            "fatal_uncertainties": [],
            "disposition": "survive" if position <= 30 else "reject",
        }
    )
dump(
    d / "SCORES.json",
    {
        "artifact": "fixture",
        "rubric_version": "fixture",
        "calibration_notes": "fixture",
        "ideas": score_rows,
    },
)
dump(
    d / "SURVIVORS.json",
    {
        "artifact": "fixture",
        "selection_rule": "fixture",
        "ideas": [
            {
                "idea_id": idea_id,
                "p4_rank": rank,
                "total_100": 55,
                "gate_status": "pass",
                "p5_focus": "fixture",
            }
            for rank, idea_id in enumerate(survivors, 1)
        ],
    },
)
text(d / "P4_REPORT.md", "# Fixture P4\n")
dump(
    d / "RESULT.json",
    result("20_p4", ["SCORES.json", "SURVIVORS.json", "P4_REPORT.md"]),
)

# 30_redteam
d = OUT / "30_redteam"
dump(
    d / "REDTEAM.json",
    {
        "artifact": "fixture",
        "method": "fixture",
        "ideas": [
            {
                "idea_id": idea_id,
                "decision": "survive",
                "failure_modes": [],
                "strongest_counterargument": "fixture",
                "demand_separability": "fixture",
                "competition_test": "fixture",
                "technical_kill_test": "fixture",
                "commercial_kill_test": "fixture",
                "geography_findings": "fixture",
                "source_defects": [],
                "repair_requirements": [],
                "residual_risk": "fixture",
                "confidence": "fixture",
                "source_ids": [],
            }
            for idea_id in survivors
        ],
    },
)
text(d / "REDTEAM.md", "# Fixture red team\n")
dump(
    d / "RESULT.json",
    result("30_redteam", ["REDTEAM.json", "REDTEAM.md"]),
)

# 40_select
d = OUT / "40_select"
selection_rows = []
for rank, idea_id in enumerate(final24, 1):
    selection_rows.append(
        {
            "idea_id": idea_id,
            "rank": rank,
            "concept": f"Fixture {idea_id}",
            "primary_lane": "L00",
            "is_hts": False,
            "product_role_class": "direct_value",
            "customer_class": "industrial",
            "first_experiment_budget_usd": 1000,
            "us_beachhead": True,
            "china_beachhead": True,
            "dual_market": True,
            "side_market_primary": False,
            "markets": ["US", "China"],
            "g7_pass": True,
            "experiment_by_2028": True,
            "engagement_by_2029": True,
            "score_total": 55,
            "why_now": "fixture",
            "key_kill": "fixture",
            "source_ids": [],
        }
    )
selection = {
    "artifact": "fixture",
    "policy": "fixture",
    "final_24": selection_rows,
    "top_10_deep_dives": top10,
    "near_misses": [],
}
dump(d / "SELECTION.json", selection)
dump(
    d / "PORTFOLIO_CHECKS.json",
    {"checks": {"count": {"pass": True}, "quota": {"pass": True}}},
)
text(d / "SELECTION.md", "# Fixture selection\n")
dump(
    d / "RESULT.json",
    result(
        "40_select",
        ["SELECTION.json", "PORTFOLIO_CHECKS.json", "SELECTION.md"],
    ),
)

# 45_packs
d = OUT / "45_packs"
source_rows = []
for number in range(1, 26):
    source_rows.append(
        {
            "id": f"TST-S{number:03d}",
            "title": f"Fixture source {number}",
            "url": f"https://example.com/{number}",
            "publisher": "Fixture",
            "published_at": "2026-01-01",
            "accessed_at": "2026-07-27",
            "source_type": "fixture",
            "peer_reviewed": number <= 10,
            "primary_demand": number <= 8,
            "geography": ["US"],
            "claim_supported": "fixture",
            "locator": "fixture",
            "access_level": "open",
            "accepted": True,
            "india_origin_status": "not_applicable_nonacademic",
            "non_indian_affiliation_evidence": "fixture",
        }
    )
all_source_ids = [row["id"] for row in source_rows]
dump(d / "SOURCES.json", source_rows)
dump(
    d / "PACKS.json",
    {
        "artifact": "fixture",
        "ideas": [
            {
                "idea_id": idea_id,
                "source_ids": all_source_ids[:20],
                "peer_reviewed_source_ids": all_source_ids[:7],
                "primary_demand_source_ids": all_source_ids[:5],
                "claim_source_map": {"fixture": all_source_ids[:2]},
                "coverage_gaps": [],
                "quality_notes": "fixture",
            }
            for idea_id in top10
        ],
    },
)
text(d / "PACKS.md", "# Fixture packs\n")
dump(
    d / "RESULT.json",
    result("45_packs", ["SOURCES.json", "PACKS.json", "PACKS.md"]),
)

# 50_deep
d = OUT / "50_deep"
index_rows = []
for number, idea_id in enumerate(top10, 1):
    name = f"D{number:02d}.md"
    words = " ".join(["evidence"] * 2600)
    text(d / "DEEP" / name, words + "\n")
    index_rows.append(
        {
            "idea_id": idea_id,
            "file": name,
            "word_count": 2600,
            "source_ids": all_source_ids[:20],
            "peer_reviewed_source_ids": all_source_ids[:7],
            "primary_demand_source_ids": all_source_ids[:5],
        }
    )
dump(d / "INDEX.json", {"ideas": index_rows})
text(d / "GEOGRAPHY.md", "# Fixture geography\n")
dump(d / "ADD_SOURCES.json", [])
dump(
    d / "RESULT.json",
    result(
        "50_deep",
        ["DEEP", "INDEX.json", "GEOGRAPHY.md", "ADD_SOURCES.json"],
    ),
)

# 60_synth
d = OUT / "60_synth"
portfolio = {"items": selection_rows, "top_10_deep_dives": top10}
dump(d / "PORTFOLIO.json", portfolio)
for name in (
    "00_EXECUTIVE.md",
    "01_IDEA_CARDS.md",
    "02_MATRIX.md",
    "03_MAP.md",
    "04_ROADMAP.md",
    "05_MODEL_REPORT.md",
):
    text(d / name, f"# Fixture {name}\n")
with (d / "02_MATRIX.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["idea_id", "rank"])
    for rank, idea_id in enumerate(final24, 1):
        writer.writerow([idea_id, rank])
dump(
    d / "RESULT.json",
    result(
        "60_synth",
        [
            "PORTFOLIO.json",
            "00_EXECUTIVE.md",
            "01_IDEA_CARDS.md",
            "02_MATRIX.csv",
            "02_MATRIX.md",
            "03_MAP.md",
            "04_ROADMAP.md",
            "05_MODEL_REPORT.md",
        ],
    ),
)

# 70_audit
d = OUT / "70_audit"
final_dir = d / "FINAL"
portfolio_dir = final_dir / "PORTFOLIO"
portfolio_dir.mkdir(parents=True)
for source_file in (OUT / "60_synth").iterdir():
    if source_file.is_file() and source_file.name != "RESULT.json":
        shutil.copy2(source_file, portfolio_dir / source_file.name)
shutil.copytree(OUT / "50_deep" / "DEEP", final_dir / "DEEP")
text(final_dir / "GEOGRAPHY.md", "# Fixture final geography\n")
dump(final_dir / "SELECTION.json", selection)
dump(final_dir / "SOURCES.json", source_rows)
dump(
    d / "AUDIT.json",
    {
        "verdict": "PASS",
        "checks": {f"check_{number}": True for number in range(1, 11)},
        "repairs": [],
        "unresolved_critical": [],
        "unresolved_major": [],
        "unresolved_minor": [],
        "final_24_count": 24,
        "deep_dive_count": 10,
        "source_count": len(source_rows),
    },
)
text(d / "AUDIT.md", "# Fixture audit\n\nPASS\n")
text(d / "CHANGELOG.md", "# Fixture changelog\n\nNo change.\n")
dump(
    d / "RESULT.json",
    {
        **result(
            "70_audit",
            ["FINAL", "AUDIT.json", "AUDIT.md", "CHANGELOG.md"],
        ),
        "audit_verdict": "PASS",
    },
)

