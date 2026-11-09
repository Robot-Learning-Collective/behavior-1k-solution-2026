"""Fetch bounded public RGB samples for two patio demos; no simulator imports.
Run /usr/bin/python3 from any cwd. Large/cache outputs stay outside Workbench.
"""
import json
import subprocess
import sys
from pathlib import Path

CACHE = Path.home() / 'Downloads/behavior-challenge-2026-samples/clean_a_patio'
REV = '4f50b44796641a4d526a19d9aeadc8aa51e2f2c2'
BASE = f'https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/resolve/{REV}'
FFMPEG = 'ffmpeg'
# Include approach before and withdrawal after annotated sweep.
CHAIRS = '--chairs' in sys.argv
PATH = '--path' in sys.argv
PATH_END = '--path-end' in sys.argv
SUFFIX = '-path-end' if PATH_END else ('-path' if PATH else ('-chairs' if CHAIRS else ''))
SEGMENTS = ({7217: (11040, 11250), 7218: (10230, 10450)} if PATH_END else
            {7217: (10620, 10920), 7218: (9700, 9940)} if PATH else
            {7217: (4612, 5359), 7218: (4032, 4477)} if CHAIRS else
            {7217: (2193, 2340), 7218: (3657, 3861)})
CAMERAS = {'head': 'zed_link_camera_0', 'left': 'left_realsense_link_camera_0', 'right': 'right_realsense_link_camera_0'}

for ep, (start, end) in SEGMENTS.items():
    meta = json.loads((CACHE / f'episode-{ep}-metadata.json').read_text())
    out = CACHE / f'study-{ep}{SUFFIX}'
    out.mkdir(exist_ok=True)
    for cam, feature in CAMERAS.items():
        key = f'videos/observation.rgb.{feature}'
        url = f"{BASE}/{key}/chunk-{meta[key+'/chunk_index']:03d}/file-{meta[key+'/file_index']:03d}.mp4"
        offset = meta[key+'/from_timestamp']
        cmd = [FFMPEG, '-hide_banner', '-loglevel', 'error', '-ss', str(offset + start/30), '-i', url,
               '-t', str((end-start)/30), '-vf', 'select=not(mod(n\\,10))', '-vsync', '0',
               '-q:v', '2', '-y', str(out / f'{cam}-%03d.jpg')]
        subprocess.run(cmd, check=True)
        print(f'READY episode{ep} {cam} frames{start}:{end}:10', flush=True)
    if CHAIRS or PATH or PATH_END:
        continue
    # Whole-episode navigation overview, original head samples every15seconds.
    feature = CAMERAS['head']; key = f'videos/observation.rgb.{feature}'
    url = f"{BASE}/{key}/chunk-{meta[key+'/chunk_index']:03d}/file-{meta[key+'/file_index']:03d}.mp4"
    subprocess.run([FFMPEG, '-hide_banner', '-loglevel', 'error', '-ss', str(meta[key+'/from_timestamp']),
                    '-i', url, '-t', str(meta['length']/30), '-vf', 'select=not(mod(n\\,450))',
                    '-vsync', '0', '-q:v', '3', '-y', str(out/'overview-%03d.jpg')], check=True)
    print(f'READY episode{ep} whole-episode head overview', flush=True)
(CACHE/('path-end-study-selection.json' if PATH_END else 'path-study-selection.json' if PATH else 'chair-study-selection.json' if CHAIRS else 'study-selection.json')).write_text(json.dumps({'revision':REV,'segments':SEGMENTS,'stride_frames':10,'overview_stride_frames':450},indent=2)+'\n')
