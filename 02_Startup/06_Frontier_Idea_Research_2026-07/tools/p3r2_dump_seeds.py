# Temporary helper for P3R2 fix application: dump compact seed views + ledger checks.
# Usage: python tools/p3r2_dump_seeds.py <group> [chunk]
import json, sys, os, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POOL = os.path.join(ROOT, "20_OPPORTUNITY_POOL")

FILES = {
    "A": "P3R2_A_us_pain.json",
    "B": "P3R2_B_china_pain.json",
    "C": "P3R2_C_dual_us_cn.json",
    "D": "P3R2_D_wildcards.json",
    "E": "P3R2_E_jptwkr_side.json",
}

def load_all():
    seeds = {}
    for k, fn in FILES.items():
        with open(os.path.join(POOL, fn), encoding="utf-8") as f:
            for rec in json.load(f):
                seeds[rec["idea_id"]] = rec
    return seeds

FIX_SEEDS = ["P3R2-A-03","P3R2-A-11","P3R2-A-16","P3R2-B-06","P3R2-B-14","P3R2-B-21",
    "P3R2-B-22","P3R2-C-02","P3R2-C-03","P3R2-C-04","P3R2-C-12","P3R2-C-13","P3R2-C-19",
    "P3R2-C-20","P3R2-C-21","P3R2-D-07","P3R2-D-08","P3R2-D-11","P3R2-D-12","P3R2-D-16",
    "P3R2-D-18","P3R2-D-19","P3R2-D-20","P3R2-E-02","P3R2-E-11"]

CANON = ["P3R2-C-01","P3R2-C-05","P3R2-C-07","P3R2-C-08","P3R2-C-09","P3R2-A-02",
    "P3R2-A-05","P3R2-A-10","P3R2-A-13","P3R2-A-14","P3R2-A-21","P3R2-B-01","P3R2-D-01",
    "P3R2-D-02","P3R2-D-09","P3R2-D-10","P3R2-E-04","P3R2-E-14"]

ABSORBED = ["P3R2-A-01","P3R2-B-03","P3R2-B-04","P3R2-E-01","P3R2-C-06","P3R2-B-05",
    "P3R2-E-03","P3R2-A-12","P3R2-B-07","P3R2-E-08","P3R2-A-07","P3R2-B-09","P3R2-D-05",
    "P3R2-E-05","P3R2-A-08","P3R2-C-10","P3R2-A-09","P3R2-A-04","P3R2-C-17","P3R2-E-07",
    "P3R2-B-10","P3R2-C-11","P3R2-B-11","P3R2-D-03","P3R2-B-12","P3R2-A-06","P3R2-D-17",
    "P3R2-A-18","P3R2-B-19","P3R2-A-17","P3R2-A-19","P3R2-B-13","P3R2-C-15","P3R2-A-15",
    "P3R2-B-02","P3R2-B-18","P3R2-D-15","P3R2-E-10","P3R2-B-17","P3R2-D-14","P3R2-E-09",
    "P3R2-E-12","P3R2-E-13","P3R2-B-08","P3R2-C-16"]

TRIM_FULL = ["extreme_edge","frontier_vision","founder_fit_note","gate_results","score_total",
             "sector_cluster","product_role","primary_customer_archetype"]
ABS_FIELDS = ["idea_id","concept","primary_market","named_buyer_examples","secondary_markets",
              "us_beachhead","china_beachhead","product","demand_trigger_2030_2034",
              "demand_source_ids","technical_source_ids","competitor_source_ids"]

def dump(recs, ids, fields=None, trim=None):
    for i in ids:
        r = recs[i]
        if fields:
            view = {k: r.get(k) for k in fields if k in r}
        else:
            view = {k: v for k, v in r.items() if k not in (trim or [])}
        print("### " + i)
        print(json.dumps(view, ensure_ascii=False, indent=1))
        print()

def chunk(lst, n, idx):
    size = (len(lst) + n - 1) // n
    return lst[idx*size:(idx+1)*size]

def main():
    group = sys.argv[1]
    seeds = load_all()
    if group == "keys":
        # sanity: all ids present, field-name superset
        allk = collections.Counter()
        for r in seeds.values():
            for k in r: allk[k] += 1
        print("total seeds:", len(seeds))
        print(dict(allk))
        missing = [i for i in FIX_SEEDS+CANON+ABSORBED if i not in seeds]
        print("missing:", missing)
    elif group == "fix":
        idx = int(sys.argv[2]); dump(seeds, chunk(FIX_SEEDS, 7, idx), trim=TRIM_FULL)
    elif group == "canon":
        idx = int(sys.argv[2]); dump(seeds, chunk(CANON, 6, idx), trim=TRIM_FULL)
    elif group == "abs":
        idx = int(sys.argv[2]); dump(seeds, chunk(ABSORBED, 5, idx), fields=ABS_FIELDS)
    elif group == "ledger":
        # check eligibility of all source IDs cited across all seeds
        with open(os.path.join(ROOT, "90_BIBLIOGRAPHY", "sources.json"), encoding="utf-8") as f:
            led = json.load(f)
        srcs = led["sources"] if isinstance(led, dict) and "sources" in led else led
        print("ledger records:", len(srcs))
        print("sample keys:", sorted(srcs[0].keys()))
        print(json.dumps(srcs[0], ensure_ascii=False)[:500])
        by_id = {}
        for s in srcs:
            sid = s.get("source_id") or s.get("id")
            by_id[sid] = s
        def eligible(s):
            acc = s.get("accepted")
            audit = s.get("india_origin_audit")
            astat = audit.get("status") if isinstance(audit, dict) else audit
            return acc is True and astat in (
                "verified_non_india_origin", "verified_multinational_allowed", None)
        bad = []
        for i, r in seeds.items():
            for f in ("demand_source_ids","technical_source_ids","competitor_source_ids"):
                for sid in r.get(f) or []:
                    s = by_id.get(sid)
                    if s is None:
                        bad.append((i, f, sid, "MISSING")); continue
                    if not eligible(s):
                        audit = s.get("india_origin_audit")
                        astat = audit.get("status") if isinstance(audit, dict) else audit
                        bad.append((i, f, sid, str(s.get("accepted"))+"/"+str(astat)))
        print("ineligible/missing citations:", len(bad))
        for b in bad[:80]: print(b)
        import collections as c
        print("audit statuses:", c.Counter(
            (s.get("india_origin_audit") or {}).get("status") if isinstance(s.get("india_origin_audit"), dict)
            else str(s.get("india_origin_audit")) for s in srcs))
        print("accepted:", c.Counter(str(s.get("accepted")) for s in srcs))

if __name__ == "__main__":
    main()
