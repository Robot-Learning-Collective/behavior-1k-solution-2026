# The agent: GPT-6 Astra plays the tasks the policy can't, starting from its own practice

Our learned policy (π0.5-based, [main README](../README.md)) plays all 100 BEHAVIOR tasks. On some long,
precise tasks it scores close to zero: attaching a camera to a tripod, cleaning a trumpet, building cabinet doors.
For 14 tasks the policy server hands the episode to an **LLM agent** instead. Those are tasks where the policy scores
about zero, so there is little to lose, or where the agent's practice results beat the policy's score.
 GPT-6 Astra drives the R1Pro through
three Python calls (`observe`, `act`, `xyz`), and it doesn't start cold. Before evaluation, a copy of the agent
**practised each task in the simulator**, sometimes for hours. It ranked the hard parts, drilled them, compared itself
with the human demonstrations, and wrote down what worked. Every evaluation episode starts from a fork of that frozen
practice session.

```
  public leaderboard          learned policy only   38.9 %
  (100 tasks, q-score)        + agent on 14 tasks   44.6 %   →  9th place, best independent team
```

With the policy's score alone, we would have ranked around 21st on the final leaderboard. "Independent" means a team
without company or lab funding behind it.

- [How it fits together](#how-it-fits-together)
- [Results](#results)
- [The practice loop](#the-practice-loop-how-the-agent-learns-a-task)
- [The evaluation loop](#the-evaluation-loop-one-episode)
- [What the agent sees and does](#what-the-agent-sees-and-does)
- [What we changed along the way](#what-we-changed-along-the-way)
- [Guards](#guards-time-money-and-the-robot)
- [Running it](#running-it)
- [Code map](#code-map)
- [Limits](#limits)

---

## How it fits together

```
                    official evaluator  (OmniGibson + Isaac Sim, R1Pro, 30 Hz)
                                 │  websocket: one observation in, one 23-D action out, every step
                                 ▼
             ┌──────────── scripts/serve_b1k.py --agent ─────────────┐
             │                                                       │
      task enabled in                                          any other task,
   agent/tasks/tasks.json?                                    or the agent failed
             │ yes                                                   │
             ▼                                                       ▼
   AgentRoute                                               learned policy (π0.5, JAX)
   src/b1k/policies/agent.py                                unchanged
             │ new episode
             ▼
   FrozenRuntime ── agent/eval/runtime.py
     │  1. copy NOTES.md, examples/, task pack into a private run dir
     │  2. start a loopback HTTP bridge  (agent/control/official_policy_server.py)
     │  3. pi --fork agent/tasks/<task>/session.jsonl   ← the frozen practice session
     ▼
   GPT-6 Astra (OpenAI API, thinking: medium)
     │  bash → python:  s.observe()   s.act(goal)   s.xyz(camera)
     ▼
   sim_client.py ──HTTP──► bridge ──► per-tick controller (agent/control/portable_control.py)
                                         │  one native action per evaluator step, toward the goal
                                         ▼
                                     back to the evaluator
```

One piece of code is shared end to end. **Practice and evaluation use the same controller and the same client**
(`agent/control/`). The controller modules are byte-for-byte what ran in both during the competition. The client
differed only in its transport code then, and is one file here. The only difference is where an `act` goes: the
practice worker's job queue, or the policy server's loopback bridge.

---

## Results

Final ranking: **9th**, the best-placed independent team. Public leaderboard (it gives the overall score, not
per-task agent scores):

| | public q-score |
|---|---:|
| learned policy only | 38.9 % |
| learned policy + agent on 14 tasks | **44.6 %** |

The 14 routed tasks: what the policy scored on them, and what the agent did. "Base q" is the learned policy (200k
checkpoint, 10 local episodes per task). "Budget" is the official native step budget, which is also the wall budget
in seconds. Numbered layouts are training-split instance ids. "Dev 11" is training instance 11, which we kept for
development runs with the official evaluator. 312/313 are instances held out from practice.

| task | budget | base q | agent evidence before submission |
|---|---:|---:|---|
| attach a camera to a tripod | 5,867 | 0.00 | official evaluator (dev 11)¹: **success** in 2,786 steps; first tries on unseen layouts 88 and 277: success (1,565 and 1,351 steps; 808 and 693 s wall) |
| clean a patio | 18,106 | 0.00 | official evaluator (dev 11)¹: q 0 at the step limit; practice never cleared the whole floor |
| clean a trumpet | 7,960 | 0.00 | first try on unseen layout 278: success, 4,040 steps (4,708 s wall) |
| cook cabbage | 21,217 | 0.00 | practice success from a restored mid-task state (11,344 steps); no fresh full run |
| make cabinet doors | 5,163 | 0.00 | first try on unseen layout 291: success, 3,676 steps (1,921 s wall); layout 207 failed twice first |
| cook brussels sprouts | 23,492 | 0.00 | partial skills only (halving, sheet transfer); no full run |
| unloading the car | 16,985 | 0.05 | layout 261: first try q 0, success after studying the failure (16,175 steps) |
| installing a scanner | 6,387 | 0.05 | first tries on unseen layouts 199 and 55: success (1,975 and 1,771 steps; 581 and 456 s wall) |
| cook a brisket | 11,002 | 0.07 | held-out instances 312 / 313, official evaluator with the frozen context: q 0.33 and **success**; its practice success was over budget |
| installing smoke detectors | 3,853 | 0.10 | official evaluator (dev 11)¹: **success** in 3,465 steps; first tries on unseen layouts 271 and 127: success (2,392 and 2,875 steps) |
| hanging pictures | 3,581 | 0.20 | earlier held-out dev evaluations: 5 of 9 successful; adapted practice runs: 3 successes in a row |
| vacuuming floors | 3,617 | 0.20 | first tries on layouts 188 and 256: q 0; success after practice on 256 (1,452 steps) |
| installing a fax machine | 6,115 | 0.35 | first full try on unseen layout 115: success; then 7 fresh successes in a row on it; official evaluator (dev 11)¹: q 0 (fell while navigating) |
| scrubbing bathroom floor | 4,730 | 0.40 | practice: full run from reset, success in 2,809 steps |

¹ With an earlier version of that task's frozen context; practice continued afterwards. The fax and bathroom-floor
tasks were not on the list of weakest tasks we prioritised from (base q above 0.33); these two were routed on practice
evidence.

"First try on an unseen layout" means: a training instance the practicer had never seen, the first attempt, NOTES
only, with no snapshots, no restores, no practice feedback and no demo study until it finished. Over the final two days
that was **8 successes and 9 failures** across 17 first attempts (failures: pictures 262, cabinet 207, vacuum 188 and
256, car 261 and 211, pies 87, bacon 162, patio 43). These are practice measurements, not leaderboard results. Each
failure then became development data for the learn-from-mistakes loop below.

Cost: an evaluation episode costs roughly **$50-65** in API usage (brisket held-out episodes: $64.30 and $53.44).
Most practice sessions ran under a $1,500 cap; the 14 frozen sessions had spent $44-368 each.

Routing exceptions, stated plainly: patio and brussels sprouts were routed without a full successful run, and fax
with a failed official run, because the policy scores about 0 on the first two and practice was strong on fax.

---

## The practice loop: how the agent learns a task

A practicer is one long Pi session with GPT-6 Astra, bound to one simulator world: a training instance of its task,
never an evaluation instance. It gets the task's BDDL goal, the instruction, the human demonstrations (RGB plus
proprioception and actions) and the cross-task lessons of every earlier practicer. Then it is told what to do in one
paragraph (the full brief is [practice/prompts/PRACTICE-BRIEF.md](practice/prompts/PRACTICE-BRIEF.md)):

> find the hardest, non free space bits... rank the things to practice... start with highest ranked bits, go to it in
> the sim scene, try it, then refer to the proprio + rgb of humans if they're not able to get it, try again, until
> they get it and are able to do it fast... they cannot give up — everything is solvable.

```
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ READ      task pack (instruction, BDDL goal, budget, annotated human demos)                  │
 │           LESSONS.md (cross-task) · prior-practice/<related task>/NOTES.md                   │
 └──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ RANK      the hard, non-free-space bits: grasps, presses, insertions, doors, hand-overs      │
 │           → written to NOTES.md                                                              │
 └──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ DRILL     snapshot just before the bit ──► try ──► s.practice_feedback()  (goal predicates)  │
 │             ▲                                 │                                              │
 │             │      failed a few times?        ▼                                              │
 │             │  ┌─ step through 2-3 human demos of the same annotated segment:                │
 │             │  │  approach · pre-contact · contact · object-changing move · release          │
 │             │  │  tabulate human vs own (hand pose, joints, base, object) in NOTES.md        │
 │             └──┴─ change that difference ── restore snapshot ── try again                    │
 │           works? → examples/<bit>.md: the exact act() calls, key poses, xyz measurements     │
 └──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ FULL RUN  admin_reset → whole task, no restores, inside the native step budget               │
 │           → EVAL PROCEDURE at the top of NOTES.md (what a fresh copy should do)              │
 └──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ NEW LAYOUT  operator stages an unused instance (SETUP.next.json); the agent's own reset      │
 │             switches to it. First attempt is ZERO-SHOT: NOTES only, no snapshots/feedback.   │
 │               pass → WAIT_NEXT_INSTANCE                                                      │
 │               fail → analyse, compare with demos, practise the failing segment on this       │
 │                      layout, one fresh full pass, distil what generalises into NOTES         │
 └──────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
 │ FREEZE    python -m agent.eval.package: session → gzip parts + NOTES/examples/pack hashes    │
 │           → agent/tasks/tasks.json entry (enable it when it beats the policy's q)            │
 └──────────────────────────────────────────────────────────────────────────────────────────────┘
```

What keeps it going. A Pi session ends its turn whenever the model thinks it has reported something. The practice
loop extension ([pi/extensions/practice-loop.ts](pi/extensions/practice-loop.ts)) waits 60 seconds after a normal turn
and sends one fixed continuation prompt, in the same session. It never continues through a hold. A hold is a `STOP` or
`PRACTICE-HOLD` file in the run, a `PRACTICE_HOLD: <reason>` line from the agent, an aborted or failed turn, or a
person typing "stop". The loop never clears a hold. It also asks Astra for short compaction summaries, because
practice sessions run to hundreds of thousands of tokens and compact many times. Notes on disk are what survive a
compaction, which is why the brief insists on writing everything down.

What the agent leaves behind is in [tasks/](tasks/). Every routed task has the practicer's own `NOTES.md` (EVAL
PROCEDURE first), its `examples/` (reproducible sub-skills: exact `act()` sequences, key poses, measurements) and the
public task pack it started from. They are raw working notes, dense and full of tick counts, written by the agent for
the next copy of itself. Cross-task lessons that every new practicer reads first are in
[practice/prompts/LESSONS.md](practice/prompts/LESSONS.md). For example:

> **Inspect cavities, not only outer faces, when a cleaning goal remains false.** Trumpet TRAIN10 looked clean
> externally after many strokes; a central grasp/lift revealed the final black patch inside its bell. ...

> Visual proximity is not native `nextto`: public BEHAVIOR predicate uses both AABB distance and horizontal
> collision-mesh adjacency. In scanner TRAIN10, carried/released placement plus activation repeatedly yielded Q.5;
> a short RGBD-grounded lateral slide achieved Q1 in consecutive full runs ...

(TRAIN10 is training instance 10; Q is the task's q-score, Q.5 meaning half the goal predicates.)

Practice tools exist only in practice. In evaluation the client and the policy server's bridge refuse them:

| call | what it does |
|---|---|
| `admin_reset(case="episode", practice=True)` | fresh copy of the instance's official start state (exact topology + state restore) |
| `snapshot(name)` / `restore(name)` | save/restore the whole scene and controller at an RPC boundary; a restore starts a new attempt |
| `practice_feedback()` | which BDDL goal predicates hold now, and the native q-score |
| `admin_finish()` | end the attempt; returns its feedback |

---

## The evaluation loop: one episode

```
 evaluator                     AgentRoute                        FrozenRuntime / Pi fork
 ─────────                     ──────────                        ───────────────────────
 reset ──────────────────────► new epoch, undecided
 obs #1 (task id, RGB-D) ────► routed task? 1 env? full-res RGB-D?
                               OpenAI preflight (one tiny call)
                               ─────────────────────────────────► copy NOTES/examples/pack (hash-checked)
                                                                  pi --fork <frozen session>
                                                                  reads EVAL-BRIEF.md, task pack, NOTES
                                                                  s.observe()  ◄── image + state of obs #1
                                                                  thinks...
                               waits ≤ 540 s for the first answer
                                                                  s.act(right={"to": [...]}, ...)
 action #1 ◄───────────────── controller tick 1 toward the goal
 obs #2 ─────────────────────► tick 2 ... tick N (goal reached / stalled / capped)
                                                                  ◄── endpoint image + state + act_result
 ...                           agent slow? hold the robot still (same command, base stopped)
                               3 query timeouts in a row, an API error, the cost guard
                               or the wall budget → this episode falls back to the learned policy
 evaluator ends the episode ─► close: stop Pi, close the bridge; the next reset starts a fresh fork
```

- **One fork per episode.** `pi --fork` copies the frozen session into a new session file. The frozen file is never
  modified, and nothing carries over between episodes.
- **Same-session continuation.** If the model ends its turn mid-episode, the runtime resumes the same fork with
  "Episode still running: continue". Only a clean `stop` turn counts; errors and aborts end the agent for that
  episode.
- **The evaluator owns termination.** `s.admin_finish()` cannot end an official episode; it returns "continue".
  There is no reset, no snapshot, no second attempt and no simulator truth, only the official observation.
- **What the agent is told** is [eval/EVAL-BRIEF.md](eval/EVAL-BRIEF.md) and the eval skill
  [pi/skills/behavior-sim-control/SKILL.md](pi/skills/behavior-sim-control/SKILL.md), verbatim as submitted.

---

## What the agent sees and does

Each `observe()` and each `act()` endpoint returns one image and a text state block. The image-delivery extension
([pi/extensions/observation_delivery.ts](pi/extensions/observation_delivery.ts)) attaches the image to the tool result
the model sees, even from inside a codemode script. Without it the agent would be acting blind, so the client
prints a loud warning.

```
 ┌────────────┬──────────────────────────┬────────────┐
 │ left wrist │          head            │ right wrist│   1680 × 720 RGB, native resolutions
 │  480×480   │         720×720          │  480×480   │   (RGBDFullResWrapper); pixel rulers only
 └────────────┴──────────────────────────┴────────────┘
 [obs #014 | act=3f2a91c0 | sim= 52.17s | ... | intent]
   base_odom: rel_xyz rel_yaw vel     (integrated body velocity: uncertain, not world pose)
   torso, torso command
   L/R: rigid TCP (fwd,left,up) · finger positions · grip command · pad start/end · measured pinch
        closing/finger axes · joints q · q_lag · joint-limit margins · commanded q
   diagnosis per arm · execution: requested/executed ticks, stop reason, fault, uncertainty
   steps used / official budget          (practice meter)
```

`s.xyz("head")` returns a 720×720×3 array: the robot-frame position (forward, left, up, metres) of every pixel, from
the native float depth. Images say *what* things are; `xyz` says *where* they are.

`act()` is the only motor command. One call is one full goal:

```python
s.act("Pinch the cornet's central tube",
      right={"to": [0.62, -0.11, 0.93], "grip": 0.0},   # rigid-TCP target in the body frame, close
      left={"grip": 1.0},                               # keep open
      base={"yaw_deg": 10},                             # turn 10° left in place
      max_steps=90)                                     # cap the whole move (≤ 3 s at 30 Hz)
```

```
 act(goal) ─► controller, every native tick (30 Hz):
                read proprioception → one damped-least-squares IK step from the persistent COMMAND
                toward the full goal → slew-limited joint targets (≤ 0.025 rad/tick)
                base: heading-first, ≤ 0.20 m/s, ≤ 0.40 rad/s, velocity-mismatch guard
              until reached · stalled · timeout · caller cap
           ◄─ endpoint image + state + act_result {achieved, per-arm residuals, diagnosis}
```

Commands persist between calls. A target pushed into a surface keeps pushing until it is changed, and relative moves
start from the command, not from the measured, deflected pose. Every endpoint says what was and wasn't achieved.
Pose completion is never reported as a grasp: nothing exposes contact, force or "held object".

---

## What we changed along the way

The harness was rebuilt several times in the ten days before the deadline. Each change below came from a failure we could see in the
recordings.

| change | why | evidence |
|---|---|---|
| **One goal per `act`, closed loop every tick** (replaced open-loop action chunks) | chunks drifted; the agent couldn't tell what had happened | free motion reached at 0.83 mm, base+arm at 0.41 mm; an obstructed move reports `stalled`, not success |
| **Persistent commanded setpoints** and model Jacobians at the commanded configuration | measured-joint anchoring made a pressing hand creep back | a 0.117 rad press lag persisted; releasing to measured joints left 0.003 rad |
| **Native float depth + `xyz()`** with the official camera poses | eyeballed pixel positions missed grasps by centimetres | 3,598 wrist finger-mesh samples: worst XYZ error 1.06 µm against the simulator |
| **Endpoint readback fence** | an `act` endpoint could return the image from *before* the move | act depth now matches an immediate `observe` bit-for-bit |
| **Images attached to every tool result** | images printed to stdout or produced inside codemode never reached the model | delivery tested for nested codemode calls and redirected stdout |
| **Base guard + 0.20 m/s cap** | long base moves fell over (fax: fall before manipulation) | sustained command/velocity mismatch now stops as `stalled` |
| **Practice instead of prompting** | 18 measured autoresearch experiments on one fixed two-book benchmark produced 2 successful episodes; most prompt and harness variants scored 0/3 | a different setting, so not a like-for-like comparison: practicers succeeded on 8 of 17 first tries on unseen layouts of their own task |
| **Practice worker = evaluator physics** | practice on a lighter base and different cameras did not transfer | official `r1pro.yaml`, 250 kg base, the evaluator's head-camera aperture (`horizontal_aperture` 40), full-res RGB-D, official room-filtered scenes |
| **Zero-shot first attempt on new layouts** | repeating a known layout measured memory, not skill | the 17 first tries above are exactly these attempts; `practice_client.py` refuses snapshots/feedback until they finish |
| **Frozen fork per episode + same-session continuation** | a fresh agent with only notes lost the practised context; a turn end stopped the episode | every evaluation episode starts from the practised context |
| **Hold on slow answers, fall back per episode** | a slow model answer must not crash the episode or block the evaluator's 600 s query limit | 3 consecutive timeouts or any error → learned policy for the rest of that episode |

How we got there, including what didn't work (the monitor-and-intervene system, the human-study protocol, the
autoresearch rounds), is in [research/README.md](research/README.md).

---

## Guards: time, money and the robot

```
 wall budget        max_steps × 1 s per episode (official rule), enforced by the runtime watchdog
 query limit        first answer ≤ 540 s, later ≤ 570 s (official: 600 s per query)
 slow answer        hold the robot still; 3 consecutive timeouts → learned policy
 any agent error    learned policy for the rest of the episode; next episode tries the agent again
 cost               Pi cost guard: stops the agent when the session's total cost passes its limit. A fork inherits the
                    practice session's spent cost and saved limit ($1,500 with $145-368 spent for 13 tasks; the
                    $400 default with $44 spent for scrubbing), so the headroom per episode is about $360-1,350.
                    PI_COST_LIMIT only sets the limit of sessions without a saved one.
 API key            every bash call runs with model keys unset; reading /proc/*/environ is refused. This avoids
                    leaking the key into tool output by accident; it is not a sandbox against malicious code.
 startup            server refuses to start if the OpenAI check fails or a frozen context is missing
 no replay          an uncertain action is never re-sent; no resets, retries or snapshots in evaluation
```

---

## Running it

CPU tests (no GPU, no simulator, no API calls; Python 3.11 with numpy, pillow, scipy, msgpack, websockets), from the
repository root:

```bash
python -m unittest agent.eval.test_runtime agent.eval.test_route agent.eval.test_run_episode
for t in agent/control/test_*.py agent/practice/test_*.py; do python "$t" || exit 1; done
npx --yes --package=tsx@4.20.6 tsx agent/pi/test_practice_loop.ts
npx --yes --package=tsx@4.20.6 tsx agent/pi/test_replay_extension.ts
PI_PACKAGE_ROOT=<node_modules/@earendil-works/pi-coding-agent> node agent/pi/test_delivery.mjs
```

**Frozen contexts.** The 14 practice sessions (29-395 MB each, 1.8 GB compressed) are not in git, and they are not
public: the transcripts contain the practice machine's unrelated workspace context. **Without them the agent route
cannot run**, and everything else here can. A cleaned release would ship with a new `tasks.json`. The hashes in the
current one identify exactly the sessions we submitted. With the bundle in `agent/frozen/`:

```bash
python -m agent.eval.frozen                      # reassemble + verify agent/tasks/<task>/session.jsonl
python -m agent.eval.frozen --disable-missing    # no bundle: disable the agent tasks (learned policy only)
```

**Serve.** Pi 1.2.0 on `PATH` (`npm install -g @earendil-works/pi-coding-agent@1.2.0`, Node 22) and `OPENAI_API_KEY`
with access to `gpt-6-astra`:

```bash
uv run hf download IliaLarchenko/BEHAVIOR2026VLA --local-dir models/behavior2026_vla
uv run scripts/serve_b1k.py --agent --policy.config configs/train_b1k_2026.yaml --policy.dir models/behavior2026_vla
python -m agent.eval.serve_agent_only --port 8000     # agent tasks only, no JAX/checkpoint
```

Without `--agent` the same server plays all 100 tasks with the learned policy and needs neither the bundle nor a key.

Run the evaluator with `--env-wrapper omnigibson.eval.wrappers.RGBDFullResWrapper` and one environment per connection
for agent tasks. With the default wrapper, the route logs a red warning and the learned policy plays.

**One episode end to end**, with the agent-only server and the official evaluator (Linux):

```bash
python -m agent.eval.run_episode --full --native-python <evaluator python> --key-file ~/.openai.env \
    --task installing_smoke_detectors --mode train --instance 20 --output runs/smoke-20 --replay
```

The runner's own wall guard defaults to the task's budget plus 30 minutes (`--deadline-seconds`).

`--replay` records the agent's model turns and tool calls (`agent-events.jsonl`) and its robot RPCs
(`robot-events.jsonl`) next to the official JSON and video.

**Practise a new task**: [practice/README.md](practice/README.md).

---

## Code map

```
agent/
├── control/                    ONE robot stack for practice and evaluation
│   ├── sim_client.py           the agent's API: observe / act / xyz (+ practice-only reset, snapshot, feedback)
│   ├── portable_control.py     per-tick controller: arms (DLS IK + nullspace), torso, base guard, odometry
│   ├── official_controller.py  evaluator observation → controller packet → native 23-D action
│   ├── official_policy_server.py  loopback HTTP bridge between sim_client and evaluator steps
│   ├── hybrid_arm_control.py · torso_control.py · joint_action.py · action_validation.py
│   ├── robot_kinematics.py · robot_model.json · rgbd_geometry.py · motion_diagnostics.py
│   ├── static-profile.json     R1Pro cameras and observation layout of the official wrapper
│   └── test_*.py
├── eval/                       one evaluation episode inside the policy server
│   ├── runtime.py              FrozenRuntime: run dir, bridge, `pi --fork`, watchdog, continuation
│   ├── EVAL-BRIEF.md           what the forked agent is told (verbatim)
│   ├── frozen.py               bundle layout; reassemble and verify sessions
│   ├── package.py              freeze a practice session into tasks.json
│   ├── scrub.py                credential scan before packaging
│   ├── replay_recording.py     opt-in recording of robot RPCs
│   ├── serve_agent_only.py · run_episode.py   agent episodes without the VLA
│   └── test_*.py
├── pi/                         what Pi loads
│   ├── extensions/observation_delivery.ts   attach endpoint images to tool results
│   ├── extensions/practice-loop.ts          keep a practicer going; holds
│   ├── extensions/cost-guard.ts · auth-isolation.ts · replay.ts
│   └── skills/behavior-sim-control/SKILL.md (evaluation skill)
├── practice/                   the practice harness
│   ├── worker.py               the practice simulator (official robot config + eval physics)
│   ├── rpc.py · admin.py       observe/act and practice-only jobs through the worker's file queue
│   ├── practice_client.py      holds, budget meter, layout switching, zero-shot fence
│   ├── practice_scene.py · practice_snapshots.py · practice_feedback.py · depth_image.py · ...
│   ├── bin/                    worker.sh · make_run.py · pi_session.sh · live_view.py
│   ├── prompts/                PRACTICE-BRIEF.md · PRACTICER-KICKOFF.md · LESSONS.md
│   └── skill/                  practice skill + full interface reference
├── tasks/
│   ├── tasks.json              the 14 routed tasks: budgets, session + support hashes
│   └── <task>/                 NOTES.md · EVAL-PROCEDURE.md · examples/ · pack/ (public task pack)
└── research/README.md          what we tried before practice, and what we learned
```

---

## Limits

- **Small samples.** Most per-task evidence is one or two runs. First-try transfer was 8 of 17 in practice; the
  official evaluator runs before submission were on dev instance 11, one episode each.
- **Notes are written by the agent.** They are honest about failures but dense, and some coordinates in them are
  specific to the layout they were measured on. The EVAL PROCEDURE tells the forked agent to re-measure everything.
- **Practice sessions differ by task.** Some tasks got a full practice-and-transfer cycle; cabbage, brussels sprouts
  and brisket were routed with partial or over-budget practice because the policy scored about 0 on them anyway.
- **Expensive and slow.** About $50-65 and up to the full wall budget per episode. The cost is in long contexts and
  images, not in output tokens.
- **Simulator only.** Nothing here touches a physical robot. The controller is reactive, not a collision planner.
