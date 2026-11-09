"""Public human RGBD plane/nail estimates, static R1Pro head calibration.
No simulator state query; integrated odometry is an approximation, not truth.
"""
import pathlib,json,sys
import pandas as pd,numpy as np
P=pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
R=pathlib.Path(__file__).parents[1];sys.path.insert(0,str(R/'client_helpers'))
from robot_kinematics import quaternion_matrix
D=json.loads((P/'hang-study-measurements.json').read_text())
F=pd.concat([pd.read_parquet(P/n) for n in ['data.parquet','study-data-1.parquet']])
# Native720 head pixels selected manually from original RGB; rectangle is wall-only.
settings={6846:((256,164),(450,520),(280,230)),6854:((270,140),(480,530),(280,230)),6863:((362,194),(420,470),(315,250)),6878:((122,134),(360,420),(200,210)),6935:((298,224),(400,470),(270,250)),6958:((228,148),(430,480),(290,220)),6974:((282,172),(460,520),(290,230)),6984:((314,196),(430,490),(290,250))}
def cloud(ep,frame,tab):
 z=np.load(P/f'depth-{ep}-{frame}.npy');v,u=np.indices(z.shape)
 cam=np.stack([(u+.5-360)*z/306,(v+.5-360)*z/306,z],-1)
 # Camera pose is measured robot-relative graphics frame. Position group lag1.
 pose=tab.iloc[max(0,frame-1)]['observation.robot2cam_pose.zed_link_camera_0']
 rot=quaternion_matrix(pose[3:])@np.diag([1,-1,-1])
 return cam@rot.T+pose[:3]
out=[]
for r in D:
 ep=r['episode'];f=F[F.episode_index==ep].sort_values('frame_index');nailpix,xs,posterpx=settings[ep];start=r['hang'][0];pre=r['release_commands'][-1]-30
 x=cloud(ep,pre,f);p=x[20:80,xs[0]:xs[1]].reshape(-1,3);c=p.mean(0);n=np.linalg.svd(p-c,full_matrices=False)[2][-1];n*=np.sign(n[0]);d=float(n@c)
 u,v=posterpx;pp=x[v-3:v+4,u-3:u+4].reshape(-1,3).mean(0)
 q=next(s for s in r['samples'] if s['frame']==pre)
 a=cloud(ep,start,f);u,v=nailpix;nail=a[v,u]
 first=next(s for s in r['samples'] if s['frame']==start)
 def world(p,s):
  xx,yy,t=s['approx_odom'];c,ss=np.cos(t),np.sin(t);return np.array([xx+c*p[0]-ss*p[1],yy+ss*p[0]+c*p[1],p[2]])
 eef_nail=world(q['eef'],q)-world(nail,first)
 row=dict(episode=ep,pre_frame=pre,wall_normal_body=n.tolist(),wall_offset_m=d,wall_fit_rms=float(np.std(p@n)),poster_sample_body=pp.tolist(),poster_front_wall_gap_m=float(d-n@pp),eef_wall_gap_m=float(d-n@q['eef']),pad_wall_gaps_m=[float(d-n@pad) for pad in q['model_pad_ray_endpoints']],nail_start_pixel=list(nailpix),nail_start_body=nail.tolist(),approx_pre_eef_minus_nail= eef_nail.tolist())
 post=min(r['release_commands'][-1]+47,r['hang'][1]);xp=cloud(ep,post,f);wp=xp[20:80,xs[0]:xs[1]].reshape(-1,3);cp=wp.mean(0);nn=np.linalg.svd(wp-cp,full_matrices=False)[2][-1];nn*=np.sign(nn[0]);uu,vv=posterpx
 row['post_frame']=post;row['post_wall_rms']=float(np.std(wp@nn));row['post_poster_front_gap_m']=float(nn@cp-nn@xp[vv,uu])
 out.append(row);print(ep,'RMS',round(row['wall_fit_rms'],4),'front_gap',round(row['poster_front_wall_gap_m'],3),'pads',np.round(row['pad_wall_gaps_m'],3),'EEF-nail',np.round(eef_nail,3),'n',np.round(n,3))
(R/'examples/hang-study-geometry.json').write_text(json.dumps(out,indent=2))
