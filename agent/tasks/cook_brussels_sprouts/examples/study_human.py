"""Public TRAIN demo study only; no live simulator RPC or hidden scene state."""
import argparse, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import pyarrow.parquet as pq
import numpy as np

ROOT = Path('<demo-samples>/cook_brussels_sprouts')
parser = argparse.ArgumentParser()
parser.add_argument('--study', choices=['cut', 'tray'], default='cut')
args = parser.parse_args()
OUT = ROOT / ('three-episode-study' if args.study == 'cut' else 'three-episode-tray-study')
OUT.mkdir(exist_ok=True)
REV = '4f50b44796641a4d526a19d9aeadc8aa51e2f2c2'
BASE = f'https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/resolve/{REV}'
WINDOWS = ({19000: (10020, 11010), 19001: (8610, 9420), 19002: (5580, 6620)} if args.study == 'cut'
           else {19000: (7650, 8850), 19001: (7050, 7860), 19002: (4200, 4920)})
META = {r['episode_index']: r for r in pq.read_table(ROOT/'episodes.parquet').to_pylist()}
DATA = pq.read_table(ROOT/'data-000.parquet', columns=['episode_index','frame_index','timestamp','observation.state','action']).to_pylist()
ROWS = {(r['episode_index'], r['frame_index']): r for r in DATA}
CAMERAS = {'head':'zed_link_camera_0','left':'left_realsense_link_camera_0','right':'right_realsense_link_camera_0'}
manifest = []
for ep, (start, end) in WINDOWS.items():
    meta = META[ep]
    entry = {'episode':ep,'raw_episode_id':meta['raw_episode_id'],'task_instance_id':meta['task_instance_id'],'revision':REV,'frame_window':[start,end],'cameras':{}}
    records = []
    for n in range(start, end, 15):
        p = np.array(ROWS[ep,n-1]['observation.state'])
        a = np.array(ROWS[ep,n-2]['action'])
        records.append({'rgb_frame':n,'rgb_seconds':n/30,'position_source_row':n-1,'action_source_row':n-2,
            'measured':{'left_q':p[3:10].tolist(),'right_q':p[28:35].tolist(),'torso_q':p[53:57].tolist(),'left_grip':p[24:26].tolist(),'right_grip':p[49:51].tolist(),'left_eef':p[17:24].tolist(),'right_eef':p[42:49].tolist()},
            'action':{'base':a[:3].tolist(),'torso_q':a[3:7].tolist(),'left_q':a[7:14].tolist(),'left_grip_native':a[14],'right_q':a[15:22].tolist(),'right_grip_native':a[22]}})
    (OUT/f'{ep}-aligned.json').write_text(json.dumps(records,indent=2))
    for name, feature in CAMERAS.items():
        key = 'videos/observation.rgb.'+feature
        offset = meta[key+'/from_timestamp']
        path = f'{key}/chunk-{meta[key+"/chunk_index"]:03d}/file-{meta[key+"/file_index"]:03d}.mp4'
        entry['cameras'][name] = {'url':BASE+'/'+path,'seek':offset+start/30,'duration':(end-start)/30,'output':str(OUT/f'{ep}-{name}.mp4')}
    manifest.append(entry)
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2))

def fetch(item):
    ep, name, v = item
    if Path(v['output']).exists(): return
    print(f'FETCH {ep} {name}',flush=True)
    subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',str(v['seek']),'-i',v['url'],'-t',str(v['duration']),'-an','-c:v','libx264','-preset','ultrafast','-crf','23','-y',v['output']],check=True,timeout=240)
    print(f'DONE {ep} {name}',flush=True)
with ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(fetch,[(e['episode'],n,v) for e in manifest for n,v in e['cameras'].items()]))
print('ALL_CLIPS_READY',flush=True)
