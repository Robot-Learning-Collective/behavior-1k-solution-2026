# Simulator interface and manipulation workflow

## Surface and launch

```text
native bash
    |
    +-- sim_client.py observe      RGBD + robot self-state, no motor action
    +-- sim_client.py pixel ...    native float-depth scene point, no motor action
    +-- sim_client.py act '{...}'  sole public motor interface
```

Practice sessions are launched with the image-delivery extension loaded (`agent/practice/bin/pi_session.sh`). Set `BEHAVIOR_SIM_RUN_DIR` to the run containing `SETUP.json`. The client derives the worker queue and transport from SETUP. No packages are installed or simulator workers started by this client.

For Python, add the run directory to `PYTHONPATH`, then `import sim_client as sim`.

## 1. Observation

```python
obs = sim.observe("Inspect target and clearance")
obs = sim.last_obs()  # cached; fresh observe if uncertain
```

Delivered image is **RGB only**: left480×480, head720×720, right480×480. Wrist panels are black-padded below, not resized; overall1680×720. No depth visualization panels are attached. `image_layout.camera_panels` retains native source bounds; metric depth remains in NPZ/`xyz`. Original received RGBD/video sources remain on disk.

Full supplied self-state: arm/torso joints and velocities, EEF positions/quaternions, own-link/finger geometry, measured finger joint positions/velocities, last commanded arm/torso targets, tracking errors, endpoint limits, and velocity-integrated planar base odometry (uncalibrated drift, no observed global pose/vertical displacement/tilt). Quaternions are **xyzw**. Tracking error is target minus measured joint position, **not torque/contact force**. Protocol4 also exposes PhysX measured joint efforts in Nm when available, with source/availability labels. These are joint efforts, not contact-force measurements or object-held flags; the official evaluator's fixed proprioception may not expose them.

Each endpoint includes capture/action/observation IDs and simulator time. Attempt-qualified directories retain old images after reset. `local_image_path` names the annotated image; `raw_image_path` is the unmodified received JPEG, **not metric depth**. `depth_path` names native float32 NPZ data; calibrated camera poses/intrinsics remain in disk-backed state.

**No pad dots, lines or labels are drawn on any delivered view.** Pad coordinates/projections remain in the saved self-state, not the image. The full compact text is unchanged: rigid TCP, measured pinch, pads/axes, fingers, joint lag/limit margins, diagnosis/fault and depth guidance. The project bridge attaches **every** public `act/observe` endpoint to the outer tool result even when stdout is redirected or codemode discards it; old images are not pruned. Without the bridge, a loud per-call warning tells you to read the image.

## 2. Float-depth XYZ — perception only

```python
xyz = sim.xyz("right", obs=obs)        # H×W×3 float32 BODY metres
point = xyz[190, 280]                  # [v,u], not [u,v]
patch = xyz[180:210, 260:300]           # ordinary NumPy slicing
point = sim.pixel_to_body("right", 280, 190, obs=obs)  # nearest native pixel
```

Camera is `left`, `head`, or `right`; u increases screen-right, v screen-down, within that camera's native dimensions. `xyz` works in fresh Python processes using the saved observation/NPZ. It unprojects **axial optical+Z float depth**, not radial distance or JPEG colors. Invalid/nonpositive/nonfinite depth becomes NaN; valid depths beyond2.4m remain valid. The JPEG palette's0–2.4m scale is visualization only. Calibration includes native pixel-centre offset, intrinsics and optical-camera→BODY transform. `d_override` and JPEG median/spread heuristics are removed.

A selected image box is not an object mask or a free-space/contact certificate. Example using a manually chosen, visible surface patch near the pads:

```python
import numpy as np
arm = obs["robot"]["right"]["own_links_body"]
pads = np.array([arm["ag_start_point_body"], arm["ag_end_point_body"]])
surface = sim.xyz("right", obs=obs)[v0:v1, u0:u1]  # choose native bounds from RGB
valid = surface[np.isfinite(surface).all(axis=-1)]
if len(valid):
    gap_z = pads[:, 2].min() - np.median(valid[:, 2])
    print("lower pad reference minus selected surface BODY-Z (m):", float(gap_z))
    # A visible point within this conservative interior box is evidence of a surface;
    # zero points is NOT proof the gap is empty (occlusion, selection and invalid depth).
    lo, hi = pads.min(axis=0), pads.max(axis=0)
    axis = int(np.argmax(hi-lo))
    lo -= .005; hi += .005
    lo[axis] += .01; hi[axis] -= .01  # exclude pad-end neighborhoods
    print("visible samples in interior box:", int(((valid > lo) & (valid < hi)).all(axis=1).sum()))
```

The BODY-axis-aligned box is only an approximate region, especially with rotated fingers; `gap_z` is a pad-reference height difference, **not collision clearance or grasp proof**. Re-observe after motion; old XYZ belongs to the old BODY frame. Inspect geometry and choose a safe hand goal separately. **No `to_pixel` field or special section/inspect/measure API exists.**

## 3. The sole motion entry point

```python
result = sim.act(
    intent="Describe intended physical change",
    left=None, right=None, base=None, torso=None,
    seconds=None, max_steps=None,
    position_tol=0.005, rotation_tol=0.035,
    accept_partial=False, timeout_seconds=30.,
)
```

Every component is optional. Omitting an arm preserves its **last commanded joint target across calls**, including preload; it does not re-anchor to measured joints or fix the hand in world space when base/torso moves. Explicit `to=current_eef_position` retains a rigid-TCP Cartesian pose goal, including zero initial error, while the torso moves (BODY-relative, not world-fixed during base motion). Omitted grippers preserve the last known **executed** explicit command. A zero-tick cancellation preserves previous intent; uncertain execution clears it. After reset/uncertain RPC, specify both grippers; no inference from measured finger opening. An uncertain motion also requires a fresh `observe()` before any further action; unresolved pose prerequisites survive that observation.

The per-tick client requires a fresh **controller protocol6** observation; call `observe()` before the first motion. The worker reads RGB-D back only after the move (no pre-move images at an act endpoint), and the controller supplies the base feedback guard and caller tick caps.

```text
requested endpoints
       |
       v
one native30Hz step --> new proprioception --> reached? --> terminal hold/return
       ^                                      |
       +---------- command-space IK ----------+ no

Stop instead on a measured plateau (stalled) or overall timeout.
All ticks run inside ONE RPC; render/capture the endpoint only.
```

Units: metres, joint radians; fields ending `_deg` use degrees. `act()` sends ONE full goal in ONE RPC. There are no50mm/20° sub-goals or open-loop ramps. At every physics tick the shared controller reads new proprioception, takes one IK step from persistent command toward the full goal, and applies the unchanged0.025rad/tick arm command slew. Measured lag is not capped; native effort limits remain authoritative. Explicit `seconds` and positive-integer `max_steps` bound the **whole call including terminal hold**; the tighter cap wins. `seconds` must be finite and at least1/30s (at most120s), and converts to floor(seconds×30) ticks. DefaultNone does not silently impose16ticks. `timeout_seconds` remains the overall simulated-motion timeout (.1–120s, default30s), plus one terminal hold, intersected with explicit caller caps. A1tick cap executes only safe hold. Early stop reports `achieved=false`, measured progress and `caller_limits`; do not assume the requested displacement completed. A measured plateau or sustained command/velocity mismatch stops as `stalled`; neither proves contact. The base guard uses a15tick net translational tracking window and angular tracking error plus a meaningful heading miss, with bounded tolerance floors. It also fades translation at0.05–0.15rad heading error, holding translation above0.15rad. After a stop, inspect RGBD/state and deliberately change approach; there is no automatic reverse, retry or force override. These are reactive guards, not collision planning or a guarantee against falls. The same step function serves official evaluator observations, one native action per evaluator query.

### BODY frame

```text
TOP VIEW                         SIDE VIEW
     +X forward                       +Z up
         ^                                ^
         |                                |
+Y left--+ robot                          +----> +X forward
```

Origin/axes belong to the **current mobile base**, not the floor or a fixed world frame. Cartesian arm targets remain base-relative at the final endpoint. Camera offsets are converted with camera axes measured at call start.

### Arm translation

```python
sim.act(right={"fwd": -.02, "left": .01, "up": .02})
sim.act(right={"to": [.55, -.28, .85]})  # example coordinate, not a safe universal pose
sim.act(right={"to": point, "offset": [0, 0, .03]})
```

```text
rigid TCP * -----> X requested rigid TCP position
       advance / withdraw / lateral align / lift / place
```

`fwd/left/up` are BODY translations relative to the **commanded rigid TCP** (static-model FK of the last arm/torso setpoints), not the measured/deflected hand. `to` is an absolute BODY **rigid TCP** target, currently the EEF origin; `offset` is a BODY vector added to `to`. Absolute and relative translation fields cannot be mixed. Cartesian translation holds the commanded orientation unless rotation is requested; relative rotations also start from the command. Measured pad positions/pinch midpoint remain useful diagnostics but never move the control point when fingers deflect.

### Camera-relative arm translation

```python
sim.act(right={"cam_right": .02, "cam_down": -.01, "cam_fwd": .01})
```

```text
image:   up (-cam_down)
                 ^
                 +----> cam_right
                 v
             cam_down
cam_fwd = into the image, optical depth axis
```

Distances are metres along camera axes, **not pixel servo targets**. Can be added to relative BODY translations. Stationary scenery generally shifts opposite a translating camera. Use for small view-aligned corrections, not as proof of object distance.

### Rotation

```python
sim.act(right={"roll_deg": 20})
sim.act(right={"pitch_deg": 15})
sim.act(right={"yaw_deg": -10})
sim.act(right={"finger_dir": [1,0,0], "close_dir": [0,0,1]})
```

```text
fingers ---->             fingers /
       * rigid TCP  ->           * rigid TCP
                    rotate around midpoint
```

`roll,pitch,yaw` specify **one BODY rotation vector `[roll,-pitch,yaw]`**, not sequential Euler rotations. Axes are +X,-Y,+Z respectively; names do not promise a particular fingertip motion in every posture. Magnitude≤180°; larger requests rejected explicitly. Exact180° has an ambiguous path sign; deterministic sign chosen, then per-tick corrections toward the orientation.

`finger_dir` is desired EEF+Z (finger extension axis); `close_dir` desired EEF+Y (jaw-closing axis). Supply both finite nonparallel3-vectors. Closing direction is orthogonalized against finger direction. Do not mix target axes with rotation deltas. Rotation pivots about the rigid EEF-origin TCP, not the deflecting pad midpoint. Accuracy still depends on measured feedback and reachability.

### Gripper

```python
sim.act(left={"grip": 0}, right={"grip": 1})  # intentional commands, not a default recipe
```

```text
open: |         |    close: |   |
```

`grip`0=close,1=open; finite intermediate commands0–1 accepted but partial-opening precision is not calibrated. A gripper-only call acknowledges the command, **not secure grasp or reached jaw position**. Feedback gives command and measured finger-joint sum, not a binary HOLDING verdict. Opening a loaded hand releases it: choose explicitly from task intent, not a copied example.

Closing is gated: a compound pose/base/torso-plus-close request keeps the prior gripper command until **all requested poses** reach tolerance, then sends the close on a later native tick. Timeout/stall leaves an unissued close deferred. Explicit gripper targets wait for measured finger endpoints or stall; a blocked closure is not grasp proof. A prior missed arm goal blocks later grip-only closing for that arm; missed base/torso goals block either hand. The result is `prerequisite_not_met`: the client-side cached gate dispatches zero motor ticks; the shared core also enforces this prerequisite, returning only an idle hold. Reach an explicit replacement goal, or deliberately acknowledge the earlier miss using `accept_partial=True`. `accept_partial=True` explicitly permits closing despite acknowledged prior or current pose misses (including intentional presses). It does not disable joint/command-slew bounds, uncertainty fencing or terminal checks. It does not establish object contact or secure grasp.

### Joint targets and posture preference

```python
sim.act(right={"q": [q1,q2,q3,q4,q5,q6,q7]})
sim.act(right={"dq": [0,0,0,0,.1,0,0]})
sim.act(right={"preset": "ready"})
sim.act(right={"up": .02, "bias": "current"})
```

```text
shoulder o                 shoulder o
          \                         \
           o elbow                  o elbow
            \                      /
             * hand               * hand
```

Joint positions/deltas are radians,7elements. `q` is absolute; `dq` adds to the **previous command**, not measured joints. Goals outside supplied endpoint limits are rejected, not silently clipped.

**Persistent pressing and release:** a command into a surface keeps pushing until changed, including through omitted-arm/base moves. To remove that preload without requesting a different physical pose:

```python
obs = sim.last_obs()
sim.act(left={"q": obs["robot"]["left"]["joints"]}, accept_partial=True)
# Same existing q field for right, or torso={"q": obs["robot"]["torso_joints"]}.
```

This uses normal command slew, not an instantaneous jump or a new mode. Once the command reaches the measured-pose request, the extra position-error preload is removed; small settling/gravity effort can remain. It is not a zero-contact-force guarantee. `preset` selects an existing named **joint posture**, not a grasp macro; do not treat historical task-named poses as guaranteed safe/working. Joint/preset commands cannot mix with Cartesian fields, apart from grip.

Cartesian `bias`: `current` default, `nominal`, a named posture or7joint values. It is a nullspace preference, not exact elbow control or a zero-drift guarantee. No automatic posture/path search is supplied.

### Base

```python
sim.act(base={"fwd": -.05, "left": .02, "yaw_deg": 5})
sim.act(base={"to_rel": [start_x, start_y, start_yaw_degrees]})
```

```text
[R] ---- translate ----> [R]       [^] -- yaw --> [<]
```

Relative translation is in the call-start BODY frame; positive yaw turns left viewed from above. `to_rel` uses the practice-start frame; optional yaw is degrees. Do not mix `to_rel` with relative fields. Raw velocity lists are not accepted by public act.

Worker Cartesian targets are WORLD-fixed within a finite step. The client predicts base motion to compensate arm endpoints, then corrects from measured feedback. Translation/rotation acceleration, slip and paths are not exact. This is endpoint control, **not collision planning**.

### Torso

```python
sim.act(torso="normal")
sim.act(torso={"to": [joint1_radians, joint3_radians]})
sim.act(torso={"q": [joint1_radians, joint2_radians, joint3_radians, joint4_radians]})
```

```text
 shoulders [--]          shoulders [--]
              |                    /
              |      ->           /
            [base]              [base]
```

Presets: `tall=(.840,-.420)`, `normal=(1.074,-.612)`, `mid=(1.250,-.750)`, `low=(1.605,-1.073)`, in joint1/joint3 radians. Preset/`to` shorthand expands **once at call start** to four absolute goals: q1/q3 as requested, q2=start_q2−(2.1/1.15)×(goal_q1−start_q1), q4=start_q4. Explicit `q` independently targets all four joints. Omitted torso preserves its last four commanded targets across calls. Shorthand starts from those commands, not measured deflection. All four targets remain fixed throughout the move; explicitly requested torso goals use measured and commanded residuals for convergence. Tracking lag on an omitted/held torso is reported but does not prevent an unrelated requested motion. Runtime `robot.torso_joint_limits_rad` bounds are required; nonfinite/out-of-bounds goals reject without clipping. The single goal carries absolute torso targets, with native POSITION and per-tick command-slew guards. A new worker observation with bounds is required before motion; this client deliberately refuses the older backend.\n\nPresets are postures, not exact shoulder heights or collision-free guarantees. Clear arms before lowering the torso; a hanging hand may obstruct a crouch. Metric `torso.up` is unsupported. Shorthand preserves the call-start coupling offset—it does not automatically repair pre-existing drift. Tracking lag alone does not prove contact. Intentional into-surface commands persist until changed; observe lag/effort and use the measured-q release above when appropriate.

### Composition and result

```python
r = sim.act(right={"up": .02, "grip": 1}, base={"fwd": -.03})
status = r["act_result"]
if not status["achieved"]:
    print(status["reason"], status["errors"])
    # Inspect endpoint RGB/state before choosing a revised action.
```

Result includes `interface=act-v4-per-tick-persistent-goal`, `high_level_action_id`, `achieved`, `reason`, native-tick `steps`, per-component `errors`, per-tick error `trace`, per-arm whole-move diagnostics, `prerequisite_gate`, tolerances, `ended`, and `execution` (executed ticks, timeout budget, stop reason, structured fault and execution uncertainty). `requested_ticks` is null because convergence determines duration; the overall budget is `timeout_ticks` plus one terminal hold tick. Cancellation, partial/ended execution and controller faults never count as pose achievement. Expected torso feasibility faults stop the current action without invalidating the whole trial; they do not authorize automatic retry or removal of a guard. The action JSONL also retains original/resolved targets and partial/failure records. Success means requested **robot pose** within tolerance: default position5mm, orientation0.035rad(~2°), joint goals0.025rad(~1.43°). These are requested tolerances, **not universally demonstrated precision**. Normal reasons: `reached`, `stalled`, `timeout`, `prerequisite_not_met`; execution reasons include `cancelled`, `episode_ended`, `controller_fault`, `simulator_error`, `partial_execution`, and `execution_status_missing`. Untargeted arms, world objects and grasp stability are not success predicates. No object contact flags, collision oracle, object-held state or hidden scoring data is used. Reported joint efforts are diagnostic self-state, not a contact/grasp gate.

### Per-arm evidence and diagnosis

`act_result.arms[arm]` contains requested / model-predicted / measured **same rigid TCP**, position/orientation residuals, finger readings/asymmetry, joint lag, endpoint margins and Jacobian spectrum. Diagnoses use the whole move's observed tick sequence; `trace` retains per-tick errors, not intermediate images. `ik_predicted` means FK of the last emitted joint setpoint—not a separately solved reachability target or collision prediction. `model_valid` checks FK against measured EEF pose before trusting model-dependent diagnoses.

Diagnoses include `reached`, `not_targeted`, `IK_stalled`, `joint_limit`, `ran_out_of_steps`, `unknown` and `mixed`. `blocked` is always **suspected**: sustained joint tracking lag with stalled progress, not proof of contact, obstruction identity or grasp. These are limited-evidence hypotheses, not global feasibility certificates. Full records persist to `control-action-results.jsonl`; pending prerequisites are written before transport, so a lost reply cannot silently erase an unmet goal.

## 4. Practice lifecycle

Only when reset is authorized and this controller owns the run:

```python
sim.admin_finish("practice drill complete")
sim.admin_reset(case="pair1", attempt_name="unique-drill-name", practice=True, unbounded_practice=True)
obs = sim.observe("Fresh state after reset")
```

Cases: `pair1`, `pair2`, `pair3`, `episode`. Reset replaces world state and invalidates cached pose/gripper intent. Do not reset to hide failed evidence. Ordinary skill use does not authorize scored trials, additional paid/model campaigns, worker restarts or infrastructure recovery.

## 5. What has actually been tested

Original controller tests (simulator self-state, one run each):

- Combined50mm base retreat +10° arm rotation: base error1.89mm, arm error4.00mm at that endpoint.
-20mm camera-down/right nudges: endpoint vector errors0.51/0.56mm. Independent recorded RGB shifts confirmed the signs, not absolute scene calibration.
-180° orientation target:9bounded steps, final orientation error0.040°, pinch error0.475mm.
-~198mm absolute Cartesian target:4steps,2.24mm final error.
- Intent preserved through a real open-but-deflected gripper; intentionally incomplete80mm request returned achieved=false/31.24mm residual with max_steps1.
- Explicit torso target max joint residual0.0000403rad in one test.

These measured errors use simulator-provided robot self-state. They do not establish physical-robot accuracy, arbitrary-pose repeatability, contact safety, book-grasp reliability, cross-camera absolute calibration, partial-gripper accuracy or centimetre-accurate pixel localization. The rename/packaging retains this controller; current API smoke checks are recorded separately in the authorized run.

## 6. Existing model resources and boundaries

URDF supplies joint axes, limits and link kinematics. USD supplies camera mounts; protocol3 now carries runtime native intrinsics and BODY-relative camera poses. Measured on 3,598 wrist finger-mesh samples, depth-derived XYZ matched the simulator to about 1 µm (head partial-mesh occlusion outliers up to 22 mm). Current wrist transform provenance: `r1pro.usda` SHA256 `6029617cdd3aefce981428058a1c82cffe6af20ae61dc5be1da7334342c3bc52`. Do not assume URDF contains force readings or that geometry substitutes for measured force.

Native read/write/edit/bash remain the model's tools. This skill teaches how to invoke existing simulator code; it adds no agent, no model, no robot primitive, no scorer access and no runtime lifecycle authority. Keep STOP/cost/finite-action/GPU boundaries intact.
