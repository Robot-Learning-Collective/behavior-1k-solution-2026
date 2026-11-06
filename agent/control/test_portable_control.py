"""CPU-only synthetic servo tests, not simulator/contact/grasp evidence."""
import copy
import unittest
import numpy as np
from portable_control import Controller, PlanarOdometry
from robot_kinematics import RobotModel, rotation_error
from hybrid_arm_control import PRESETS


def matrix_quaternion(R):
    v=rotation_error(R,np.eye(3));angle=np.linalg.norm(v)
    return np.r_[v*.5*np.sinc(angle/(2*np.pi)),np.cos(angle/2)]


def robot_fixture(model):
    joints={j['name']:j for j in model.data['joints']};torso=[1.025,-1.45,-.47,0.]
    r={'base_velocity':[0.,0.,0.],'torso_joints':torso,'last_torso_q_target':torso,
       'torso_joint_limits_rad':{k:[joints[f'torso_joint{i}']['limits'][k] for i in range(1,5)] for k in ('lower','upper')},
       'torso_slew_rad_per_tick':[.025]*4}
    for a in ('left','right'):
        q=PRESETS[a]['ready'].copy();p,R,_=model.arm(a,torso,q)
        r[a]={'joints':q.tolist(),'joint_velocities':[0.]*7,'eef_position':p.tolist(),'eef_quaternion':matrix_quaternion(R).tolist(),
              'finger_positions':[.05,.05],'finger_velocities':[0.,0.],
              'joint_endpoint_metadata':{f'endpoint_{k}_rad':[joints[f'{a}_arm_joint{i}']['limits'][k]+sign*.01 for i in range(1,8)]
                  for k,sign in [('lower',1),('upper',-1)]}}
    return r


def goal(r,**kwargs):
    return {'id':'test','arms':{},'base':None,'torso':None,'grippers':{'left':1.,'right':1.},
            'targeted_grippers':[],'position_tol':.005,'rotation_tol':.035,'timeout_seconds':5.,'accept_partial':False,**kwargs}


def advance(r,action,model):
    r['torso_joints']=action[3:7].tolist();r['base_velocity']=(action[:3]*[.75,.75,1.]).tolist()
    for a,i in [('left',7),('right',15)]:
        p,R,_=model.arm(a,r['torso_joints'],action[i:i+7])
        r[a].update(joints=action[i:i+7].tolist(),eef_position=p.tolist(),eef_quaternion=matrix_quaternion(R).tolist())


class PortableControlTest(unittest.TestCase):
    def test_odometry_twist_reset_invalid(self):
        o=PlanarOdometry([.2,0.,.4])
        for _ in range(150):o.update([.2,0.,.4])
        np.testing.assert_allclose(o.xy,[.5*np.sin(2),.5*(1-np.cos(2))],atol=1e-12)
        self.assertAlmostEqual(o.yaw,2.);self.assertNotIn('position_world',o.state())
        self.assertFalse(o.state()['tilt_observed']);np.testing.assert_array_equal(PlanarOdometry().xy,[0.,0.])
        with self.assertRaises(ValueError):o.update([np.nan,0,0])
        with self.assertRaises(ValueError):o.update([0,0,0],0)

    def test_free_and_base_combined_same_step(self):
        for with_base in (False,True):
            model=RobotModel();r=robot_fixture(model);c=Controller(model)
            p,R,_=model.arm('left',r['torso_joints'],r['left']['joints'])
            g=goal(r,arms={'left':{'p':(p+[0,.06,.02]).tolist(),'R':R.tolist(),'bias':'current'}},base=[.08,.02,.1] if with_base else None)
            for tick in range(150):
                obs={'step':tick,'robot':r};action,done=c.step(obs,g)
                again,again_done=c.step(obs,g)
                np.testing.assert_array_equal(action,again);self.assertEqual(done,again_done)
                self.assertEqual(action.shape,(23,));self.assertTrue(np.isfinite(action).all())
                if done:break
                advance(r,action,model)
            self.assertEqual(c.reason,'reached',c.result)
            self.assertLessEqual(c.max_command_slew,.025+1e-6)
            if with_base:self.assertLess(np.linalg.norm(c.odom.xy-[.08,.02]),.005)
            self.assertLess(c.result['errors']['left_position_m'],.005)

    def test_stuck_feedback_stalls_not_timeout_without_lag_cap(self):
        model=RobotModel();r=robot_fixture(model);c=Controller(model)
        p,R,_=model.arm('left',r['torso_joints'],r['left']['joints'])
        g=goal(r,arms={'left':{'p':(p+[0,.08,.02]).tolist(),'R':R.tolist(),'bias':'current'}})
        for tick in range(50):
            action,done=c.step({'step':tick,'robot':r},g) # Measured joints deliberately frozen.
            if done:break
        self.assertEqual(c.reason,'stalled');self.assertLess(tick,30)
        self.assertGreater(np.max(abs(c.command_q['left']-r['left']['joints'])),.025)
        self.assertEqual(c.result['arms']['left']['diagnosis']['status'],'blocked')
        close=goal(r,id='blind-close',grippers={'left':0.,'right':1.})
        action,done=c.step({'step':tick,'robot':r},close)
        self.assertTrue(done);self.assertEqual(c.reason,'prerequisite_not_met');self.assertEqual(action[14],1.)
        close.update(id='accepted-close',accept_partial=True)
        action,done=c.step({'step':tick,'robot':r},close)
        self.assertFalse(done);self.assertEqual(action[14],-1.)
        c.reset();self.assertFalse(c.misses)

    def test_omitted_arm_torso_keep_preload(self):
        model=RobotModel();r=robot_fixture(model);c=Controller(model)
        r['left']['last_commanded_q_target']=(np.array(r['left']['joints'])+[.1,0,0,0,0,0,0]).tolist()
        r['last_torso_q_target']=(np.array(r['torso_joints'])+[.1,0,0,0]).tolist()
        g=goal(r)
        a,done=c.step({'step':0,'robot':r},g)
        np.testing.assert_allclose(a[7:14],r['left']['last_commanded_q_target'],atol=1e-7)
        np.testing.assert_allclose(a[3:7],r['last_torso_q_target'],atol=1e-7)
        _,done=c.step({'step':1,'robot':r},g)
        self.assertTrue(done);self.assertEqual(c.reason,'reached')

    def test_timeout_reset_and_missing_feedback(self):
        model=RobotModel();r=robot_fixture(model);c=Controller(model)
        q=np.array(r['left']['joints']);q[0]+=.2
        g=goal(r,arms={'left':{'q':q.tolist()}},timeout_seconds=.1)
        for tick in range(4):a,done=c.step({'step':tick,'robot':r},g)
        self.assertTrue(done);self.assertEqual(c.reason,'timeout')
        with self.assertRaises(RuntimeError):c.step({'step':6,'robot':r},g)
        c.reset();self.assertIsNone(c.odom);self.assertFalse(c.grips)
        c.step({'step':0,'robot':r},goal(r,id='fresh'))
        np.testing.assert_array_equal(c.odom.xy,[0.,0.])

    def test_invalid_goal_and_deferred_close(self):
        model=RobotModel();r=robot_fixture(model);c=Controller(model)
        bad=goal(r,base=[float('nan'),0.,0.])
        with self.assertRaises(ValueError):c.step({'step':0,'robot':r},bad)
        q=np.array(r['left']['joints']);q[0]+=.2
        close=goal(r,arms={'left':{'q':q.tolist()}},grippers={'left':0.,'right':1.})
        with self.assertRaisesRegex(ValueError,'Initialize explicit'):c.step({'step':0,'robot':r},close)
        close['id']='accepted';close['accept_partial']=True
        action,_=c.step({'step':0,'robot':r},close);self.assertEqual(action[14],-1.)


if __name__=='__main__':unittest.main()
