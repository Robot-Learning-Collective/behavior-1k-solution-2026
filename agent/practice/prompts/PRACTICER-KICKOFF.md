# Practicer kickoff: {{TASK}}

You are the practice agent for BEHAVIOR task **{{TASK}}** on training instance {{INSTANCE}} (scene `{{SCENE}}`).
Your run directory is `{{RUN_DIR}}`. In every bash/Python call: `export BEHAVIOR_SIM_RUN_DIR={{RUN_DIR}}`.

Read, in this order, before any simulator action:

1. `{{CAMPAIGN}}/PRACTICE-BRIEF.md`: your instructions (workflow, notes, never give up).
2. `{{CAMPAIGN}}/LESSONS.md`: what other practicers already learned. Use it.
3. This run's `SETUP.json`, the skill `behavior-sim-control` (`SKILL.md` and `references/interface.md`) and the public
   task pack `{{CAMPAIGN}}/task_pack/{{TASK}}/README.md`. Use only this run's `sim_client.py`.

The native step budget is **{{BUDGET}} steps** ({{BUDGET}} wall seconds in evaluation); aim to finish well inside it.
New attempts: `s.admin_reset(case='episode', attempt_name=<name>, practice=True, unbounded_practice=True)`.
Write `NOTES.md` and `examples/` in your run directory.
