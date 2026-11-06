"""Agent routing against the real serve_b1k.py connection handler, without JAX.

A tiny fake policy and a fake agent runtime isolate the routing rules; this is not task-success evidence.
Run from the repository root: python -m unittest agent.eval.test_route
"""
from copy import deepcopy
import json
import sys
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import numpy as np
import websockets

from .serve_agent_only import load_agent_route, load_server_class, pack, unpack

route_module = load_agent_route()
AgentRoute = route_module.AgentRoute


class Tensor:
    def __init__(self,value):self.value=np.asarray(value,dtype=np.float32)
    def cpu(self):return self
    def numpy(self):return self.value


class Policy:
    def __init__(self):self.calls=0;self.reset()
    def reset(self):self.action_index=0;self.prediction_count=0;self.current_stage=2
    def act(self,obs):
        self.calls+=1;self.action_index+=1;self.prediction_count+=1
        return Tensor(np.full(23,self.action_index))


def batched(policies,obs):
    return Tensor(np.stack([p.act({k:v[i] for k,v in obs.items()}).numpy() for i,p in enumerate(policies)]))


def server_class():
    return load_server_class(act_batched=batched)


class Socket:
    remote_address=('cpu-test',0)
    def __init__(self,messages):self.messages=iter(messages);self.sent=[]
    async def recv(self):
        try:return pack(next(self.messages))
        except StopIteration:raise websockets.ConnectionClosed(None,None)
    async def send(self,data):self.sent.append(unpack(data))
    async def close(self,**kwargs):pass


class Runtime:
    """Fake frozen runtime: answers 42, or fails / hangs on a chosen call."""
    def __init__(self,epoch,fail_at=None,hang_at=None,bridge_timeout_at=None,slow=0):
        self.epoch=epoch;self.closed=False;self.calls=0;self.fail_at=fail_at;self.hang_at=hang_at
        self.bridge_timeout_at=bridge_timeout_at;self.slow=slow;self.released=threading.Event()
    def act(self,obs):
        self.calls+=1
        if self.calls==self.fail_at:raise RuntimeError('provider error (test)')
        if self.calls==self.bridge_timeout_at:raise TimeoutError(route_module.BRIDGE_WAIT_TIMEOUT)
        if self.calls==self.hang_at:
            self.released.wait(10);raise RuntimeError('closed while planning')
        if self.slow:time.sleep(self.slow)
        return np.full((1,23),42,dtype=np.float32)
    def close(self):self.closed=True;self.released.set()


OK=lambda model:(True,'test')
AGENT_OBS={'robot_r1::proprio':np.zeros((1,61)),'task_id':np.array([[34]]),
           'robot_r1::cam_rel_poses':np.zeros((1,21)),'head::depth_linear':np.ones((1,1,1))}


class RoutingTests(unittest.IsolatedAsyncioTestCase):
    async def run_handler(self,messages,enabled,runtime_factory=None,preflight=OK):
        policies=[]
        def factory():p=Policy();policies.append(p);return p
        server=server_class()(factory,port=0,metadata={'base':'unchanged'},
                              agent_tasks={34:{'task_name':'hanging_pictures'}} if enabled else None)
        socket=Socket(messages)
        shim=SimpleNamespace(AgentRoute=lambda task:AgentRoute(task,runtime_factory=runtime_factory,preflight=preflight,
                                                               camera_check=lambda obs:None))
        try:
            with patch.dict(sys.modules,{'b1k.policies.agent':shim}):
                await server._handler(socket)
        finally:server._worker.shutdown(wait=True)
        return socket.sent,policies

    async def test_base_single_batch_and_partial_reset_unchanged(self):
        obs={'robot_r1::proprio':np.zeros(61),'task_id':np.array([0])}
        batch={k:np.stack([v,v]) for k,v in obs.items()}
        messages=[{'reset':True},obs,obs,{'reset':True},batch,batch,{'reset':True,'env_indices':[1]},batch]
        baseline,old=await self.run_handler(deepcopy(messages),False)
        routed,new=await self.run_handler(deepcopy(messages),True)
        self.assertEqual([p.calls for p in old],[p.calls for p in new])
        for left,right in zip(baseline,routed):
            self.assertEqual(left.keys(),right.keys())
            for key in left:
                if key!='server_timing':np.testing.assert_array_equal(left[key],right[key])

    async def test_agent_bypasses_base_and_closes(self):
        made=[]
        def factory(epoch):r=Runtime(epoch);made.append(r);return r
        sent,base=await self.run_handler([{'reset':True},AGENT_OBS,{'reset':True},AGENT_OBS],True,factory)
        self.assertEqual(sum(p.calls for p in base),0)
        self.assertEqual(len(made),2);self.assertNotEqual(made[0].epoch,made[1].epoch)
        self.assertTrue(all(r.closed for r in made))
        self.assertEqual(sent[-1]['action_owner'],'agent')

    async def test_agent_error_falls_back_for_the_episode_only(self):
        made=[]
        def factory(epoch):r=Runtime(epoch,fail_at=2);made.append(r);return r
        msgs=[{'reset':True},AGENT_OBS,AGENT_OBS,AGENT_OBS,{'reset':True},AGENT_OBS]
        with self.assertLogs(level='ERROR') as logs:
            sent,base=await self.run_handler(msgs,True,factory)
        owners=[m.get('action_owner') for m in sent[1:]]
        self.assertEqual(owners,['agent',None,None,'agent'])  # episode 2 starts fresh
        self.assertEqual(sum(p.calls for p in base),2)
        self.assertEqual(len(made),2);self.assertTrue(made[0].closed)
        self.assertTrue(any('AGENT FAILED' in line for line in logs.output))

    async def test_preflight_failure_runs_base_and_retries_next_episode(self):
        made=[];checks=[]
        def factory(epoch):r=Runtime(epoch);made.append(r);return r
        def preflight(model):checks.append(model);return (len(checks)>1,'HTTP 401 invalid_api_key: sk-***')
        msgs=[{'reset':True},AGENT_OBS,AGENT_OBS,{'reset':True},AGENT_OBS]
        with self.assertLogs(level='ERROR'):
            sent,base=await self.run_handler(msgs,True,factory,preflight)
        self.assertEqual([m.get('action_owner') for m in sent[1:]],[None,None,'agent'])
        self.assertEqual(len(checks),2);self.assertEqual(len(made),1)

    async def test_slow_agent_holds_then_falls_back_on_third_timeout(self):
        made=[]
        def factory(epoch):r=Runtime(epoch,hang_at=2);made.append(r);return r
        with patch.object(route_module,'QUERY_LIMIT_S',0.3),self.assertLogs(level='ERROR') as logs:
            sent,base=await self.run_handler([{'reset':True}]+[AGENT_OBS]*5,True,factory)
        owners=[m.get('action_owner') for m in sent[1:]]
        self.assertEqual(owners,['agent','agent','agent',None,None])  # act, hold, hold, base
        hold=sent[2]['action'];self.assertEqual(hold.shape,(1,23));self.assertTrue(np.all(hold[0,:3]==0))
        self.assertEqual(sum(p.calls for p in base),2);self.assertTrue(made[0].closed)
        text='\n'.join(logs.output)
        self.assertEqual(text.count('AGENT SLOW'),2);self.assertIn('3 consecutive',text)

    async def test_slow_answer_after_hold_resets_the_count(self):
        def factory(epoch):return Runtime(epoch,slow=0.5)
        with patch.object(route_module,'FIRST_QUERY_LIMIT_S',0.3),patch.object(route_module,'QUERY_LIMIT_S',0.4), \
                self.assertLogs(level='ERROR'):
            sent,base=await self.run_handler([{'reset':True}]+[AGENT_OBS]*4,True,factory)
        actions=[m['action'] for m in sent[1:]]
        self.assertTrue(all(m.get('action_owner')=='agent' for m in sent[1:]))
        self.assertTrue(np.all(actions[1]==42) and np.all(actions[3]==42))  # holds answered, then the plans arrived
        self.assertEqual(sum(p.calls for p in base),0)

    async def test_bridge_wait_timeout_is_reissued_not_failed(self):
        def factory(epoch):return Runtime(epoch,bridge_timeout_at=2)
        sent,base=await self.run_handler([{'reset':True},AGENT_OBS,AGENT_OBS],True,factory)
        self.assertEqual([m.get('action_owner') for m in sent[1:]],['agent','agent'])
        self.assertTrue(np.all(sent[2]['action']==42));self.assertEqual(sum(p.calls for p in base),0)

    async def test_action_chunk_request_is_answered_per_step(self):
        def factory(epoch):return Runtime(epoch)
        sent,base=await self.run_handler([{'reset':True},{**AGENT_OBS,'__action_chunk_size__':8}],True,factory)
        self.assertEqual(sent[1]['action_owner'],'agent');self.assertNotIn('action_chunk',sent[1])

    async def test_unsupported_setups_use_base(self):
        made=[]
        def factory(epoch):r=Runtime(epoch);made.append(r);return r
        batch={k:np.stack([v[0],v[0]]) for k,v in AGENT_OBS.items()}
        msgs=[AGENT_OBS,{'reset':True},batch]  # no reset / num-envs 2 on one connection
        with self.assertLogs(level='ERROR') as logs:
            sent,base=await self.run_handler(msgs,True,factory)
        self.assertEqual(made,[]);self.assertTrue(all('action_owner' not in m for m in sent))
        text='\n'.join(logs.output)
        for needle in ('no evaluator reset','--num-envs 1'):self.assertIn(needle,text)

    def test_wrong_resolution_warns_for_every_task_and_agent_falls_back(self):
        default={'robot_r1::proprio':np.zeros(61),'robot_r1::robot_r1:zed_link:Camera:0::rgb':np.zeros((224,224,3),np.uint8)}
        self.assertIn('expected (720, 720)',route_module.camera_problem(default))
        full={'robot_r1::proprio':np.zeros(61),'robot_r1::cam_rel_poses':np.zeros(21)}
        for meta in route_module._profile()['cameras'].values():
            h,w=meta['image_size_hw'];full[meta['observation_prefix']+'::rgb']=np.zeros((h,w,4),np.uint8)
            full[meta['observation_prefix']+'::depth_linear']=np.zeros((h,w),np.float32)
        self.assertIsNone(route_module.camera_problem(full))
        for task in (0,34):
            route=AgentRoute({34:{'task_name':'hanging_pictures'}},runtime_factory=Runtime,preflight=OK);route.reset()
            with self.assertLogs(level='ERROR') as logs:
                self.assertIsNone(route.step({**default,'task_id':np.array([task])}))
            self.assertIn('WRONG OBSERVATIONS',''.join(logs.output));route.shutdown()
        route=AgentRoute({34:{'task_name':'hanging_pictures'}},runtime_factory=Runtime,preflight=OK);route.reset()
        self.assertIsNotNone(route.step({**full,'task_id':np.array([34])}));route.shutdown()

    def test_hold_action_from_proprio_keeps_joints(self):
        q=np.arange(61,dtype=np.float64)/100
        a=route_module.hold_action({'robot_r1::proprio':q})
        np.testing.assert_allclose(a[:3],0);np.testing.assert_allclose(a[3:7],q[53:57],rtol=1e-6)
        np.testing.assert_allclose(a[7:14],q[3:10],rtol=1e-6);np.testing.assert_allclose(a[15:22],q[28:35],rtol=1e-6)
        self.assertTrue(-1<=a[14]<=1 and -1<=a[22]<=1)
        last=np.arange(23,dtype=np.float32)
        b=route_module.hold_action({'robot_r1::proprio':q},last)
        np.testing.assert_allclose(b[:3],0);np.testing.assert_allclose(b[3:],last[3:])

    def test_registry_enabled_set(self):
        all_tasks=json.loads(route_module.REGISTRY.read_text())['tasks']
        tasks=route_module.load_enabled_tasks()
        self.assertTrue({e['task_name'] for e in tasks.values()}<=set(all_tasks))
        self.assertEqual(set(all_tasks),
                         {'attach_a_camera_to_a_tripod','clean_a_patio','installing_smoke_detectors','clean_a_trumpet',
                          'make_cabinet_doors','installing_a_scanner','hanging_pictures','cook_a_brisket','cook_cabbage',
                          'cook_brussels_sprouts','installing_a_fax_machine','vacuuming_floors','unloading_the_car',
                          'scrubbing_bathroom_floor'})
        self.assertTrue(all(e['model']=='openai/gpt-6-astra' and e['thinking']=='medium' for e in tasks.values()))
        obs={'robot_r1::proprio':np.zeros(61),'robot_r1::cam_rel_poses':np.zeros(21),'head::depth_linear':np.ones((1,1))}
        for task_id in (*tasks,0):
            route=AgentRoute(tasks,runtime_factory=Runtime,preflight=OK,camera_check=lambda o:None);route.reset()
            self.assertEqual(route.step({**obs,'task_id':np.array([task_id])}) is not None,task_id in tasks)
            route.shutdown()

    def test_missing_frozen_context_stops_startup(self):
        with patch.object(route_module,'api_preflight',return_value=(True,'ok')):
            with patch.object(route_module,'missing_contexts',return_value=['clean_a_trumpet']),self.assertLogs(level='ERROR') as logs:
                self.assertFalse(route_module.startup_check({37:{'task_name':'clean_a_trumpet'}}))
        self.assertTrue(any('FROZEN PRACTICE CONTEXTS ARE MISSING' in line for line in logs.output))

    @patch.object(route_module,'missing_contexts',return_value=[])
    def test_preflight_without_key_is_offline_and_loud(self,_):
        with patch.dict(route_module.os.environ,{},clear=True):
            self.assertEqual(route_module.api_preflight('openai/gpt-6-astra'),
                             (False,'OPENAI_API_KEY is not set in the container'))
            with self.assertLogs(level='ERROR') as logs:
                self.assertFalse(route_module.startup_check({35:{'task_name':'attach_a_camera_to_a_tripod'}}))
        self.assertTrue(any('STARTUP FAILED' in line for line in logs.output))
        self.assertTrue(any('OPENAI_API_KEY is not set.' in line for line in logs.output))
        with patch.object(route_module,'api_preflight',return_value=(True,'ok')):
            self.assertTrue(route_module.startup_check({35:{'task_name':'attach_a_camera_to_a_tripod'}}))
        with patch.dict(route_module.os.environ,{'OPENAI_API_KEY':'sk-x'}),\
             patch.object(route_module,'api_preflight',return_value=(False,'URLError: timed out')):
            with self.assertLogs(level='ERROR') as logs:
                self.assertFalse(route_module.startup_check({35:{'task_name':'attach_a_camera_to_a_tripod'}}))
        self.assertTrue(any('reach api.openai.com' in line for line in logs.output))
        self.assertEqual(route_module.api_preflight('openai-codex/gpt-6-astra')[0],True)


if __name__=='__main__':unittest.main(verbosity=2)
