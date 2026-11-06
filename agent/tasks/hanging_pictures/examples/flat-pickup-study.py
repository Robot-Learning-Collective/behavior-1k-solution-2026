"""Recorded RGB/proprio only: three pickup segments and adjacent handovers, no sim RPC."""
import json, pathlib, subprocess
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
P=pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
E=pd.read_parquet(P/'episodes.parquet')
D=pd.concat([pd.read_parquet(P/n) for n in ['data.parquet','study-data-1.parquet']])
# Contact windows every five frames, plus approach/lift and adjacent transfer phases.
windows={6846:([729,800,900]+list(range(938,979,5))+[1000,1050,1092], [1092,1170,1200]+list(range(1214,1255,5))+[1300,1400,1482]),
6854:([688,800,900]+list(range(928,969,5))+[1000,1100,1200,1288,1350,1410], [1410,1724,1814,1842,1844,1849,1860,1891]),
6878:([493,600,670]+list(range(697,738,5))+[770,807], [807,950,1000]+list(range(1029,1070,5))+[1100,1131,1200,1548])}
out=[]
for ep,groups in windows.items():
 meta=E[E.episode_index==ep].iloc[0];f=D[D.episode_index==ep].sort_values('frame_index');h=np.stack(f['observation.state']);a=np.stack(f.action)
 assert np.array_equal(f.frame_index,np.arange(len(f))) and h.shape[1]==61 and a.shape[1]==23
 for group,frames in enumerate(groups):
  sheet=Image.new('RGB',(1280,320*((len(frames)+3)//4)));draw=ImageDraw.Draw(sheet)
  for j,i in enumerate(frames):
   dest=P/f'pickup-{ep}-{i}.jpg'
   if not dest.exists():subprocess.run(['ffmpeg','-v','error','-ss',str(float(meta['videos/observation.rgb.zed_link_camera_0/from_timestamp'])+i/30),'-i',str(P/f'study-head-{int(meta["videos/observation.rgb.zed_link_camera_0/file_index"])}.mp4'),'-frames:v','1','-y',str(dest)],check=True)
   sheet.paste(Image.open(dest).resize((320,320)),((j%4)*320,(j//4)*320));draw.text(((j%4)*320+5,(j//4)*320+5),f'{ep} frame {i}',fill='red',stroke_width=1,stroke_fill='white')
   out.append(dict(episode=ep,frame=i,annotation=meta.annotation_path,right_q=h[i,28:35].tolist(),left_q=h[i,3:10].tolist(),torso=h[i,53:57].tolist(),right_tcp=h[i,42:45].tolist(),right_quat=h[i,45:49].tolist(),right_fingers=h[i,49:51].tolist(),left_tcp=h[i,17:20].tolist(),left_quat=h[i,20:24].tolist(),left_fingers=h[i,24:26].tolist(),left_grip_command=float(a[i,14]),right_grip_command=float(a[i,22])))
  sheet.save(P/f'pickup-{ep}-group{group}.jpg');print(ep,group,len(frames),flush=True)
pathlib.Path(__file__).with_name('flat-pickup-study-measurements.json').write_text(json.dumps(out,indent=2)+'\n')
