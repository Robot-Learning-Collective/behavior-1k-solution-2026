"""Public 61D state analysis; no rewards, objects, scorer or simulator reads."""
import json
import sys
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq

CACHE=Path.home()/'Downloads/behavior-challenge-2026-samples/clean_a_patio'
META=Path.home()/'Downloads/behavior-challenge-2026-metadata-4f50b447'
PATH='--path' in sys.argv
PATH_END='--path-end' in sys.argv
OUT=Path(__file__).with_name('human-path-end-measurements.md' if PATH_END else 'human-path-measurements.md' if PATH else 'human-sweep-measurements.md')

def rotation(q):
    x,y,z,w=np.asarray(q)/np.linalg.norm(q)
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
                     [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
                     [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])

def vec(a): return '['+','.join(f'{x:.3f}' for x in a)+']'

md=['# Public human sweep measurements\n',
    'HF revision4f50b44796641a4d526a19d9aeadc8aa51e2f2c2. RGB selected every10frames; visual review is recorded separately in NOTES, not established by these numeric measurements. For RGB n, position/quaternion/joint groups use n−1; velocities/actions n−2, following source-reported conversion lag in human_proprio.py. Not simultaneous shutter/contact proof. BODY axes forward,left,up; metres/radians. Recorded configured EEF is not a calibrated pad/contact point. Finger gaps below are measured joint sums, not grasp sensors. EEF+Z/+Y axes are model axes, not direct measured bristle orientation. No measured absolute base/target pose or force exists. Integrated base path is an uncalibrated planar estimate.\n']
segments = ([(7217,11040,11250,11103,11190),(7218,10230,10450,10289,10390)] if PATH_END else
            [(7217,10620,10920,10710,10763),(7218,9700,9940,9787,9870)] if PATH else
            [(7217,2193,2340,2223,2310),(7218,3657,3861,3687,3831)])
for ep,start,end,a,b in segments:
    meta=json.loads((CACHE/f'episode-{ep}-metadata.json').read_text())
    tab=pq.read_table(CACHE/f'episode-{ep}-frames.parquet')
    assert tab['frame_index'].to_pylist()==list(range(meta['length']))
    s=np.array(tab['observation.state'].to_pylist()); acts=np.array(tab['action'].to_pylist())
    assert s.shape==(meta['length'],61) and acts.shape==(meta['length'],23) and np.isfinite(s).all()
    odom=np.zeros((len(s),3))
    for j in range(1,len(s)):
        v=(s[j-1,:3]+s[j,:3])/2; th=odom[j-1,2]+v[2]/60
        odom[j,:2]=odom[j-1,:2]+np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])@v[:2]/30
        odom[j,2]=odom[j-1,2]+v[2]/30
    ann=json.loads((META/meta['annotation_path']).read_text())
    durations={};counts={}
    for seg in ann['skill_annotation']:
        label=', '.join(seg['skill_description']); f=seg['frame_duration']
        spans=[f] if isinstance(f[0],(int,float)) else f
        durations[label]=durations.get(label,0)+sum(max(0,min(hi,len(s))-max(lo,0))/30 for lo,hi in spans)
        counts[label]=counts.get(label,0)+1
    md += [f'\n## Episode{ep} / TRAIN{meta["task_instance_id"]}\n',
           f'Length{len(s)/30:.3f}s. Annotation durations (may overlap): `{json.dumps(durations,sort_keys=True)}`. Counts `{json.dumps(counts,sort_keys=True)}`.\n']
    for label,lo,hi in [('approach',start,a),('annotated sweep/contact candidate',a,b),('neighboring after segment (may include another sweep)',b,end)]:
        ss=s[lo:hi]; ds=odom[hi-1]-odom[lo]
        md.append(f'- {label} frames{lo}–{hi}: {(hi-lo)/30:.3f}s, integrated deltaXYyaw{vec(ds)}, planar path{np.linalg.norm(ss[:,:2],axis=1).sum()/30:.3f}m, max base speed{np.linalg.norm(ss[:,:2],axis=1).max():.3f}m/s; L EEF excursion{vec(np.ptp(ss[:,17:20],axis=0))}, R{vec(np.ptp(ss[:,42:45],axis=0))}.\n')
    md.append('\n|RGBframe / phase|Base XYyaw estimate|BODY vx,vy,wz|Torso q|L EEF position / +Z / +Y / gap mm|R EEF position / +Z / +Y / gap mm|Native grip L,R; recorded base normalized; recorded torso q|\n|---|---|---|---|---|---|---|\n')
    for n in range(start,end,10):
        p=s[n-1];v=s[n-2];act=acts[n-2]
        left=rotation(p[20:24]);right=rotation(p[45:49])
        phase='approach' if n<a else ('sweep' if n<b else 'withdraw')
        md.append(f'|{n} {phase}|{vec(odom[n-2])}|{vec(v[:3])}|{vec(p[53:57])}|{vec(p[17:20])} / {vec(left[:,2])} / {vec(left[:,1])} / {p[24:26].sum()*1000:.1f}|{vec(p[42:45])} / {vec(right[:,2])} / {vec(right[:,1])} / {p[49:51].sum()*1000:.1f}|{act[14]:.0f},{act[22]:.0f}; base{vec(act[:3])}; torso{vec(act[3:7])}|\n')
OUT.write_text(''.join(md))
print(OUT)
