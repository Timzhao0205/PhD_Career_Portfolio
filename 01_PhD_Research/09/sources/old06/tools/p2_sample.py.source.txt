#!/usr/bin/env python3
"""Stratified sample of accepted ledger records for the P2 Fable atlas adjudication.

Samples 5 records per lane (80 total): one demand-primary, one academic, one
government/standard, one industry/commercial, one random remainder, seeded for
reproducibility. Writes a compact extract to 05_STATE/P2_SAMPLE_80.json (kept out of
10_SOURCE_ATLAS so merge_sources never scans it).
"""
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "90_BIBLIOGRAPHY" / "sources.json").read_text(encoding="utf-8-sig"))
acc = [s for s in data if s.get("accepted") is True]
random.seed(20260712)

by_lane = {}
for s in acc:
    for lane in s.get("lane_ids") or []:
        by_lane.setdefault(lane, []).append(s)

BUCKETS = (
    ("demand", lambda s: s.get("demand_evidence_type") not in (None, "", "none")),
    ("acad", lambda s: s.get("source_type") == "academic_peer_reviewed"),
    ("gov", lambda s: s.get("source_type") in ("government", "national_lab", "standard", "regulator")),
    ("ind", lambda s: s.get("source_type") in (
        "market_industry", "vendor_datasheet", "trade_press", "company_filing", "buyer_procurement", "patent")),
)

sample, seen = [], set()
for lane in sorted(by_lane):
    pool = [s for s in by_lane[lane] if s["id"] not in seen]
    picks = []
    for _, pred in BUCKETS:
        cands = [s for s in pool if pred(s) and s["id"] not in {p["id"] for p in picks}]
        if cands:
            picks.append(random.choice(cands))
    rest = [s for s in pool if s["id"] not in {p["id"] for p in picks}]
    while len(picks) < 5 and rest:
        c = random.choice(rest)
        rest.remove(c)
        picks.append(c)
    seen.update(p["id"] for p in picks)
    sample.extend(picks)

out = [
    {
        "id": s["id"],
        "lane": s.get("lane_ids"),
        "tier": s.get("tier"),
        "type": s.get("source_type"),
        "demand": s.get("demand_evidence_type"),
        "geo": s.get("geography"),
        "year": s.get("year"),
        "title": str(s.get("title", ""))[:110],
        "claim": str(s.get("claim_supported", ""))[:220],
        "fetched": s.get("fetched"),
        "peer": s.get("peer_review_status"),
    }
    for s in sample
]
dest = ROOT / "05_STATE" / "P2_SAMPLE_80.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"sampled {len(out)} records across {len(by_lane)} lanes -> {dest.relative_to(ROOT)}")
