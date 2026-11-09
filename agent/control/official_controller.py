"""BEHAVIOR3.9.3 RGBDFullResWrapper -> shared per-tick controller adapter.

Policy imports no simulator code. A separately captured STATIC robot/camera
profile supplies limits/intrinsics; all changing state comes from the official
observation. Exactly one native23 action is returned per evaluator observation.
No action chunks, retry/reconnect recovery, object/contact/scoring inputs.
"""
import time
import uuid
import numpy as np
from portable_control import Controller
from robot_kinematics import RobotModel, quaternion_matrix


def array(value):
    return value.detach().cpu().numpy() if hasattr(value,'detach') else np.asarray(value)


def single(value, shape, name):
    a=array(value)
    if a.shape==(1,*shape):a=a[0]
    if a.shape!=shape:raise ValueError(f'{name}: expected one environment with shape{shape}, got{a.shape}')
    return a


def decode_observation(flat, profile, step, model):
    """Allowlist flat official inputs. Unknown fields are never passed to a planner."""
    name=profile['robot_name']
    q=single(flat[name+'::proprio'],(61,),'R1Pro proprio')
    if not np.isfinite(q).all():raise ValueError('Nonfinite proprioception')
    r={'frame':'current mobile base; xforward,yleft,zup','quaternion_order':'xyzw',
       'base_velocity':q[:3].astype(float).tolist(),'torso_joints':q[53:57].astype(float).tolist(),
       'torso_velocities':q[57:61].astype(float).tolist(),
       'torso_joint_limits_rad':profile['torso_joint_limits_rad'],
       'torso_slew_rad_per_tick':profile['torso_slew_rad_per_tick'],
       'torso_joint_efforts_nm':None,'joint_effort_semantics':'unavailable in official proprioception'}
    for a,s in [('left',3),('right',28)]:
        r[a]={'joints':q[s:s+7].astype(float).tolist(),'joint_velocities':q[s+7:s+14].astype(float).tolist(),
              'eef_position':q[s+14:s+17].astype(float).tolist(),'eef_quaternion':q[s+17:s+21].astype(float).tolist(),
              'finger_positions':q[s+21:s+23].astype(float).tolist(),'finger_velocities':q[s+23:s+25].astype(float).tolist(),
              'joint_endpoint_metadata':profile['arms'][a], 'joint_efforts_nm':None,
              'joint_effort_semantics':'unavailable in official proprioception'}
    poses=single(flat[name+'::cam_rel_poses'],(21,),'relative camera poses').reshape(3,7)
    cameras={};rgb={};depth={}
    for i,a in enumerate(profile['camera_order']):
        meta=profile['cameras'][a];h,w=meta['image_size_hw'];prefix=meta['observation_prefix']
        image=array(flat[prefix+'::rgb'])
        if image.ndim==4 and image.shape[0]==1:image=image[0]
        if image.shape not in ((h,w,3),(h,w,4)) or image.dtype!=np.uint8:raise ValueError('Expected native uint8 RGB/RGBA')
        rgb[a]=image[...,:3]
        depth[a]=single(flat[prefix+'::depth_linear'],(h,w),a+' linear depth')
        if depth[a].dtype!=np.float32:raise ValueError('Expected native float32 axial depth, not normalized display depth')
        T=np.eye(4);T[:3,:3]=quaternion_matrix(poses[i,3:])@np.diag([1.,-1.,-1.]);T[:3,3]=poses[i,:3]
        if not np.isfinite(T).all():raise ValueError('Nonfinite camera pose')
        cameras[a]={'intrinsics':meta['intrinsics'],'camera_to_body':T.tolist(),'image_size_hw':[h,w],
                    'camera_axes':'optical: +X right, +Y down, +Z forward; axial depth metres',
                    'pose_source':'official onboard camera pose relative to robot body','pixel_center_offset':.5}
    # Robot geometry is model-derived from permitted joints, not scene link queries.
    links=model.all_link_poses(r)
    for a in ('left','right'):
        own={'source':'static_robot_model_from_official_joint_proprioception',
             'elbow_position_body':links[a+'_arm_link4'][:3,3].tolist()}
        for field,key in [('ag_start_point_body','ag_start'),('ag_end_point_body','ag_end')]:
            points=profile['arms'][a].get(key,[])
            if points:
                own[field]=np.mean([links[p['link']]@np.r_[p['position'],1.] for p in points],axis=0)[:3].tolist()
        if 'ag_start_point_body' in own and 'ag_end_point_body' in own:
            own['ag_ray_midpoint_body']=((np.array(own['ag_start_point_body'])+own['ag_end_point_body'])/2).tolist()
        r[a]['own_links_body']=own
    task=single(flat['task_id'],(1,),'task_id')
    return {'step':step,'robot':r,'cameras':cameras,'rgb':rgb,'depth':depth,
            'task_id':int(task[0]),'controller_protocol':6}


class OfficialControllerPolicy:
    """Planner callback receives only decoded official inputs and last move result.

    The callback returns one full goal in portable_control.Controller's schema.
    It is called at rollout start and after a terminal controller hold. It may
    use RGBD/robot model, but no simulator handle is retained by this adapter.
    Runner enforces wall deadlines; this class also rejects late replies. Use
    action_chunk_size=0 and allow_reconnect=False with the official transport:
    the protocol has no tick/request IDs for safe recovery after a lost reply.
    """
    def __init__(self, profile, goal_provider, max_steps, clock=time.monotonic):
        if profile['schema']!='r1pro-v393-static-profile-v1':raise ValueError('Unsupported static profile')
        if type(max_steps) is not int or max_steps<1:raise ValueError('Finite episode step budget required')
        self.profile=profile;self.goal_provider=goal_provider;self.max_steps=max_steps;self.clock=clock
        self.model=RobotModel();self.controller=Controller(self.model);self.reset_count=0;self.reset()

    def reset(self):
        self.reset_count+=1;self.controller.reset();self.tick=0;self.goal=None;self.done=False
        self.started=None;self.query_seconds=[];self.completed_goals=[];self.action_trace=[];self.packet=None;self.planner_finished=False
        if hasattr(self.goal_provider,'reset'):self.goal_provider.reset()

    def observation(self, flat):
        """Acknowledge one actual evaluator observation; no action dispatch here."""
        packet=decode_observation(flat,self.profile,self.tick,self.model)
        if self.goal is not None:
            # Acknowledge the prior emitted native action, including the final
            # terminal hold. Repeating step on this frame does not advance twice.
            action,done=self.controller.step(packet,self.goal)
        else:
            self.controller._observe(packet)
        packet['robot']=self.controller.robot
        packet['robot']['base_odometry']=self.controller.odom.state()
        r=packet['robot']
        r['torso_q_tracking_error_rad']=(self.controller.command_torso-r['torso_joints']).tolist()
        for arm in ('left','right'):
            st=r[arm];q=np.asarray(st['joints']);meta=st['joint_endpoint_metadata']
            st['q_tracking_error_rad']=(self.controller.command_q[arm]-q).tolist()
            lower=q-meta['endpoint_lower_rad'];upper=np.asarray(meta['endpoint_upper_rad'])-q
            st['joint_limit_margins_rad']={'to_lower':lower.tolist(),'to_upper':upper.tolist(),
                                           'min_margin_rad':float(min(lower.min(),upper.min()))}
            R=quaternion_matrix(st['eef_quaternion'])
            st['closing_axis_body']=R[:,1].tolist();st['finger_axis_body']=R[:,2].tolist()
        packet.update(observation_id=self.tick+1,simulated_seconds=self.tick/30,
                      wall_seconds=self.clock()-self.started,action_id=None if self.goal is None else self.goal['id'])
        packet['last_commanded_grip']=self.controller.grips.copy()
        return packet

    def act(self, flat):
        start=self.clock()
        if self.started is None:self.started=start
        if start-self.started>=self.max_steps:raise TimeoutError('Episode wall budget max_steps*1second exhausted')
        packet=self.observation(flat)
        previous=None
        if self.goal is None or (self.done and not self.planner_finished):
            if self.goal is not None:
                previous=self.controller.result
                self.completed_goals.append(previous)
            goal=self.goal_provider(packet,previous)
            if goal is None:
                if self.goal is None:raise ValueError('Initial goal required')
                self.planner_finished=True
            else:
                goal={**goal,'id':goal.get('id') or uuid.uuid4().hex}
                self.goal=goal
        action,done=self.controller.step(packet,self.goal)
        self.packet=packet
        elapsed=self.clock()-start;self.query_seconds.append(elapsed)
        if elapsed>600:raise TimeoutError('Policy query exceeded600seconds')
        if self.clock()-self.started>=self.max_steps:raise TimeoutError('Episode wall budget exceeded during query')
        if action.shape!=(23,) or action.dtype!=np.float32 or not np.isfinite(action).all():raise ValueError('Bad native action')
        self.done=done;self.tick+=1
        self.action_trace.append({'tick':self.tick,'goal':self.goal['id'],'done':done,
                                  'reason':self.controller.reason,'action':action.tolist()})
        return action[None,:]


class SmokeGoals:
    """Deliberately small integration motions, NOT a task-solving policy."""
    def reset(self):self.index=0

    def __call__(self, packet, previous):
        if self.index>=3:return None
        r=packet['robot']
        goal={'arms':{},'base':None,'torso':None,'grippers':{'left':1.,'right':1.},
              'targeted_grippers':[],'position_tol':.005,'rotation_tol':.035,
              'timeout_seconds':5.,'accept_partial':False}
        if self.index==1:
            q=np.array(r['left']['last_commanded_q_target']);q[3]-=.1
            goal['arms']['left']={'q':q.tolist()}
        elif self.index==2:
            model=RobotModel();p,R,_=model.arm('left',r['last_torso_q_target'],r['left']['last_commanded_q_target'])
            goal['arms']['left']={'p':(p+[.01,0.,.01]).tolist(),'R':R.tolist(),'bias':'current'}
            o=r['base_odometry'];goal['base']=[o['position_rel_start_body'][0]+.02,o['position_rel_start_body'][1],o['yaw_rel_start_rad']+.03]
        self.index+=1
        return goal
