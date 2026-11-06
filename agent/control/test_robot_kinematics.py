"""Finite-difference checks; optional saved public-proprio FK calibration audit.
No simulator import or motor calls. --receipts accepts a directory of saved JSONs.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from robot_kinematics import RobotModel, quaternion_matrix, rotation_error


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--receipts',type=Path)
    args=parser.parse_args();model=RobotModel();rng=np.random.default_rng(1729)
    worst=0.
    for arm in ('left','right'):
        for _ in range(30):
            torso=rng.uniform([.8,-2.5,-1.1,-.3],[1.6,-1.2,-.4,.3])
            q=np.array([rng.uniform(j['limits']['lower']+.02,j['limits']['upper']-.02)
                        for i in range(7) for j in model.data['joints'] if j['name']==f'{arm}_arm_joint{i+1}'])
            p,R,J=model.arm(arm,torso,q)
            for i in range(7):
                dq=np.zeros(7);dq[i]=1e-6
                p2,R2,_=model.arm(arm,torso,q+dq)
                measured=np.r_[(p2-p)/1e-6,rotation_error(R2,R)/1e-6]
                worst=max(worst,float(np.max(np.abs(measured-J[:,i]))))
    assert worst<2e-6,worst
    result={'finite_difference_cases':420,'worst_jacobian_element_error':worst}
    if args.receipts:
        errors=[]
        for path in sorted(args.receipts.glob('receipt_*.json')):
            obs=json.loads(path.read_text());r=obs['robot']
            for arm in ('left','right'):
                p,R,_=model.arm(arm,r['torso_joints'],r[arm]['joints'])
                errors.append([np.linalg.norm(p-r[arm]['eef_position']),
                               np.linalg.norm(rotation_error(R,quaternion_matrix(r[arm]['eef_quaternion'])))])
        assert errors,'No saved public receipts'
        maximum=np.max(errors,axis=0)
        result.update(saved_arm_poses=len(errors),max_fk_position_error_m=float(maximum[0]),max_fk_rotation_error_rad=float(maximum[1]))
        assert maximum[0]<.001 and maximum[1]<.001,result
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
