# Practice harness

How to make the agent practise a BEHAVIOR task, the way the 14 routed tasks were practised. The concepts are in the
[agent README](../README.md#the-practice-loop-how-the-agent-learns-a-task); this page is the how-to.

```
  bin/worker.sh ───────► worker.py (Isaac Sim, one training instance, 30 Hz)
                            ▲  file queue: <PRACTICE_HOME>/runtime/<run>/queue
                            │  rpc.py (observe/act) · admin.py (reset/finish/snapshot/restore/feedback)
  bin/make_run.py ──► run dir: SETUP.json · sim_client.py → practice_client.py → agent/control/sim_client.py
                            ▲
  bin/pi_session.sh ──► Pi + GPT-6 Astra, cwd = campaign, extensions:
                         observation_delivery · practice-loop · cost-guard · auth-isolation
                         reads PRACTICER-KICKOFF.md → PRACTICE-BRIEF.md → LESSONS.md → skill → task pack
                         writes NOTES.md · examples/ · appends LESSONS.md
  python -m agent.eval.package ──► agent/tasks/tasks.json (+ agent/frozen bundle)
```

## Requirements

- A Linux box with one NVIDIA GPU (we used RTX PRO 6000 96 GB and H100 80 GB), with the BEHAVIOR-1K v3.9.3 stack
  (Isaac Sim 5.1, OmniGibson) installed as for the official evaluator, and the 2026 task instances and assets.
- Node 22 and Pi 1.2.0 (`npm install -g @earendil-works/pi-coding-agent@1.2.0`), an OpenAI key with `gpt-6-astra`
  (or a ChatGPT subscription through `openai-codex/gpt-6-astra`), and tmux.
- `python3` with NumPy, Pillow and SciPy for the agent's own scripts.
- The task's public pack and its human demonstrations from `behavior-1k/2026-challenge-demos`. Packs for the 14
  routed tasks are in `agent/tasks/<task>/pack/` (the dense keyframe/proprio files of the camera and pictures packs
  travel with the frozen bundle). **The pack builder is not included**: for another task, write the pack by hand in
  the same format. `TASK.md` holds the official instruction, the installed BDDL problem and the step budget.
  `ANNOTATIONS.md` holds the coarse and fine annotations of three demos, with frame ranges and durations. `README.md`
  says what to read first. Put it in `.practice/campaign/task_pack/<task>/`.

## One practice run

```bash
export SIM_PY=/path/to/isaac-sim-env/bin/python OMNIGIBSON_DATA_PATH=/path/to/behavior/datasets
export OPENAI_API_KEY=...                          # only Pi's model process sees it

agent/practice/bin/worker.sh clean_a_trumpet 20 trumpet-01        # boots the simulator (2-10 min)
#   wait for .practice/runtime/trumpet-01/queue/ready.json
agent/practice/bin/make_run.py clean_a_trumpet 20 trumpet-01      # campaign + run directory
tmux new -s trumpet 'agent/practice/bin/pi_session.sh trumpet-01' # the practicer; re-run to resume
agent/practice/bin/live_view.py 8765                              # what it sees, on localhost:8765
```

The practicer reads its kickoff and works on its own. The practice loop continues it after every turn. To stop it,
`touch .practice/campaign/runs/trumpet-01/STOP`, or type `stop`. It stops on its own (writing `PRACTICE-HOLD`) when
something is really broken. Delete the hold file and send a message to resume the same session.

Useful files in the run directory:

| file | what |
|---|---|
| `NOTES.md` | the practicer's notes; the **EVAL PROCEDURE** at the top is what the eval fork follows |
| `examples/` | one file per success: exact `act()` calls, key poses, measurements |
| `practicer-events.jsonl` | content-free log: turns, tool calls, simulator calls with sim time and ticks |
| `control-action-results.jsonl` | every motion's result |
| `PRACTICE-HOLD`, `STOP` | holds; the loop and the client both refuse to act |

## A new layout (transfer test)

Boot a second worker on an unused instance and stage it into the existing run. The practicer keeps its session, and its
own next `admin_reset` switches worlds. The first attempt is zero-shot: the client refuses snapshots, restores and
practice feedback until `admin_finish`.

```bash
agent/practice/bin/worker.sh clean_a_trumpet 278 trumpet-278
agent/practice/bin/make_run.py clean_a_trumpet 278 trumpet-01 --next trumpet-278
# tell the practicer (or let the loop do it) that a new layout is staged
```

When it writes `WAIT_NEXT_INSTANCE` into `PRACTICE-HOLD`, it has finished with that layout.

## Freeze and route

```bash
python -m agent.eval.package --task cook_bacon --task-id 46 --max-steps 11519 \
    --session .practice/campaign/runs/bacon-01/sessions/<session>.jsonl \
    --run-dir .practice/campaign/runs/bacon-01 --pack .practice/campaign/task_pack/cook_bacon \
    --env-file ~/.openai.env
```

To re-freeze one of the 14 routed tasks, first remove its entry from `tasks.json`, its `agent/tasks/<task>/` directory
and its parts in `agent/frozen/` (`package.py` refuses to overwrite), and pass the campaign's copy of the pack
(`--pack .practice/campaign/task_pack/<task>`).

This refuses a session containing the API key or credential-shaped text, splits it into gzip parts in
`agent/frozen/`, copies NOTES, examples and pack, and adds a **disabled** entry to `agent/tasks/tasks.json`. Then:

```bash
# set "enabled": true for the task in agent/tasks/tasks.json, then assemble + verify its session.jsonl
# (--disable-missing also disables routed tasks whose sessions you don't have, e.g. the unpublished 14)
python -m agent.eval.frozen --disable-missing
PI_PACKAGE_ROOT=$(npm root -g)/@earendil-works/pi-coding-agent node agent/pi/test_forks.mjs cook_bacon
```

Keep it enabled only if the agent beats the policy on that task (or the policy scores about zero). The credential
scan does **not** check a transcript for private context (paths, hosts, other projects the session read). Review a
session before you publish it.

## Notes from running ~30 practicers

- Start a practicer from a related task's session (`FORK_FROM=<session.jsonl>`) when the skills overlap: the brisket
  practicer started from the bacon practicer (fridge, pan, pour, heat).
- Keep the evaluator's step budget in front of the agent (the state block's meter). Practice is unbounded, but an
  over-budget success is not an evaluation success.
- One full run from a fresh reset is enough before moving to a new layout. Repeating a known layout teaches it the
  layout, not the task.
- Watch `practicer-events.jsonl`, not the screen. A model response is not progress; `sim_call` entries are.
