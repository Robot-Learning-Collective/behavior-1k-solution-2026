"""Training-instance bootstrap using installed official evaluator loaders; no policy truth output."""
import copy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace


def config_for(task, scene, instance, robot_config):
    if not 10 <= instance <= 300:
        raise ValueError('Practice slots accept TRAIN native instance IDs10..300 only; never0..9 or test splits')
    from omnigibson.macros import gm
    # Evaluator initializes macros at import; do this BEFORE Environment locks them.
    from omnigibson.eval import evaluator
    from omnigibson.eval.utils.eval_utils import generate_basic_environment_config, TASK_NAMES_TO_ROOMS
    from omnigibson.eval.utils.score_utils import load_human_stats
    from gello.utils.og_teleop_utils import load_available_tasks
    from gello.utils.og_teleop_cfg import DISABLED_TRANSITION_RULES
    # Same setup as BatchedEvaluator.load_env: these require disabled GPU dynamics.
    for rule in DISABLED_TRANSITION_RULES:
        rule.ENABLED = False
    task_cfg=load_available_tasks()[task][0]
    assert task_cfg['scene_model']==scene, 'Requested task/scene mismatch'
    cfg=generate_basic_environment_config(task,task_cfg)
    base=Path(gm.DATA_PATH)/'2026-challenge-task-instances/scenes'/scene/'json'
    prefix=f'{scene}_task_{task}'
    # Official v3.9.3-post1/post2 resolves template0, then filters rooms at load.
    # The separately pre-pruned partial_rooms file is NOT that evaluator scene.
    template=base/f'{prefix}_0_0_template.json'
    fixture=base/f'{prefix}_instances'/f'{prefix}_0_{instance}_template-tro_state.json'
    assert template.is_file() and fixture.is_file()
    # Template0 is the shared structural scene, NOT a0..9 task-instance TRO/start.
    cfg['scene'].update(scene_file=str(template),load_room_instances=TASK_NAMES_TO_ROOMS[task])
    cfg['task'].update(activity_instance_id=instance,use_presampled_robot_pose=False,include_obs=False)
    cfg['env']['automatic_reset']=False
    robot=copy.deepcopy(robot_config)
    robot['position']=task_cfg['robot_start_position'];robot['orientation']=task_cfg['robot_start_orientation']
    cfg['robots']=[robot]
    stats=load_human_stats(task)
    proof={'task':task,'scene':scene,'mode':'train','native_instance_id':instance,
        'fixture':str(fixture),'fixture_sha256':hashlib.sha256(fixture.read_bytes()).hexdigest(),
        'structural_template':str(template),'template_sha256':hashlib.sha256(template.read_bytes()).hexdigest(),
        'load_room_instances':list(cfg['scene']['load_room_instances']),
        'scene_selection':'official full template0 plus evaluator partial_scene_load room filter',
        'task_mean_human_steps':stats['length'],'official_nominal_step_budget':int(1.5*stats['length'])}
    return cfg,proof


def verify_loaded_ground(scene, proof):
    """Private bootstrap proof: every official-filtered ground object actually loaded."""
    from omnigibson.utils.constants import GROUND_CATEGORIES
    data=json.loads(Path(proof['structural_template']).read_text())
    rooms=set(proof['load_room_instances']);expected={}
    for info in data['objects_info']['init_info'].values():
        args=info['args'];in_rooms=args.get('in_rooms',[])
        if isinstance(in_rooms,str):in_rooms=[in_rooms]
        if args.get('category') in GROUND_CATEGORIES and rooms.intersection(in_rooms):
            expected[args['name']]=in_rooms
    loaded={obj.name for obj in scene.objects}
    missing=sorted(set(expected)-loaded)
    assert not missing, f'Official ground objects missing from native scene: {missing}'
    return {'expected_count':len(expected),'loaded_count':len(expected),
        'missing':missing,'ground_by_room':{room:sum(room in rr for rr in expected.values()) for room in sorted(rooms)},
        'limit':'Native object presence, not a traversability or task-success test'}


def load_training_instance(env, instance):
    from omnigibson.eval.evaluator import BatchedEvaluator, InstanceEnvAccessor
    accessor=InstanceEnvAccessor(shared_env=env,env_idx=0)
    state=SimpleNamespace(env_accessor=accessor)
    context=SimpleNamespace(env=env,cfg={'mode':'train'},should_sync_lights=False,instance_eval_states=[state])
    BatchedEvaluator._load_instance_state(context,instance,state)
    BatchedEvaluator._settle_and_finalize(context,[0])
    env.reset()


def predicate(env):
    # Same native compiled goal as PredicateGoal; keep all output evaluator-only.
    done,_=env.task.compiled_task.check_goal(lambda name,*entities:env.task._evaluate_predicate(0,name,*entities))
    return bool(done)
