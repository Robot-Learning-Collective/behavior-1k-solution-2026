"""Render original aligned human camera samples with measured/requested labels."""
import argparse,json,subprocess,io,sys
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'client_helpers'))
from robot_kinematics import RobotModel
ROOT=Path('<demo-samples>/cook_brussels_sprouts/three-episode-study')
FRAMES={19000:{'cut':[10260,10320,10440,10500,10545],'transfer':[10680,10710,10905,10950]},19001:{'cut':[8790,8835,8910,8970,9015],'transfer':[9150,9180,9330,9360]},19002:{'cut':[5820,5850,6000,6180,6240],'transfer':[6270,6315,6480,6525]}}
starts={19000:10020,19001:8610,19002:5580}
parser=argparse.ArgumentParser();parser.add_argument('--study',choices=['cut','tray','half'],default='cut');args=parser.parse_args()
if args.study=='tray':
 ROOT=ROOT.parent/'three-episode-tray-study'
 starts={19000:7650,19001:7050,19002:4200}
 FRAMES={19000:{'pickup':[7695,7800,7965,8040],'placement':[8250,8700,8835]},19001:{'pickup':[7080,7185,7290,7380],'placement':[7650,7785,7845]},19002:{'pickup':[4215,4320,4470,4545],'placement':[4680,4845,4905]}}
if args.study=='half':
 FRAMES={19000:{'half-pickup':[10770,10815,10845]},19001:{'half-pickup':[9225,9255,9285]},19002:{'half-pickup':[6375,6420,6450]}}
m=RobotModel();summary={}
for ep,groups in FRAMES.items():
 rows={r['rgb_frame']:r for r in json.loads((ROOT/f'{ep}-aligned.json').read_text())};summary[ep]=[]
 for group,ns in groups.items():
  sheet=Image.new('RGB',(720,290*len(ns)),(245,245,245));draw=ImageDraw.Draw(sheet)
  for i,n in enumerate(ns):
   r=rows[n];p=r['measured'];a=r['action'];L,_,_=m.arm('left',p['torso_q'],p['left_q']);R,rot,_=m.arm('right',p['torso_q'],p['right_q'])
   r.update({'tcp_left_model':L.tolist(),'tcp_right_model':R.tolist(),'right_finger_direction':rot[:,2].tolist(),'right_closing_direction':rot[:,1].tolist()});summary[ep].append(r)
   label=f'{ep} RGB frame {n} ({n/30:.2f}s); source positions {n-1}, action {n-2}\nMeasured TCP L {np.round(L,3)} R {np.round(R,3)} | finger sum L/R {sum(p["left_grip"]):.3f}/{sum(p["right_grip"]):.3f}m\nRequested grip L/R {a["left_grip_native"]:+.0f}/{a["right_grip_native"]:+.0f} (-1closed,+1open); columns HEAD / LEFT / RIGHT'
   draw.text((5,i*290+2),label,fill='black')
   for j,cam in enumerate(['head','left','right']):
    data=subprocess.check_output(['ffmpeg','-v','error','-ss',str((n-starts[ep])/30),'-i',str(ROOT/f'{ep}-{cam}.mp4'),'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
    im=Image.open(io.BytesIO(data)).resize((240,240));sheet.paste(im,(240*j,i*290+50))
  sheet.save(ROOT/f'{ep}-{group}.jpg',quality=92)
(ROOT/('half-pickup-aligned-records.json' if args.study=='half' else 'selected-aligned-records.json')).write_text(json.dumps(summary,indent=2))
print('SHEETS_READY')
