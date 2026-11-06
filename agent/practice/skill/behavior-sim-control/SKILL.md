---
name: behavior-sim-control
description: Observe RGBD, estimate pixel locations, and control the simulated R1Pro in a BEHAVIOR practice run. Use for simulator manipulation, grasp practice, scene inspection and control-tool debugging. Not for physical robots or simulator provisioning.
compatibility: python3 with NumPy and Pillow; a practice run directory (SETUP.json + sim_client.py) bound to a running practice worker.
---

# BEHAVIOR simulator control (practice)

The client is the run-local **`$BEHAVIOR_SIM_RUN_DIR/sim_client.py`**. It is a Python/CLI interface invoked through
**bash**; it adds no model tools. **`act()` is the only motor-control entry point.** `observe()`, `xyz()` and
`pixel_to_body()` are perception; `admin_reset`, `admin_finish`, `snapshot`, `restore` and `practice_feedback` manage
the practice lifecycle and do not exist in evaluation.

Read [references/interface.md](references/interface.md) before the first action: full schema, frame diagrams, feedback
semantics, examples and tested precision limits.

## Bind your run

Use only the run you were given, one controller at a time. Read its `SETUP.json` first. Do not reset another agent's
practice or start simulators. Bind the run explicitly in every bash call:

```bash
export BEHAVIOR_SIM_RUN_DIR=/absolute/path/to/your/run
python3 "$BEHAVIOR_SIM_RUN_DIR/sim_client.py" observe
```

## Observe → decide → act → inspect

1. Get a fresh observation first and after every reset. `last_obs()` is cached.
2. Inspect all relevant RGB views and the robot self-state. `xyz(camera)` gives native pixel-aligned BODY coordinates
   from saved float depth; use NumPy slicing. It does not move the robot or identify objects or contact.
3. Choose the spatial goal yourself; there is no task-specific grasp macro. Each `act()` is one full goal in one RPC;
   the worker closes the loop every native tick and returns one endpoint. Choose small goals near objects and inspect
   feedback between them.
4. Read the returned `act_result`, including the per-arm diagnosis. Cartesian targets refer to the **rigid EEF-origin
   TCP**, not a deflecting pad midpoint. Pose completion is **not** grasp, contact or placement success. On
   `achieved=false`, inspect residuals and images and change the approach instead of retrying blindly. Closing waits
   until requested poses align unless `accept_partial=True` deliberately accepts an intentional press or pose miss.
   Arm and torso commands persist across actions; relative moves start from the command, not measured deflection.
5. Verify a claimed grasp by visible object motion with the hand, then lift, carry and retention. Finger separation
   alone is not enough. No force, contact, held-object or scorer readings are exposed.

**Measure geometry with depth, don't eyeball it.** `s.xyz(camera)` returns every pixel's robot-frame position
(forward, left, up) in metres, the same frame `act()` uses. Before a contact move, slice the region of interest (around
or between your pads, an edge you'll approach, the surface under a placement, the floor ahead), compare it with your pad
positions from the state block, and turn the difference into the `act()` offset.

You can **chain several `act()` calls in one Python script**. Each endpoint image is still delivered, and each
`act_result` reports `achieved`, so the script can stop when something isn't achieved.

```bash
python3 "$BEHAVIOR_SIM_RUN_DIR/sim_client.py" pixel right 280 190
python3 "$BEHAVIOR_SIM_RUN_DIR/sim_client.py" act '{"intent":"Withdraw right hand 2cm","right":{"fwd":-0.02}}'

PYTHONPATH="$BEHAVIOR_SIM_RUN_DIR" python3 - <<'PY'
import sim_client as sim
obs = sim.observe("Inspect before planning")
PY
```

After a reset or an uncertain transport, gripper intent is unknown: set both `left={"grip":...}` and
`right={"grip":...}` on the first action. Uncertain transport also requires a fresh `observe()` before any motion.

## Images, evidence and stopping

- Every `act()` and `observe()` publishes its endpoint image plus compact self-state. The image-delivery extension
  attaches every endpoint to the tool result, including redirected stdout and codemode. If it is not loaded, the client
  prints **`WARNING: image not attached — read <path>`**: stop and report it.
- `ROBOT_RECEIPT_FILE=...` names the full self-state and the image/depth paths. Motion summaries go to
  `<run>/control-action-results.jsonl`.
- Native float32 depth is saved to NPZ, never dumped into context. `xyz('left'|'head'|'right')[v,u]` returns BODY
  metres, invalid pixels NaN. Wrists are 480x480, head 720x720; the delivered 1680x720 collage is RGB only.
- A `STOP` file in your run and a user stop are authoritative. Stop reasons are `reached`, `stalled` and `timeout`.
  Explicit `seconds`/`max_steps` cap the whole call including the terminal hold (the tighter wins; default none).
  `timeout_seconds` is the overall motion budget (default 30 s). A sustained command/velocity mismatch stops base motion
  as `stalled`; inspect the fresh RGB-D and change approach, never repeat or force through. The guard is reactive, not
  collision planning.

## Practice lifecycle

```python
sim.admin_reset(case="episode", attempt_name="unique-name", practice=True, unbounded_practice=True)
obs = sim.observe("Fresh state after reset")   # the first observe starts the attempt clock
sim.snapshot("before-grasp"); ...; sim.restore("before-grasp")   # restore starts a NEW attempt
sim.practice_feedback()        # which goal predicates hold now (practice only)
sim.admin_finish("attempt complete")   # ends the attempt and returns its feedback
```

Do not reset to hide failed evidence. On the first attempt of a newly staged instance, snapshots, restores and feedback
are refused until `admin_finish`.
