"""Public original-RGB dense pickup/regrasp study; no simulator calls."""
import json,subprocess,sys
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path.home()/'Downloads/behavior-challenge-2026-samples/installing_smoke_detectors'
BASE='https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/resolve/4f50b44796641a4d526a19d9aeadc8aa51e2f2c2'
CAMERAS=['left_realsense','zed','right_realsense']
mount='--mount' in sys.argv
windows={12612:(3600,3840),12613:(2310,2540),12614:(2340,2580)} if mount else {12612:(1500,1740),12613:(1200,1470),12614:(1170,1380)}
for ep,(start,end) in windows.items():
    meta=json.loads((ROOT/f'episode-{ep}-metadata.json').read_text())
    out=ROOT/f'{"mount" if mount else "dense"}-{ep}';out.mkdir(exist_ok=True)
    frames=list(range(start,end,10))
    for cam in CAMERAS:
        key=f'videos/observation.rgb.{cam}_link_camera_0'
        url=f'{BASE}/{key}/chunk-{meta[key+"/chunk_index"]:03d}/file-{meta[key+"/file_index"]:03d}.mp4'
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(meta[key+'/from_timestamp']+start/30),'-i',url,'-t',str((end-start)/30),'-vf','select=not(mod(n\\,10))','-vsync','0','-q:v','2','-y',str(out/f'{cam}-%03d.jpg')],check=True)
    state=np.load(ROOT/f'state-{ep}.npy');samples=[]
    for i,n in enumerate(frames):
        q=state[n-1]
        samples.append({'rgb_frame':n,'position_row':n-1,'left_q':q[3:10].tolist(),'left_TCP':q[17:20].tolist(),'left_quat_xyzw':q[20:24].tolist(),'left_fingers':q[24:26].tolist(),'torso':q[53:57].tolist()})
    (out/'samples.json').write_text(json.dumps(samples,indent=2))
    for page in range((len(frames)+5)//6):
        subset=frames[page*6:page*6+6];im=Image.new('RGB',(720,260*len(subset)));d=ImageDraw.Draw(im)
        for row,n in enumerate(subset):
            i=frames.index(n)+1;d.text((5,row*260+3),f'ep{ep} RGB{n} t{n/30:.3f} position row{n-1} LEFT/HEAD/RIGHT',fill='white')
            for col,cam in enumerate(CAMERAS):
                src=out/f'{cam}-{i:03d}.jpg';assert src.exists(),src
                im.paste(Image.open(src).resize((240,240)),(col*240,row*260+20))
        im.save(out/f'page-{page}.jpg',quality=90)
    print('READY_DENSE',ep,len(frames),flush=True)
