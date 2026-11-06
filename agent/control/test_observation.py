"""CPU-only native RGBD persistence, RGB-only delivery, warning and fresh-process checks."""
import base64
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from unittest.mock import patch
import numpy as np
from PIL import Image


def main(fixture_dir=None):
    here=Path(__file__).resolve().parent
    sys.path.insert(0,str(here));sys.path.insert(0,str(here.parent/"practice"))
    from depth_image import compose_rgbd
    from rgbd_geometry import project_body
    scope=contextlib.nullcontext(str(fixture_dir)) if fixture_dir else tempfile.TemporaryDirectory(prefix='rgbd-cpu-')
    with scope as directory:
        run=Path(directory)
        (run/'SETUP.json').write_text(json.dumps({'queue':'CPU_ONLY'}))
        env={**os.environ,'BEHAVIOR_SIM_RUN_DIR':str(run),
             'BEHAVIOR_SIM_DELIVERY_DIR':str(run/'delivery'),'BEHAVIOR_SIM_DELIVERY_ACTIVE':'0'}
        with patch.dict(os.environ,env):
            spec=importlib.util.spec_from_file_location('candidate',here/'sim_client.py')
            s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
            try:
                robot={'torso_joints':[0.]*4,'torso_q_tracking_error_rad':[0.]*4,'simulator_base_odom':{}}
                cameras={}
                for arm,y in [('left',.2),('right',-.2)]:
                    robot[arm]={'eef_position':[.4,y,.5],'eef_quaternion':[0,0,0,1],
                        'own_links_body':{'ag_start_point_body':[.4,y+.02,.5],'ag_end_point_body':[.4,y-.02,.5],
                                          'ag_ray_midpoint_body':[.4,y,.5]},
                        'joints':[0.]*7,'finger_positions':[.02,.02],'q_tracking_error_rad':[0.]*7,
                        'joint_limit_margins_rad':{'min_margin_rad':1.,'to_lower':[1.]*7,'to_upper':[2.]*7}}
                rgbs=[];depths=[]
                for name,size,y in [('left',480,.2),('head',720,0.),('right',480,-.2)]:
                    T=np.eye(4);T[:3,3]=[.4,y,0.]
                    cameras[name]={'intrinsics':[[400.,0.,size/2],[0.,400.,size/2],[0.,0.,1.]],
                        'camera_to_body':T.tolist(),'image_size_hw':[size,size],'pixel_center_offset':0.}
                    rgbs.append(np.full((size,size,3),50,dtype=np.uint8))
                    d=np.full((size,size),.5,dtype=np.float32);d[3,4]=np.nan;d[5,6]=3.75;depths.append(d)
                source=run/'observation_000001.jpg';Image.new('RGB',(1440,480)).save(source)
                endpoint=compose_rgbd({'image':str(source)},depths,rgbs)
                blob=Path(endpoint['depth_file']).read_bytes()
                def packet(attempt):
                    return {'image_base64':base64.b64encode(Path(endpoint['image']).read_bytes()).decode(),
                        'depth_npz_base64':base64.b64encode(blob).decode(),'depth_sha256':hashlib.sha256(blob).hexdigest(),
                        'controller_protocol':3,'attempt_id':attempt,'observation_id':1,'action_id':None,
                        'simulated_seconds':0.,'wall_seconds':0.,'robot':copy.deepcopy(robot),'cameras':copy.deepcopy(cameras),
                        'image_layout':endpoint['image_layout']}
                first=s._save_and_summarize(packet('cpu_A'));old_image=Path(first['local_image_path']).read_bytes()
                second=s._save_and_summarize(packet('cpu_B'))
                assert first['local_image_path']!=second['local_image_path']
                assert Path(first['local_image_path']).read_bytes()==old_image
                for name,size in [('left',480),('head',720),('right',480)]:
                    points=s.xyz(name)
                    assert points.shape==(size,size,3) and np.isnan(points[3,4]).all()
                    assert points[5,6,2]==3.75
                    np.testing.assert_array_equal(s.pixel_to_body(name,6,5),points[5,6])
                    assert second['robot'][name if name!='head' else 'left']['pad_pixels'][name]['in_view']==[True,True]
                with Image.open(second['local_image_path']) as image:
                    pixels=np.asarray(image)
                    for arm in ('left','right'):
                        for camera in (arm,'head'):
                            u,v=project_body(robot[arm]['own_links_body']['ag_start_point_body'],cameras[camera])
                            x0=endpoint['image_layout']['camera_panels'][camera]['rgb_xywh'][0]
                            color=pixels[round(v),x0+round(u)]
                            assert int(color.max())-int(color.min())<6,(arm,camera,color)  # No colored pad dot.
                # A new interpreter needs no retained NumPy state or simulator request.
                code=f"import sys;sys.path.insert(0,{str(here)!r});import sim_client as s;print(s.xyz('head').shape,s.pixel_to_body('right',6,5).tolist())"
                fresh=subprocess.check_output([sys.executable,'-c',code],env=env,text=True)
                assert '(720, 720, 3)' in fresh and '3.75' in fresh
                # sys.__stdout__ warning escapes an ordinary redirect_stdout wrapper.
                code=f"import sys,contextlib,io;sys.path.insert(0,{str(here)!r});import sim_client as s\nwith contextlib.redirect_stdout(io.StringIO()):s._publish_observation(s.last_obs(),'CPU publication test')"
                output=subprocess.check_output([sys.executable,'-c',code],env=env,text=True)
                assert 'WARNING: image not attached — read '+second['local_image_path'] in output
                assert 'depth saved:' in output and 'pad_start=' in output and 'limit_margins=' in output
                files=list((run/'delivery').glob('*.json'));assert len(files)==1
                manifest=json.loads(files[0].read_text())
                assert 'diagnosis=' in manifest['state_text'] and 'fault=' in manifest['state_text']
                assert len(manifest['state_text'])<4000
                assert 'depth_npz_base64' not in s.STATE_CACHE.read_text()
                assert Image.open(second['local_image_path']).size==(1680,720)
                print('PASS native float persistence, RGB-only delivery with pad state retained, attempt history, fresh-process xyz, redirected-output warning')
            finally:
                if fixture_dir:
                    (run/'fixture-cache-path.txt').write_text(str(s.LOCAL_OBS_DIR))
                else:shutil.rmtree(s.LOCAL_OBS_DIR)


if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else None)
