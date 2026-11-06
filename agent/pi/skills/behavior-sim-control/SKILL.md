---
name: behavior-sim-control
description: Drive the authorized official BEHAVIOR R1Pro rollout using run-local act, observe and native-depth xyz. Use for simulated task manipulation, not provisioning or physical robots.
compatibility: Python 3.11 with NumPy/Pillow; supervisor-bound official HTTP client and endpoint image extension.
---

# Official evaluation control

This is the evaluation-only portable adaptation of the practice skill. Read the current run's `EVAL-BRIEF.md` and `SETUP.json`. Only import the run-local `sim_client`; inherited practice permissions and absolute paths are inactive. Do not run old skill scripts, change PYTHONPATH, contact practice workers or query simulator truth.

```python
import sim_client as s
obs = s.observe('Inspect the official start')
points = s.xyz('head')  # [v,u] → BODY x-forward, y-left, z-up, metres
```

`act(intent, left=None, right=None, base=None, torso=None, seconds=None, max_steps=None, position_tol=.005, rotation_tol=.035, accept_partial=False, timeout_seconds=30.)` is the only motor API. Read the run-local client for exact argument schemas; use the frozen NOTES/examples as learned guidance, not commands to replay blindly. Explicitly initialize both grip intents on the first act. Grip1=open,0=close; pose attainment or finger width does not prove grasp.

Each act is one full goal/one RPC, with shared controller feedback on every native30Hz frame. Explicit seconds/max_steps cap the complete move including terminal hold; defaultNone. Goals/persistent commanded arm and torso targets survive between calls. Relative commands anchor to command state, not measured deflection. To cancel obstructed preload, command freshly measured joints through act; no raw controller or force override. Reasons reached/stalled/timeout require endpoint inspection. Inspect velocity-guard stalls and change approach rather than repeat blindly.

Use RGB to identify the relevant object/edge; measure its geometry from native float depth before contact. Wrist480²/head720², BODY optical transform from the official relative camera pose. Delivered triptych is RGB-only1680×720. No effort, exact global pose, gravity/contact/held/scorer input is available. Odometry is an uncertain integration of public body velocity.

Every endpoint emits a receipt and image; the pinned observation_delivery extension must attach it to the model-visible outer tool result, including nested codemode bash calls. If delivery fails, stop and report it. `last_obs()` is cached. Never replay an uncertain act.

No admin_reset, snapshots, restore, retries, private evaluation state or controller modification. `s.admin_finish('evaluation-complete')` ends planning, not scoring. The evaluator owns termination. Stop on closed/error/ended or user STOP. Preserve approved cost/safety guards.
