# Submission image

One container serves all 100 tasks. For every episode it uses exactly one of two policies, chosen by the `task_id`
in the first observation:

```
evaluator ── policy server (this container) ┬─ 14 agent tasks → GPT-6 Astra (OpenAI API) → controller in the container
                                            └─ other 86 tasks → learned π0.5-based policy (checkpoint in the image, GPU)
```

The learned policy also plays an agent task's episode if the agent fails during it (API error, three consecutive slow
answers, its wall or cost limit). See [agent/README.md](../agent/README.md).

What we submitted was `ilialarchenko/behavior:step199999-agent-r5`
(`sha256:5b4fbe637d1de02ea48f945339a96a1c1d91387d7e5e96939aa5bb3cccc89b20`). That image is private and will not be
published: it contains the raw frozen sessions and our OpenAI key (since revoked). It was built from the equivalent
Dockerfile on our development branch. This version takes the key at runtime.

## Build

The agent tasks need the frozen-context bundle in `agent/frozen/`, which is not public (see
[agent/README.md](../agent/README.md#running-it)). Without it, build with `AGENT_BUNDLE=optional`. The agent tasks are
then disabled and the image serves the learned policy for every task.

```bash
git submodule update --init openpi BEHAVIOR-1K
git -C BEHAVIOR-1K fetch origin tag v3.9.3-post2
# without the bundle (learned policy for every task):
B1K_DATA=/path/to/behavior/datasets AGENT_BUNDLE=optional submission/build.sh /path/to/checkpoint/step_dir rlc-behavior2026:latest
# with the bundle in agent/frozen/:
B1K_DATA=/path/to/behavior/datasets submission/build.sh /path/to/checkpoint/step_dir rlc-behavior2026:latest
```

`build.sh` stages BEHAVIOR-1K and openpi from their pinned commits with `git archive` (local edits never reach the
image) and copies only the checkpoint's inference files. With the bundle, the `agent-check` stage builds a
checkpoint-free image that runs the agent tests and serves agent tasks only:
`docker build --target agent-check -f submission/Dockerfile -t rlc-agent-check .`

## Run

```bash
# /private/openai.env: chmod 600, one line OPENAI_API_KEY=<key with gpt-6-astra access>
docker run --rm --gpus '"device=0"' -p 8000:8000 --env-file /private/openai.env rlc-behavior2026:latest
docker run --rm --gpus '"device=0"' -p 8000:8000 rlc-behavior2026:latest --offline-only   # learned policy only
```

At start the container checks the OpenAI key and API with one tiny request, and checks that every routed task's frozen
context is present. If either check fails it prints a red `STARTUP FAILED` and exits without serving. It is ready
after the policy loads (1-3 min).

## Evaluator settings the agent needs

```bash
python -m omnigibson.eval.eval --task-name <TASK> --mode <MODE> --instance-indices <I> \
  --num-envs 1 --num-rollouts 1 --host <POLICY_HOST> --port 8000 \
  --env-wrapper omnigibson.eval.wrappers.RGBDFullResWrapper --output-dir <OUT> --write-video
```

| setting | value | why |
|---|---|---|
| `--env-wrapper` | `RGBDFullResWrapper`, for all tasks | the agent needs full-resolution RGB (720² head, 480² wrists) and depth; with another wrapper it logs `WRONG OBSERVATIONS` and the learned policy plays |
| `--num-envs` | `1`, one evaluator process per container | agent episodes pause the simulation for seconds to minutes while the model plans; batched environments would all wait for the slowest |
| `--num-rollouts` | `1`, one instance per process | a fresh simulation per episode; the instance loader does not reset objects outside the task scope |
| `--replay-action-chunk-size` | unset | the agent decides every step from the newest observation |

## Timing and resources

- Learned-policy tasks: about 6.5 GB of GPU memory and 5 GB of RAM per container. The first model call compiles
  (10-40 s depending on the GPU); after that a call takes 0.1-4 s, once every 13 steps.
- Agent tasks: the first step of an episode takes longest (the fork reads its notes). Every request is answered within
  570 s (540 s for the first, inside the evaluator's 600 s limit); if the agent is still planning, the container sends
  a hold action and keeps waiting. An agent episode is bounded by one wall second per allowed step, so long tasks can
  take hours (`cook_brussels_sprouts`: up to about 6.5 h). It costs roughly $50-65 in API usage.
- Results are not deterministic (flow-matching sampling, LLM sampling, rendering): the same episode can succeed and
  fail in different runs.
