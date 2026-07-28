"""Append one checkpoint line to 05_STATE/PROGRESS_LOG.md."""
import datetime
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

line = sys.argv[1]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
with open(os.path.join(ROOT, '05_STATE/PROGRESS_LOG.md'), 'a', encoding='utf-8') as f:
    f.write(f'[{stamp}] {line}\n')
print('appended')
