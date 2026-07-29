"""Mechanical validation of P3R2 seed batches before elegance adjudication.

Checks: JSON parses, batch minimums, unique idea_ids, 2030-contract fields
populated, primary_market values legal, lane spread, and that every cited
source ID is accepted + origin-eligible in the canonical ledger.
"""
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BATCHES = {
    'A': ('20_OPPORTUNITY_POOL/P3R2_A_us_pain.json', 18, {'US'}),
    'B': ('20_OPPORTUNITY_POOL/P3R2_B_china_pain.json', 18, {'CN'}),
    'C': ('20_OPPORTUNITY_POOL/P3R2_C_dual_us_cn.json', 18, {'US+CN'}),
    'D': ('20_OPPORTUNITY_POOL/P3R2_D_wildcards.json', 16, {'US', 'CN', 'US+CN'}),
    'E': ('20_OPPORTUNITY_POOL/P3R2_E_jptwkr_side.json', 10, {'US', 'CN', 'US+CN'}),
}
CONTRACT_FIELDS = ['current_trl', 'precompany_plan_2026_2029', 'demand_trigger_2030_2034',
                   'competition_outlook_2030', 'timing_window_risk',
                   'commercial_readiness_kill_date', 'first_experiment',
                   'first_experiment_budget_usd', 'painful_job', 'product']
ID_FIELDS = ['demand_source_ids', 'technical_source_ids', 'competitor_source_ids']


def main() -> int:
    with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8-sig') as f:
        canon = json.load(f)
    eligible = set()
    for r in canon:
        if r.get('accepted') is True and (r.get('india_origin_audit') or {}).get('status') in (
                'verified_non_india_origin', 'verified_multinational_allowed'):
            eligible.add(r['id'])

    errors = []
    all_ids = []
    lane_counter = Counter()
    market_counter = Counter()
    total = 0
    for tag, (rel, minimum, markets) in BATCHES.items():
        path = os.path.join(ROOT, rel)
        try:
            with open(path, encoding='utf-8-sig') as f:
                seeds = json.load(f)
        except Exception as e:
            errors.append(f'batch {tag}: cannot load {rel}: {e}')
            continue
        if len(seeds) < minimum:
            errors.append(f'batch {tag}: {len(seeds)} seeds < required {minimum}')
        total += len(seeds)
        for s in seeds:
            sid = s.get('idea_id', '?')
            all_ids.append(sid)
            lane_counter[s.get('primary_lane')] += 1
            market_counter[s.get('primary_market')] += 1
            if s.get('primary_market') not in markets:
                errors.append(f'{sid}: primary_market {s.get("primary_market")} not allowed for batch {tag}')
            for fld in CONTRACT_FIELDS:
                v = s.get(fld)
                if v in (None, '', []):
                    errors.append(f'{sid}: contract field {fld} empty')
            cited = set()
            for fld in ID_FIELDS:
                cited |= {x for x in (s.get(fld) or [])}
            if not cited:
                errors.append(f'{sid}: no cited source IDs')
            bad = sorted(x for x in cited if x not in eligible)
            if bad:
                errors.append(f'{sid}: ineligible/unknown cited IDs {bad}')
            if not s.get('demand_source_ids'):
                errors.append(f'{sid}: no demand_source_ids')

    dup = [i for i, c in Counter(all_ids).items() if c > 1]
    if dup:
        errors.append(f'duplicate idea_ids: {dup}')
    if total < 80:
        errors.append(f'total seeds {total} < 80')

    print(f'total={total} lanes={len(lane_counter)} markets={dict(market_counter)}')
    print('lane spread:', dict(sorted(lane_counter.items())))
    if errors:
        print('P3R2 SEED VALIDATION FAIL')
        for e in errors[:80]:
            print('-', e)
        return 1
    print('P3R2 SEED VALIDATION PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
