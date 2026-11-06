"""Original human RGB plus source-mapped 61D measurements and 23D requests; no reward/object truth."""
from pathlib import Path
import json,os,sys
import numpy as np
import pyarrow.parquet as pq
import demo_rgb

FIELDS={'base_qvel':(0,3),'arm_left_qpos':(3,10),'arm_left_qvel':(10,17),'eef_left_pos':(17,20),'eef_left_quat':(20,24),'gripper_left_qpos':(24,26),'gripper_left_qvel':(26,28),'arm_right_qpos':(28,35),'arm_right_qvel':(35,42),'eef_right_pos':(42,45),'eef_right_quat':(45,49),'gripper_right_qpos':(49,51),'gripper_right_qvel':(51,53),'trunk_qpos':(53,57),'trunk_qvel':(57,61)}
VELOCITIES=[k for k in FIELDS if k.endswith('qvel')]
CONTRACT={'state_order':'OG eval_utils PROPRIOCEPTION_INDICES R1Pro, 61 floats; named groups preserve every value','arm_joint_order':'left_arm_joint1..7/right_arm_joint1..7','trunk_joint_order':'torso_joint1..4, all revolute radians','finger_joint_order':'left/right_gripper_finger_joint1..2, prismatic metres','units':'arm/trunk qpos rad, qvel rad/s; finger qpos m,qvel m/s; base_qvel BODY[vx,vy,wz] m/s,m/s,rad/s at fixedHF4f50; EEF pos metres/quat xyzw relative to robot articulation base, configured EEF link NOT calibrated jaw/pad/TCP','alignment':'Official HF4f50 positions row i≈S[i-1], velocities row i≈S[i], RGB row i≈S[i-2]. For RGB row n>=2: position groups from n-1, velocity groups from n-2, command from n-2. Exact row provenance below; renderer lag is source-reported, NOT simultaneous shutter/force/contact proof. First2 video frames have no complete aligned pair; explicit unavailable, never extrapolate.','requested_action_order':'base0:3 normalized BODY drive fractions; trunk3:7 absolute POSITION rad; left7:14 absolute POSITION rad; left grip14 native[-1closed,+1open]; right15:22 absolute POSITION rad; right grip22 native[-1closed,+1open]','command_scaling':'Human native base fraction multiplied[.75,.75,1]→requested physical BODY m/s,m/s,rad/s. Gripper equivalence for live act=(native+1)/2. Human arm POSITION targets are requests, not achieved q and NOT Cartesian deltas; do not paste seven numbers into live six-delta act.','absent':'No measured force/effort/contact/object-held/scorer truth, no measured absolute base/world/object pose in 61D. Measured finger aperture does not establish grasp.'}

def observe(times):
    rgb=demo_rgb.observe(times)
    table=pq.read_table(Path(os.environ['ASTRA_HUMAN_RGB_DIR']).parent/'frames.parquet',columns=['frame_index','timestamp','observation.state','action'])
    assert table.num_rows==26007
    needed=sorted({k for f in rgb['frames'] for k in (f['frame'],max(0,f['frame']-1),max(0,f['frame']-2))})
    rows={n:{c:table[c][n].as_py() for c in table.column_names} for n in needed}
    for f in rgb['frames']:
        n=f['frame'];row=rows[n];assert row['frame_index']==n and abs(row['timestamp']-n/30)<1e-4
        if n<2:f['aligned_proprio']={'available':False,'reason':'Beginning-edge: no complete lag-aligned earlier rows; RGB remains original.'};continue
        pos,vel=rows[n-1],rows[n-2];p=np.asarray(pos['observation.state']);v=np.asarray(vel['observation.state']);a=np.asarray(vel['action']);assert p.shape==v.shape==(61,) and a.shape==(23,) and np.isfinite(p).all() and np.isfinite(v).all() and np.isfinite(a).all()
        measured={k:(v if k in VELOCITIES else p)[lo:hi].tolist() for k,(lo,hi) in FIELDS.items()}
        requested={'base_native_fractions':a[:3].tolist(),'base_requested_BODY_velocity':(a[:3]*np.array([.75,.75,1])).tolist(),'trunk_POSITION_rad':a[3:7].tolist(),'left_POSITION_rad':a[7:14].tolist(),'left_native_grip':float(a[14]),'left_live_grip_equivalent':float((a[14]+1)/2),'right_POSITION_rad':a[15:22].tolist(),'right_native_grip':float(a[22]),'right_live_grip_equivalent':float((a[22]+1)/2)}
        f['aligned_proprio']={'available':True,'position_source_row':n-1,'velocity_source_row':n-2,'command_source_row':n-2,'position_row_timestamp':pos['timestamp'],'velocity_command_timestamp':vel['timestamp'],'measured':measured,'requested_next_command':requested}
    rgb['proprio_contract']=CONTRACT;rgb['source']='Human episode4600/raw230010 HF4f50 original sampled RGB + source-lag-aligned measured proprio and explicitly separate recorded command; NOT live, NOT continuous1x, NOT annotation/contact/goal truth'
    return rgb

if __name__=='__main__':print(json.dumps(observe(json.load(sys.stdin)['reference_time']),allow_nan=False))
