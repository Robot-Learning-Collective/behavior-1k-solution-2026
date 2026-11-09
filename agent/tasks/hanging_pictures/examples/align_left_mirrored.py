"""RGBD-only mirror of successful oblique seating geometry for a left-side grasp; no motor call."""
import json, pathlib, sys, numpy as np
import practice_client as s
sys.modules['sim_client']=s
RUN=pathlib.Path(__file__).resolve().parents[1]
ns={'__file__':str(RUN/'examples/align_saved_nail.py')}
exec((RUN/'examples/align_saved_nail.py').read_text().split('ref=old(447)')[0],ns)
old,rz,normal,frame=(ns[k] for k in ['old','rz','normal','frame'])
ref=old(447);early=old(372);current=s.last_obs()
a=early['robot']['simulator_base_odom'];b=ref['robot']['simulator_base_odom']
no=rz(-b['yaw_world_rad'])@(rz(a['yaw_world_rad'])@s.xyz('head',obs=early)[157,348]+np.array(a['position_world'])-np.array(b['position_world']))
xo=s.xyz('head',obs=ref);xn=s.xyz('head',obs=current)
Fo,po=frame(xo,(317,108),(464,78));wo=normal(xo[30:80,510:600]);wo[2]=0;wo/=np.linalg.norm(wo)
n=normal(xn[355:425,175:250]);l=xn[337,80];r=xn[276,300];t=l-r;t-=n*(t@n);t/=np.linalg.norm(t)
Fn=np.column_stack((n,t,np.cross(n,t)));pn=(l+r)/2
wn=normal(xn[100:200,80:250]);wn[2]=0;wn/=np.linalg.norm(wn)
Z=rz(np.arctan2(wn[1],wn[0])-np.arctan2(wo[1],wo[0]))
M=2*np.outer(wo,wo)+2*np.diag([0,0,1])-np.eye(3)
Ft=Z@M@Fo@np.diag([1,-1,1]);nail=xn[63,201];target=nail+Z@M@(po-no)
R=Ft@Fn.T;th=np.arccos(np.clip((np.trace(R)-1)/2,-1,1));rv=np.degrees(th)/(2*np.sin(th))*np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])
tcp=np.array(current['robot']['left']['eef_position']);pivot=(R-np.eye(3))@(tcp-pn)
out={'current_receipt_observation':current['observation_id'],'new_nail':nail.tolist(),'current_top':pn.tolist(),'target_top':target.tolist(),'rotation_xyz_deg':rv.tolist(),'pivot_delta':pivot.tolist(),'translation_after_rotation':(target-pn).tolist(),'wall_normal':wn.tolist(),'mirror_hypothesis':True,'target_normal':Ft[:,0].tolist()}
print(json.dumps(out,indent=2));(RUN/'examples/instance262-left-mirrored-align.json').write_text(json.dumps(out,indent=2)+'\n')
