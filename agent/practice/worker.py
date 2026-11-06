"""The practice simulator: one persistent BEHAVIOR world that executes the agent's observe/act jobs.

    python agent/practice/worker.py --task clean_a_trumpet --scene <scene> --instance 20 --artifacts <dir>

It loads a TRAIN instance with the official evaluator's robot config, eval physics (base mass, head
aperture) and full-resolution RGB-D cameras, then polls its job queue (ASTRA_WORK_DIR) for jobs written by
rpc.py (observe/act) and admin.py (reset/finish/snapshot/restore/practice_feedback). Each act is one goal
for the per-tick controller in agent/control, stepped at the native 30 Hz until reached, stalled or capped.
The simulator's scorer and object state stay inside this process; the agent only gets onboard RGB-D and
proprioception, plus per-predicate feedback when it asks for it in practice.

--raw/--full-episode are the earlier research benchmark (start states from a recorded demo); practice
uses --task.
"""
import argparse
import copy
import hashlib
import importlib
import json
import os
import random
from pathlib import Path
import sys
import time
import traceback

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'control'))  # shared controller
import gpu_canary  # noqa: E402  (pins the GPU before Isaac Sim starts)

def write_json(path, value):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, help='Historical HDF5 (pair mode). Task mode uses the evaluator r1pro.yaml instead')
    parser.add_argument('--robot-config', type=Path, help='Robot YAML for task mode (default: the official evaluator r1pro.yaml)')
    parser.add_argument('--artifacts', type=Path, required=True)
    parser.add_argument('--full-episode', action='store_true', help='Separate six-book episode benchmark; leaves historical pair checkpoints untouched')
    parser.add_argument('--task', help='Independent2026 training-task practice slot; raw supplies only the unchanged robot/controller config')
    parser.add_argument('--scene')
    parser.add_argument('--instance', type=int, default=10)
    args = parser.parse_args()
    if not args.task and args.raw is None:
        parser.error('--raw is required outside task mode')
    if args.task and (not args.scene or not 10 <= args.instance <= 300):
        parser.error('Task slots require a scene and TRAIN instance10..300, never0..9/test')
    root = Path(__file__).resolve().parents[2]
    work = Path(os.environ.get('ASTRA_WORK_DIR', str(root / '.runtime/work')))
    work.mkdir(parents=True, exist_ok=True)
    gpu_canary.isolate_gpu()
    import h5py
    import numpy as np
    import torch
    from PIL import Image, ImageDraw
    from scipy.spatial.transform import Rotation
    import omnigibson as og
    from omnigibson.envs.data_wrapper import _add_recorded_non_kin_states_to_scene_file, _align_scene_object_states_with_recorded_schema
    from omnigibson.macros import macros
    from omnigibson.eval.utils.eval_utils import PROPRIOCEPTION_INDICES
    from omnigibson.object_states import Inside
    from robot_kinematics import RobotModel
    command_model = RobotModel()
    from action_validation import InvalidAction
    from depth_image import compose_rgbd
    from portable_control import Controller, PlanarOdometry
    from torso_control import slew_limits as torso_slew_limits, ControllerFault
    from practice_snapshots import save_episode_scene, restore_episode

    gm = og.gm
    gm.RENDER_VIEWER_CAMERA = False
    if args.task and args.raw is None:
        # Same robot/controller config the official evaluator loads (--robot-config r1pro.yaml).
        from omegaconf import OmegaConf
        from omnigibson.eval.evaluator import DEFAULT_ROBOT_CONFIG_PATH
        robot_yaml = OmegaConf.to_container(OmegaConf.load(str(args.robot_config or DEFAULT_ROBOT_CONFIG_PATH)), resolve=True)
        robot_yaml.pop('eval', None); robot_yaml['model'] = robot_yaml['model'].lower()
        config = {'env': {'automatic_reset': False}, 'robots': [robot_yaml]}
    else:
      with h5py.File(args.raw) as raw:
        config = json.loads(raw['data'].attrs['config'])
        assert config['env']['automatic_reset'] is False, 'Preparation requires actual configured no-auto-reset world'
        if not args.task:
            recorded_scene = json.loads(raw['data'].attrs['scene_file'])
            states = raw['data/demo_0/state'][:]
            sizes = raw['data/demo_0/state_size'][:]
            init_metadata = {key:value[:] for key,value in raw['data/demo_0/init_metadata'].items()}
            assert json.loads(raw['data/demo_0'].attrs['transitions']) == {}, 'Unexpected topology transitions'
    if args.task:
        from practice_scene import config_for, load_training_instance, predicate as task_predicate
        config, task_instance = config_for(args.task,args.scene,args.instance,config['robots'][0])
    else:
        # Legacy OG3.7→3.9 field migration; preserve recorded goals and live contacts.
        for state in recorded_scene['state']['registry']['object_registry'].values():
            if 'controllers' in state and 'controller_groups' not in state:
                state['controller_groups'] = state.pop('controllers')
                for controller in state['controller_groups'].values():
                    controller['goal_set'] = controller.pop('goal_is_valid')
                    controller['goals'] = controller.pop('goal')
        config['scene']['scene_file'] = copy.deepcopy(recorded_scene)
        _add_recorded_non_kin_states_to_scene_file(config['scene']['scene_file'], [recorded_scene])
    config['task'].update(online_object_sampling=False, use_presampled_robot_pose=False, include_obs=False)
    config['task']['termination_config']['max_steps'] = 1000000
    config['env'].update(num_envs=1, device='cpu', external_sensors=[])
    for robot_config in config['robots']:
        robot_config['obs_modalities'] = ['rgb','depth_linear','proprio']
        robot_config['proprio_obs'] = list(PROPRIOCEPTION_INDICES['R1Pro'])
        robot_config['sensor_config'] = {'VisionSensor': {'sensor_kwargs': {'image_height':480,'image_width':480}},
            'zed_link:Camera:0': {'sensor_kwargs': {'image_height':720,'image_width':720,'horizontal_aperture':40.}}}
    random.seed(0); np.random.seed(0); torch.manual_seed(0)
    setup_start = time.monotonic()
    env = og.Environment(configs=config)
    scene, robot = env.scenes[0], env.scenes[0].robots[0]
    if args.task:
        # What evaluator._apply_robot_eval_settings applies at eval (heavier base, 40 deg head), before the instance load.
        from omnigibson.eval.evaluator import EVAL_BASE_LINK_MASS, EVAL_HEAD_HORIZONTAL_APERTURE
        og.sim.stop(); robot.base_footprint_link.mass = EVAL_BASE_LINK_MASS; og.sim.play()
        for name, sensor in robot.sensors.items():
            if 'zed_link' in name: sensor.horizontal_aperture = EVAL_HEAD_HORIZONTAL_APERTURE
        og.sim.update_handles()
        load_training_instance(env,args.instance)
    else:
        scene.restore(recorded_scene, update_initial_file=True)
        og.sim.stop()
        for attr, values in init_metadata.items():
            assert len(values) == len(scene.objects)
            for obj, value in zip(scene.objects, values): setattr(obj, attr, value.item() if value.ndim == 0 else torch.as_tensor(value))
        og.sim.play()
        env.reset()
        _align_scene_object_states_with_recorded_schema(scene, recorded_scene)
    with macros.unlocked(): macros.utils.registry_utils.STABILIZE_SKIPPED_OBJECTS = True
    scene.object_registry.set_dump_filter(lambda obj: obj.initialized)
    camera_names = ('left_realsense','zed','right_realsense')
    cameras = [next(s for name,s in robot.sensors.items() if camera in name and 'Camera' in name) for camera in camera_names]
    array = lambda x: x.detach().cpu().numpy() if hasattr(x,'detach') else np.asarray(x)
    # Initialize the native camera-parameter annotators before any policy capture.
    # Their first access renders four times, but does not step physics.
    from camera_bootstrap import read_intrinsics
    camera_intrinsics = read_intrinsics(cameras,array,og.sim)
    lower, upper = array(robot.joint_lower_limits), array(robot.joint_upper_limits)
    torso_idx = array(robot.trunk_control_idx).astype(int)
    torso_bounds = (lower[torso_idx].copy(), upper[torso_idx].copy())
    torso_step_limit = torso_slew_limits(array(robot.max_joint_velocities)[torso_idx])
    args.artifacts.mkdir(parents=True, exist_ok=True)
    cases = [('pair1',4736,10774,['hardback_51','hardback_54']),
             ('pair2',12192,18012,['hardback_52','hardback_55']),
             ('pair3',19290,24788,['hardback_53','hardback_50'])]
    if args.task:
        cases = [('episode',0,int(task_instance['task_mean_human_steps']),[])]
    elif args.full_episode:
        cases = [('episode',0,len(states)-1,[f'hardback_{i}' for i in range(50,56)])]
    snapshots = args.artifacts / ('benchmark-full-episode' if args.full_episode else 'benchmark')
    snapshots.mkdir(exist_ok=True)
    manifest = {'config':config, 'raw_sha256':None if args.task or args.raw is None else hashlib.sha256(args.raw.read_bytes()).hexdigest(),
        'version':og.__version__, 'scene':config['scene']['scene_model'], 'objects':sorted(o.name for o in scene.objects),
        'gpu_uuid':gpu_canary.UUID, 'seed':0, 'cases':[],
        'scope':'full-six-book-episode' if args.full_episode else 'historical-two-book-segments',
        'practice_wall_seconds':1200 if args.full_episode else 600,
        'contact_control':'Live control and contacts; native30Hz action/render,120Hz physics',
        'json_migration':'controller_groups/goals/goal_set field renames only, preserving recorded values',
        'worker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'source_restore':'Sequential recorded STATE rows only; no action-prefix or tail execution'}

    if args.task:
        from practice_scene import verify_loaded_ground
        manifest['official_ground_check'] = verify_loaded_ground(scene, task_instance)
        manifest.update(scope='training-task-practice',task_instance=task_instance,
            source_restore='Official train TRO loader + settle; native topology restore then exact original NPZ state on reset',
            json_migration=None,scorer='Native compiled BDDL goal, private;60tick stability is research-only, not official certification')

    def refresh(capture=False):
        og.sim._sim_context.physics_sim_view.update_articulations_kinematic()
        og.sim.sync_physx_to_fabric()
        og.sim._refresh_state_caches(dt=0.)
        if capture:
            # Kit render() schedules rendering but does not fence annotator readback.
            # After physics-only ticks, explicitly capture a zero-time Replicator
            # frame and wait for its dispatcher, rather than reading the old buffer.
            before=og.sim.current_time
            settings=og.sim._sim_context._settings
            key='/app/player/playSimulations';was_enabled=settings.get(key)
            assert type(was_enabled) is bool
            settings.set_bool(key,False) # Same no-physics guard as SimulationContext.render().
            try:
                # Replicator updates its DispatchSync graph USD attributes. Keep
                # OG's guard enabled and synchronize those render-graph edits.
                with og.sim.editing_usd():
                    importlib.import_module('omni.replicator.core').orchestrator.step(
                        rt_subframes=3,pause_timeline=False,delta_time=0.,wait_for_render=True)
            finally:settings.set_bool(key,was_enabled)
            if abs(og.sim.current_time-before)>1e-9:
                raise RuntimeError('Endpoint capture unexpectedly advanced physics')
        else:
            for _ in range(3): og.sim.render()

    def picture(path, label='', include_depth=False):
        packets = [sensor.get_obs()[0] for sensor in cameras]
        rgb = [array(packet['rgb'])[...,:3] for packet in packets]
        triptych = Image.fromarray(np.concatenate([np.asarray(Image.fromarray(view).resize((480,480))) for view in rgb],axis=1))
        if label: ImageDraw.Draw(triptych).text((10,10),label,fill='white',stroke_width=1,stroke_fill='black')
        triptych.save(path,quality=86)
        return ([array(packet['depth_linear']) for packet in packets],rgb) if include_depth else None

    # Complete modern snapshots are immutable after first construction; don't replay
    # or overwrite them on candidate restarts. Parser alignment is ONLY for raw rows.
    existing_manifest = snapshots/'manifest.json'
    reused = existing_manifest.exists()
    if reused:
        frozen = json.loads(existing_manifest.read_text())
        assert frozen['raw_sha256'] == manifest['raw_sha256']
        assert frozen['objects'] == manifest['objects']
        if args.task:
            assert frozen.get('task_instance') == task_instance
        if args.full_episode and not args.task:
            assert frozen.get('scope') == 'full-six-book-episode'
            assert [(c['id'],c['start'],c['end'],c['targets']) for c in frozen['cases']] == cases
        for case in frozen['cases']:
            assert hashlib.sha256((snapshots/f"{case['id']}.npz").read_bytes()).hexdigest() == case['sha256']
            if args.task:
                assert 'scene_checkpoint' in case, 'Old task snapshot lacks topology; use a fresh worker'
                assert hashlib.sha256((snapshots/f"{case['id']}.scene.json").read_bytes()).hexdigest() == case['scene_checkpoint']['scene_sha256']
        manifest = frozen
        cases = []
    previous = -1
    for case, start, end, targets in cases:
        prefix_start = time.monotonic()
        for frame in ([] if args.task else range(previous+1,start+1)):
            state = torch.from_numpy(states[frame,:int(sizes[frame])].copy())
            decoded, consumed = og.sim.deserialize(state)
            assert consumed == len(state), f'Native schema mismatch frame{frame}: {consumed}/{len(state)}'
            og.sim.load_state(decoded, serialized=False)
        previous = start
        refresh()
        state = array(og.sim.dump_state(serialized=True))
        target = snapshots / f'{case}.npz'
        np.savez_compressed(target,state=state)
        picture(snapshots/f'{case}.jpg',f'NATIVE start frame{start}; setup diagnostic, NOT policy rollout')
        manifest['cases'].append({'id':case,'start':start,'end':end,'teleop_seconds':(end-start)/30,'targets':targets,
            'sha256':hashlib.sha256(target.read_bytes()).hexdigest(), 'state_floats':len(state),
            'proprio':array(robot.get_proprioception()[0]).tolist(),
            'held':{arm:obj.name if obj else None for arm,obj in robot._ag_obj_in_hand.items()},
            'prefix_seconds':time.monotonic()-prefix_start})
        if args.task:
            manifest['cases'][-1]['scene_checkpoint']=save_episode_scene(og,scene,env.task,target)
        print('SNAPSHOT_READY',case,len(state),flush=True)
    # Raw schema filters must not parse a complete modern dump: its newly-added
    # non-kinematic fields would shift following object UUIDs (concrete reset failure).
    for obj in scene.objects:
        obj._recorded_non_kin_state_order = None
        obj._recorded_non_kin_state_names = None
    if not reused:
        manifest['setup_seconds'] = time.monotonic()-setup_start
        write_json(snapshots/'manifest.json',manifest)
    assert gpu_canary.seen == {gpu_canary.UUID}, 'Pinned-GPU allocation not confirmed'
    session = None

    def joint_metadata():
        metadata = {}
        for arm,start in (('left',7),('right',15)):
            idx = array(robot.arm_control_idx[arm]).astype(int)
            action_idx = array(robot.arm_action_idx[arm]).astype(int)
            assert len(idx)==7 and np.array_equal(action_idx,np.arange(start,start+7)), 'Unexpected configured23D arm action mapping'
            names = [robot.dof_names_ordered[i] for i in idx]
            assert names==robot.arm_joint_names[arm], 'Configured arm name/index mismatch'
            lo,hi = array(robot.joint_lower_limits)[idx],array(robot.joint_upper_limits)[idx]
            assert np.isfinite(lo).all() and np.isfinite(hi).all() and np.all(lo+.01<hi-.01)
            metadata[arm]={'joint_names':names,'dof_indices':idx.tolist(),'native_action_indices':action_idx.tolist(),
                'hard_lower_rad':lo.tolist(),'hard_upper_rad':hi.tolist(),'endpoint_lower_rad':(lo+.01).tolist(),'endpoint_upper_rad':(hi-.01).tolist(),
                'units':'Persistent joint POSITION radians; relative Cartesian6 starts at commanded FK; NULL holds previous command; tracking lag is not capped',
                'command_slew_rad_per_30Hz_tick':.025,
                'native_effort_limits_nm':array(robot.max_joint_efforts)[idx].tolist(),'safety_margin_rad':.01}
        return metadata

    def own_arm_links_body(arm, base_p_arr, base_R):
        info = {}
        elbow_keys = [k for k in robot.links if arm in k and ('arm_link4' in k or 'link4' in k)]
        if elbow_keys:
            ep, _ = robot.links[elbow_keys[0]].get_position_orientation()
            info['elbow_link_name'] = elbow_keys[0]
            info['elbow_position_body'] = (base_R.T @ (array(ep) - base_p_arr)).tolist()
        if hasattr(robot, 'finger_links') and arm in robot.finger_links:
            f_pos = {}
            for fl in robot.finger_links[arm]:
                fp, _ = fl.get_position_orientation()
                f_pos[fl.name] = (base_R.T @ (array(fp) - base_p_arr)).tolist()
            info['finger_link_positions_body'] = f_pos
        if hasattr(robot, 'assisted_grasp_start_points') and robot.assisted_grasp_start_points.get(arm) and robot.assisted_grasp_end_points.get(arm):
            def _pts_body(pts):
                out = []
                for pt in pts:
                    lp, lq = robot.links[pt.link_name].get_position_orientation()
                    pw = array(lp) + Rotation.from_quat(array(lq)).as_matrix() @ array(pt.position)
                    out.append(base_R.T @ (pw - base_p_arr))
                return np.mean(np.stack(out), axis=0)
            s_body = _pts_body(robot.assisted_grasp_start_points[arm])
            e_body = _pts_body(robot.assisted_grasp_end_points[arm])
            mid_body = 0.5 * (s_body + e_body)
            info['ag_start_point_body'] = s_body.tolist()
            info['ag_end_point_body'] = e_body.tolist()
            info['ag_ray_midpoint_body'] = mid_body.tolist()
        return info

    def proprio():
        base_p, base_q = robot.base_footprint_link.get_position_orientation()
        base_p_arr = array(base_p)
        base_R = Rotation.from_quat(array(base_q)).as_matrix()
        raw_proprio = array(robot.get_proprioception()[0])
        joints = array(robot.get_joint_positions())
        qvel = array(robot.get_joint_velocities())
        try:
            effort=array(robot.get_joint_efforts())
            if effort.shape != joints.shape or not np.isfinite(effort).all():
                raise ValueError('Malformed joint effort readout')
            effort_status='PhysX measured joint effort; not contact force'
        except Exception as error:
            effort=None;effort_status='unavailable:'+type(error).__name__
        metadata = joint_metadata()
        odometry=session['controller'].odom if session is not None else None
        result = {
            'frame': 'current mobile base; xforward,yleft,zup',
            'quaternion_order': 'xyzw',
            'base_velocity':raw_proprio[:3].tolist(),
            'base_odometry':(odometry or PlanarOdometry(raw_proprio[:3])).state(),
        }
        for arm in ('left','right'):
            p,q = robot.get_eef_pose(arm)
            arm_idx = array(robot.arm_control_idx[arm])
            grip_idx = array(robot.gripper_control_idx[arm])
            q_arm = joints[arm_idx]
            lo_ep = np.asarray(metadata[arm]['endpoint_lower_rad'], dtype=float)
            hi_ep = np.asarray(metadata[arm]['endpoint_upper_rad'], dtype=float)
            last_q_tgt = session['last_arm_q_target'][arm] if (session is not None and 'last_arm_q_target' in session) else q_arm.tolist()
            q_err = (np.asarray(last_q_tgt, dtype=float) - q_arm).tolist()
            to_lo = (q_arm - lo_ep).tolist()
            to_hi = (hi_ep - q_arm).tolist()
            result[arm] = {
                'eef_position': (base_R.T@(array(p)-base_p_arr)).tolist(),
                'eef_quaternion': Rotation.from_matrix(base_R.T@Rotation.from_quat(array(q)).as_matrix()).as_quat().tolist(),
                'own_links_body': own_arm_links_body(arm, base_p_arr, base_R),
                'joints': q_arm.tolist(),
                'joint_velocities': qvel[arm_idx].tolist(),
                'joint_efforts_nm': None if effort is None else effort[arm_idx].tolist(),
                'joint_effort_semantics': effort_status,
                'last_commanded_q_target': last_q_tgt,
                'q_tracking_error_rad': q_err,
                'q_tracking_error_semantics': 'last_commanded_position_target_minus_measured_q_rad_not_measured_torque_or_contact_force',
                'joint_limit_margins_rad': {
                    'min_margin_rad': float(min(np.min(q_arm - lo_ep), np.min(hi_ep - q_arm))),
                    'to_lower': to_lo,
                    'to_upper': to_hi,
                },
                'finger_positions': joints[grip_idx].tolist(),
                'finger_velocities': qvel[grip_idx].tolist(),
                'joint_endpoint_metadata': metadata[arm],
            }
        trunk_idx = array(robot.trunk_control_idx)
        q_trunk = joints[trunk_idx]
        last_trunk_tgt = session['last_torso_q_target'] if (session is not None and 'last_torso_q_target' in session) else q_trunk.tolist()
        result['torso_joints'] = q_trunk.tolist()
        result['torso_velocities'] = qvel[trunk_idx].tolist()
        result['torso_joint_efforts_nm'] = None if effort is None else effort[trunk_idx].tolist()
        result['joint_effort_semantics'] = effort_status
        result['last_torso_q_target'] = last_trunk_tgt
        result['torso_q_tracking_error_rad'] = (np.asarray(last_trunk_tgt, dtype=float) - q_trunk).tolist()
        result['torso_joint_limits_rad'] = {'lower':torso_bounds[0].tolist(), 'upper':torso_bounds[1].tolist()}
        result['torso_slew_rad_per_tick'] = torso_step_limit.tolist()
        goal = np.asarray(session.get('last_torso_q_goal', q_trunk.tolist()) if session else q_trunk, dtype=float)
        result['last_torso_q_goal'] = goal.tolist()
        result['torso_goal_error_rad'] = (goal-q_trunk).tolist()
        result['torso_goal_tolerance_rad'] = 0.02
        result['torso_goal_reached'] = bool(np.max(np.abs(goal-q_trunk)) <= 0.02)
        result['torso_control_mode'] = session.get('last_torso_mode', 'reset') if session else 'reset'
        return result

    def camera_calibration():
        # Public self-relative sensor poses only; never publish world camera/base transforms here.
        bp,bq=robot.base_footprint_link.get_position_orientation()
        bp=array(bp);br=Rotation.from_quat(array(bq)).as_matrix()
        result={}
        for name,sensor,K in zip(('left','head','right'),cameras,camera_intrinsics):
            p,q=sensor.get_position_orientation()
            relative=br.T@Rotation.from_quat(array(q)).as_matrix()
            transform=np.eye(4)
            transform[:3,:3]=relative@np.diag([1.,-1.,-1.]) # USD camera -> optical axes
            transform[:3,3]=br.T@(array(p)-bp)
            result[name]={'intrinsics':K.tolist(),'camera_to_body':transform.tolist(),
                'image_size_hw':[int(sensor.image_height),int(sensor.image_width)],
                'camera_axes':'optical: +X right, +Y down, +Z forward; axial depth metres',
                'pose_source':'onboard camera pose relative to current base footprint',
                'pixel_center_offset':0.5}
        return result

    def observation(action_id=None, include_depth=True):
        if session['started'] is None: session['started'] = time.monotonic()
        session['observation'] += 1
        path = session['root'] / f"observation_{session['observation']:06}.jpg"
        # Fence current RGB/depth annotation output without advancing physics ticks.
        refresh(capture=True)
        wall = time.monotonic()-session['started']
        captured = picture(path,f"SIM {session['step']/30:.3f}s | action {action_id or '-'} | onboard RGB",include_depth=include_depth)
        capture = time.monotonic_ns()
        session['frames'].append({'path':str(path),'wall':wall,'step':session['step'],'action_id':action_id})
        endpoint = {'image':str(path),'observation_id':session['observation'],'action_id':action_id,
            'simulated_seconds':session['step']/30,'wall_seconds':wall,'capture_monotonic_ns':capture,'robot':proprio(),
            'controller_protocol':6, 'attempt_id':session['root'].name}
        if not include_depth:return endpoint
        endpoint['cameras']=camera_calibration()
        return compose_rgbd(endpoint,*captured)

    def truth():
        if args.task:
            return {'inside':{},'held':sorted(obj.name for obj in robot._ag_obj_in_hand.values() if obj is not None),
                    'predicate':task_predicate(env)}
        box = scene.object_registry('name','storage_box_49')
        inside = {name:bool(scene.object_registry('name',name).states[Inside].get_value(box)) for name in ['hardback_50','hardback_51','hardback_52','hardback_53','hardback_54','hardback_55']}
        held = {obj.name for obj in robot._ag_obj_in_hand.values() if obj is not None}
        okay = all(inside[name] and name not in held for name in session['case']['targets']) and all(inside[name] for name in session['preserve'])
        return {'inside':inside,'held':sorted(held),'predicate':okay}

    def finished():
        return session.get('infrastructure_invalid',False) or (session['success'] and not session.get('practice',False)) or (session['started'] is not None and not session.get('unbounded_practice',False) and time.monotonic()-session['started'] >= ((1200 if args.full_episode else 600) if session.get('practice',False) else 4*session['case']['teleop_seconds']))

    def execute(goal, request_id):
        controller=session['controller']
        state=lambda:{'step':session['step'],'robot':proprio()}
        try:
            action,done=controller.step(state(),goal)  # Validate before any motor dispatch.
        except (ValueError,KeyError,TypeError) as error:
            raise InvalidAction(str(error)) from error
        session['last_torso_q_goal']=controller.result['torso_target_rad']
        session['last_torso_mode']='per_tick_absolute4' if goal['torso'] is not None else 'persistent_hold'
        executed=0;first_motor=last_motor=None
        stop_reason=fault=diagnostic_traceback=None
        try:
            while True:
                if (work/f'{request_id}.cancel').exists() or (work/'CANCEL').exists():
                    stop_reason='cancelled';break
                if finished():
                    stop_reason='episode_ended';break
                proposed=action.tolist()
                # Native physics/controller callbacks continue at30Hz/120Hz. No
                # intermediate endpoint captures or camera renders inside this RPC.
                with og.sim.render_on_step(False):
                    env.step(torch.as_tensor(action,dtype=torch.float32).unsqueeze(0))
                last_motor=proposed
                if first_motor is None:first_motor=proposed
                session['last_torso_q_target']=proposed[3:7]
                session['last_arm_q_target']={'left':proposed[7:14],'right':proposed[15:22]}
                session['step']+=1;executed+=1
                score=truth()  # Evaluator-only; NEVER passed to controller.step.
                session['stable']=session['stable']+1 if score['predicate'] else 0
                session['success']=session['stable']>=60
                if session['success']:session['completion_wall']=time.monotonic()-session['started']
                session['truth'].append({'step':session['step'],**score})
                # A terminal action is one zero-base persistent hold tick. Its
                # feedback is included in the endpoint and whole-move diagnosis.
                was_done=done
                action,done=controller.step(state(),goal)
                if was_done:
                    stop_reason=controller.reason;break
        except ControllerFault as error:
            stop_reason,fault='controller_fault',error.as_dict()
        except Exception:
            stop_reason='simulator_error';diagnostic_traceback=traceback.format_exc()
            session['infrastructure_invalid']=True
            fault={'code':'simulator_error','message':'Execution failed; private diagnostic recorded',
                   'recoverable':False,'automatic_retry':False}
        execution={'requested_ticks':None,'timeout_ticks':controller.max_ticks,'executed_ticks':executed,
                   'stop_reason':stop_reason,'fault':fault,'execution_uncertain':stop_reason=='simulator_error'}
        result={**controller.result,'reason':stop_reason,'achieved':stop_reason=='reached',
                'execution':execution,'steps':executed}
        receipt={'kind':'PER_TICK_PERSISTENT_GOAL','action_id':request_id,'requested':goal,
                 'first_native23_motor_action':first_motor,'last_native23_motor_action':last_motor,
                 'max_command_slew_rad':controller.max_command_slew,
                 'max_torso_slew_rad':controller.max_torso_slew,'max_torso_measured_lead_rad':controller.max_torso_lead,
                 'execution':execution,'diagnostic_traceback':diagnostic_traceback}
        with (session['root']/'joint-motor.evaluator-only.jsonl').open('a') as output:output.write(json.dumps(receipt)+'\n')
        return {**observation(request_id),'execution':execution,'act_result':result,
                'last_commanded_grip':{} if execution['execution_uncertain'] else controller.grips}

    from practice_feedback import feedback as practice_goal_feedback
    from omnigibson.metrics.task_metric import compute_q_score

    def close_attempt(reason):
        result = {'success':session['success'],'simulated_seconds':session['step']/30,
            'wall_seconds':session.get('completion_wall',time.monotonic()-session['started']) if session['started'] else 0,
            'wall_seconds_through_finish_admin':time.monotonic()-session['started'] if session['started'] else 0,
            'teleop_seconds':session['case']['teleop_seconds'],'reason':reason,'final':truth(),
            'practice':session['practice'],'restored_from_step':session.get('restored_from_step',0),
            'attempt_executed_ticks':session['step']-session.get('restored_from_step',0),
            'infrastructure_invalid':session.get('infrastructure_invalid',False)}
        if session['practice']:
            result['practice_feedback']=practice_goal_feedback(env.task,session,compute_q_score)
        write_json(session['root']/'verdict.json',result)
        write_json(session['root']/'scoring.json',session['truth'])
        write_json(session['root']/'timeline.json',session['frames'])
        return result

    from practice_snapshots import Snapshots, SnapshotRejected
    snapshot_source = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        Path(__file__).parent.iterdir() if p.suffix in ('.py','.json')}
    snapshot_store = Snapshots(args.artifacts,og,scene,robot,refresh,close_attempt,snapshot_source,task=env.task)
    if os.environ.get('ASTRA_SNAPSHOT_SELF_TEST') == '1':
        # New green worker only, before accepting RPCs; never an existing learner world.
        test_root=args.artifacts/'operator-native-snapshot-validation';test_root.mkdir()
        j0=array(robot.get_joint_positions()).copy()
        session={'case':manifest['cases'][0],'root':test_root,'started':None,'step':0,'stable':0,
            'success':False,'truth':[],'frames':[],'observation':0,'preserve':[],
            'practice':True,'unbounded_practice':True,'controller':Controller(command_model),
            'last_arm_q_target':{a:j0[array(robot.arm_control_idx[a])].tolist() for a in ('left','right')},
            'last_torso_q_target':j0[torso_idx].tolist(),'last_torso_q_goal':j0[torso_idx].tolist(),'last_torso_mode':'test',
            'practice_feedback_initial':env.task.get_goal_option_satisfaction(0)}
        session['controller']._observe({'step':0,'robot':proprio()})
        session['controller'].command_q['left'][0]+=.05
        session['last_arm_q_target']['left']=session['controller'].command_q['left'].tolist()
        session['controller'].grips={'left':.7,'right':.8}
        snapshot_store.save(session,'operator-native-validation',None)
        target=next(o for o in scene.objects if o is not robot and not getattr(o,'fixed_base',True))
        p0,q0=target.get_position_orientation();target.set_position_orientation(p0+torch.tensor([.03,0.,0.]),q0)
        moved=j0.copy();moved[array(robot.arm_control_idx['left']).astype(int)[0]]+=.02
        robot.set_joint_positions(torch.as_tensor(moved,dtype=torch.float32));refresh()
        assert np.max(np.abs(array(target.get_position_orientation()[0])-array(p0)))>.02
        assert np.max(np.abs(array(robot.get_joint_positions())-j0))>.01
        session,validation=snapshot_store.restore(session,'operator-native-validation')
        assert abs(session['controller'].command_q['left'][0]-j0[array(robot.arm_control_idx['left']).astype(int)[0]]-.05)<1e-7
        assert session['controller'].grips=={'left':.7,'right':.8}
        assert session['last_arm_q_target']['left']==session['controller'].command_q['left'].tolist()
        write_json(args.artifacts/'snapshot-validation.evaluator-only.json',{'passed':True,'robot_and_object_perturbed':True,
            'robot_objects_restored':True,'nonmeasured_preload_and_grips_preserved':True,
            'restore_proof':str(session['root']/'restore-proof.evaluator-only.json')})
        snapshot_store.path('operator-native-validation').rename(args.artifacts/'operator-native-snapshot-evidence')
        close_attempt('operator-native-snapshot-validation');session=None
    write_json(work/'ready.json',{'pid':os.getpid(),'pgid':os.getpgid(0),'version':og.__version__,'manifest':str(snapshots/'manifest.json'),'gpu_seen':sorted(gpu_canary.seen),'work_dir':str(work),'executed_worker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'automatic_reset_configured':config['env']['automatic_reset'],'protocol':6,'snapshot_restore':True,'practice_feedback':True})
    print('WORKER_READY',str(work),flush=True)
    while not (work/'QUIT').exists():
        jobs = sorted(work.glob('*.job.json'),key=lambda path:path.stat().st_mtime_ns)
        if not jobs:
            time.sleep(.1)
            continue
        path = jobs[0]
        try:
            job = json.loads(path.read_text())
            op = job['op']
            if op == 'reset':
                assert session is None, 'Finish prior attempt first'
                assert type(job.get('practice',False)) is bool
                if any(c['id'] == job['case'] for c in manifest['cases']):
                    case = next(case for case in manifest['cases'] if case['id'] == job['case'])
                    snapshot = snapshots/f"{case['id']}.npz"
                elif job.get('practice',False) and (args.artifacts/'benchmark/manifest.json').exists():
                    pair_manifest = json.loads((args.artifacts/'benchmark/manifest.json').read_text())
                    case = next(case for case in pair_manifest['cases'] if case['id'] == job['case'])
                    snapshot = args.artifacts/'benchmark'/f"{case['id']}.npz"
                else:
                    case = next(case for case in manifest['cases'] if case['id'] == job['case'])
                    snapshot = snapshots/f"{case['id']}.npz"
                assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == case['sha256']
                restore_episode(og,scene,env.task if args.task else None,snapshot,case.get('scene_checkpoint'))
                refresh()
                output = args.artifacts / job['attempt']
                output.mkdir(exist_ok=False)
                (work/'CANCEL').unlink(missing_ok=True)
                j0 = array(robot.get_joint_positions())
                session = {
                    'case':case,'root':output,'started':None,'step':0,'stable':0,'success':False,'truth':[], 'frames':[],'observation':0,'preserve':[],
                    'practice':job.get('practice',False),
                    'unbounded_practice':bool(job.get('practice',False) and job.get('unbounded_practice',False)),
                    'controller':Controller(command_model),
                    'last_arm_q_target': {a: j0[array(robot.arm_control_idx[a])].tolist() for a in ('left', 'right')},
                    'last_torso_q_target': j0[array(robot.trunk_control_idx)].tolist(),
                    'last_torso_q_goal': j0[torso_idx].tolist(),
                    'last_torso_mode': 'reset',
                    'practice_feedback_initial':env.task.get_goal_option_satisfaction(0) if job.get('practice',False) else None,
                }
                first = truth()
                session['preserve'] = [name for name,value in first['inside'].items() if value]
                assert not first['predicate'], 'Source case already solved'
                assert not first['held'] and all(value is None for value in robot._ag_obj_constraints.values()), 'Frozen reset must not inherit a practice grasp/AG constraint'
                expected_inside = {'episode':set(),'pair1':set(),'pair2':{'hardback_51','hardback_54'},'pair3':{'hardback_51','hardback_52','hardback_54','hardback_55'}}[case['id']]
                assert {name for name,value in first['inside'].items() if value} == expected_inside, 'Frozen inherited book state changed'
                reset_proprio = array(robot.get_proprioception()[0])
                assert np.allclose(reset_proprio,np.asarray(case['proprio']),atol=1e-4,rtol=0), 'Frozen declared robot state changed'
                write_json(output/'reset-proof.evaluator-only.json',{'snapshot_sha256':case['sha256'],'practice':session['practice'],'initial_truth':first,'AG_constraints_absent':True,'expected_inherited_inside':sorted(expected_inside),'proprio_max_abs_delta':float(np.max(np.abs(reset_proprio-np.asarray(case['proprio'])))),'proprio_tolerance':1e-4,'onboard_robot':proprio(),'initial_scene_sha256':case.get('scene_checkpoint',{}).get('scene_sha256'),'source':'Initial native topology/bindings restored before exact frozen NPZ/controllers/AG + refresh; private invariants, not policy input' if args.task else 'Exact original frozen NPZ load_state includes controllers/AG + original refresh; private invariant checks, NOT pose correction/oracle/input. Scorer stays PRIVATE'})
                result = {'reset':True,'setup_seconds':manifest['setup_seconds']}
            elif op == 'observe':
                result = {'observation':observation(),'ended':finished()}
            elif op == 'act':
                result = {'observation':execute(job['action'],job['request_id']),'ended':finished()}
            elif op == 'practice_feedback':
                result = practice_goal_feedback(env.task,session,compute_q_score)
                write_json(session['root']/f'practice-feedback-{time.time_ns()}.json',result)
            elif op == 'snapshot':
                result = snapshot_store.save(session,job.get('name'),job.get('client_state'))
            elif op == 'restore':
                if job.get('practice') is not True:raise SnapshotRejected('Restore requires explicit practice mode')
                session, result = snapshot_store.restore(session,job.get('name'))
                session['practice_feedback_initial']=env.task.get_goal_option_satisfaction(0)
            elif op == 'finish':
                private = close_attempt(job.get('reason'))
                result = {k:private[k] for k in ('simulated_seconds','wall_seconds','wall_seconds_through_finish_admin')}
                if session['practice']:result['practice_feedback']=private['practice_feedback']
                session = None
            else: raise ValueError('Unknown worker operation')
            write_json(path.with_name(path.name.replace('.job.json','.result.json')),{'status':'ok','result':result})
        except SnapshotRejected as error:
            write_json(path.with_name(path.name.replace('.job.json','.result.json')),{'status':'rejected','message':str(error)})
        except InvalidAction as error:
            write_json(path.with_name(path.name.replace('.job.json','.result.json')),{'status':'invalid_action','message':str(error)})
        except Exception:
            print(traceback.format_exc(),flush=True)
            if session is not None: session['infrastructure_invalid'] = True
            if op in ('reset','snapshot','restore'):
                (work/'CANCEL').touch()
                write_json(path.with_name(path.name.replace('.job.json','.result.json')),{'status':'error','message':op.capitalize()+' operation failed; world fenced. Private diagnostic retained; do not continue.'})
            else:
                write_json(path.with_name(path.name.replace('.job.json','.result.json')),{'status':'error','traceback':traceback.format_exc()})
        path.rename(path.with_suffix('.done'))
        print('RPC_DONE',path.name,flush=True)
    gpu_canary.stop.set()
    og.shutdown()


if __name__ == '__main__': main()
