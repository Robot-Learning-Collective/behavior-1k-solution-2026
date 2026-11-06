"""Offline RGBD-derived a07 pre-seat poster-to-nail alignment; no RPC."""
import json, os, sys
from pathlib import Path
import numpy as np
RUN=Path(__file__).resolve().parents[1]
os.environ.setdefault('BEHAVIOR_SIM_RUN_DIR',str(RUN))
sys.path.insert(0,str(RUN))
import sim_client as s
refs=json.loads((RUN/'examples/hang-v1-a07-retained.json').read_text())['receipts']
def old(i): return json.load(open(next(r['receipt'] for r in refs if r['observation_id']==i)))
def rz(a):
 c,t=np.cos(a),np.sin(a)
 return np.array([[c,-t,0],[t,c,0],[0,0,1]])
def normal(p):
 p=p.reshape(-1,3); n=np.linalg.svd(p-p.mean(0),full_matrices=False)[2][-1]
 return n*np.sign(n[0])
def frame(x,lp,rp):
 n=normal(x[190:260,335:385]); l=x[lp[1],lp[0]];r=x[rp[1],rp[0]]
 t=l-r;t-=n*(t@n);t/=np.linalg.norm(t)
 return np.column_stack([n,t,np.cross(n,t)]),(l+r)/2
ref=old(447); earlier=old(372); current=s.last_obs()
a=earlier['robot']['simulator_base_odom'];b=ref['robot']['simulator_base_odom']
nail_old=rz(-b['yaw_world_rad'])@(rz(a['yaw_world_rad'])@s.xyz('head',obs=earlier)[157,348]+np.array(a['position_world'])-np.array(b['position_world']))
xo=s.xyz('head',obs=ref);xn=s.xyz('head',obs=current)
# Visually checked black top-frame points, a few pixels inside the frame.
Fo,po=frame(xo,(317,108),(464,78));Fn,pn=frame(xn,(320,175),(451,172))
wo=normal(xo[30:80,510:600]);wn=normal(xn[30:80,510:600]);yaw=np.arctan2(wn[1],wn[0])-np.arctan2(wo[1],wo[0]);Z=rz(yaw)
nail_new=xn[130,384];target=nail_new+Z@(po-nail_old)
R=Z@Fo@Fn.T;th=np.arccos(np.clip((np.trace(R)-1)/2,-1,1));rv=np.degrees(th)/(2*np.sin(th))*np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])
tcp=np.array(current['robot']['right']['eef_position']);pivot_delta=(R-np.eye(3))@(tcp-pn)
result={'old_nail':nail_old.tolist(),'new_nail':nail_new.tolist(),'old_top':po.tolist(),'current_top':pn.tolist(),'target_top':target.tolist(),'rotation_xyz_deg':rv.tolist(),'pivot_delta':pivot_delta.tolist(),'translation_after_rotation':(target-pn).tolist(),'wall_normal':wn.tolist()}
print(json.dumps(result,indent=2))
(RUN/'examples/recovery-geometric-alignment.json').write_text(json.dumps(result,indent=2)+'\n')
