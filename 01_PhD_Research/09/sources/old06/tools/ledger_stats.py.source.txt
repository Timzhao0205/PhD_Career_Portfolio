#!/usr/bin/env python3
"""Print acceptance-mix statistics for the canonical ledger (same math as validate_sources)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "90_BIBLIOGRAPHY" / "sources.json").read_text(encoding="utf-8-sig"))
acc = [s for s in data if s.get("accepted") is True]
n = len(acc)
peer = sum(s.get("source_type") == "academic_peer_reviewed" and s.get("peer_review_status") == "verified" for s in acc)
pd_types = {"buyer_tender", "buyer_specification", "procurement_award", "company_filing", "earnings_transcript", "official_project_award", "direct_customer_documentation"}
demand = sum(s.get("demand_evidence_type") in pd_types for s in acc)
gov = sum(s.get("source_type") in ("government", "national_lab", "standard", "regulator") for s in acc)
industry = sum(s.get("source_type") in ("market_industry", "vendor_datasheet", "trade_press") for s in acc)
us = sum("US" in (s.get("geography") or []) for s in acc)
china = sum("CN" in (s.get("geography") or []) for s in acc)
side = sum(any(g in (s.get("geography") or []) for g in ("JP", "TW", "KR")) for s in acc)
asia = sum(any(g in (s.get("geography") or []) for g in ("CN", "JP", "TW", "KR")) for s in acc)
local = sum(any(g in (s.get("geography") or []) for g in ("CN", "JP", "TW", "KR")) and s.get("language") in ("zh", "ja", "ko", "Chinese", "Japanese", "Korean") for s in acc)
t1 = sum(s.get("tier") == "T1" for s in acc)
t12 = sum(s.get("tier") in ("T1", "T2") for s in acc)
lanes = {}
for s in acc:
    for l in s.get("lane_ids") or []:
        lanes[l] = lanes.get(l, 0) + 1
print(f"reviewed={len(data)} accepted={n} peer={peer}/360 demand={demand}/120 gov={gov}/60 industry={industry}/60 US={us}/150 CN={china}/100 JP_TW_KR={side}/40 Asia={asia}/80 local_asia={local}/40")
if n:
    print(f"T1={t1} ({t1/n:.1%} vs 70%) T1+T2={t12} ({t12/n:.1%} vs 90%)")
print("per-lane accepted:", dict(sorted(lanes.items())))
