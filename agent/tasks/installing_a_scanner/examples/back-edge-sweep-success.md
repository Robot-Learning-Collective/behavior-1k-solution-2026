# Back-edge sweep: first visible scanner relocation

Attempt scanner-run-007-v4-a02, obs788→876. One successful sweep, not repeatability/mastery and not grasp. Scanner translated toward robot and rotated; displacement persisted after withdrawal. Switch still red.

## Preconditions / steps

Base rel_start [0.617,-0.795,0], yaw -1.278rad. Torso [1.15,-.67,-.02,0]. Left hand parked via q=[-.4,0,0,-1.9,0,0,0], open: TCP [1.052,.252,.926]. Right initially open. Reacquire geometry; these coordinates are not universal. Rear rim head(450,292)=[1.3234,-.2000,.8292], (470,300)=[1.2959,-.2378,.8286], (510,320)=[1.2311,-.3028,.8286]. Table Z≈.765. A vertical finger direction was joint-limited; diagonal fingers enabled reach.

Exact successful sequence, run-local protocol4 sim_client:
```python
s.act(intent='Relax downward orientation to diagonal hook behind scanner',right={'to':[1.32,-.29,.91],'finger_dir':[.707,0,-.707],'close_dir':[0,1,0]},max_steps=20)
s.act(intent='Close right fingers in free air before back edge sweep',right={'grip':0},max_steps=8)
s.act(intent='Lower closed fingers behind scanner rear edge without lid pressure',right={'to':[1.32,-.29,.80]},max_steps=16)
s.act(intent='Sweep scanner rear edge toward robot instead of pressing lid',right={'to':[1.10,-.29,.81]},max_steps=20)
s.act(intent='Withdraw after visible back-edge sweep and verify scanner displacement remains',right={'to':[1.10,-.29,.96]},max_steps=16)
```

1. Approach above rear edge with diagonal fingers, open. Right actual TCP [1.317,-.290,.910], pads [1.317,-.242,.910]/[1.317,-.337,.910].
2. Close in air: zero gap, explicitly no grasp claim.
3. Descend: actual TCP [1.315,-.289,.809], command Z=.800 did NOT reach; ~9mm residual and elevated effort. This was accepted as a press/sweep start, not free-space alignment.
4. Pull backward 22cm at Z=.81: actual [1.101,-.291,.811], scanner visibly moves/rotates toward robot.
5. Lift clear: actual [1.100,-.290,.957]; scanner stays displaced. Visible top corners after: head(465,350)=[1.14765,-.19307,.82954], (410,400)=[1.03880,-.08061,.82905], (500,500)=[.88767,-.17877,.82803]. These are different visible points, not tracked rigid landmarks or exact translation measurement.

## Evidence

`back-edge-sweep-evidence.json` preserves each step's exact submitted action, complete robot proprioception (base, torso, joints, pads/grips), compact state and image/depth/receipt paths. Original images in `/tmp/scanner-run-007_obs/scanner-run-007-v4-a02/`:
- obs0788 before contact
- obs0792 closed above
- obs0828 contact/start of sweep
- obs0857 after sweep
- obs0876 withdrawn, persistent displacement

No retention, placement, switch activation, or episode success in this example. Next: repeat sweep toward table edge only with fresh geometry and stop before falling; prepare edge clamp with bottom jaw clearance.
