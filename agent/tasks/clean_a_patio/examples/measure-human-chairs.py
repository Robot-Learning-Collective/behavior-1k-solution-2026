"""Measure public chair-push neighborhoods; no simulator or privileged columns."""
import json
from pathlib import Path
import numpy as np
import pyarrow.parquet as pq

cache = Path.home()/'Downloads/behavior-challenge-2026-samples/clean_a_patio'
selections = [(7217,4612,5359,4789,5299),(7218,4032,4477,4116,4417)]
vec = lambda x: '['+','.join(f'{v:.3f}' for v in x)+']'
md = ['# Human chair-coverage neighborhoods\n\nHF4f50b447. RGB n paired with position groups n−1, velocity/action n−2 per source-reported conversion lag; not simultaneous contact proof. Only public61D state and23D action. EEF is configured link, not calibrated jaw/TCP. Base command scales native fractions by[.75,.75,1]. All aligned raw states/commands retained in local chair-aligned.json; no hidden object state or native score.\n']
for ep,start,end,push_start,push_end in selections:
    tab=pq.read_table(cache/f'episode-{ep}-frames.parquet',columns=['frame_index','observation.state','action'])
    state=np.array(tab['observation.state'].to_pylist()); actions=np.array(tab['action'].to_pylist())
    assert state.shape[1]==61 and actions.shape[1]==23
    assert tab['frame_index'].to_pylist()==list(range(len(state)))
    assert np.isfinite(state).all() and np.isfinite(actions).all()
    rows=[]
    for n in range(start,end,10):
        p,v,a=state[n-1],state[n-2],actions[n-2]
        rows.append({'rgb_frame':n,'position_row':n-1,'velocity_command_row':n-2,
                     'position_state61':p.tolist(),'velocity_state61':v.tolist(),'action23':a.tolist()})
    (cache/f'study-{ep}-chairs'/'chair-aligned.json').write_text(json.dumps(rows,indent=2)+'\n')
    md.append(f'\n## Episode{ep}, frames{start}–{end}; push annotation{push_start}–{push_end}\n')
    for label,lo,hi in [('release/approach',start,push_start),('annotated push',push_start,push_end),('withdraw',push_end,end)]:
        s=state[lo:hi]; a=actions[lo:hi]
        md.append(f'- {label}: {(hi-lo)/30:.3f}s; integrated planar path {np.linalg.norm(s[:,:2],axis=1).sum()/30:.3f}m, signed yaw integral{s[:,2].sum()/30:.3f}rad; EEF excursions L{vec(np.ptp(s[:,17:20],axis=0))}, R{vec(np.ptp(s[:,42:45],axis=0))}; left/right grip commands{np.unique(a[:,14]).tolist()}/{np.unique(a[:,22]).tolist()}.\n')
    md.append('\n|RGB frame|phase|measured BODY velocity|requested BODY velocity|measured torso / commanded torso|L EEF / gap mm|R EEF / gap mm|grip request L,R|\n|---|---|---|---|---|---|---|---|\n')
    for r in rows[::3]:
        n=r['rgb_frame']; p=np.array(r['position_state61']);v=np.array(r['velocity_state61']);a=np.array(r['action23'])
        phase='before push' if n<push_start else ('push' if n<push_end else 'withdraw')
        md.append(f'|{n}|{phase}|{vec(v[:3])}|{vec(a[:3]*[.75,.75,1])}|{vec(p[53:57])} / {vec(a[3:7])}|{vec(p[17:20])} / {1000*p[24:26].sum():.1f}|{vec(p[42:45])} / {1000*p[49:51].sum():.1f}|{a[14]:.0f},{a[22]:.0f}|\n')
out=Path(__file__).with_name('human-chair-measurements.md');out.write_text(''.join(md));print(out)
