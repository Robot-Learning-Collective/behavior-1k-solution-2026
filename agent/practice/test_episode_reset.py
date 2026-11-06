"""CPU fake-native regression: slicing topology -> original episode, not live physics proof."""
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np
from practice_snapshots import save_episode_scene, restore_episode


class Body:
    def __init__(self,name,uuid,value=0):self.name,self.uuid,self.value=name,uuid,value


class Scene:
    available_systems={'water','juice'}
    def __init__(self):
        self.bodies={'robot':Body('robot',17,.125),'sprout':Body('sprout',44510368,.5)}
        self.systems={'water':Body('water',20)}
    @property
    def objects(self):return list(self.bodies.values())
    def object_registry(self,key,name):
        assert key=='name';return self.bodies.get(name)
    def get_system(self,name,force_init):
        assert not force_init;return self.systems.get(name)


class Sim:
    def __init__(self,scene,task):self.scene,self.task,self.calls,self.leave_extra=scene,task,[],False
    def save(self,json_paths):
        Path(json_paths[0]).write_text(json.dumps({'objects':{o.name:o.uuid for o in self.scene.objects},'systems':list(self.scene.systems)}))
    def restore(self,paths):
        self.calls.append('topology');d=json.loads(Path(paths[0]).read_text())
        bodies={n:self.scene.bodies.get(n,Body(n,uuid,-9)) for n,uuid in d['objects'].items()}
        if self.leave_extra:self.scene.bodies.update(bodies)
        else:self.scene.bodies=bodies
        self.scene.systems={n:Body(n,20) for n in d['systems']}
        # Native add/remove callbacks are not an exact symbolic-binding restore.
        self.task.object_scopes[0]['whole']=None
    def load_state(self,state,serialized):
        self.calls.append('npz');assert serialized
        for uuid,value in np.asarray(state)[1:].reshape(-1,2):
            obj=next((o for o in self.scene.objects if o.uuid==int(uuid)),None)
            assert obj is not None,f'Could not find object while deserializing with hash_key uuid: {int(uuid)}'
            obj.value=float(value)


scene=Scene();robot=scene.bodies['robot']
task=SimpleNamespace(object_scopes=[{'whole':scene.bodies['sprout'],'half1':None,'half2':None,'water':scene.systems['water']}])
sim=Sim(scene,task);og=SimpleNamespace(sim=sim)
state=np.asarray([2,17,.125,44510368,.5],dtype=np.float32)
def cut():
    scene.bodies.pop('sprout')
    for i in (1,2):scene.bodies[f'half{i}']=Body(f'half{i}',90+i,.9)
    robot.value=8
    scene.systems={'juice':Body('juice',21)}
    task.object_scopes[0].update(whole=None,half1=scene.bodies['half1'],half2=scene.bodies['half2'],water=scene.systems['juice'])

with tempfile.TemporaryDirectory() as directory,patch.dict(sys.modules,torch=SimpleNamespace(from_numpy=lambda x:x)):
    snapshot=Path(directory)/'episode.npz';np.savez_compressed(snapshot,state=state)
    checkpoint=save_episode_scene(og,scene,task,snapshot)
    cut()
    try:sim.load_state(state,serialized=True)
    except AssertionError as e:assert '44510368' in str(e)
    else:raise AssertionError('Old serialized-only reset should fail after slicing')
    for repeat in range(3):
        if repeat:cut()
        sim.calls.clear();restore_episode(og,scene,task,snapshot,checkpoint)
        assert sim.calls==['topology','npz']
        assert set(scene.bodies)=={'robot','sprout'} and scene.bodies['robot'] is robot
        assert robot.value==.125 and scene.bodies['sprout'].value==.5
        assert set(scene.systems)=={'water'}
        assert task.object_scopes[0]=={'whole':scene.bodies['sprout'],'half1':None,'half2':None,'water':scene.systems['water']}
    # Historical non-task checkpoints retain their exact serialized-only route.
    sim.calls.clear();restore_episode(og,scene,None,snapshot)
    assert sim.calls==['npz']
    for invalid in (None,{**checkpoint,'scene_sha256':'wrong'}):
        sim.calls.clear()
        try:restore_episode(og,scene,task,snapshot,invalid)
        except RuntimeError:pass
        else:raise AssertionError('Missing/corrupt topology admitted')
        assert sim.calls==[], 'Reject bad checkpoint before any native mutation'
    cut();sim.leave_extra=True;sim.calls.clear()
    try:restore_episode(og,scene,task,snapshot,checkpoint)
    except RuntimeError as e:assert 'registry mismatch' in str(e)
    else:raise AssertionError('Generated parts left in scene were accepted')
    assert sim.calls==['topology'], 'Do not deserialize into unreconciled topology'

source=Path(__file__).with_name('worker.py').read_text()
reset=source.split("if op == 'reset':",1)[1].split("elif op == 'observe':",1)[0]
assert 'restore_episode(' in reset and 'og.sim.load_state(' not in reset
assert "if op in ('reset','snapshot','restore'):" in source and "(work/'CANCEL').touch()" in source
assert 'scene_checkpoint' in source and 'save_episode_scene(og,scene,env.task,target)' in source
print('EPISODE_RESET_CPU_PASS: old missing-UUID reproduced; topology/parts/systems + exact bindings + NPZ restored3x; legacy preserved; corrupt/incomplete reset rejected and worker fences reset faults')
