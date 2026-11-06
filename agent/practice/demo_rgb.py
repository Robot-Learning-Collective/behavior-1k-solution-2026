"""Read-only RGB teacher access. No actions, states, contacts, scorer, or model calls."""
from pathlib import Path
import io,json,math,os,re,subprocess,sys
from PIL import Image,ImageDraw
import base64,hashlib

FPS=30
LAST_FRAME=26006
VIDEOS=('rgb-left.mp4','rgb-zed.mp4','rgb-right.mp4')

def requested_frames(times):
    if isinstance(times,(int,float)) and not isinstance(times,bool):times=[times]
    if not isinstance(times,list) or not 1<=len(times)<=6:raise ValueError('reference_time requires one timestamp or 1–6 timestamps in seconds')
    if any(type(t) not in (int,float) or not math.isfinite(t) or t<0 or t*FPS>=LAST_FRAME+1 for t in times):raise ValueError('Human RGB times must be finite in [0,866.9), at30Hz')
    return [int(math.floor(t*FPS+1e-7)) for t in times]

def frame(path,n):
    run=subprocess.run(['ffmpeg','-nostdin','-hide_banner','-threads','1','-copyts','-ss',f'{n/FPS:.9f}','-i',str(path),'-vf','showinfo','-frames:v','1','-f','image2pipe','-vcodec','png','-threads','1','pipe:1'],capture_output=True,timeout=30,check=True)
    pts=re.search(rb'n:\s*0\s+pts:.*?pts_time:([\d.]+)',run.stderr)
    if not pts or abs(float(pts[1])-n/FPS)>1e-3:raise RuntimeError('Actual decoded source PTS does not match declared frame; no nearby-frame fallback')
    image=Image.open(io.BytesIO(run.stdout)).convert('RGB')
    return image,hashlib.sha256(run.stdout).hexdigest(),float(pts[1])

def observe(times):
    indices=requested_frames(times)
    root=Path(os.environ['ASTRA_HUMAN_RGB_DIR'])
    full=len(indices)==1;w,h=(1440,500) if full else (1440,260*math.ceil(len(indices)/2))
    canvas=Image.new('RGB',(w,h),'black');draw=ImageDraw.Draw(canvas);records=[]
    for i,n in enumerate(indices):
        x,y=(0,0) if full else (i%2*720,i//2*260);tile=480 if full else 240
        draw.text((x+5,y+3),f'HUMAN recorded frame {n} | {n/FPS:.3f}s | LEFT WRIST | HEAD | RIGHT WRIST',fill='white')
        views=[]
        for j,name in enumerate(VIDEOS):
            im,sha,pts=frame(root/name,n);views.append({'source':name,'native_resolution':list(im.size),'decoded_png_sha256':sha,'actual_source_pts':pts});canvas.paste(im.resize((tile,tile)),(x+j*tile,y+20))
        records.append({'frame':n,'time_seconds':n/FPS,'views':views})
    buf=io.BytesIO();canvas.save(buf,format='JPEG',quality=86);data=buf.getvalue()
    return {'frames':records,'source':'Human episode004600/raw00230010, original RGB only; read-only sampled/seeked866.9s record, not live/not1x/not actions/proprio/object truth','width':w,'height':h,'image_bytes_sha256':hashlib.sha256(data).hexdigest(),'image_base64':base64.b64encode(data).decode()}

if __name__=='__main__':print(json.dumps(observe(json.load(sys.stdin)['reference_time'])))
