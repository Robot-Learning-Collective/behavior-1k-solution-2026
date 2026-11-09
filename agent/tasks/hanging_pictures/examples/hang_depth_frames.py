"""Range-seek public depth at eight sampled human hang segments (offline)."""
import json,pathlib,subprocess,concurrent.futures
import pandas as pd,numpy as np
P=pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
E=pd.read_parquet(P/'episodes.parquet');D=json.loads((P/'hang-study-measurements.json').read_text())
BASE='https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/resolve/4f50b44796641a4d526a19d9aeadc8aa51e2f2c2/'
jobs=[]
for r in D:
 m=E[E.episode_index==r['episode']].iloc[0];key='videos/observation.depth_linear.zed_link_camera_0';url=BASE+f'{key}/chunk-{int(m[key+"/chunk_index"]):03d}/file-{int(m[key+"/file_index"]):03d}.mp4'
 for frame in [r['hang'][0],r['release_commands'][-1]-30,min(r['release_commands'][-1]+47,r['hang'][1])]:
  jobs.append((r['episode'],frame,url,float(m[key+'/from_timestamp'])+frame/30))
def get(job):
 ep,f,url,t=job;out=P/f'depth-{ep}-{f}.npy'
 if out.exists():return
 raw=subprocess.run(['ffmpeg','-v','error','-rw_timeout','60000000','-ss',str(t),'-i',url,'-frames:v','1','-f','rawvideo','-pix_fmt','gray12le','pipe:1'],capture_output=True,timeout=150)
 if raw.returncode:raise RuntimeError(raw.stderr.decode()[-1000:])
 q=np.frombuffer(raw.stdout,dtype='<u2').reshape(720,720);assert q.max()<=4095
 z=np.exp(np.log(3.51)+q.astype(np.float32)/4095*(np.log(13.5)-np.log(3.51)))-3.5
 np.save(out,z);print('DONE',ep,f,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(get,jobs))
