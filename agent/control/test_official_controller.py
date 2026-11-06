"""Synthetic official-observation adapter tests; no simulator imports."""
import copy
import unittest
import numpy as np
from official_controller import OfficialControllerPolicy,decode_observation
from portable_control import Controller
from robot_kinematics import RobotModel
from test_portable_control import robot_fixture,goal,advance


def profile_fixture(r):
    return {'schema':'r1pro-v393-static-profile-v1','robot_name':'robot_r1',
        'arms':{a:copy.deepcopy(r[a]['joint_endpoint_metadata']) for a in ('left','right')},
        'torso_joint_limits_rad':r['torso_joint_limits_rad'],'torso_slew_rad_per_tick':r['torso_slew_rad_per_tick'],
        'camera_order':['left','right','head'],'cameras':{a:{'observation_prefix':'robot_r1::'+a,
            'intrinsics':[[10.,0.,1.],[0.,10.,1.],[0.,0.,1.]],'image_size_hw':[2,2]} for a in ('left','head','right')}}


def encode(r):
    p=np.zeros(61,dtype=np.float32);p[:3]=r['base_velocity'];p[53:57]=r['torso_joints']
    for a,s in [('left',3),('right',28)]:
        p[s:s+7]=r[a]['joints'];p[s+14:s+17]=r[a]['eef_position'];p[s+17:s+21]=r[a]['eef_quaternion']
        p[s+21:s+23]=r[a]['finger_positions']
    flat={'robot_r1::proprio':p[None],'robot_r1::cam_rel_poses':np.tile([0.,0.,0.,0.,0.,0.,1.],3)[None],
          'task_id':np.array([[23]],dtype=np.int64),'untrusted_object_pose':np.ones(7)}
    for a in ('left','right','head'):
        flat['robot_r1::'+a+'::rgb']=np.zeros((1,2,2,4),dtype=np.uint8)
        flat['robot_r1::'+a+'::depth_linear']=np.ones((1,2,2),dtype=np.float32)
    return flat


class OfficialAdapterTests(unittest.TestCase):
    def test_one_action_same_core_and_reset(self):
        model=RobotModel();r=robot_fixture(model);profile=profile_fixture(r)
        q=np.array(r['left']['joints']);q[3]-=.06
        g=goal(r,arms={'left':{'q':q.tolist()}})
        calls=[]
        def planner(packet,previous):
            self.assertNotIn('untrusted_object_pose',packet)
            calls.append(packet)
            return copy.deepcopy(g) if previous is None else None
        policy=OfficialControllerPolicy(profile,planner,50);direct=Controller(model)
        for tick in range(20):
            flat=encode(r);action=policy.act(flat)
            packet=decode_observation(flat,profile,tick,model)
            expected,_=direct.step(packet,g)
            np.testing.assert_array_equal(action,expected[None])
            self.assertEqual(action.shape,(1,23));self.assertEqual(action.dtype,np.float32)
            advance(r,action[0],model)
        self.assertEqual(len(calls),2);self.assertEqual(len(policy.completed_goals),1)
        self.assertEqual(policy.completed_goals[0]['reason'],'reached')
        self.assertEqual(policy.packet['rgb']['head'].shape,(2,2,3))
        np.testing.assert_array_equal(np.array(policy.packet['cameras']['head']['camera_to_body'])[:3,:3],np.diag([1.,-1.,-1.]))
        policy.reset();self.assertEqual(policy.tick,0);self.assertIsNone(policy.goal)
        self.assertIsNone(policy.controller.odom);self.assertFalse(policy.controller.grips)

    def test_budget_and_batch_shape(self):
        model=RobotModel();r=robot_fixture(model);p=profile_fixture(r);clock=[0.]
        def slow(packet,previous):clock[0]+=601;return goal(r)
        policy=OfficialControllerPolicy(p,slow,1000,clock=lambda:clock[0])
        with self.assertRaisesRegex(TimeoutError,'query'):policy.act(encode(r))
        policy=OfficialControllerPolicy(p,lambda *args:goal(r),10,clock=lambda:clock[0])
        policy.act(encode(r));clock[0]+=11
        with self.assertRaisesRegex(TimeoutError,'Episode'):policy.act(encode(r))
        policy=OfficialControllerPolicy(p,lambda *args:goal(r),1,clock=lambda:0.)
        policy.act(encode(r));policy.act(encode(r))
        self.assertEqual(policy.tick,2) # Official evaluator owns native termination, not this wall budget.
        flat=encode(r);flat['robot_r1::proprio']=np.zeros((2,61))
        with self.assertRaises(ValueError):decode_observation(flat,p,0,model)
        flat=encode(r);flat['robot_r1::head::depth_linear']=np.zeros((1,2,2),dtype=np.uint8)
        with self.assertRaises(ValueError):decode_observation(flat,p,0,model)


if __name__=='__main__':unittest.main()
