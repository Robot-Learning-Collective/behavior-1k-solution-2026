"""Offline comparison of saved public receipts only; no simulator RPCs."""
import json
import os
import sys
from pathlib import Path
import numpy as np

RUN = Path(__file__).resolve().parents[1]
os.environ['BEHAVIOR_SIM_RUN_DIR'] = str(RUN)
os.environ['BEHAVIOR_SIM_CAMPAIGN_DIR'] = str(RUN.parents[3])
sys.path.insert(0, str(RUN))
import sim_client as s

old = json.loads((RUN / 'examples/hang-v1-a07-retained.json').read_text())
new_dir = Path('/tmp/pictures-run-009-p6-8ecdee/practice-restore-p6-pregrasp-a10-9490ad53074542cd965109e8509ed4d5')
new = {a['observation_id']: a for f in new_dir.glob('receipt*.json') for a in [json.loads(f.read_text())]}
rows = []
for label, oi, ni in [('prehang',383,10), ('approached',443,11), ('last_q',447,12), ('seat',451,13)]:
    op = next(r['receipt'] for r in old['receipts'] if r['observation_id']==oi)
    a, b = json.loads(Path(op).read_text()), new[ni]
    row = {'stage':label,'p4_observation':oi,'p6_observation':ni,'p4_receipt':op}
    for name, obs in [('p4',a),('p6',b)]:
        arm = obs['robot']['right']
        xyz = s.xyz('head', obs=obs)
        pts = xyz[160:250,330:390].reshape(-1,3)
        pts = pts[np.isfinite(pts).all(1)]
        _, sv, vt = np.linalg.svd(pts-pts.mean(0), full_matrices=False)
        normal = vt[-1] * np.sign(vt[-1,0])
        normal_tcp = s._quat_to_mat(arm['eef_quaternion']).T @ normal
        trace = obs.get('act_result',{}).get('trace',[])
        row[name] = {'simulated_seconds':obs['simulated_seconds'], 'joints':arm['joints'],
            'tcp':arm['eef_position'], 'fingers':arm['finger_positions'],
            'pad_start':arm['own_links_body']['ag_start_point_body'],
            'pad_end':arm['own_links_body']['ag_end_point_body'],
            'poster_normal_body':normal.tolist(),'poster_normal_tcp':normal_tcp.tolist(),
            'plane_rms_m':float(sv[-1]/np.sqrt(len(pts))),
            'command':arm['last_commanded_q_target'], 'trace_samples':len(trace),
            'execution':obs.get('execution'),
            'base':obs['robot'].get('base_odometry',obs['robot'].get('simulator_base_odom'))}
    row['delta_q_rad'] = (np.array(row['p6']['joints'])-row['p4']['joints']).tolist()
    row['delta_tcp_m'] = (np.array(row['p6']['tcp'])-row['p4']['tcp']).tolist()
    row['poster_normal_tcp_difference_deg'] = float(np.degrees(np.arccos(np.clip(np.dot(row['p4']['poster_normal_tcp'],row['p6']['poster_normal_tcp']),-1,1))))
    rows.append(row)
result = {'qualification':'Saved first protocol6 drill versus historical a07; not newly dispatched controlled replay. Restore for requested replay was blocked by evicted pod before any execution. Different grasp/nav histories confound controller-only attribution. p4 traces are chunk endpoints; p6 traces expose per-tick errors, not full proprio/pads. No fabricated tickwise joint trajectory.', 'stages':rows}
(RUN / 'examples/p4-p6-saved-comparison.json').write_text(json.dumps(result,indent=2)+'\n')
for row in rows:
    print(row['stage'],'maxdq',max(map(abs,row['delta_q_rad'])),'dTCP_mm',np.round(np.array(row['delta_tcp_m'])*1000,2),'grasp_normal_delta_deg',row['poster_normal_tcp_difference_deg'])
