"""Extract exact RGB PTS and lag-aligned public proprio; no simulator RPC."""
from pathlib import Path
import json, sys
import av
import numpy as np
import pyarrow.parquet as pq
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'client_helpers'))
from robot_kinematics import RobotModel

ROOT = Path.home() / 'Downloads/behavior-challenge-2026-samples/clean_a_trumpet/human-study-r2'
MODEL = RobotModel()
CAMERAS = ['left_realsense_link_camera_0', 'zed_link_camera_0', 'right_realsense_link_camera_0']
WINDOWS = {7409: (3500, 3620), 7419: (3220, 3340), 7420: (4180, 4300)}
for ep, (first, last) in WINDOWS.items():
    out = ROOT / str(ep)
    meta = json.loads((out/'metadata.json').read_text())
    frames = list(range(first, last+1, 10))
    rgb = {}
    pts = {}
    for camera in CAMERAS:
        offset = meta[f'videos/observation.rgb.{camera}/from_timestamp']
        with av.open(str(ROOT/'raw'/f'{camera}.mp4')) as video:
            stream = video.streams.video[0]
            video.seek(int((offset+first/30)/stream.time_base), stream=stream, backward=True)
            for frame in video.decode(stream):
                time = float(frame.pts*stream.time_base)
                index = round((time-offset)*30)
                if index > last: break
                if index in frames:
                    assert abs((time-offset)*30-index) < .01
                    rgb[camera, index] = frame.to_image().resize((320,320))
                    pts[camera, index] = time
        assert all((camera, n) in rgb for n in frames)
    table = pq.read_table(out/'frames.parquet', columns=['observation.state','action'])
    state = np.array(table['observation.state'].to_pylist())
    action = np.array(table['action'].to_pylist())
    samples = []
    for n in frames:
        q, velocity, command = state[n-1], state[n-2], action[n-2]
        sample = {'rgb_frame':n, 'seconds':n/30, 'position_row':n-1,
                  'velocity_command_row':n-2, 'torso':q[53:57].tolist(),
                  'base_BODY_velocity':velocity[:3].tolist(),
                  'rgb_original_pts':{c:pts[c,n] for c in CAMERAS}}
        for arm, qs, gs, ac, grip in [('left',slice(3,10),slice(24,26),slice(7,14),14),
                                      ('right',slice(28,35),slice(49,51),slice(15,22),22)]:
            p,R,_ = MODEL.arm(arm,q[53:57],q[qs])
            sample[arm] = {'joints':q[qs].tolist(),'fingers':q[gs].tolist(),
                          'model_TCP':p.tolist(),'model_axis0':R[:,0].tolist(),
                          'model_close':R[:,1].tolist(),'model_finger':R[:,2].tolist(),
                          'command_q':command[ac].tolist(),'native_grip_command':float(command[grip])}
        samples.append(sample)
    (out/'fine-samples.json').write_text(json.dumps(samples,indent=2))
    for page in range((len(frames)+4)//5):
        subset = frames[page*5:page*5+5]
        image = Image.new('RGB',(960,344*len(subset)), 'black')
        draw = ImageDraw.Draw(image)
        for row,n in enumerate(subset):
            y=344*row
            draw.text((5,y+4),f'ep{ep} RGB frame{n} t={n/30:.3f}s | LEFT / HEAD / RIGHT | position row {n-1}',fill='white')
            for column,c in enumerate(CAMERAS): image.paste(rgb[c,n],(320*column,y+24))
        image.save(out/f'fine-{page+1}.jpg',quality=92)
    print('FINE_READY',ep,frames[0],frames[-1],len(frames),flush=True)
