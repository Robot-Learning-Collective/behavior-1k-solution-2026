# Task practicer brief (shared by all practice agents)

## The instruction (verbatim, from the operator)

> look at the prompt, task description, fine annotations, understand what needs to be done and what decisions need to be taken, and then find the hardest, non free space bits that they'll need to practice.
> then they should rank the things to practice and the aim should be to create notes and learn how to do this, with real poses and learnings. they need to start with highest ranked bits, go to it in the sim scene, try it, then refer to the proprio + rgb of humans if they're not able to get it, try again, until they get it and are able to do it fast.
> the main thing is, try it out, if it doesn't work, look through the human proprio, try again. it should look at saving little example trajectories and notes too. and they cannot give up — everything is solvable.

## What practice is for

Your `NOTES.md`, its top **EVAL PROCEDURE** section and your `examples/` are what a fresh copy of you will start from in
evaluation: a fork of this session, on a layout it has never seen, with no resets, no snapshots, no practice feedback
and a wall budget of one second per native step. Write them for that reader. Practice ends with an independent full
attempt from a fresh reset, within the task's native step budget.

## Your run

- Your task and run directory are in the kickoff message. Read the run's `SETUP.json` first.
- `export BEHAVIOR_SIM_RUN_DIR=<your run dir>` in every bash/Python call. If you see `WARNING: image not attached`,
  stop and say so: you would be acting blind.
- Your simulator slot is yours alone. Practice only on training-split instances; the public test instances are for
  evaluation.
- Tools: the `behavior-sim-control` skill (`SKILL.md`, `references/interface.md`) and the run's `sim_client.py`. Every
  `act()`/`observe()` returns the endpoint RGB image and a state block (hand point, both pad positions, axes, fingers,
  lag, margins); `act_result` reports `achieved` and why a move fell short. You can chain several `act()` calls in one
  Python script and stop when something isn't achieved.
- **Measure geometry with depth, don't eyeball it.** `s.xyz(camera)` gives every pixel's position in the robot frame
  (forward, left, up) in metres from exact float depth, the same frame `act()` uses. Use it before any contact move:
  slice the region around/between your pads and compare its heights with your pad heights from the state block (is the
  object between the pads? how far above/below?); find an edge's position and height before approaching it; check the
  surface under a planned placement; check the floor ahead before a base move. Turn the difference straight into the
  `act()` offset. Images are for *what* things are; `s.xyz` is for *where* they are.
- Simulator ground truth is never an input. Use images, state and `s.xyz`. `s.practice_feedback()` (which goal
  predicates are satisfied) is a practice-only aid.

## Read first: what other practicers learned

- `LESSONS.md`: cross-task lessons. Read it before practising; append general lessons you discover.
- Related tasks' notes and examples (`prior-practice/<task>/`), if your campaign has them.

## Workflow

1. **Understand the task:** the BDDL goal, the instruction, the fine annotations and the RGB of human demos for your
   task in the 2026 demo dataset (`behavior-1k/2026-challenge-demos`; your task pack has the paths). Write down what
   must be done and which decisions must be taken.
2. **List the hard, non-free-space bits** (grasps, presses, insertions, hangs, door opening, placing, hand-overs...) and
   **rank** them by difficulty and importance. Write the ranking to `NOTES.md`.
3. **Practise from the top of the ranking:** get to that bit in the scene (snapshot just before it), try it. If it
   doesn't work, study the human proprioception + RGB for exactly that interval (aligned state/actions, pads/hand pose,
   approach direction, base position), compare with your measured state and `s.xyz`, change the approach, try again.
   Repeat until it works, then until it works reliably and fast.
   - **If a few short tries still fail, go deep on the human runs:** step through that interval's proprio + RGB finely,
     across 2-3 different demos, in short segments (approach, pre-contact, contact, the move that changes the object,
     release/withdraw). For each segment write down what the human's hand, wrist, joints, base and the object do. Lay
     that against your own pattern for the same segment, find where you differ, and retry with that difference fixed.
4. **Record what works:** `NOTES.md` (what worked, real poses and measurements, what failed and why) and small example
   trajectories under `examples/`. Notes on disk survive context compaction; keep them current.
   - **Every success (sub-step or whole task) gets its own file in `examples/`**, linked from `NOTES.md`: the exact
     `act()` commands in order (or the script), short step-by-step instructions, the key proprioception at each step
     (base, torso, arm joints, pad positions, grip), key `s.xyz` measurements, and pointers to the key images.
5. Move to the next ranked bit. When the bits work, run the whole episode from a fresh reset.

Don't give up: everything is solvable. If something is truly blocked by infrastructure (simulator fault, missing
assets), write `PRACTICE_HOLD: <exact error>` and stop; routine progress stays in NOTES and examples.

## New layouts: transfer first, then learn

When the operator stages an unused training instance (a new layout) for you:

1. **The first attempt on each new instance is zero-shot:** follow only your top EVAL PROCEDURE. No demo study,
   snapshots, restores or practice feedback until `admin_finish` (the worker refuses them). Ground everything in the
   current RGB-D and proprioception, not remembered coordinates.
2. **If it fails:** analyse the failure in NOTES (what was missed and why, with observation/tick references), compare
   the failing segments with 2-3 human demos, practise those segments (this layout is now development data), and retry
   from fresh resets until one full attempt passes.
3. **Distil what generalises** into the EVAL PROCEDURE and `examples/`: perception, coverage, grasp and recovery rules
   that transfer, not this layout's coordinates or routes. The goal is that the next unseen layout passes first try.
4. One full-reset pass is enough. Then write `PRACTICE-HOLD` containing `WAIT_NEXT_INSTANCE` in your run directory and
   end your turn; do not start another reset of the same layout.
