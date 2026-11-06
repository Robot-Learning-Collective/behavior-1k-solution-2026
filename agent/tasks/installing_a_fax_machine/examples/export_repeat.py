"""Offline export of this run's public commands and endpoint self-state; no RPC."""
import json
import sys
from pathlib import Path

run = Path(__file__).resolve().parents[1]
suffix = sys.argv[1] if len(sys.argv) > 1 else 'a02'
protocol = sys.argv[2] if len(sys.argv) > 2 else 'v4'
attempt = 'fax-run-008-' + protocol + '-' + suffix
rows = [json.loads(s) for s in (run / 'control-action-results.jsonl').read_text().splitlines()]
rows = [r for r in rows if r.get('attempt_id') == attempt]
receipts = {}
receipt_root = Path(sys.argv[3]) if len(sys.argv) > 3 else Path('/tmp/fax-run-008-p6-918bba' if protocol == 'v6' else '/tmp/fax-run-008_obs')
for p in sorted((receipt_root / attempt).glob('receipt_*.json')):
    r = json.loads(p.read_text())
    if not r.get('call_failure'):
        receipts[r['observation_id']] = (p, r)
parts = [f'# {suffix} exact public action sequence\n\nHistorical record, not a blind replay script. Includes unsuccessful recovery motions and rejected requests; inspect images and remeasure before contacts. All arguments preserved, including max_steps.\n']
for i, row in enumerate(rows, 1):
    oid = row.get('last_observation_id')
    parts.append(f'## {i}. {row["intent"]}\n\n```python\ns.act(**{row["requested"]!r})\n```\nResult: {row.get("reason")}; observation {oid}.\n')
    if oid in receipts:
        p, r = receipts[oid]
        parts.append(f'Receipt: `{p}`\nImage: `{r["local_image_path"]}`\nSim seconds: {r["simulated_seconds"]}\n\n```text\n{r["compact_state"]}\n```\n')
(run / 'examples' / f'repeat-{suffix}-exact.md').write_text('\n'.join(parts))
print(f'Exported {len(rows)} public requests and endpoint states')
