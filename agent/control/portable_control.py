"""Per-tick persistent R1Pro controller; official proprioception + static model only.

No simulator queries, world pose, contacts, objects, task truth or image-derived
privileged state. The worker and official policy call the SAME step(observation,
goal). RGBD may inform the goal provider, never changes the servo's input contract.
"""
import math
import numpy as np
from hybrid_arm_control import nullspace_dls_step, _resolve_bias
from robot_kinematics import RobotModel, rotation_vector_matrix, rotation_error, quaternion_matrix
from torso_control import bounded_target
from motion_diagnostics import arm_sample, diagnose


def finite(value, shape):
    if any(isinstance(x,(bool,np.bool_)) or not isinstance(x,(int,float,np.integer,np.floating))
           for x in np.asarray(value,dtype=object).flat):raise ValueError('Expected numeric goal')
    a=np.asarray(value,dtype=float)
    if a.shape!=shape or not np.isfinite(a).all():raise ValueError('Invalid goal shape/finite values')
    return a.copy()


def wrap(angle):return (angle+math.pi)%(2*math.pi)-math.pi


class PlanarOdometry:
    """BODY-velocity trapezoidal/SE(2) integration at simulation dt, not wall dt."""
    def __init__(self, velocity=(0.,0.,0.)):
        self.xy=np.zeros(2);self.yaw=0.;self.seconds=0.;self.distance=0.
        self.velocity=finite(velocity,(3,))

    @property
    def rotation(self):return rotation_vector_matrix([0.,0.,self.yaw])

    def update(self, velocity, dt=1/30):
        v=finite(velocity,(3,))
        if not np.isfinite(dt) or not 0.<dt<=1.:raise ValueError('Invalid simulation-step dt')
        mean=(self.velocity+v)/2;theta=mean[2]*dt
        a=np.sinc(theta/np.pi);b=(1-math.cos(theta))/theta if abs(theta)>1e-8 else theta/2
        self.xy+=self.rotation[:2,:2]@(dt*np.array([[a,-b],[b,a]])@mean[:2])
        self.yaw+=theta;self.seconds+=dt;self.distance+=float(np.linalg.norm(mean[:2])*dt)
        self.velocity=v

    def state(self):
        return {'source':'integrated_proprio_base_qvel_planar_estimate','position_rel_start_body':[*self.xy,0.],
                'yaw_rel_start_rad':self.yaw,'body_velocity':self.velocity.tolist(),
                'integrated_simulation_seconds':self.seconds,'integrated_distance_m':self.distance,
                'uncertainty':'uncalibrated drift; no absolute world pose, vertical motion or tilt observation',
                'vertical_position_observed':False,'tilt_observed':False}


class Controller:
    """One observation -> one command-space IK/slew step, with measured stopping.

    observation={step: monotonic physics-tick index, robot: public self-state}.
    A fresh observation acknowledges the previous emitted action; repeated calls
    on the same observation never integrate odometry or advance the command.
    done=True means the supplied action is an idle hold, not another IK step.
    The worker can stop without executing that hold; the evaluator may emit it.
    A new goal id resets move diagnostics, NOT persistent commands or odometry.
    reset() is mandatory at every rollout boundary.
    """
    def __init__(self, model=None):
        self.model=model or RobotModel();self.reset()

    def reset(self):
        self.odom=None;self.last_step=None;self.last_action=None;self.goal_id=None
        self.command_q={};self.command_torso=None;self.grips={};self.reason=None
        self.history={};self.trace=[];self.result={};self.misses={}
        self.base_feedback=[];self.base_safety={};self.base_guard_triggered=False

    def _observe(self, observation):
        r=observation['robot'];n=observation['step']
        if type(n) is not int or n<0:raise ValueError('Invalid physics tick index')
        velocity=finite(r['base_velocity'],(3,))
        if self.last_step is None:
            self.odom=PlanarOdometry(velocity)
            self.command_q={a:finite(r[a].get('last_commanded_q_target',r[a]['joints']),(7,)) for a in ('left','right')}
            self.command_torso=finite(r.get('last_torso_q_target',r['torso_joints']),(4,))
        elif n==self.last_step+1:
            if self.last_action is None:raise RuntimeError('Physics advanced without a controller action')
            # Pair measured feedback with the action actually emitted last tick.
            self.base_feedback.append((self.last_action[:3].astype(float)*[.75,.75,1.],velocity.copy()))
            self.base_feedback=self.base_feedback[-15:]
            self.command_torso=self.last_action[3:7].astype(float).copy()
            self.command_q={a:self.last_action[i:i+7].astype(float).copy() for a,i in [('left',7),('right',15)]}
            self.grips={a:float((self.last_action[i]+1)/2) for a,i in [('left',14),('right',22)]}
            self.odom.update(velocity)
        elif n!=self.last_step:raise RuntimeError('Missing/reordered physics feedback; reset required')
        self.last_step=n
        self.robot={**r,'last_torso_q_target':self.command_torso.tolist()}
        for a in ('left','right'):
            self.robot[a]={**r[a],'last_commanded_q_target':self.command_q[a].tolist()}

    def _start(self, goal):
        expected={'id','arms','base','torso','grippers','targeted_grippers','position_tol','rotation_tol','timeout_seconds','accept_partial'}
        if set(goal)-{'max_steps'}!=expected:raise ValueError('Unknown/missing goal fields')
        if not isinstance(goal['id'],str) or not goal['id']:raise ValueError('Goal id required')
        self.bounds={a:tuple(finite(self.robot[a]['joint_endpoint_metadata'][k],(7,)) for k in ('endpoint_lower_rad','endpoint_upper_rad')) for a in ('left','right')}
        self.torso_bounds=tuple(finite(self.robot['torso_joint_limits_rad'][k],(4,)) for k in ('lower','upper'))
        self.torso_slew=finite(self.robot['torso_slew_rad_per_tick'],(4,))
        self.pos_tol=float(goal['position_tol']);self.rot_tol=float(goal['rotation_tol'])
        if not .001<=self.pos_tol<=.05 or not .005<=self.rot_tol<=.2:raise ValueError('Invalid tolerance')
        timeout=float(goal['timeout_seconds'])
        if not np.isfinite(timeout) or not .1<=timeout<=120:raise ValueError('Invalid overall timeout')
        self.max_ticks=math.ceil(timeout*30);self.caller_step_limit=goal.get('max_steps')
        if self.caller_step_limit is not None:
            if type(self.caller_step_limit) is not int or self.caller_step_limit<1:raise ValueError('max_steps must be a positive native tick count')
            # Reserve the final tick for zero-base persistent hold + feedback.
            self.max_ticks=min(self.max_ticks,self.caller_step_limit-1)
        # Retain feedback across ordinary short goals; a new goal after a trip
        # permits deliberate recovery, not automatic retries or a force override.
        if self.base_guard_triggered:self.base_feedback=[]
        self.base_guard_triggered=False;self.base_safety={}
        if type(goal['accept_partial']) is not bool:raise ValueError('Explicit boolean accept_partial required')
        if set(goal['arms'])-{'left','right'}:raise ValueError('Unknown arm')
        self.arms={}
        for a,g in goal['arms'].items():
            if set(g)=={'q'}:
                q=finite(g['q'],(7,));lo,hi=self.bounds[a]
                if np.any(q<lo) or np.any(q>hi):raise ValueError('Joint goal outside endpoint bounds')
                self.arms[a]={'q':q}
            elif set(g)=={'p','R','bias'}:
                p,R=finite(g['p'],(3,)),finite(g['R'],(3,3))
                if np.max(abs(R.T@R-np.eye(3)))>1e-5 or np.linalg.det(R)<.99999:raise ValueError('Invalid goal rotation')
                bias=self.command_q[a].tolist() if isinstance(g['bias'],str) and g['bias']=='current' else g['bias']
                self.arms[a]={'p':p,'R':R,'bias':_resolve_bias(a,bias,self.bounds)}
            else:raise ValueError('Arm goal requires q7 or rigid BODY p/R/bias')
        self.base=None if goal['base'] is None else finite(goal['base'],(3,))
        self.torso=None if goal['torso'] is None else finite(goal['torso'],(4,))
        if self.torso is not None and (np.any(self.torso<self.torso_bounds[0]) or np.any(self.torso>self.torso_bounds[1])):raise ValueError('Torso goal outside limits')
        if set(goal['grippers'])!={'left','right'}:raise ValueError('Both gripper intents required')
        self.desired_grips={a:float(goal['grippers'][a]) for a in ('left','right')}
        if any(not np.isfinite(v) or not 0<=v<=1 for v in self.desired_grips.values()):raise ValueError('Invalid gripper intent')
        self.targeted_grips=set(goal['targeted_grippers'])
        if self.targeted_grips-{'left','right'}:raise ValueError('Unknown gripper target')
        self.accept_partial=goal['accept_partial']
        self.closing={a for a,g in self.desired_grips.items() if g<self.grips.get(a,1.)-1e-6}
        self.gated={a:self.misses[a] for a in self.closing if a in self.misses and a not in self.arms and not self.accept_partial}
        if self.closing and not self.accept_partial:
            for component,target in [('base',self.base),('torso',self.torso)]:
                if target is None and component in self.misses:self.gated[component]=self.misses[component]
        self.goal_id=goal['id'];self.start_step=self.last_step
        self.reason='prerequisite_not_met' if self.gated else None
        self.history={a:[] for a in ('left','right')};self.trace=[];self.max_command_slew=0.
        self.initial_command={a:q.copy() for a,q in self.command_q.items()}
        self.max_torso_lead=self.max_torso_slew=0.

    def _sample(self):
        errors={};scores={};pose_scores={}
        def add(key,error,tolerance,pose=True):
            errors[key]=float(error);scores[key]=float(error/tolerance)
            if pose:pose_scores[key]=scores[key]
        for a,g in self.arms.items():
            r=self.robot[a];cp,cR,_=self.model.arm(a,self.command_torso,self.command_q[a])
            if 'q' in g:
                add(a+'_joint_rad',np.max(abs(g['q']-r['joints'])),.025)
                add(a+'_command_joint_rad',np.max(abs(g['q']-self.command_q[a])),1e-5)
            else:
                add(a+'_position_m',np.linalg.norm(g['p']-r['eef_position']),self.pos_tol)
                add(a+'_rotation_rad',np.linalg.norm(rotation_error(g['R'],quaternion_matrix(r['eef_quaternion']))),self.rot_tol)
                add(a+'_command_position_m',np.linalg.norm(g['p']-cp),self.pos_tol)
                add(a+'_command_rotation_rad',np.linalg.norm(rotation_error(g['R'],cR)),self.rot_tol)
        if self.base is not None:
            add('base_position_m',np.linalg.norm(self.base[:2]-self.odom.xy),self.pos_tol)
            add('base_rotation_rad',abs(wrap(self.base[2]-self.odom.yaw)),self.rot_tol)
        if self.torso is not None:
            add('torso_joint_rad',np.max(abs(self.torso-self.robot['torso_joints'])),.025)
            add('torso_command_joint_rad',np.max(abs(self.torso-self.command_torso)),1e-5)
        for a in self.targeted_grips:
            # Static model finger limits; closure/lag does NOT prove grasp/contact.
            finger_goal=[]
            for i in (1,2):
                limits=next(j['limits'] for j in self.model.data['joints'] if j['name']==f'{a}_gripper_finger_joint{i}')
                finger_goal.append(limits['lower']+self.desired_grips[a]*(limits['upper']-limits['lower']))
            add(a+'_finger_m',np.max(abs(np.asarray(finger_goal)-self.robot[a]['finger_positions'])),.001,False)
        pose_reached=max(pose_scores.values(),default=0.)<=1
        reached=max(scores.values(),default=0.)<=1 and all(abs(self.grips.get(a,float('inf'))-g)<1e-6 for a,g in self.desired_grips.items())
        row={'tick':self.last_step-self.start_step,'errors':errors,'normalized_error':max(scores.values(),default=0.)}
        if not self.trace or self.trace[-1]['tick']!=row['tick']:
            self.trace.append(row)
            for a in ('left','right'):
                s=arm_sample(a,self.arms.get(a),self.robot,self.torso)
                if self.history[a]:
                    old=self.history[a][-1]
                    s['measured_displacement_m']=(np.asarray(s['measured']['position_m'])-old['measured']['position_m']).tolist()
                self.history[a].append(s)
        return errors,scores,pose_reached,reached

    def _base_tracking_guard(self):
        """Onboard velocity mismatch, not a contact/force/fall measurement.

        Half a second at30Hz filters startup/one-tick lag. A sustained50% tracking
        error (with3–5mm /0.02rad absolute floors) ends the move instead of pushing
        until a30s timeout. Thresholds require scene validation; no gravity sensor
        or obstacle geometry is available in official proprioception.
        """
        if self.base is None or len(self.base_feedback)<15:return False
        command,measured=np.asarray(self.base_feedback).transpose(1,0,2)
        expected_xy=float(np.linalg.norm(command[:,:2],axis=1).sum()/30)
        difference_xy=measured[:,:2]-command[:,:2]
        # Compare displacement over the window, not accumulated absolute jitter.
        # Alternating wheel-release vibration is not blocked forward progress.
        error_xy=float(np.linalg.norm(difference_xy.sum(axis=0))/30)
        absolute_error_xy=float(np.linalg.norm(difference_xy,axis=1).sum()/30)
        expected_yaw=float(abs(command[:,2]).sum()/30)
        error_yaw=float(abs(measured[:,2]-command[:,2]).sum()/30)
        # Free native turns can drift a few mm while the base rotates. Allow the
        # advertised position tolerance, but never relax the floor beyond5mm.
        translation_floor=max(.003,min(self.pos_tol,.005))
        bad_xy=error_xy>max(translation_floor,.5*expected_xy)
        heading_error=abs(wrap(self.base[2]-self.odom.yaw))
        heading_threshold=min(self.rot_tol,.035)
        # A brief release/settling impulse inside the requested heading band is
        # not a sustained heading failure. Never loosen this gate beyond~2deg.
        bad_yaw=error_yaw>max(.02,.5*expected_yaw) and heading_error>heading_threshold
        self.base_safety={'triggered':bool(bad_xy or bad_yaw),'window_ticks':15,
            'commanded_translation_m':expected_xy,'velocity_tracking_error_m':error_xy,
            'absolute_velocity_error_integral_m':absolute_error_xy,'translation_error_floor_m':translation_floor,
            'commanded_rotation_rad':expected_yaw,'angular_tracking_error_rad':error_yaw,
            'heading_error_rad':heading_error,'heading_guard_threshold_rad':heading_threshold,
            'translation_mismatch':bool(bad_xy),'rotation_mismatch':bool(bad_yaw),
            'semantics':'command versus onboard velocity; obstruction/slip/instability suspected, not contact proof'}
        return self.base_safety['triggered']

    def step(self, observation, goal):
        self._observe(observation)
        if goal['id']!=self.goal_id:self._start(goal)
        errors,scores,pose_reached,reached=self._sample()
        elapsed=self.last_step-self.start_step
        if self.reason is None:
            if self._base_tracking_guard():self.reason='stalled';self.base_guard_triggered=True
            elif reached:self.reason='reached'
            elif elapsed>=self.max_ticks:self.reason='timeout'
            elif len(self.trace)>=16:
                # Stop a measured plateau; a changing persistent command is not progress.
                keys=[k for k,v in scores.items() if v>1 and '_command_' not in k]
                window=self.trace[-16:]
                if keys and all((max(r['errors'][k] for r in window)-min(r['errors'][k] for r in window))
                                <(.0005 if k.endswith('_m') else .005) for k in keys):self.reason='stalled'
        if self.closing and not self.accept_partial and not pose_reached and any(a not in self.grips for a in self.closing):
            raise ValueError('Initialize explicit gripper intent before compound motion and close')
        action=np.zeros(23,dtype=np.float32)
        action[3:7]=self.command_torso
        for a,i in [('left',7),('right',15)]:action[i:i+7]=self.command_q[a]
        for a,i in [('left',14),('right',22)]:
            defer=a in self.closing and not self.accept_partial and not pose_reached
            action[i]=2*(self.grips[a] if defer else self.desired_grips[a])-1
        if self.reason is None:
            if self.torso is not None:
                action[3:7]=bounded_target(self.torso,np.asarray(self.robot['torso_joints']),self.command_torso,self.torso_bounds,self.torso_slew)
            for a,g in self.arms.items():
                q=self.command_q[a];lo,hi=self.bounds[a]
                if 'q' in g:target=q+np.clip(g['q']-q,-.025,.025)
                else:
                    p,R,J=self.model.arm(a,action[3:7],q)
                    error=np.r_[g['p']-p,rotation_error(g['R'],R)]
                    _,target=nullspace_dls_step(J,error,q,lo,hi,a,g['bias'])
                start=7 if a=='left' else 15
                action[start:start+7]=target
            if self.base is not None:
                delta=np.r_[self.odom.rotation[:2,:2].T@(self.base[:2]-self.odom.xy),wrap(self.base[2]-self.odom.yaw)]
                velocity=2*delta
                velocity*=min(1.,.2/max(np.linalg.norm(velocity[:2]),1e-12),.4/max(abs(velocity[2]),1e-12))
                # Hold heading before translating: fade translation between~3–9deg.
                # Apply AFTER the speed cap so a distant goal cannot renormalize
                # a reduced translation back to full speed.
                velocity[:2]*=np.clip((.15-abs(delta[2]))/.10,0.,1.)
                action[:3]=velocity/[.75,.75,1.]
        else:
            # A terminal hold must not newly close a deferred gripper.
            for a,i in [('left',14),('right',22)]:action[i]=2*self.grips.get(a,self.desired_grips[a])-1
        slew=max(float(np.max(abs(action[i:i+7]-self.command_q[a]))) for a,i in [('left',7),('right',15)])
        self.max_command_slew=max(self.max_command_slew,slew)
        self.max_torso_lead=max(self.max_torso_lead,float(np.max(abs(action[3:7]-self.robot['torso_joints']))))
        self.max_torso_slew=max(self.max_torso_slew,float(np.max(abs(action[3:7]-self.command_torso))))
        if not np.isfinite(action).all() or slew>.025+1e-6:raise ValueError('Finite/command-slew guard')
        self.last_action=action.copy()
        self.result={'interface':'act-v4-per-tick-persistent-goal','high_level_action_id':self.goal_id,
            'achieved':self.reason=='reached','reason':self.reason,'steps':elapsed,'errors':errors,'trace':self.trace,
            'position_tolerance_m':self.pos_tol,'rotation_tolerance_rad':self.rot_tol,
            'max_command_slew_rad':self.max_command_slew,'timeout_ticks':self.max_ticks,
            'caller_max_steps':self.caller_step_limit,'base_safety':dict(self.base_safety),
            'stop_reason_detail':('base_velocity_tracking_mismatch' if self.base_guard_triggered else
                ('caller_step_limit' if self.caller_step_limit is not None and self.max_ticks==self.caller_step_limit-1 else 'motion_timeout_seconds')
                if self.reason=='timeout' else None),
            'arms':{a:{**self.history[a][-1],'diagnosis':diagnose(self.history[a],self.reason,self.pos_tol,self.rot_tol)} for a in ('left','right')},
            'torso_target_rad':(self.command_torso if self.torso is None else self.torso).tolist(),
            'prerequisite_gate':{'accepted_previous_miss':self.accept_partial,'blocked_previous_misses':self.gated,
                'closing_deferred':{a:abs(self.grips.get(a,float('inf'))-self.desired_grips[a])>1e-6 for a in self.closing}},
            'semantics':'measured proprioception and estimated planar odometry; not object/contact/grasp success'}
        if self.reason in ('reached','stalled','timeout'):
            for a in self.arms:
                s=self.result['arms'][a]
                if s['diagnosis']['status']=='reached':self.misses.pop(a,None)
                else:self.misses[a]={'action_id':self.goal_id,'requested':s['requested'],'diagnosis':s['diagnosis']}
            for component,target,error in (
                ('base',self.base,max(errors.get('base_position_m',0.)/self.pos_tol,errors.get('base_rotation_rad',0.)/self.rot_tol)),
                ('torso',self.torso,errors.get('torso_joint_rad',0.)/.025)):
                if target is not None:
                    if error<=1:self.misses.pop(component,None)
                    else:self.misses[component]={'action_id':self.goal_id,'requested':target.tolist(),'normalized_error':error}
        self.result['unresolved_pose_misses']=dict(self.misses)
        return action,self.reason is not None
