"""CPU fake-native roundtrip + real whole-Controller serialization, not live physics proof."""
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'control'))
from portable_control import Controller  # noqa: E402
from robot_kinematics import RobotModel
from test_portable_control import robot_fixture, goal
from practice_snapshots import Snapshots, SnapshotRejected, name_ok


class Tensor:
    def __init__(self, x):self.x=np.asarray(x)
    def detach(self):return self
    def cpu(self):return self
    def numpy(self):return self.x


class Body:
    name='robot'
    def __init__(self):self.p=np.zeros(3);self.q=np.zeros(4)
    def get_position_orientation(self):return self.p.copy(),np.array([0,0,0,1.])
    def get_joint_positions(self):return Tensor(self.q)


r=robot_fixture(RobotModel());c=Controller();g=goal(r)
g.update(base=[.3,0.,0.],max_steps=30)
c.step({'step':7,'robot':r},g)
c.command_q['left'][0]+=.07;c.command_torso[0]+=.04
c.grips={'left':.3,'right':.7};c.misses={'left':{'action_id':'prior','diagnosis':'miss'}}
c.odom.xy[:]=[1.,2.];c.odom.velocity[:]=[.1,.2,.3]
# Snapshot just before the fifteenth blocked-feedback sample trips the guard.
c.base_feedback=[(np.array([.2,0.,0.]),np.zeros(3)) for _ in range(14)]
expected_controller=copy.deepcopy(c)
expected=expected_controller.step({'step':7,'robot':r},g)[0]
body=Body();scene=SimpleNamespace(objects=[body]);closed=[]
class Sim:
    def save(self,json_paths):Path(json_paths[0]).write_text(json.dumps({'p':body.p.tolist(),'q':body.q.tolist()}))
    def restore(self,files):
        d=json.loads(Path(files[0]).read_text());body.p=np.array(d['p']);body.q=np.array(d['q'])
fake_torch=SimpleNamespace(get_rng_state=lambda:b'rng',set_rng_state=lambda v:None,
    cuda=SimpleNamespace(is_initialized=lambda:False))
with tempfile.TemporaryDirectory() as temp,patch.dict(sys.modules,torch=fake_torch):
    root=Path(temp);run=root/'original';run.mkdir()
    s={'root':run,'started':None,'step':7,'practice':True,'unbounded_practice':True,'controller':c,
       'last_arm_q_target':{a:q.tolist() for a,q in c.command_q.items()},'last_torso_q_target':c.command_torso.tolist(),
       'stable':0,'success':False,'truth':[{'PRIVATE':True}],'frames':[],'observation':3}
    store=Snapshots(root,SimpleNamespace(sim=Sim()),scene,body,lambda:None,closed.append,{'code':'same'})
    for name in ['../oops','/tmp/x','a/b','', '.', 'x'*65]:
        try:name_ok(name)
        except SnapshotRejected:pass
        else:raise AssertionError(name)
    try:store.save(dict(s,practice=False),'eval',None)
    except SnapshotRejected:pass
    else:raise AssertionError('Evaluation checkpoint admitted')
    cache={'attempt_id':'original','observation_id':3,'motion_memory':{'misses':['left']},'last_commanded_grip':c.grips.copy()}
    assert store.save(s,'before',cache)=={'saved':True,'name':'before','attempt_id':'original'}
    try:store.save(s,'before',cache)
    except SnapshotRejected:pass
    else:raise AssertionError('Snapshot silently overwritten')
    body.p[:]=2;body.q[:]=.2;c.command_q['left'][:]=0;c.grips.clear()
    restored,reply=store.restore(s,'before')
    assert closed==['practice-snapshot-restore-boundary'] and reply['attempt_id']!='original'
    assert restored['step']==7 and restored['observation']==0 and restored['started'] is None
    assert restored['truth']==[] and reply['client_state']==cache
    assert restored['controller'].grips=={'left':.3,'right':.7}
    assert restored['controller'].misses=={'left':{'action_id':'prior','diagnosis':'miss'}}
    np.testing.assert_array_equal(restored['controller'].step({'step':7,'robot':r},g)[0],expected)
    assert len(restored['controller'].base_feedback)==14 and restored['controller'].caller_step_limit==30
    next_action=restored['controller'].step({'step':8,'robot':r},g)[0]
    np.testing.assert_array_equal(next_action,expected_controller.step({'step':8,'robot':r},g)[0])
    np.testing.assert_array_equal(next_action[:3],0)
    assert restored['controller'].base_guard_triggered and restored['controller'].reason=='stalled'
    np.testing.assert_array_equal(body.p,np.zeros(3));np.testing.assert_array_equal(body.q,np.zeros(4))
    _,again=store.restore(restored,'before');assert again['attempt_id']!=reply['attempt_id']
    try:store.restore(dict(restored,practice=False),'before')
    except SnapshotRejected:pass
    else:raise AssertionError('Restore during evaluation admitted')
    store.source={'code':'changed'}
    try:store.restore(restored,'before')
    except SnapshotRejected:pass
    else:raise AssertionError('Source mismatch admitted')
print('PRACTICE_SNAPSHOT_BOUNDARIES_WHOLE_CONTROLLER_NEXT_ACTION_CACHE_NAMESPACE_CPU_PASS')
