"""Freeze the P3R2 longlist from the judge's eligible ID set.

Reads longlist_eligible_ids from P3R2_ELEGANCE_ADJUDICATION_R3.json, pulls the
seed records from the A-G seed files (honoring merges: only canonical IDs are
eligible), verifies gates once more, and writes:
- 30_SCREENING/LONGLIST.json  (frozen idea records)
- 30_SCREENING/LONGLIST.md    (compact index; founder-fit notes appended later)
"""
import datetime
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SEED_FILES = ['P3R2_A_us_pain.json', 'P3R2_B_china_pain.json', 'P3R2_C_dual_us_cn.json',
              'P3R2_D_wildcards.json', 'P3R2_E_jptwkr_side.json', 'P3R2_F_cn_topup.json',
              'P3R2_G_cn_microwave.json']


def main() -> int:
    with open(os.path.join(ROOT, '20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION_R3.json'),
              encoding='utf-8-sig') as f:
        r3 = json.load(f)
    eligible = r3.get('longlist_eligible_ids')
    if not eligible:
        print('FAIL: no longlist_eligible_ids in R3 adjudication')
        return 1

    seeds = {}
    for rel in SEED_FILES:
        with open(os.path.join(ROOT, '20_OPPORTUNITY_POOL', rel), encoding='utf-8-sig') as f:
            for s in json.load(f):
                seeds[s['idea_id']] = s

    missing = [i for i in eligible if i not in seeds]
    if missing:
        print('FAIL: eligible ids missing from seed files:', missing)
        return 1

    longlist = []
    for i in eligible:
        s = dict(seeds[i])
        v = s.get('elegance_verdict')
        if v not in ('PROMOTE', 'FIX_APPLIED'):
            print(f'FAIL: {i} has verdict {v}, not longlist-eligible')
            return 1
        s['longlist_frozen_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        longlist.append(s)

    mk = Counter(s.get('primary_market') for s in longlist)
    lanes = Counter(s.get('primary_lane') for s in longlist)
    us = mk.get('US', 0) + mk.get('US+CN', 0)
    cn = mk.get('CN', 0) + mk.get('US+CN', 0)
    dual = mk.get('US+CN', 0)
    jptwkr = sum(1 for s in longlist if s.get('primary_market') in ('JP', 'TW', 'KR'))
    gates = [(len(longlist), 48, 'total ideas'), (len(lanes), 14, 'lanes'),
             (us, 36, 'credible US'), (cn, 36, 'credible CN'), (dual, 24, 'dual')]
    errors = [f'{label} {v} < {req}' for v, req, label in gates if v < req]
    if jptwkr > 8:
        errors.append(f'JP/TW/KR-primary {jptwkr} > 8')
    if errors:
        print('LONGLIST FREEZE FAIL')
        for e in errors:
            print('-', e)
        return 1

    os.makedirs(os.path.join(ROOT, '30_SCREENING'), exist_ok=True)
    with open(os.path.join(ROOT, '30_SCREENING/LONGLIST.json'), 'w', encoding='utf-8') as f:
        json.dump({'frozen_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   'gates': {'total': len(longlist), 'lanes': len(lanes), 'us': us, 'cn': cn,
                             'dual': dual, 'jptwkr_primary': jptwkr},
                   'ideas': longlist}, f, ensure_ascii=False, indent=1)
        f.write('\n')

    md = ['# P3R2 frozen longlist', '',
          f'Frozen: {datetime.datetime.now(datetime.timezone.utc).isoformat()}',
          f'Gates: total {len(longlist)}/48, lanes {len(lanes)}/14, US {us}/36, CN {cn}/36, '
          f'dual {dual}/24, JP/TW/KR-primary {jptwkr}/<=8 - ALL PASS', '',
          'Source: P3R2 seeds A-G after three independent Fable/xhigh elegance adjudications '
          'and fix rounds. Founder-fit notes are appended post-freeze per rule 3 (2/100 cap).', '',
          '| idea_id | lane | market | concept | TRL | kill date |', '|---|---|---|---|---|---|']
    for s in sorted(longlist, key=lambda x: x['idea_id']):
        concept = (s.get('concept') or s.get('product') or '')[:90].replace('|', '/')
        md.append(f"| {s['idea_id']} | {s.get('primary_lane')} | {s.get('primary_market')} | "
                  f"{concept} | {s.get('current_trl')} | "
                  f"{s.get('commercial_readiness_kill_date')} |")
    md.append('')
    with open(os.path.join(ROOT, '30_SCREENING/LONGLIST.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f'LONGLIST FROZEN: total={len(longlist)} lanes={len(lanes)} US={us} CN={cn} '
          f'dual={dual} jptwkr={jptwkr}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
