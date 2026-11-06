"""Evidence-only motion diagnosis from public proprio + a robot model.
The command endpoint is FK(last emitted setpoint), NOT a collision/reachability oracle.
Tracking lag never establishes contact or grasp. All points share the rigid EEF TCP.
"""
import numpy as np
from robot_kinematics import RobotModel, quaternion_matrix, rotation_error

MODEL=RobotModel()


def arm_sample(arm, goal, robot, torso_goal=None):
    st=robot[arm];q=np.asarray(st['joints']);p=np.asarray(st['eef_position'])
    R=quaternion_matrix(st['eef_quaternion']);torso=robot['torso_joints']
    fk_p,fk_R,J=MODEL.arm(arm,torso,q)
    sample={'control_point':'rigid_eef_tcp','frame':'current_body',
            'measured':{'position_m':p.tolist(),'rotation_matrix':R.tolist()},
            'model_error_m':float(np.linalg.norm(fk_p-p)),
            'model_error_rad':float(np.linalg.norm(rotation_error(fk_R,R))),
            'jacobian_singular_values':np.linalg.svd(J,compute_uv=False).tolist(),
            'jacobian_spectrum_units':'mixed m/rad and rad/rad; heuristic, not reachability proof',
            'joints_rad':q.tolist(),'joint_velocities_rad_s':st.get('joint_velocities'),
            'torso_q_tracking_error_rad':robot.get('torso_q_tracking_error_rad'),
            'finger_positions_m':st.get('finger_positions'),
            'finger_velocities_m_s':st.get('finger_velocities'),
            'requested':None,'ik_predicted':None}
    sample['model_valid']=sample['model_error_m']<.002 and sample['model_error_rad']<.002
    fingers=st.get('finger_positions')
    if fingers is not None:
        sample.update(finger_asymmetry_m=float(fingers[0]-fingers[1]),aperture_joint_sum_m=float(sum(fingers)))
    if 'last_commanded_q_target' in st:
        command_q=np.asarray(st['last_commanded_q_target'])
        pp,pr,_=MODEL.arm(arm,robot.get('last_torso_q_target',torso),command_q)
        sample['ik_predicted']={'position_m':pp.tolist(),'rotation_matrix':pr.tolist(),
                                'meaning':'FK of last emitted joint setpoint; not a separately solved goal',
                                'joints_rad':command_q.tolist()}
        sample['q_tracking_error_rad']=(command_q-q).tolist()
    if goal is None:return sample
    if 'q' in goal:
        requested_p,requested_R,_=MODEL.arm(arm,torso if torso_goal is None else torso_goal,goal['q'])
        sample['joint_error_rad']=float(np.max(np.abs(np.asarray(goal['q'])-q)))
    else:requested_p,requested_R=np.asarray(goal['p']),np.asarray(goal['R'])
    sample['requested']={'position_m':requested_p.tolist(),'rotation_matrix':requested_R.tolist(),
                         'mode':'joint' if 'q' in goal else 'cartesian'}
    sample['position_error_m']=float(np.linalg.norm(requested_p-p))
    sample['rotation_error_rad']=float(np.linalg.norm(rotation_error(requested_R,R)))
    if sample['ik_predicted'] is not None:
        pred=sample['ik_predicted']
        sample['predicted_position_error_m']=float(np.linalg.norm(requested_p-pred['position_m']))
        sample['predicted_rotation_error_rad']=float(np.linalg.norm(rotation_error(requested_R,pred['rotation_matrix'])))
    meta=st['joint_endpoint_metadata'];lo=np.asarray(meta['endpoint_lower_rad']);hi=np.asarray(meta['endpoint_upper_rad'])
    gradient=(np.asarray(goal['q'])-q) if 'q' in goal else J.T@np.r_[requested_p-p,rotation_error(requested_R,R)]
    sample['joint_limit_margins_rad']={'to_lower':(q-lo).tolist(),'to_upper':(hi-q).tolist()}
    sample['outward_near_limit_joints']=np.flatnonzero(((q-lo<.015)&(gradient<-.0001))|((hi-q<.015)&(gradient>.0001))).tolist()
    return sample


def diagnose(samples, stop_reason, position_tol=.005, rotation_tol=.035):
    last=samples[-1]
    if last['requested'] is None:
        return {'status':'not_targeted','causes':[],'confidence':'none'}
    def error(s):
        return s['joint_error_rad']/.025 if 'joint_error_rad' in s else max(s['position_error_m']/position_tol,s['rotation_error_rad']/rotation_tol)
    values=[error(s) for s in samples]
    if values[-1]<=1:return {'status':'reached','causes':[],'confidence':'measured'}
    # Need three observed endpoints, not one noisy lag sample. Trends remain evidence.
    plateau=len(values)>=3 and max(values[-3:])-min(values[-3:])<.15
    progress=values[0]-values[-1]
    lag=[max(map(abs,s.get('q_tracking_error_rad',[0.]))) for s in samples[-3:]]
    sustained_lag=len(lag)==3 and min(lag)>.018
    limits=last.get('outward_near_limit_joints',[]) if last['model_valid'] or last['requested']['mode']=='joint' else []
    predicted_error=max(last.get('predicted_position_error_m',float('inf'))/position_tol,
                        last.get('predicted_rotation_error_rad',float('inf'))/rotation_tol)
    torso_lag=max(map(abs,last.get('torso_q_tracking_error_rad') or [0.]))
    causes=[]
    if plateau and sustained_lag:causes.append('blocked')
    if limits:causes.append('joint_limit')
    if (plateau and not sustained_lag and torso_lag<.018 and last['model_valid'] and not limits
            and last['requested']['mode']=='cartesian' and last['ik_predicted'] is not None
            and predicted_error>1 and abs(predicted_error-values[-1])<.5):
        causes.append('IK_stalled')
    if stop_reason in ('step_limit','timeout') and not plateau and progress>.15:causes.append('ran_out_of_steps')
    if not causes:causes=['unknown']
    return {'status':causes[0] if len(causes)==1 else 'mixed','causes':causes,
            'confidence':'suspected' if 'blocked' in causes else 'limited',
            'plateau':plateau,'normalized_error_history':values,'normalized_progress':progress,
            'recent_max_joint_lag_rad':lag,'outward_near_limit_joints':limits,
            'meaning':'blocked means sustained tracking lag with stalled progress; contact, obstruction identity, grasp and global unreachability are NOT established'}
