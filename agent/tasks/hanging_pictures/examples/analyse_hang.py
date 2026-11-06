"""Offline only: deterministic 8-episode human hanging study; no sim imports/calls."""
import json, pathlib, sys, glob
import numpy as np
import pandas as pd
ROOT=pathlib.Path(__file__).parents[1]
CACHE=pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
META=pathlib.Path.home()/'Downloads/behavior-challenge-2026-metadata-4f50b447'
sys.path.insert(0,str(ROOT/'client_helpers'))
from robot_kinematics import RobotModel
model=RobotModel()
# Calibrate model-local pad-ray endpoints from our prior PUBLIC self-state receipt.
receipt=json.loads(pathlib.Path(sorted(glob.glob('/tmp/pictures-run-009_obs/pictures-run-009-v4-a06/receipt*.json'))[0]).read_text())
robot=receipt['robot']; links=model.all_link_poses(robot)
pad_local=[]
for field,link in [('ag_start_point_body','right_gripper_finger_link1'),('ag_end_point_body','right_gripper_finger_link2')]:
    pad_local.append((link,(np.linalg.inv(links[link])@np.r_[robot['right']['own_links_body'][field],1])[:3]))
IDS=[6846,6854,6863,6878,6935,6958,6974,6984]
episodes=pd.read_parquet(CACHE/'episodes.parquet')
frames=pd.concat([pd.read_parquet(CACHE/n) for n in ['data.parquet','study-data-1.parquet']])
result=[]
for ep in IDS:
    meta=episodes[episodes.episode_index==ep].iloc[0]
    ann=json.loads((META/meta.annotation_path).read_text())
    hang=[a for a in ann['skill_annotation'] if 'hang' in a['skill_description']]
    f=frames[frames.episode_index==ep].sort_values('frame_index')
    h=np.stack(f['observation.state']);a=np.stack(f.action)
    assert np.array_equal(f.frame_index,np.arange(len(f)))
    start,end=hang[0]['frame_duration'];end=min(end,len(f)-1)
    releases=(np.where((a[1:,22]>0)&(a[:-1,22]<=0))[0]+1).tolist()
    releases=[i for i in releases if start<=i<=end+30]
    r=releases[-1] if releases else end
    # Integrate measured BODY velocity into an approximate episode-start frame.
    odom=np.zeros((len(h),3))
    for i in range(1,len(h)):
        vx,vy,w=h[i,:3];t=odom[i-1,2]
        odom[i]=odom[i-1]+np.array([np.cos(t)*vx-np.sin(t)*vy,np.sin(t)*vx+np.cos(t)*vy,w])/30
    world=[]
    for i,p in enumerate(h[:,42:45]):
        t=odom[i,2];world.append([odom[i,0]+np.cos(t)*p[0]-np.sin(t)*p[1],odom[i,1]+np.sin(t)*p[0]+np.cos(t)*p[1],p[2]])
    world=np.array(world)
    keys=sorted(set([start,max(start,r-120),max(start,r-60),max(start,r-30),r,min(r+15,len(h)-1),min(r+45,len(h)-1),end]))
    samples=[]
    for i in keys:
        q=h[i];p,R,_=model.arm('right',q[53:57],q[28:35])
        joint_map={f'torso_joint{k+1}':v for k,v in enumerate(q[53:57])}
        joint_map.update({f'right_arm_joint{k+1}':v for k,v in enumerate(q[28:35])})
        joint_map.update({f'right_gripper_finger_joint{k+1}':v for k,v in enumerate(q[49:51])})
        pads=[(model.pose(link,joint_map)@np.r_[v,1])[:3].tolist() for link,v in pad_local]
        samples.append(dict(model_pad_ray_endpoints=pads,frame=i,time=i/30,arm_right=q[28:35].tolist(),arm_left=q[3:10].tolist(),torso=q[53:57].tolist(),eef=q[42:45].tolist(),quat_xyzw=q[45:49].tolist(),fingers=q[49:51].tolist(),grip_command=float(a[i,22]),base_velocity=q[:3].tolist(),approx_odom=odom[i].tolist(),approx_world_eef=world[i].tolist(),fk_eef=p.tolist(),fk_axes=R.tolist()))
    row=dict(episode=ep,instance=int(meta.task_instance_id),annotation=meta.annotation_path,hang=[start,end],release_commands=releases,video_shard=int(meta['videos/observation.rgb.zed_link_camera_0/file_index']),video_start=float(meta['videos/observation.rgb.zed_link_camera_0/from_timestamp']),samples=samples,pre_release_z_range=h[max(start,r-120):r+1,44].tolist(),last_second_world_delta=(world[r]-world[max(start,r-30)]).tolist(),last_four_seconds_world_delta=(world[r]-world[max(start,r-120)]).tolist(),withdraw_world_delta=(world[min(r+45,len(h)-1)]-world[r]).tolist(),peak_last_four_seconds_height=float(h[max(start,r-120):r+1,44].max()),release_height=float(h[r,44]),grip_before=float(h[max(start,r-15),49:51].sum()))
    row['approach_height_delta']=float(h[r,44]-h[start,44])
    row['last_second_body_delta']=(h[r,42:45]-h[max(start,r-30),42:45]).tolist()
    row['last_second_orientation_change_deg']=float(np.degrees(2*np.arccos(np.clip(abs(np.dot(h[r,45:49],h[max(start,r-30),45:49])),0,1))))
    widths=h[:,49:51].sum(1)
    opened=np.where(widths[r:]>0.08)[0];row['full_open_frame']=int(r+opened[0]) if len(opened) else None
    row['model_pad_local_offsets']=[(n,v.tolist()) for n,v in pad_local]
    result.append(row)
(CACHE/'hang-study-measurements.json').write_text(json.dumps(result,indent=2))
(ROOT/'examples/hang-study-measurements.json').write_text(json.dumps(result,indent=2))
for r in result:
 print(r['episode'],'hang',r['hang'],'release',r['release_commands'],'gap',round(r['grip_before'],4),'height',round(r['release_height'],3),'drop',round(r['peak_last_four_seconds_height']-r['release_height'],3),'last1',np.round(r['last_second_world_delta'],3),'last4',np.round(r['last_four_seconds_world_delta'],3),'withdraw',np.round(r['withdraw_world_delta'],3))
