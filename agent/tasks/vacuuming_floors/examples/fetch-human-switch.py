"""Bounded public demo study: acquisition -> switch -> departure, two episodes.
No simulator imports. Cache stays outside Workbench. RGB n uses pose row n-1.
"""
import json
import sys
import subprocess
import urllib.request
from pathlib import Path
import pyarrow.parquet as pq
import pyarrow.compute as pc
from PIL import Image, ImageDraw

REV = '4f50b44796641a4d526a19d9aeadc8aa51e2f2c2'
BASE = f'https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/resolve/{REV}'
CACHE = Path.home() / 'Downloads/behavior-challenge-2026-samples/vacuuming_floors'
CACHE.mkdir(parents=True, exist_ok=True)
PHASE = 'cleaning' if '--cleaning' in sys.argv else 'switch'
SEGMENTS = ({13814: (780, 1240), 13815: (780, 1760)} if PHASE == 'cleaning'
            else {13814: (240, 810), 13815: (210, 810)})
CAMS = {'head': 'zed_link_camera_0', 'left': 'left_realsense_link_camera_0', 'right': 'right_realsense_link_camera_0'}

def fetch(remote, local):
    if not local.exists():
        urllib.request.urlretrieve(f'{BASE}/{remote}', str(local) + '.partial')
        Path(str(local) + '.partial').rename(local)
    return local

meta = pq.read_table(fetch('meta/episodes/chunk-069/file-000.parquet', CACHE/'episodes.parquet'))
for ep, (start, end) in SEGMENTS.items():
    rows = meta.filter(pc.equal(meta['episode_index'], ep)).to_pylist()
    assert len(rows) == 1
    m = rows[0]
    (CACHE/f'episode-{ep}-metadata.json').write_text(json.dumps(m, indent=2))
    remote = f"data/chunk-{m['data/chunk_index']:03d}/file-{m['data/file_index']:03d}.parquet"
    data = pq.read_table(fetch(remote, CACHE/f"data-{m['data/chunk_index']}-{m['data/file_index']}.parquet"))
    data = data.filter(pc.equal(data['episode_index'], ep)).sort_by([('frame_index', 'ascending')])
    assert len(data) == m['length']
    pq.write_table(data, CACHE/f'episode-{ep}-frames.parquet')
    out = CACHE/f'{PHASE}-study-{ep}'; out.mkdir(exist_ok=True)
    for cam, feature in CAMS.items():
        key = f'videos/observation.rgb.{feature}'
        url = f"{BASE}/{key}/chunk-{m[key+'/chunk_index']:03d}/file-{m[key+'/file_index']:03d}.mp4"
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(m[key+'/from_timestamp']+start/30), '-i', url, '-t', str((end-start)/30), '-vf', 'select=not(mod(n\\,10))', '-vsync', '0', '-q:v', '2', '-y', str(out/f'{cam}-%03d.jpg')], check=True)
        print(f'READY {ep} {cam} {start}:{end}:10', flush=True)
    frames = sorted(out.glob('head-*.jpg'))
    for page in range((len(frames)+7)//8):
        sheet = Image.new('RGB', (640, 1010), 'white'); draw = ImageDraw.Draw(sheet)
        for j, head in enumerate(frames[page*8:(page+1)*8]):
            idx = int(head.stem.split('-')[1]); frame = start+(idx-1)*10
            x,y = (j%4)*160,(j//4)*505
            draw.text((x+2,y+2), f'{ep} f{frame} pose{frame-1}', fill='black')
            for c,cam in enumerate(CAMS):
                im = Image.open(out/f'{cam}-{idx:03d}.jpg').convert('RGB'); im.thumbnail((160,160))
                sheet.paste(im,(x,y+23+c*160))
        sheet.save(out/f'contact-{page+1}.jpg',quality=90)
    print(f'READY {ep} aligned frames and {page+1} contact sheets', flush=True)
(CACHE/f'{PHASE}-study-selection.json').write_text(json.dumps({'revision':REV,'segments':SEGMENTS,'stride':10,'rgb_pose_lag':1,'rgb_velocity_action_lag':2},indent=2))
