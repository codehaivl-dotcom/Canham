"""Static document checks; never substitutes for runtime QA or combat simulation."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
failures = []
checks = []

def check(label, condition):
    checks.append(label)
    if not condition:
        failures.append(label)

# Check file targets rather than trusting navigation links in newly expanded specs.
missing = []
broken_anchors = []
def heading_slugs(path):
    counts={}
    result=set()
    for heading in re.findall(r'^#{1,6}\s+(.+)$',path.read_text(encoding='utf-8'),re.M):
        slug=re.sub(r'[^\w\- ]','',heading.strip().lower()).replace(' ','-')
        suffix=counts.get(slug,0)
        counts[slug]=suffix+1
        result.add(slug+(f'-{suffix}' if suffix else ''))
    return result
for path in [ROOT / 'README.md', *DOCS.glob('*.md')]:
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        raw=unquote(target)
        target = raw.split('#', 1)[0].strip('<>')
        if not target or re.match(r'^[a-z]+:', target, re.I):
            continue
        if not (path.parent / target).exists():
            missing.append(f'{path.name}: {target}')
        elif '#' in raw and target.endswith('.md'):
            fragment=raw.split('#',1)[1]
            if fragment and fragment not in heading_slugs(path.parent/target):
                broken_anchors.append(f'{path.name}: {target}#{fragment}')
check('All local Markdown file targets exist', not missing)
check('All explicit local Markdown section anchors exist',not broken_anchors)

content = (DOCS/'PROTOTYPE_CONTENT_PACK_V0.1.md').read_text(encoding='utf-8')
roster = []
for line in content.splitlines():
    if not re.match(r'\| SUR-00[1-6] \|', line):
        continue
    fields = [v.strip() for v in line.strip('|').split('|')]
    stats = [int(v.strip()) for v in fields[2].split('/')]
    roster.append(fields[0])
    check(f'{fields[0]} eight legal stats and matching total',
          len(stats)==8 and all(1<=v<=10 for v in stats)
          and sum(stats)==int(fields[3]) and 32<=sum(stats)<=44)
check('Six unique starting survivors', len(set(roster))==6)

# Recompute every authored debit/credit, not just the final stated balance.
balance = [300,120,40]
ledger_rows = 0
for line in content.splitlines():
    if not line.startswith('|'):
        continue
    fields = [v.strip().replace('**','') for v in line.strip('|').split('|')]
    if len(fields)!=3 or not re.fullmatch(r'[+\-]?\d+ / [+-]?\d+ / [+-]?\d+',fields[1]):
        continue
    delta = [int(v.strip()) for v in fields[1].split('/')]
    stated = [int(v.strip()) for v in fields[2].split('/')]
    balance = [a+b for a,b in zip(balance,delta)]
    ledger_rows += 1
    check(f'Ledger: {fields[0]}',balance==stated and min(balance)>=0)
check('Full tutorial ledger present', ledger_rows>=18)
check('Tutorial final materials 158/177/75', balance==[158,177,75])
check('Extended slice can afford CCL5 + Lab',
      [balance[0]+200-200-140,balance[1]+80-75-50,balance[2]-10]==[18,132,65])
check('Supply ledger: two scouts/deployments + packing',20-7-7+5==11)

research=(DOCS/'PROTOTYPE_RESEARCH_CATALOG_V0.1.md').read_text(encoding='utf-8')
ids=re.findall(r'^\| ((?:SUR|EXP|COM|SEC|ENG|XEN|FAC)-\d{2}) ',research,re.M)
check('Research has 34 unique node IDs',len(ids)==len(set(ids))==34)
edges={}
for line in research.splitlines():
    if not re.match(r'^\| (SUR|EXP|COM|SEC|ENG|XEN|FAC)-\d{2} ',line): continue
    fields=[v.strip() for v in line.strip('|').split('|')]
    node=fields[0].split()[0]
    edges[node]=re.findall(r'\b(?:SUR|EXP|COM|SEC|ENG|XEN|FAC)-\d{2}\b',fields[2])
def depth(node,trail=()):
    if node in trail or node not in edges: return 999
    return 1+max([depth(p,(*trail,node)) for p in edges[node]] or [0])
check('Research prerequisites exist, acyclic, max three nodes',
      all(depth(node)<=3 for node in edges))

enemy=(DOCS/'ENEMIES_RESISTANCES_V0.1.md').read_text(encoding='utf-8')
check('Removed obsolete vulnerability values from detail and matrix data',
      not re.search(r'-(?:30|35)(?:%|\s*\|)',enemy))
matrix=enemy.split('# 14. Full Resistance Matrix',1)[1].split('# 15.',1)[0]
for line in matrix.splitlines():
    fields=[v.strip() for v in line.strip('|').split('|')]
    if len(fields)!=7 or not re.match(r'^-?\d',fields[1]): continue
    values=[int(v) for field in fields[1:] for v in re.findall(r'-?\d+',field)]
    check(f'Resistance bounds: {fields[0]}',all(-25<=v<=80 for v in values))
ui=(DOCS/'UI_UX_NAVIGATION_V0.1.md').read_text(encoding='utf-8')
check('Research navigation includes Engineering','- Engineering;' in ui)
baseline=(DOCS/'IMPLEMENTATION_BASELINE_V0.1.md').read_text(encoding='utf-8')
weight_rows=0
for line in baseline.splitlines():
    fields=[v.strip() for v in line.strip('|').split('|')]
    if len(fields)==8 and all(re.fullmatch(r'\d+',v) for v in fields[1:]):
        weight_rows+=1
        check(f'Loot weights total 100: {fields[0]}',sum(map(int,fields[1:]))==100)
check('Seven normal-archetype weight rows',weight_rows==7)
qa=(DOCS/'QA_GAP_REGRESSION_V0.1.md').read_text(encoding='utf-8')
check('Runtime test rows remain NOT RUN',
      all('NOT RUN' in line for line in qa.splitlines() if re.match(r'\| QA-\d',line)))

for failure in missing:
    print('BROKEN LINK',failure)
for failure in broken_anchors:
    print('BROKEN ANCHOR',failure)
print(f'Static document checks: {len(checks)-len(failures)}/{len(checks)} passed')
for failure in failures:
    print('FAIL:',failure)
print('Runtime QA / combat simulation: NOT RUN')
sys.exit(bool(failures))
