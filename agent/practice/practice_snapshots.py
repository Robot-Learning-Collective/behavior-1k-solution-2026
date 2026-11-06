"""Private native scene + complete portable-controller checkpoints, RPC-boundary only.

Trusted local pickle files only: names are not paths, artifacts/source are bound,
and no native scene/object/scorer data is returned through the policy API.
"""
import hashlib
import json
import os
from pathlib import Path
import pickle
import random
import re
import time
import uuid

import numpy as np


class SnapshotRejected(ValueError):
    pass


def name_ok(name):
    if not isinstance(name, str) or re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', name) is None:
        raise SnapshotRejected('Name must be 1..64 letters, digits, underscores or hyphens')
    return name


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def task_bindings(scene, task):
    return None if task is None else {
        key: None if entity is None else {'name':entity.name,'system':entity.name in scene.available_systems}
        for key,entity in task.object_scopes[0].items()}


def restore_scene(og, scene, task, path, bindings):
    # Native restore reconciles added/removed objects and systems before state load.
    og.sim.restore([str(path)])
    if task is not None:
        # Topology callbacks may bind same-category future objects in a different order.
        for key,binding in bindings.items():
            entity = None if binding is None else (
                scene.get_system(binding['name'],force_init=False) if binding['system'] else
                scene.object_registry('name',binding['name']))
            if binding is not None and entity is None:raise RuntimeError('Task binding missing after native restore')
            task.object_scopes[0][key]=entity


def save_episode_scene(og, scene, task, snapshot):
    """Private initial topology paired with the immutable episode NPZ; never policy data."""
    path=Path(snapshot).with_suffix('.scene.json')
    if path.exists():raise RuntimeError('Initial episode scene already exists; preserve it')
    og.sim.save(json_paths=[str(path)])
    if not path.is_file():raise RuntimeError('Initial episode native scene save not ready')
    os.chmod(path,0o600)
    return {'scene_sha256':sha(path),'objects':sorted(o.name for o in scene.objects),
            'task_bindings':task_bindings(scene,task)}


def restore_episode(og, scene, task, snapshot, checkpoint=None):
    if task is not None:
        if checkpoint is None:raise RuntimeError('Initial task topology missing; requires a fresh worker')
        path=Path(snapshot).with_suffix('.scene.json')
        if sha(path)!=checkpoint['scene_sha256']:raise RuntimeError('Initial episode scene checksum mismatch')
        restore_scene(og,scene,task,path,checkpoint['task_bindings'])
        if sorted(o.name for o in scene.objects)!=checkpoint['objects']:
            raise RuntimeError('Initial episode object registry mismatch')
    # Preserve the existing exact robot/controllers/AG/state reset after topology repair.
    import torch
    with np.load(snapshot) as state:
        og.sim.load_state(torch.from_numpy(state['state']),serialized=True)


class Snapshots:
    def __init__(self, artifacts, og, scene, robot, refresh, close, source, task=None):
        self.artifacts = Path(artifacts).resolve()
        self.home = self.artifacts / 'practice-snapshots-private'
        self.home.mkdir(mode=0o700, exist_ok=True)
        self.og, self.scene, self.robot = og, scene, robot
        self.refresh, self.close = refresh, close
        self.source, self.task = source, task

    def path(self, name):
        p = self.home / name_ok(name)
        if p.is_symlink() or p.resolve().parent != self.home.resolve():
            raise SnapshotRejected('Invalid snapshot location')
        return p

    @staticmethod
    def practice(session):
        if session is not None and not session.get('practice', False):
            raise SnapshotRejected('Snapshots are practice-only; evaluation/full attempts are forbidden')
        if session is not None and session.get('infrastructure_invalid'):
            raise SnapshotRejected('Uncertain simulator state cannot be checkpointed or continued')

    def journal(self, event):
        with (self.artifacts / 'practice-snapshot-results.jsonl').open('a') as f:
            f.write(json.dumps(dict(time_ns=time.time_ns(), **event))+'\n')

    def poses(self):
        def arr(x):
            return x.detach().cpu().numpy() if hasattr(x, 'detach') else np.asarray(x)
        return {o.name: tuple(arr(v).copy() for v in o.get_position_orientation()) for o in self.scene.objects}

    def save(self, session, name, client_state):
        self.practice(session)
        if session is None:
            raise SnapshotRejected('Start a practice attempt before snapshot')
        if client_state and (client_state.get('attempt_id') != session['root'].name or
                             client_state.get('observation_id') != session['observation']):
            raise SnapshotRejected('Stale client cache; observe before snapshot')
        if client_state and client_state.get('motion_execution_uncertain'):
            raise SnapshotRejected('Resolve uncertain client execution before snapshot')
        dest = self.path(name)
        if dest.exists():
            raise SnapshotRejected('Snapshot name already exists; choose a new name')
        stage = self.home / ('.saving-'+uuid.uuid4().hex)
        stage.mkdir(mode=0o700)
        self.og.sim.save(json_paths=[str(stage/'scene.json')])
        if not (stage/'scene.json').is_file():
            raise SnapshotRejected('Native save not ready; finish initialization first')
        # Retain every controller field and worker command/grip/step mirror. Only
        # attempt accounting/history is replaced on restore, not physical feedback.
        state = {k:v for k,v in session.items() if k not in
                 ('root','started','truth','frames','observation','completion_wall')}
        import torch
        packet = dict(session=state, client_state=client_state, poses=self.poses(),
                      robot_joints=self.robot.get_joint_positions().detach().cpu().numpy().copy(),
                      origin_attempt=session['root'].name, random=random.getstate(),
                      numpy_random=np.random.get_state(), torch_random=torch.get_rng_state(),
                      cuda_random=torch.cuda.get_rng_state() if torch.cuda.is_initialized() else None)
        packet['task_bindings'] = task_bindings(self.scene,self.task)
        (stage/'state.pkl').write_bytes(pickle.dumps(packet, protocol=5))
        meta = dict(protocol=6, source=self.source, artifact_root=str(self.artifacts),
                    scene_sha256=sha(stage/'scene.json'), state_sha256=sha(stage/'state.pkl'))
        (stage/'metadata.json').write_text(json.dumps(meta))
        for p in stage.iterdir():os.chmod(p, 0o600)
        stage.rename(dest)
        self.journal(dict(op='snapshot', name=name, attempt=session['root'].name, step=session['step']))
        return dict(saved=True, name=name, attempt_id=session['root'].name)

    def restore(self, session, name):
        self.practice(session)
        p = self.path(name)
        if not p.is_dir():raise SnapshotRejected('Unknown snapshot name')
        meta = json.loads((p/'metadata.json').read_text())
        if (meta['protocol'] != 6 or meta['source'] != self.source or
                meta['artifact_root'] != str(self.artifacts) or
                meta['scene_sha256'] != sha(p/'scene.json') or meta['state_sha256'] != sha(p/'state.pkl')):
            raise SnapshotRejected('Snapshot source/model/protocol/ownership or checksum mismatch')
        packet = pickle.loads((p/'state.pkl').read_bytes())  # Trusted own files, after binding/integrity checks.
        restored = packet['session']
        self.practice(restored)
        if not restored.get('practice'):raise SnapshotRejected('Saved state was not practice')
        attempt = 'practice-restore-'+name+'-'+uuid.uuid4().hex
        output = self.artifacts / attempt
        output.mkdir(exist_ok=False)
        closed = self.close('practice-snapshot-restore-boundary') if session is not None else None
        self.journal(dict(op='restore_started', name=name, attempt=attempt,
                          origin_attempt=packet['origin_attempt'], step=restored['step']))
        # Native restore handles registry topology, particles, robot native
        # controller groups and assisted-grasp constraints. Never env.reset().
        restore_scene(self.og,self.scene,self.task,p/'scene.json',packet['task_bindings'])
        self.refresh()
        current = self.poses()
        if set(current) != set(packet['poses']):raise RuntimeError('Restored object registry mismatch')
        position_error = max(float(np.max(np.abs(current[n][0]-v[0]))) for n,v in packet['poses'].items())
        orientation_error = max(float(min(np.max(np.abs(current[n][1]-v[1])),
                                          np.max(np.abs(current[n][1]+v[1])))) for n,v in packet['poses'].items())
        joint_error = float(np.max(np.abs(self.robot.get_joint_positions().detach().cpu().numpy()-packet['robot_joints'])))
        if position_error > 1e-4 or orientation_error > 1e-4 or joint_error > 1e-4:
            raise RuntimeError('Native restore pose verification failed; world fenced')
        import torch
        random.setstate(packet['random']);np.random.set_state(packet['numpy_random'])
        torch.set_rng_state(packet['torch_random'])
        if packet['cuda_random'] is not None:torch.cuda.set_rng_state(packet['cuda_random'])
        restored.update(root=output, started=None, truth=[], frames=[], observation=0,
                        restored_from_step=restored['step'], restored_from_attempt=packet['origin_attempt'],
                        restored_snapshot=name)
        # Controller is deliberately NOT reset/reseeded; its feedback tick,
        # odometry, commands, grips, pending goals, misses and history survive.
        (output/'restore-proof.evaluator-only.json').write_text(json.dumps(dict(
            source=self.source, snapshot=name, origin_attempt=packet['origin_attempt'],
            step=restored['step'], objects_verified=len(current),
            max_position_error=position_error, max_orientation_error=orientation_error,
            max_robot_joint_error=joint_error, complete_controller_restored=True)))
        self.journal(dict(op='restore_complete', name=name, attempt=attempt, step=restored['step']))
        return restored, dict(restored=True, name=name, attempt_id=attempt,
                              simulation_offset_seconds=restored['step']/30,
                              client_state=packet['client_state'],
                              previous_attempt_feedback=closed.get('practice_feedback') if isinstance(closed,dict) else None)
