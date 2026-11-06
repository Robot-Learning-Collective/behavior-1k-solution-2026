"""Extract eight recorded RGB contact sheets; no simulator calls."""
import json,pathlib,subprocess
from PIL import Image,ImageDraw
P=pathlib.Path.home()/'Downloads/behavior-challenge-2026-samples/hanging_pictures'
for r in json.loads((P/'hang-study-measurements.json').read_text()):
 release=r['release_commands'][-1];frames=[r['hang'][0],release-120,release-30,release+2,release+17,min(release+47,r['hang'][1])]
 sheet=Image.new('RGB',(1080,720));draw=ImageDraw.Draw(sheet)
 for j,f in enumerate(frames):
  image=P/f'study-{r["episode"]}-{f}.jpg'
  subprocess.run(['ffmpeg','-v','error','-ss',str(r['video_start']+f/30),'-i',str(P/f'study-head-{r["video_shard"]}.mp4'),'-frames:v','1','-y',str(image)],check=True)
  sheet.paste(Image.open(image).resize((360,360)),((j%3)*360,(j//3)*360));draw.text(((j%3)*360+6,(j//3)*360+6),f'{r["episode"]} f{f} delta{(f-release)/30:+.2f}s',fill='red',stroke_width=1,stroke_fill='white')
 sheet.save(P/f'hang-{r["episode"]}.jpg')
 print('DONE',r['episode'],flush=True)
