# How we got to practice: ten days of trying to make an LLM drive the R1Pro

The final design (practise each task, freeze the session, fork it for every evaluation episode) was the last of
several approaches. This page records the others: what we tried, what we measured, and what each one taught us.
Numbers come from our own runs. They are small samples, and the conditions changed between phases, so they are not a
controlled comparison.

```
 Oct 7  ─ Oct 10   harness v1: Pi + observe/act on one fixed benchmark; autoresearch rounds
 Oct 8  ─ Oct 17   monitor-and-intervene: Sol watches the learned policy, Astra recovers          (Keerti)
 Oct 11 ─ Oct 13   human study: watch the demo, play, then one scored attempt
 Oct 13 ─ Oct 16   controller rebuild: per-tick control, persistent commands, native depth, official adapter
 Oct 15 ─ Oct 17   practice at scale: one practicer per task, unseen-layout transfer, freeze → route 14 tasks
```

## 1. Harness v1 and autoresearch

The first harness gave GPT-6 Astra a native Pi session with two tools, `observe` and `act`, on one fixed benchmark:
put two books into a box from three fixed start states, scored by a hidden simulator scorer. We ran it as autoresearch:
a lead, a researcher and a runner (each a Pi agent) took turns proposing one falsifiable harness change, measuring it on
all three starts and keeping or rejecting it. The instruction for the second round (typos fixed):

> Run autoresearch. Get this thing working, focus on harness simplicity, and root cause analysis on source of errors
> early. Be creative. 20 experiments. Go

Result: 18 measured experiments, 2 genuine full successes (EXP12 start 2 in 561 s, EXP15 start 3 in 716 s); both
failed their paired repeat. Most variants scored 0/3. Things we tried included joint-space targets, action-effect
summaries, self-overlays on the image, axis annotations, sparse deltas, pixel-reach helpers, async observation and
larger images.

What it taught us came from the root-cause analysis, not the score:

- **The earliest divergence was perception of the grasp, not planning.** The agent often closed the gripper when the
  pixels didn't show the book between the jaws. Success followed several realign-and-regrasp attempts. That led to
  native depth with `xyz()`, pad positions in the state block, and "measure, don't eyeball" in every prompt.
- **The tool's semantics mattered more than prompt wording.** Open-loop action chunks, ambiguous completion and stale
  endpoint images produced failures that no prompt could fix. That led to the controller rebuild (section 4).
- **One benchmark, many variants, is the wrong loop for 100 tasks.** It optimised a harness for one scene. It did not
  produce a way for the agent to get better at a task.

## 2. Monitor and intervene (Keerti)

The learned policy stays in control. A GPT-6.1 Sol monitor watches recent observations (all three cameras at 1 FPS
over a 30 s window, reviewed every 10 simulated seconds). When it sees persistent lack of progress, it hands control to
Astra for a bounded recovery (at most 3 interventions of 900 actions each). Then the policy resumes.

- Gift bags, instance 307: policy alone q 1/6. Two monitored runs q 2/3, one with 725 Astra actions ($168), one with
  zero Astra actions ($160). Higher q, but not attributable to the intervention.
- Recovery-v4 with reviewed historical failure comments (tripod and cabinet, 8 instances): all q 0, the same as the
  policy-only controls. Attachment tasks give no partial credit for getting close.

Lesson: the monitor costs money even when it does nothing, and handing back to a policy that can't do the precise part
doesn't finish the task. The agent needs to own the whole episode on tasks where the policy scores zero.

## 3. Human study: watch, play, then score

One Astra session per trial. 300 s watching the human demonstration (RGB plus aligned proprioception), 600 s of free
play in the scene, an exact world reset, then one scored attempt, all in the same conversation.

- The low-effort run reached the full goal *during play* (579.6 s), then failed the scored attempt after the reset.
- A shorter study-then-execute run (69 s of study, one scored attempt) did not reach the goal; it cost $28.87.

Lesson: the agent can learn inside a session, but a short window teaches a lucky trajectory, not a procedure. Learning
has to be written down and tested from fresh resets. That became NOTES.md, `examples/`, and the "one full run from a
fresh reset" rule.

## 4. Controller rebuild

Driven by the failures above (details and numbers in the [main agent README](../README.md#what-we-changed-along-the-way)):

```
 before                                          after
 ──────                                          ─────
 act = short open-loop action chunk              act = one full goal; the controller closes the loop every tick
 measured-joint anchoring (a pressing hand       persistent commanded setpoints; explicit release to measured q
   creeps back)
 RGB only, pixel guesses                         native float depth, xyz() in the robot frame (~1 µm vs simulator)
 act endpoint could show the pre-move image      readback fence: endpoint depth == immediate observe
 images lost inside codemode                     every endpoint image attached to the outer tool result
 base drives until timeout                       heading-first base, 0.20 m/s, velocity-mismatch stall guard
 custom worker interface                         official evaluator adapter: same step function, one action per query
```

The official-evaluator integration smoke (BEHAVIOR 3.9.3, RGBDFullResWrapper) ran 121 native actions in 8.6 s of
wall time with three scripted goals reached. That was plumbing, not task skill. The first model-backed official run
(fax, training instance 11) fell while navigating at 80 s: the long base moves led to the base guard.

## 5. Practice at scale

One practicer per task, each on its own training instance, with practice feedback, snapshots, the human demos and a
shared LESSONS.md. In the last two days: 28 frozen contexts for 27 tasks, then an unseen-layout round (zero-shot first
attempts, then learn-from-mistakes), then routing. We routed 14 tasks: those where the policy scores about zero and
those where the agent's practice beat the policy's q. See [practice/](../practice/) and the [practice loop](../README.md#the-practice-loop-how-the-agent-learns-a-task).

## What we would do next

- **Practise every task, not 27.** The bottleneck was simulator slots and wall-clock time, not the method.
- **Distil.** The practice sessions are a large new source of task-specific demonstrations and corrections for the
  learned policy (per-task LoRA on them is untested).
- **A cheaper model for the easy parts.** Most of an episode is navigation and approach; the expensive model matters
  most at contact.
