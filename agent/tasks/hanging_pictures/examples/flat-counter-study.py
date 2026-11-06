"""Recorded public flat-counter pickup and neighbouring phases; no simulator calls."""
import json, pathlib, subprocess, sys
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
P = pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
E = pd.read_parquet(P/'episodes.parquet')
D = pd.read_parquet(P/'data.parquet')
windows = {
6807: ([478,700,900,976]+list(range(1001,1042,5))+[1080,1120,1167], [1168,1400,1759,2000,2300,2522]+list(range(2542,2573,5))+[2600,2718]),
6816: ([755,1200,1800,2402,2800,2986]+list(range(3021,3062,5))+[3100,3200,3300,3465], [3465,3722,4000,4450,4523]+list(range(4543,4574,5))+[4600,4640]),
6823: ([748,1000,1279,1400,1486]+list(range(1511,1552,5))+[1580,1650,1750,1818], [1818,2000,2145,2500,2753]+list(range(2773,2804,5))+[2830,2894])}
out=[]
for ep,groups in windows.items():
    meta=E[E.episode_index==ep].iloc[0]
    f=D[D.episode_index==ep].sort_values('frame_index')
    h=np.stack(f['observation.state']); a=np.stack(f.action)
    idx=int(meta['videos/observation.rgb.zed_link_camera_0/file_index'])
    video=P/('head.mp4' if idx==0 else f'study-head-{idx}.mp4')
    for group,frames in enumerate(groups):
        im=Image.new('RGB',(1280,320*((len(frames)+3)//4)));draw=ImageDraw.Draw(im)
        for j,i in enumerate(frames):
            dest=P/f'flat-counter-{ep}-{i}.jpg'
            if not dest.exists():
                subprocess.run(['ffmpeg','-v','error','-ss',str(float(meta['videos/observation.rgb.zed_link_camera_0/from_timestamp'])+i/30),'-i',str(video),'-frames:v','1','-y',str(dest)],check=True)
            im.paste(Image.open(dest).resize((320,320)),((j%4)*320,(j//4)*320))
            draw.text(((j%4)*320+5,(j//4)*320+5),f'{ep} frame {i}',fill='red',stroke_width=1,stroke_fill='white')
            out.append(dict(episode=ep,frame=i,annotation=meta.annotation_path,right_q=h[i,28:35].tolist(),left_q=h[i,3:10].tolist(),torso=h[i,53:57].tolist(),right_tcp=h[i,42:45].tolist(),right_quat=h[i,45:49].tolist(),right_fingers=h[i,49:51].tolist(),left_tcp=h[i,17:20].tolist(),left_quat=h[i,20:24].tolist(),left_fingers=h[i,24:26].tolist(),right_grip_command=float(a[i,22]),left_grip_command=float(a[i,14])))
        im.save(P/f'flat-counter-{ep}-group{group}.jpg')
        print(ep,group,len(frames),flush=True)
pathlib.Path(__file__).with_name('flat-counter-study-measurements.json').write_text(json.dumps(out,indent=2)+'\n')
