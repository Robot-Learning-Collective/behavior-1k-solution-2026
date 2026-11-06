"""Read-only three-demo RGB/proprio study. Large outputs stay in Downloads.
Usage: /usr/bin/python3 human_segment_study.py EP FRAME... [--label NAME]
Frames refer to RGB; measured state row=frame-1, source command row=frame-2.
"""
import argparse, json, sys
from pathlib import Path
import av, numpy as np, pyarrow.parquet as pq
from PIL import Image, ImageDraw
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'client_helpers'))
from robot_kinematics import RobotModel
p=argparse.ArgumentParser();p.add_argument('episode',type=int);p.add_argument('frames',type=int,nargs='+');p.add_argument('--label',default='study');a=p.parse_args()
root=Path.home()/'Downloads/behavior-challenge-2026-samples/unloading_the_car';out=root/'deep-study';out.mkdir(exist_ok=True)
meta=next(r for r in pq.read_table(root/'episodes.parquet').to_pylist() if r['episode_index']==a.episode)
t=pq.read_table(root/'data-shard.parquet',filters=[('episode_index','=',a.episode)]).to_pylist();model=RobotModel()
# Onboard velocity-integrated pose, relative start; uncalibrated drift, not object truth.
pose=np.zeros((len(t),3))
for n in range(1,len(t)):
 v=np.array(t[n]['observation.state'][:3]);x,y,h=pose[n-1];c,s=np.cos(h),np.sin(h)
 pose[n]=[x+(c*v[0]-s*v[1])/30,y+(s*v[0]+c*v[1])/30,h+v[2]/30]
records=[]
for f in a.frames:
 assert 2<=f<len(t)
 st=t[f-1]['observation.state'];ac=t[f-2]['action'];r={'rgb_frame':f,'seconds':f/30,'base_integrated_relative':pose[f-1].round(4).tolist(),'base_velocity':st[:3],'torso':st[53:57],'measured_state_61d':st,'recorded_action_23d':ac,'state_row':f-1,'action_row':f-2}
 for arm,qidx,gidx,ai in [('left',3,24,14),('right',28,49,22)]:
  q=st[qidx:qidx+7];tcp,R,_=model.arm(arm,st[53:57],q)
  r[arm]={'q':q,'tcp':tcp.round(4).tolist(),'finger_dir':R[:,2].round(4).tolist(),'close_dir':R[:,1].round(4).tolist(),'fingers':st[gidx:gidx+2],'grip_command':ac[ai]}
 records.append(r)
(out/f'{a.episode}-{a.label}.json').write_text(json.dumps(records,indent=2)+'\n')
containers={cam:av.open(str(root/f'{cam}-shard.mp4')) for cam in ['left','zed','right']}
images=[]
for rec in records:
 trip=Image.new('RGB',(840,390));d=ImageDraw.Draw(trip);d.text((4,3),f"ep{a.episode} f{rec['rgb_frame']} t{rec['seconds']:.3f}s",fill='white')
 x=0
 for cam,w in [('left',240),('zed',360),('right',240)]:
  feature={'left':'left_realsense','right':'right_realsense','zed':'zed'}[cam]+'_link_camera_0';target=meta[f'videos/observation.rgb.{feature}/from_timestamp']+rec['seconds'];c=containers[cam];stream=c.streams.video[0]
  c.seek(int(target/stream.time_base),stream=stream,backward=True)
  frame=next(fr for fr in c.decode(stream) if float(fr.pts*stream.time_base)>=target-1/60)
  im=frame.to_image().resize((w,w));trip.paste(im,(x,24));x+=w
 images.append(trip)
for start in range(0,len(images),8):
 batch=images[start:start+8];sheet=Image.new('RGB',(1680,390*((len(batch)+1)//2)))
 for i,im in enumerate(batch):sheet.paste(im,((i%2)*840,(i//2)*390))
 path=out/f'{a.episode}-{a.label}-{start//8:02}.jpg';sheet.save(path,quality=88);print(path)
for c in containers.values():c.close()
