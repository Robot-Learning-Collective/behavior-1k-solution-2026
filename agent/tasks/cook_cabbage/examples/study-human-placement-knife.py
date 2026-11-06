"""Offline public-demo study only; no simulator calls. RGB n, q n-1, actions n-2."""
from pathlib import Path
import io, json, subprocess, sys
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'client_helpers'))
from robot_kinematics import RobotModel

root = Path('<demo-samples>/cook_cabbage')
model = RobotModel()
samples = {
    8207: {'placement': [3903, 4020, 4073, 4085, 4110, 4165],
           'knife-a': [5464, 5630, 5647, 5680, 5730],
           'knife-b': [5780, 5820, 6220, 6443, 6470]},
    8214: {'placement': [5227, 5650, 5785, 5815, 5880, 5940],
           'knife-a': [7633, 7850, 7895, 7970, 8142],
           'knife-b': [8300, 8440, 8580, 8756, 8800]},
}
output_name = 'study-aligned-state-actions.json'
if len(sys.argv) > 1:
    sample_file = Path(sys.argv[1])
    samples = {int(k): v for k, v in json.loads(sample_file.read_text()).items()}
    output_name = sample_file.stem + '-aligned-state-actions.json'
records = []
for ep, groups in samples.items():
    df = pd.read_parquet(root / ('frames.parquet' if ep == 8207 else f'frames-{ep}.parquet')).set_index('frame_index')
    for group, frames in groups.items():
        sheet = Image.new('RGB', (960, 344 * len(frames)), 'white')
        draw = ImageDraw.Draw(sheet)
        for i, n in enumerate(frames):
            p = np.asarray(df.loc[n-1, 'observation.state'])
            a = np.asarray(df.loc[n-2, 'action'])
            assert p.shape == (61,) and a.shape == (23,)
            rec = {'episode': ep, 'group': group, 'rgb_frame': n, 'position_row': n-1,
                   'action_row': n-2, 'torso_q': p[53:57].tolist(), 'torso_target': a[3:7].tolist(),
                   'base_command': a[:3].tolist(), 'base_measured': np.asarray(df.loc[n-2, 'observation.state'])[:3].tolist()}
            for side, j, k, g, h in [('left', 3, 7, 24, 14), ('right', 28, 15, 49, 22)]:
                q, target = p[j:j+7], a[k:k+7]
                tcp, R, _ = model.arm(side, p[53:57], q)
                rec[side] = {'q': q.tolist(), 'target': target.tolist(), 'lag': (target-q).tolist(),
                             'fingers_m': p[g:g+2].tolist(), 'native_grip': float(a[h]),
                             'tcp_fk': tcp.tolist(), 'finger_dir_fk': R[:,2].tolist(), 'close_dir_fk': R[:,1].tolist()}
            records.append(rec)
            draw.text((4, i*344+4), f'{ep} {group} RGB {n} / {n/30:.3f}s; q row {n-1}; action row {n-2}; LEFT / HEAD / RIGHT', fill='black')
            for col, cam in enumerate(['left_realsense', 'zed', 'right_realsense']):
                raw = subprocess.check_output(['ffmpeg', '-loglevel', 'error', '-ss', str(n/30), '-i', str(root/f'{cam}-{ep}.mp4'), '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'])
                image = Image.open(io.BytesIO(raw)).convert('RGB').resize((320,320))
                sheet.paste(image, (col*320,i*344+24))
        sheet.save(root/f'study-{ep}-{group}.jpg', quality=90)
        print('SHEET', ep, group, flush=True)
(root/output_name).write_text(json.dumps(records, indent=2))
print('DONE', len(records), 'aligned samples')
