# TRAIN10 cabinet door — full-chain worked example

**Status: worked procedure, NOT a demonstrated native-reset completion.** Originally documented offline from full001; subsequently exercised on replacement worker as `cabinet-full-002` without snapshot restore. Full002 verified acquisition → carry → tip → retained reorientation → alignment → FIRST descent; its SECOND/final-descent RPC became uncertain, and release was not dispatched. Descent/release task successes remain snapshot continuations only. See [full002 interruption](../native-full-002-interruption.json).

Full002 delta: skip the explicitly labelled failed lower-outside call AND recovery retreat in section3; directly use the wider Cartesian route after `pre`. That simplified sequence tipped successfully with four pushes. Fresh alignment was forward.20/left−.105 instead of−.10. Other listed phases matched. Milestone `(obs,sim s,task wall s)`: lift(16,35.8667,288.0),carry(28,67.4333,446.0),tip(39,81.30,596.5),reposition(44,90.50,679.3),reorient(51,95.7667,779.2),align(53,98.9333,819.9),first descent(54,99.5333,837.3). Reset setup322.4234wall s excluded from those task clocks. Values rounded; full receipts retained.

## Safety and replay boundary

- Current full002 worker is blocked: do not replay its uncertain SECOND descent `e1c647c4-7077-4a88-878a-ebc0be26404a` or reset blindly. Client saved-reply recovery and subsequent observe failed. Await operator diagnosis/release and a fresh endpoint. Old full001 live world is gone.
- Exact assigned TRAIN10/Rs_int, protocol6/controller26efe4a and matched run-local client/helpers only. Full001 sourcea47213f; replacement full002 source5fdefd3/PID3602775. Re-read READY SETUP and interface after a handoff; no old-source snapshots.
- This is a **stepwise example**, not a blind batch script. Run ONE action, inspect its attached RGB/self-state and achievement, then select the next step. Loops below are notation for separate inspected calls.
- Coordinates below are measured values from this one instance. Remeasure grasp, clearances, cabinet plane and mating corners. Tracking/effort is not contact or collision-free proof.
- On uncertainty: stop motion, recover the saved reply or observe; never repeat an action to recover its output. Persistent missed commands must be replaced, not ignored.
- No automatic reset, retry, snapshot restore or goal-feedback-based geometric planner. Native feedback at the end is authorized practice-only.

## Environment and a separately authorized fresh start

Launch from `astra-harness/`; bridge must attach endpoint images. Use a fresh `/usr/bin/python3` process for each inspected call:

```bash
export BEHAVIOR_SIM_RUN_DIR=<workspace>/astra-harness/experiments/model-comparison/runs/cabinet-run-023
export BEHAVIOR_SIM_CAMPAIGN_DIR=<workspace>/astra-harness
export PYTHONPATH="$BEHAVIOR_SIM_RUN_DIR"
# /usr/bin/python3; import sim_client as s
```

Only after authorization for a NEW attempt and closure of its predecessor:

```python
s.admin_reset(case='episode', attempt_name='NEW-UNIQUE-NAME',
              practice=True, unbounded_practice=True)
s.observe()
```

This is not an instruction to reset the interrupted attempt. Full001 reset setup was **320.856 wall seconds**; the first observation started its task wall clock.

## 1. Approach and acquire

Both grips must be explicit on the first action. An earlier omitted-grip request was rejected before motion; it is not part of the effective trajectory.

```python
s.act(base={'yaw_deg':-40}, left={'grip':1}, right={'grip':1}, seconds=4)
s.act(base={'yaw_deg':-65}, seconds=4)
s.act(base={'yaw_deg':-65}, seconds=4)
# Four separate calls, inspecting corridor floor and furniture each time:
s.act(base={'fwd':.5}, seconds=4)
s.act(base={'fwd':.5}, seconds=4)
s.act(base={'fwd':.5}, seconds=4)
s.act(base={'fwd':.5}, seconds=4)
s.act(left={'preset':'ready'}, right={'preset':'ready'}, seconds=3)
s.act(base={'fwd':.59,'left':.01}, seconds=5)
s.act(torso={'q':[1.4505,-2.227,-.818,0]}, seconds=3)
s.act(left={'to':[.52,.27,.65], 'finger_dir':[0,0,-1],
            'close_dir':[.71,-.70,0]}, seconds=3)
```

Unfold BOTH arms before crouching. At obs12 base odom was approximately[-2.468,-.702],yaw−2.869. Fresh left-camera top-edge samples: [0.5452,.1528,.4513] and [.5711,.1827,.4513]. Depth near-corner pregrasp was adjusted to [.573,.185,.50]:

```python
s.act(left={'to':[.573,.185,.50]}, seconds=3)
s.act(left={'to':[.573,.185,.43]}, seconds=3)
```

**Actual observed branch:** insertion IK-plateaued at TCP[.566,.186,.436], not the requested goal. This was ~15mm below the .4513m top, with pads visibly spanning the panel and negligible joint lag. After inspecting that partial, replaced the unreachable Cartesian target with measured q and accepted the shallower insertion:

```python
s.act(left={'q':[-.93888,-.08571,-1.50291,-.06704,-.57461,-.45146,-.81903],
            'grip':0}, accept_partial=True, seconds=2)
s.act(left={'to':[.55,.185,.57]}, seconds=4)
```

Do not copy that acceptance if your partial differs. The close reported stalled aperture but no pending pose miss. Test lift reached; visible top rose **.4513→.5851m**, retained between pads against fixed floor/bookshelf. Finger sum≈.009m alone is not grasp proof. Obs16: sim35.8667s, wall412.7s.

## 2. Raise and carry

```python
q0 = [-1.03388,.54529,-1.33942,-1.66169,-.48348,.29445,-1.52716]
s.act(torso={'q':[1.025,-1.45,-.47,0]}, left={'q':q0}, seconds=3)
s.act(right={'q':[0,0,0,0,0,0,0]}, seconds=3)
# Four separately inspected rotations:
s.act(base={'yaw_deg':-45}, seconds=4)
s.act(base={'yaw_deg':-45}, seconds=4)
s.act(base={'yaw_deg':-45}, seconds=4)
s.act(base={'yaw_deg':-52}, seconds=4)
s.act(base={'fwd':.4}, seconds=4)
s.act(base={'fwd':.5}, seconds=4)
s.act(base={'fwd':.6}, seconds=5)
s.act(base={'fwd':.4}, seconds=4)
s.act(base={'left':-.3}, seconds=3)
s.act(base={'fwd':.5}, seconds=4)
```

This route used visible floor/depth checks between sideboard, ottoman and coffee table. Ottoman sampled top Z .36–.38m; clearance was narrow, not certified collision-free. Inspect retained panel throughout. Obs28 reached odom[-.103,-.323],yaw−5.998, TCP[.502,.187,.848]. Sim67.4333s, wall637.3s.

## 3. Tip cabinet while holding door

```python
s.act(right={'preset':'ready'}, seconds=3)
s.act(torso={'q':[1.4505,-2.227,-.818,0]}, seconds=3)
s.act(base={'fwd':.31}, seconds=3)
pre = [-.56571,-.59988,.24254,-.87404,.04208,.70416,.56755]
s.act(right={'q':pre}, seconds=3)
```

**Important full001 failure/recovery:** the old outside-lowering q below hit the cabinet top during its path (q4lag .179rad); it is NOT a robust clean waypoint sequence:

```python
# Historical failed call in full001; not a recommended blind step:
s.act(right={'q':[-.77771,-.39425,.30167,-.01963,.08172,.09287,.40054]}, seconds=2)
# Actual recovery after inspecting failure:
s.act(right={'q':pre}, seconds=2)
s.act(right={'to':[.57,-.55,.55]}, seconds=3)
s.act(right={'to':[.52,-.55,.44], 'finger_dir':[.85,0,-.53],
             'close_dir':[0,1,0]}, seconds=3)
```

Last Cartesian goal IK-plateaued at [.516,-.544,.448], with negligible lag. It was already outside/lowered, so the following **new explicit joint goal**, rather than another lowering retry, entered the opening successfully:

```python
s.act(right={'q':[-.66288,-.2537,.05998,-.02574,-.15844,-.35401,.26739]}, seconds=2)
# Four SEPARATE pushes, each followed by image/depth inspection:
s.act(base={'fwd':.06,'left':.04}, seconds=2)
s.act(base={'fwd':.06,'left':.04}, seconds=2)
s.act(base={'fwd':.06,'left':.04}, seconds=2)
s.act(base={'fwd':.06,'left':.04}, seconds=2)
```

Top-plane normals (arbitrary SVD sign) after first/second/third pushes: [.1555,.1496,.9764], [.2158,.2081,.9540], [−.2979,−.2879,−.9102]. Fourth push tipped open-face upward. Rim subsequently measured Z≈.2478m. Obs41: sim83.9667s, wall885.9s. No clean replay claim for deleting the failed waypoint: that deletion has not been independently tested.

## 4. Raise, reposition, retained reorientation

```python
s.act(right={'preset':'ready'}, torso={'q':[1.025,-1.45,-.47,0]}, seconds=3)
right_clear = [-.65,.14,-.08,-1.1,0,.05,-.1]
s.act(right={'q':right_clear}, seconds=2)
s.act(base={'left':-.3}, seconds=3)
s.act(base={'left':-.4}, seconds=4)
s.act(base={'fwd':-.18}, seconds=3)
```

Raise/adduct empty right arm before chair-side motion. Move back BEFORE wrist rotation to avoid prior wall-side preload. Obs46: sim93.1667s, wall963.2s; odom[.390,-.741],yaw−5.994. This is not proof the body route avoided every chair.

```python
q0 = [-1.03388,.54529,-1.33942,-1.66169,-.48348,.29445,-1.52716]
qu = [-.82004,.76749,-.81012,-1.23156,1.50615,1.0272,.53836]
qh = [.11953,.2051,.06719,-1.19977,1.73911,.13551,-.51735]
qd = [-.23349,-.01685,.28569,-.90476,1.73956,-.43167,-.54124]
# EACH line is one inspected call, not an unattended loop:
s.act(left={'q':[.75*a+.25*b for a,b in zip(q0,qu)]}, seconds=2)
s.act(left={'q':[.50*a+.50*b for a,b in zip(q0,qu)]}, seconds=2)
s.act(left={'q':[.25*a+.75*b for a,b in zip(q0,qu)]}, seconds=2)
s.act(left={'q':qu}, seconds=2)
s.act(left={'q':[(a+b)/2 for a,b in zip(qu,qh)]}, seconds=2)
s.act(left={'q':qh}, seconds=2)
s.act(left={'q':qd}, seconds=2)
```

All seven goals reached in full001; panel remained retained, handle-face up. At qu, measured wrist q6 upper margin≈.006rad: no farther command. Avoid direct qu→qd shortcut; its estimated panel sweep was wider near the wall. Offline FK is not collision checking. Obs53: sim98.4333s, wall1103.7s.

## 5. Align BEFORE deep descent

```python
s.act(torso={'q':[1.4505,-2.227,-.818,0]}, seconds=3)
```

Fresh obs54 permitted head-depth measurements (metres BODY):

| Corresponding corner | Door | Cabinet rim |
|---|---|---|
| D → nearB | [.5400,.4774,.5825] | [.7367,.3764,.2478] |
| C → nearA | [.6921,.2892,.5791] | [.9004,.1851,.2478] |

Averaged planar discrepancy≈[+.202,−.102]. Values came from small visible pixel patches filtered by the relevant height band, not object masks. Example sampling uses `s.xyz('head')[v,u]`; pixels in full001 obs54 were doorD[85,600],doorC[230,527],rimNearB[226,595],rimNearA[302,542]. Remeasure in a new run.

```python
s.act(base={'fwd':.20,'left':-.10}, seconds=3)
```

**Last confirmed endpoint**, obs55: sim101.5667s, wall1173.7s, odom[.607,−.780],yaw−5.996. Left TCP[.568,.449,.580],grip0; right raised,grip1. Receipt `receipt_01792160044142309000_f17560125818448fa4764266dfecd404.json` under own cache `cabinet-full-001/`.

## 6. Descent and release — first descent verified in full002, second uncertain

Full002 first call returned reached at obs54/TCP[.568,.450,.346]. The SECOND call failed with malformed/missing header and failed automatic saved-reply recovery; subsequent observe also failed. Outer650s tool timeout was not hit. No release or native task check occurred. The code below is procedural reference, NOT permission to replay the uncertain second call.

The first call below was dispatched in full001 as UUID `9277babe-51ee-48d9-863b-8f9ae24212ba` and its reply was NOT received. **DO NOT replay it in that attempt.** Observe/recover first after operator release.

```python
s.act(torso={'q':[1.75,-2.65,-1.2,0]},
      left={'q':[-.41233,-.00659,.33661,-.67196,1.8398,-.30763,-.84616]},
      seconds=3)
# Inspect: expected TCP near [.569,.450,.350], horizontal, no sustained torso/arm lag.
s.act(torso={'q':[1.744,-2.75,-1.3,0]},
      left={'q':[-.53207,.0244,.34218,-.44336,1.8552,-.28687,-.86769]},
      seconds=3)
# Inspect: expected TCP near [.569,.450,.299], shallow far-edge-down tilt.
s.act(left={'grip':1}, seconds=1)
# Practice-only; do not use during evaluation or as geometric input:
feedback = s.practice_feedback()
result = s.admin_finish()
```

The last two actions were NOT dispatched in full001. Prior successful checkpoint continuations verify this final pose/release sequence only in those states. Do not add previously failed torso q1=1.8 substep: it stalled at1.744 with high effort. Partial opening (~.086m of requested .10m) previously accompanied attachment; native predicate feedback, not apparent flush placement, establishes success. Retreat was unnecessary in those successes.

## Observed clocks and evidence limits

Task wall clock includes model deliberation, transport, inspection and intervening documentation. These are not motor-only timings. `seconds=` is a native-tick cap, NOT wall time. Cached wall values below are rounded endpoint receipts; no extrapolated completion time.

| Full001 milestone | Obs | Cumulative sim s | Increment sim s | Cumulative task wall s |
|---|---:|---:|---:|---:|
| Native reset observation | 1 | 0 | — | ~0.1 |
| Verified test lift | 16 | 35.8667 | 35.8667 | 412.7 |
| Carried-door staging | 28 | 67.4333 | 31.5666 | 637.3 |
| Cabinet tipped | 41 | 83.9667 | 16.5334 | 885.9 |
| Raised/repositioned | 46 | 93.1667 | 9.2000 | 963.2 |
| Seven-goal reorientation | 53 | 98.4333 | 5.2666 | 1103.7 |
| Basic crouch + aligned base | 55 | 101.5667 | 3.1334 | 1173.7 |
| First final descent | unknown | unknown | unknown | outer call timed out at120s |
| Release/native goal | not dispatched | — | — | — |

Additional transport recovery: observe failed after90s; saved-reply-only recovery failed after20s. Read-only exec succeeded. These waits are not scored failure or simulator-time evidence. Current cache is uncertain; last-known imagery is not current pose proof.

Earlier independent evidence: first carry-checkpoint→goal +60.20sim s/wall1696.6606s; second carry-checkpoint→goal +37.0333sim s/wall564.3025s; initially-attached=false final-descent checkpoint→goal47ticks/1.5667sim s/wall68.6175s. See `attachment-success.json`, `attachment-continuation-repeat.json`, `attachment-repeat.json`. None is a native-reset full-chain success or held-out-instance result.
