import os, re, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

EXCL = ['L01-006','L01-010','L01-026','L01-041','L01-042','L01-054','L02-003','L02-008','L03-054','L04-024','L04-037','L04-105','L05-025','L05-051','L06-047','L07-033','L07-048','L08-023','L08-028','L09-035','L11-036','L11-053','L12-043','L13-034','L13-051','L14-052','L16-021','L01-051','L01-052','L03-047','L03-049','L05-001','L06-053','L07-038','L07-039','L13-050','L14-011','L14-017','L14-023','L15-045','L16-008','L16-012']
CONSULT = ['Mordor', 'Valuates', 'MarketsandMarkets', 'DataIntelo', 'Persistence Market',
           'TBRC', 'Global Growth Insights', 'QYResearch', 'researchandmarkets',
           'MarketGrowthReports', 'Growth Market Reports']
HDR = re.compile(r'P2A origin-audit repair', re.I)

for path in sorted(glob.glob('10_SOURCE_ATLAS/*.md')):
    if path.endswith('_about.md'): continue
    text = open(path, encoding='utf-8').read()
    lines = text.splitlines()
    hdr_line = None
    for i, ln in enumerate(lines):
        if HDR.search(ln):
            hdr_line = i
            break
    bad = []
    for i, ln in enumerate(lines):
        in_repair = hdr_line is not None and i >= hdr_line
        for pat in EXCL:
            if pat in ln and not in_repair:
                bad.append((i+1, 'ID ' + pat, ln.strip()[:140]))
        for c in CONSULT:
            if c.lower() in ln.lower() and not in_repair:
                bad.append((i+1, 'CONSULT ' + c, ln.strip()[:140]))
    print(os.path.basename(path), '| repair section at line:', (hdr_line + 1) if hdr_line is not None else 'MISSING')
    for b in bad:
        print('   PRE-REPAIR MENTION line', b[0], '|', b[1], '|', b[2])
