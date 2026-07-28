#!/usr/bin/env python3
import csv, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BANNED_MARKET_PATTERN = re.compile(r"\b(India|Indian|Singapore)\b", re.I)

def main():
    errors = []
    source_result = subprocess.run([sys.executable, str(ROOT/"tools"/"validate_sources.py")], capture_output=True, text=True)
    if source_result.returncode: errors.append("source validator failed: " + source_result.stdout.strip().replace("\n", " | "))
    required = [
        "10_SOURCE_ATLAS/ATLAS.md", "05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.md",
        "05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.json", "99_AUDIT/P2A_FABLE_ORIGIN_ADJUDICATION.md",
        "20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION.md",
        "20_OPPORTUNITY_POOL/LONGLIST.md",
        "20_OPPORTUNITY_POOL/ideas.json", "30_SCREENING/SCORING_MATRIX.csv",
        "30_SCREENING/SELECTION.md", "50_GEOGRAPHY/GEOGRAPHY_BRIEF.md",
        "60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md", "60_FINAL_PORTFOLIO/01_IDEA_CARDS.md",
        "60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv", "60_FINAL_PORTFOLIO/03_FRONTIER_MAP.md",
        "60_FINAL_PORTFOLIO/04_VALIDATION_ROADMAP_2026_2030.md",
        "60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md", "99_AUDIT/MECHANICAL_AUDIT.md",
        "99_AUDIT/FABLE_ADJUDICATION.md", "99_AUDIT/FINAL_AUDIT.md"
    ]
    for rel in required:
        p=ROOT/rel
        if not p.exists() or p.stat().st_size < 20: errors.append(f"missing/empty {rel}")
    for n in range(1,17):
        if not list((ROOT/"10_SOURCE_ATLAS").glob(f"L{n:02d}_*.md")): errors.append(f"missing lane brief L{n:02d}")
    deep = list((ROOT/"40_DEEP_DIVES").glob("DD_*.md"))
    if len(deep) < 10: errors.append(f"deep dives {len(deep)} < 10")
    p3r2_ids=set()
    for p in (ROOT/"20_OPPORTUNITY_POOL").glob("P3R2_*.json"):
        if "ADJUDICATION" in p.name.upper(): continue
        try:
            payload=json.loads(p.read_text(encoding="utf-8-sig"))
            records=payload if isinstance(payload,list) else payload.get("ideas",payload.get("seeds",[]))
            for i in records:
                if isinstance(i,dict) and i.get("idea_id"): p3r2_ids.add(i["idea_id"])
        except Exception as e: errors.append(f"invalid P3R2 seed file {p.name}: {e}")
    if len(p3r2_ids)<80: errors.append(f"P3 round-2 unique seeds {len(p3r2_ids)} < 80")
    ideas_path=ROOT/"20_OPPORTUNITY_POOL"/"ideas.json"
    if ideas_path.exists():
        try:
            ideas=json.loads(ideas_path.read_text(encoding="utf-8-sig"))
            if len(ideas)<48: errors.append(f"longlist {len(ideas)} < 48")
            if BANNED_MARKET_PATTERN.search(json.dumps(ideas, ensure_ascii=False)):
                errors.append("longlist contains excluded-market references (India/Singapore)")
            truthy={True,"true","1","yes","y"}
            us=sum(i.get("us_beachhead") in truthy for i in ideas)
            cn=sum(i.get("china_beachhead") in truthy for i in ideas)
            dual=sum(i.get("us_beachhead") in truthy and i.get("china_beachhead") in truthy for i in ideas)
            side=sum(i.get("primary_market") in ("JP","TW","KR") for i in ideas)
            timing_fields=("current_trl","precompany_plan_2026_2029","launch_2030_timing_thesis",
                           "demand_trigger_2030_2034","competition_outlook_2030","timing_window_risk",
                           "commercial_readiness_kill_date")
            timing_complete=sum(all(i.get(k) not in (None,"") for k in timing_fields) for i in ideas)
            if us<36: errors.append(f"longlist credible US cases {us} < 36")
            if cn<36: errors.append(f"longlist credible China cases {cn} < 36")
            if dual<24: errors.append(f"longlist US+China dual-market cases {dual} < 24")
            if side>8: errors.append(f"longlist side-market-primary cases {side} > 8")
            if timing_complete<48: errors.append(f"longlist complete 2030 timing records {timing_complete} < 48")
        except Exception as e: errors.append(f"ideas.json invalid: {e}")
    matrix=ROOT/"60_FINAL_PORTFOLIO"/"02_COMPARISON_MATRIX.csv"
    if matrix.exists():
        try:
            with matrix.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
            if len(rows)<24: errors.append(f"final ideas {len(rows)} < 24")
            required_cols={"idea_id","rank","concept","primary_lane","sector_cluster","product_role","primary_customer_archetype","primary_market","current_trl","precompany_validation_by_2029","launch_2030_fit","timing_window","first_experiment_budget_usd","us_beachhead","china_beachhead","secondary_markets","asia_beachhead","score_total","confidence"}
            missing=required_cols-set(rows[0] if rows else [])
            if missing: errors.append(f"comparison CSV missing columns {sorted(missing)}")
            lanes={r.get("primary_lane","") for r in rows if r.get("primary_lane")}
            if len(lanes)<12: errors.append(f"final lane diversity {len(lanes)} < 12")
            lane_counts={x:sum(r.get("primary_lane")==x for r in rows) for x in lanes}
            if any(v>3 for v in lane_counts.values()): errors.append(f"lane cap exceeded {lane_counts}")
            super_count=sum("superconduct" in r.get("sector_cluster","").lower() or "hts" in r.get("sector_cluster","").lower() for r in rows)
            if super_count>4: errors.append(f"superconductivity/HTS count {super_count} > 4")
            diag=sum(r.get("product_role")=="diagnostic_test" for r in rows)
            if diag>6: errors.append(f"diagnostic/test count {diag} > 6")
            direct=sum(r.get("product_role") in ("process_output","infrastructure","scientific_system") for r in rows)
            if direct<14: errors.append(f"direct-value products {direct} < 14")
            budgets=[]
            for r in rows:
                try: budgets.append(float(r.get("first_experiment_budget_usd", "nan")))
                except ValueError: errors.append(f"invalid experiment budget {r.get('idea_id')}")
            if sum(x<100000 for x in budgets)<8: errors.append("fewer than 8 ideas have experiment budget under $100k")
            archetypes={a:sum(r.get("primary_customer_archetype")==a for r in rows) for a in ("industrial","scientific_big_physics","infrastructure_utility_transport")}
            if archetypes["industrial"]<8: errors.append(f"industrial ideas {archetypes['industrial']} < 8")
            if archetypes["scientific_big_physics"]<4: errors.append(f"scientific ideas {archetypes['scientific_big_physics']} < 4")
            if archetypes["infrastructure_utility_transport"]<4: errors.append(f"infrastructure/transport ideas {archetypes['infrastructure_utility_transport']} < 4")
            truthy={"true","1","yes","y"}
            us_count=sum(r.get("us_beachhead","").lower() in truthy for r in rows)
            cn_count=sum(r.get("china_beachhead","").lower() in truthy for r in rows)
            dual_count=sum(r.get("us_beachhead","").lower() in truthy and r.get("china_beachhead","").lower() in truthy for r in rows)
            side_primary=sum(r.get("primary_market","").upper() in ("JP","TW","KR") for r in rows)
            launch_fit=sum(r.get("launch_2030_fit","").lower() in truthy for r in rows)
            precompany=sum(r.get("precompany_validation_by_2029","").lower() in truthy for r in rows)
            if us_count<18: errors.append(f"credible US beachheads {us_count} < 18")
            if cn_count<18: errors.append(f"credible China beachheads {cn_count} < 18")
            if dual_count<12: errors.append(f"credible US+China dual beachheads {dual_count} < 12")
            if side_primary>4: errors.append(f"side-market-primary final ideas {side_primary} > 4")
            if launch_fit<24: errors.append(f"final ideas passing 2030 launch fit {launch_fit} < 24")
            if precompany<12: errors.append(f"final ideas with pre-company validation by 2029 {precompany} < 12")
            if sum(bool(r.get("timing_window","").strip()) for r in rows)<24: errors.append("final ideas missing timing-window analysis")
            ledger_path=ROOT/"90_BIBLIOGRAPHY"/"sources.json"
            if ledger_path.exists():
                ledger=[s for s in json.loads(ledger_path.read_text(encoding="utf-8-sig")) if s.get("accepted")]
                for r in rows:
                    iid=r.get("idea_id")
                    refs=[s for s in ledger if iid in (s.get("idea_ids") or [])]
                    p=sum(s.get("source_type")=="academic_peer_reviewed" for s in refs)
                    primary_demand={"buyer_tender","buyer_specification","procurement_award","company_filing","earnings_transcript","official_project_award","direct_customer_documentation"}
                    d=sum(s.get("demand_evidence_type") in primary_demand for s in refs)
                    if len(refs)<12 or p<5 or d<3: errors.append(f"{iid} source quota total={len(refs)} peer={p} demand={d}")
        except Exception as e: errors.append(f"comparison CSV invalid: {e}")
    final=ROOT/"99_AUDIT"/"FINAL_AUDIT.md"
    if final.exists() and "PASS" not in final.read_text(encoding="utf-8-sig"): errors.append("FINAL_AUDIT lacks PASS")
    for rel in ("50_GEOGRAPHY/GEOGRAPHY_BRIEF.md","60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md","60_FINAL_PORTFOLIO/01_IDEA_CARDS.md","60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv","60_FINAL_PORTFOLIO/03_FRONTIER_MAP.md","60_FINAL_PORTFOLIO/04_VALIDATION_ROADMAP_2026_2030.md"):
        p=ROOT/rel
        if p.exists() and BANNED_MARKET_PATTERN.search(p.read_text(encoding="utf-8-sig")):
            errors.append(f"{rel} contains excluded-market references")
    state=ROOT/"05_STATE"/"MASTER_STATE.json"
    try:
        s=json.loads(state.read_text(encoding="utf-8-sig"))
        if s.get("mission")!="COMPLETE": errors.append("mission state is not COMPLETE")
    except Exception as e: errors.append(f"state invalid: {e}")
    if errors:
        print("MISSION VALIDATION FAIL")
        for e in errors: print("-",e)
        return 1
    print("MISSION VALIDATION PASS")
    return 0

if __name__ == "__main__": sys.exit(main())
