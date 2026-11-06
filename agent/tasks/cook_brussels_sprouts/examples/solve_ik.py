"""Offline public rigid-body IK candidate search; never executes motions.
Usage: import solve; candidates use current run-local public robot observations.
Endpoint feasibility is NOT swept-path or collision feasibility.
"""
import os, sys
from pathlib import Path
import numpy as np
RUN = Path(os.environ['BEHAVIOR_SIM_RUN_DIR'])
sys.path[:0] = [str(RUN), str(RUN/'client_helpers')]
from robot_kinematics import RobotModel, rotation_error
import sim_client as s

def solve(target, finger, close, arm='right', starts=24):
    robot=s.last_obs()['robot']; st=robot[arm]
    bounds=st['joint_endpoint_metadata']
    lo=np.array(bounds['endpoint_lower_rad'])+.002
    hi=np.array(bounds['endpoint_upper_rad'])-.002
    z=np.array(finger,dtype=float); z/=np.linalg.norm(z)
    y=np.array(close,dtype=float); y-=z*np.dot(y,z); y/=np.linalg.norm(y)
    R=np.column_stack([np.cross(y,z),y,z]); target=np.array(target)
    model=RobotModel(); rng=np.random.default_rng(7)
    seeds=[np.array(st['joints']),np.array([-1.1459,-.3544,.5983,-.5185,-.109,.844,.5875])]
    seeds.extend(rng.uniform(lo,hi) for _ in range(starts))
    found=[]
    for q in seeds:
        q=np.clip(q,lo,hi)
        for _ in range(200):
            p,r,J=model.arm(arm,robot['torso_joints'],q)
            e=np.r_[target-p,.3*rotation_error(R,r)]; J[3:]*=.3
            if np.linalg.norm(e)<.002:break
            dq=J.T@np.linalg.solve(J@J.T+.002*np.eye(6),e)
            q=np.clip(q+np.clip(dq,-.12,.12),lo,hi)
        p,r,_=model.arm(arm,robot['torso_joints'],q)
        pe=float(np.linalg.norm(target-p)); re=float(np.linalg.norm(rotation_error(R,r)))
        if pe<.005 and re<.035 and all(np.linalg.norm(q-f['q'])>.15 for f in found):
            found.append({'q':q.tolist(),'position_error':pe,'rotation_error':re,'min_margin':float(np.min(np.minimum(q-lo,hi-q)))})
    return sorted(found,key=lambda c:-c['min_margin'])
