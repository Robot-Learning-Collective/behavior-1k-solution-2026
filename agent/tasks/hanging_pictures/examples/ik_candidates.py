"""Offline self-kinematics only; returns candidates, never actuates or certifies collision safety."""
import os, sys
import numpy as np
sys.path.insert(0, os.environ['BEHAVIOR_SIM_RUN_DIR'])
sys.path.insert(0, os.path.join(os.environ['BEHAVIOR_SIM_RUN_DIR'], 'client_helpers'))
import sim_client as s
from robot_kinematics import RobotModel, rotation_error

def solve(point, finger, close, arm='right'):
    robot=s.last_obs()['robot']; model=RobotModel(); state=robot[arm]
    z=np.array(finger,dtype=float);z/=np.linalg.norm(z)
    y=np.array(close,dtype=float);y-=z*np.dot(z,y);y/=np.linalg.norm(y)
    R=np.column_stack((np.cross(y,z),y,z)); target=np.array(point)
    m=state['joint_endpoint_metadata'];lo=np.array(m['endpoint_lower_rad'])+.02;hi=np.array(m['endpoint_upper_rad'])-.02
    rng=np.random.default_rng(34);best=None
    seeds=[np.array(state['joints']),np.array([-.92,-.38,-.17,-.56,0,.34,.07])]+[rng.uniform(lo,hi) for _ in range(32)]
    for q in seeds:
        q=np.clip(q,lo,hi)
        for _ in range(180):
            p,r,J=model.arm(arm,robot['torso_joints'],q)
            e=np.r_[target-p,rotation_error(R,r)*.3];J[3:]*=.3
            score=np.linalg.norm(e)
            if best is None or score<best[0]:best=(score,q.copy(),p.copy())
            if np.linalg.norm(e[:3])<.001 and np.linalg.norm(e[3:])<.002:return best
            dq=J.T@np.linalg.solve(J@J.T+np.eye(6)*.0005,e)
            q=np.clip(q+dq*min(1,.15/max(np.max(np.abs(dq)),1e-8)),lo,hi)
    return best

if __name__=='__main__':
    import json
    point,finger,close=json.loads(sys.argv[1]);score,q,p=solve(point,finger,close)
    print(json.dumps({'residual':score,'q':q.tolist(),'predicted_tcp':p.tolist()}))
