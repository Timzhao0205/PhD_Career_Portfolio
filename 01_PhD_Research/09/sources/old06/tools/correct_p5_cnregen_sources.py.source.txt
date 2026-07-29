#!/usr/bin/env python3
"""Apply factual metadata corrections from the fresh P5 revival red team."""

from __future__ import annotations

import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "90_BIBLIOGRAPHY" / "sources.json"


def main() -> int:
    data = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    by_id = {row["id"]: row for row in data}

    s04 = by_id["P5-CNREGEN-S04"]
    s04["lane_ids"] = ["L05"]
    s04["idea_ids"] = ["P3R2-C-09"]
    s04["notes"] = (
        "Accepted official project-timing evidence. Fresh P5 revival red team corrected "
        "the proposal's mistaken L01/F-16 association to accelerator lane L05/C-09; "
        "the source does not itself prove a merchant modulator socket."
    )

    s06 = by_id["P5-CNREGEN-S06"]
    s06["canonical_key"] = "tender:0730-264010SZ0023/11"
    s06["claim_supported"] = (
        "Guangzhou Guangxin Packaging Substrate ran an international-open retender for "
        "plasma-cleaner lot 0730-264010SZ0023/11 in March-April 2026. It confirms an "
        "additional exact-category procurement lot and an open legal-person bidder route; "
        "it is the same named buyer/project family as P3R2-F-16-S01 and is not counted as "
        "an independent buyer from that record."
    )
    s06["locator"] = (
        "MOFCOM bid page lines naming project 0730-264010SZ0023/11, plasma cleaner, "
        "Guangzhou Guangxin, international-open eligibility, and 2026-04-02 deadline."
    )
    s06["notes"] = (
        "Canonical project/lot key corrected after fresh P5 red-team readback. Same buyer "
        "and project family as P3R2-F-16-S01 (/03); do not count the two as independent buyers."
    )

    keys: dict[str, str] = {}
    for row in data:
        key = str(row.get("canonical_key", "")).strip().lower()
        if row.get("accepted") and key in keys:
            raise SystemExit(f"duplicate accepted canonical key: {key}: {keys[key]}, {row['id']}")
        keys[key] = row["id"]

    LEDGER.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("Corrected P5-CNREGEN-S04 association and P5-CNREGEN-S06 canonical lot/claim")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
