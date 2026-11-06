"""Synthetic single-RPC client/core integration; image bridge has separate tests."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
from unittest.mock import patch
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from portable_control import Controller
from robot_kinematics import RobotModel
from test_portable_control import robot_fixture, advance


def main():
    with tempfile.TemporaryDirectory(prefix='per-tick-client-test-') as temp:
        run=Path(temp)
        (run/'SETUP.json').write_text(json.dumps({'queue':'CPU_ONLY','remote_rpc':'CPU_RPC','remote_admin':'CPU_ADMIN','client_helpers':str(Path(__file__).resolve().parent)}))
        with patch.dict(os.environ,BEHAVIOR_SIM_RUN_DIR=str(run)):
            spec=importlib.util.spec_from_file_location('goal_candidate',Path(__file__).with_name('sim_client.py'))
            s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
        model=RobotModel();controller=Controller(model);r=robot_fixture(model)
        obs={'observation_id':1,'attempt_id':'cpu','controller_protocol':6,'ended':False,'simulated_seconds':0.,
             'last_commanded_grip':{'left':1.,'right':1.},'robot':r}
        r['base_odometry']={'position_rel_start_body':[0.,0.,0.],'yaw_rel_start_rad':0.}
        calls=[];ticks=0;published=[]
        cache=run/'state.json';cache.write_text(json.dumps(obs))
        def rpc(cmd,input,timeout):
            nonlocal obs,ticks
            job=json.loads(input);calls.append(job);g=job['action']
            assert 'seconds' not in g
            action,done=controller.step({'step':ticks,'robot':r},g)
            while True:
                advance(r,action,model);ticks+=1
                old_done=done
                action,done=controller.step({'step':ticks,'robot':r},g)
                if old_done:break
            r['base_odometry']=controller.odom.state()
            execution={'requested_ticks':None,'executed_ticks':controller.result['steps'],
                       'stop_reason':controller.reason,'fault':None,'execution_uncertain':False}
            obs={**obs,'observation_id':obs['observation_id']+1,'simulated_seconds':ticks/30,
                 'act_result':copy.deepcopy(controller.result),'execution':execution,
                 'last_commanded_grip':controller.grips.copy(),'motion_execution_uncertain':False}
            return json.dumps(obs).encode()
        with patch.object(s,'STATE_CACHE',cache),patch.object(s,'last_obs',side_effect=lambda:copy.deepcopy(obs)),\
             patch.object(s,'_save_and_summarize',side_effect=lambda reply,**kw:reply),\
             patch.object(s,'_publish_observation',side_effect=lambda *a,**kw:published.append(a)),\
             patch('subprocess.check_output',side_effect=rpc):
            start=np.array(r['left']['eef_position'])
            out=s.act(left={'left':.08,'up':.02})
            assert len(calls)==1 and len(published)==1 and out['act_result']['achieved']
            np.testing.assert_allclose(np.array(calls[0]['action']['arms']['left']['p'])-start,[0.,.08,.02],atol=1e-8)
            assert ticks>3 and 'max_steps' not in calls[0]['action'],'Unspecified move must not inherit a16tick limit'
            before=ticks
            out=s.act(base={'fwd':.3},seconds=.1,max_steps=16)
            assert ticks-before==3 and not out['act_result']['achieved'] and calls[-1]['action']['max_steps']==3
            before=ticks
            out=s.act(base={'fwd':.3},max_steps=1)
            assert ticks-before==1 and not out['act_result']['achieved']
            for bad in ({'max_steps':True},{'max_steps':0},{'max_steps':1.5},{'seconds':0},{'seconds':float('nan')}):
                try:s.act(base={'fwd':.3},**bad)
                except ValueError:pass
                else:raise AssertionError('Invalid caller cap accepted')
            assert len(calls)==3
            obs['motion_memory']={'unresolved_pose_misses':{'left':{'requested':'unreached previous test goal'}}}
            out=s.act(left={'grip':0})
            assert len(calls)==3 and out['act_result']['reason']=='prerequisite_not_met'
            out=s.act(left={'grip':0},accept_partial=True)
            assert len(calls)==4 and out['act_result']['reason']=='stalled' # Deliberately frozen synthetic fingers.
            def dropped(cmd,input,timeout):
                assert len(json.loads(input)['action']['arms']['right']['q'])==7
                raise TimeoutError('dropped synthetic reply')
            with patch('subprocess.check_output',side_effect=dropped):
                try:s.act(right='ready')  # Run-local preset helper must resolve before the uncertain RPC.
                except TimeoutError:pass
                else:raise AssertionError('Expected uncertain RPC')
            stored=json.loads(cache.read_text())
            assert stored['motion_execution_uncertain'] and not stored['last_commanded_grip']
        entered=threading.Event();cancelled=threading.Event();transport=[]
        def boundary(cmd,**kwargs):
            transport.append(cmd)
            if '--cancel' in cmd:cancelled.set();return b''
            entered.set();assert cancelled.wait(3),'STOP did not cancel the in-flight RPC'
            return b'cancelled-endpoint'
        def stop():
            assert entered.wait(3)
            raise RuntimeError('Synthetic user STOP')
        with patch.object(s,'check_stop',side_effect=stop),patch('subprocess.check_output',side_effect=boundary):
            assert s._goal_rpc({'op':'act','action':{},'request_id':'synthetic-id'})==b'cancelled-endpoint'
        assert len(transport)==2 and '--cancel' in transport[1] and transport[1][-1]=='synthetic-id'
        entered.clear();cancelled.clear();transport.clear()
        with patch.dict(s.SETUP,rpc_transport={'version':'framed-policy-v1','remote_rpc':'CPU_FRAMED_RPC'}),\
             patch.object(s,'check_stop',side_effect=stop),patch('subprocess.check_output',side_effect=boundary),\
             patch('rpc_stream.request',side_effect=lambda cmd,job,timeout:boundary(cmd)):
            assert s._goal_rpc({'op':'act','action':{},'request_id':'synthetic-id'})==b'cancelled-endpoint'
        assert transport[0][-1]=='CPU_FRAMED_RPC' and '--cancel' in transport[1]
        memory={'attempt_id':'old','observation_id':9,'motion_memory':{'unresolved_pose_misses':{'left':'miss'}},'last_commanded_grip':{'left':.3},'motion_execution_uncertain':False}
        def fresh_observe(intent):
            seed=json.loads(cache.read_text())
            assert seed['attempt_id']=='new' and seed['motion_memory']==memory['motion_memory']
            assert 'robot' not in seed and 'local_image_path' not in seed
            return {'attempt_id':'new','observation_id':1}
        with patch.object(s,'STATE_CACHE',cache),patch.object(s,'_snapshot_admin',return_value={'restored':True,'attempt_id':'new','client_state':memory}),patch.object(s,'observe',side_effect=fresh_observe):
            cache.write_text(json.dumps(obs))
            assert s.restore('saved')['observation']['observation_id']==1
        with patch.object(s,'STATE_CACHE',cache),patch.object(s,'_snapshot_admin',side_effect=TimeoutError('lost restore reply')):
            cache.write_text(json.dumps(obs))
            try:s.restore('saved')
            except TimeoutError:pass
            else:raise AssertionError('Expected restore timeout')
            assert not cache.exists(),'Stale old-world cache survived an uncertain restore'
    print('PASS: single full-goal RPC, explicit hard caps/defaultNone, prior-miss gate, partial close, uncertainty fence, in-flight STOP cancellation')


if __name__=='__main__':main()
