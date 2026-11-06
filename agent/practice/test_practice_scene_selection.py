"""CPU regression: use official full template0 + room filter, never partial_rooms."""
import sys
import json
import tempfile
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import patch
import practice_scene


def main():
    task='unloading_the_car';scene='house_double_floor_lower'
    rooms=['garage_0','corridor_0','living_room_0','kitchen_0','garden_0']
    with tempfile.TemporaryDirectory() as tmp:
        base=Path(tmp)/'2026-challenge-task-instances/scenes'/scene/'json';base.mkdir(parents=True)
        prefix=f'{scene}_task_{task}'
        full=base/(prefix+'_0_0_template.json');full.write_text('{}')
        partial=base/(prefix+'_0_0_template-partial_rooms.json');partial.write_text('{"not_official":true}')
        fixture=base/(prefix+'_instances')/(prefix+'_0_10_template-tro_state.json');fixture.parent.mkdir();fixture.write_text('{}')
        task_cfg={'scene_model':scene,'robot_start_position':[0,0,0],'robot_start_orientation':[0,0,0,1]}
        modules={name:ModuleType(name) for name in ['omnigibson.macros','omnigibson.eval','omnigibson.eval.utils.eval_utils','omnigibson.eval.utils.score_utils','gello.utils.og_teleop_utils','gello.utils.og_teleop_cfg']}
        modules['omnigibson.macros'].gm=SimpleNamespace(DATA_PATH=tmp)
        modules['omnigibson.eval'].evaluator=object()
        utils=modules['omnigibson.eval.utils.eval_utils'];utils.TASK_NAMES_TO_ROOMS={task:rooms}
        utils.generate_basic_environment_config=lambda *a:{'scene':{'load_room_types':None},'task':{},'env':{}}
        modules['omnigibson.eval.utils.score_utils'].load_human_stats=lambda task:{'length':100}
        modules['gello.utils.og_teleop_utils'].load_available_tasks=lambda:{task:[task_cfg]}
        rules=[SimpleNamespace(ENABLED=True) for _ in range(3)]
        modules['gello.utils.og_teleop_cfg'].DISABLED_TRANSITION_RULES=rules
        with patch.dict(sys.modules,modules):
            cfg,proof=practice_scene.config_for(task,scene,10,{'type':'R1Pro'})
            assert all(not rule.ENABLED for rule in rules)
            assert cfg['scene']['scene_file']==str(full)
            assert cfg['scene']['load_room_instances']==rooms==proof['load_room_instances']
            assert proof['structural_template']==str(full) and proof['native_instance_id']==10
            assert cfg['task']['activity_instance_id']==10
            constants=ModuleType('omnigibson.utils.constants');constants.GROUND_CATEGORIES={'floors','ground'}
            ground={'args':{'name':'hall_floor','category':'floors','in_rooms':['corridor_0']}}
            full.write_text(json.dumps({'objects_info':{'init_info':{'hall_floor':ground}}}))
            with patch.dict(sys.modules,{'omnigibson.utils.constants':constants}):
                check=practice_scene.verify_loaded_ground(SimpleNamespace(objects=[SimpleNamespace(name='hall_floor')]),proof)
                assert check['expected_count']==1 and check['ground_by_room']['corridor_0']==1
                try:practice_scene.verify_loaded_ground(SimpleNamespace(objects=[]),proof)
                except AssertionError:pass
                else:raise AssertionError('Missing native hallway floor must fail readiness')
            full.unlink()
            try:practice_scene.config_for(task,scene,10,{'type':'R1Pro'})
            except AssertionError:pass
            else:raise AssertionError('Must fail closed, not silently use partial_rooms')
    print('official full-template + room-filter selection PASS')

if __name__=='__main__':main()
