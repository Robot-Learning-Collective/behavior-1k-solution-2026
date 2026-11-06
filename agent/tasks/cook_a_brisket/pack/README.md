# Cook a brisket — lite task pack

Read **TASK.md**, then **ANNOTATIONS.md**. Required final conditions: brisket cooked; brisket on chopping board; **frying pan returned to countertop**. Fridge closure is not an explicit goal in problem0. Official budget **11002steps / ~366.73sim seconds**. Reference10212 is TRAIN20; compare10213/TRAIN22 and10214/TRAIN23 for alternate approaches. These are public instructions, exact BDDL/init/budget and three ordered annotation sequences, not task-success evidence.

For cooking/ontop/inside/switch semantics, read the BDDL goal in TASK.md; the predicates are BEHAVIOR's own, and in practice `s.practice_feedback()` reports which ones hold. Related experience: the bacon practicer (fridge, pan, pour, cooking), whose notes are in `prior-practice/` if your campaign has them. It used snapshots and is not demonstrated brisket success. Don't reuse its route, robot binding or success claim.

For RGB + human proprio, fetch only what you need from the public dataset `behavior-1k/2026-challenge-demos` (LeRobot v3): the chosen episodes' rows in `data/` (state, action, timestamps) and one camera video in `videos/`, using the episode metadata in `meta/` and the annotation sidecars in `annotations/`. Fetch chosen annotation spans across2–3 demos, not the full task's videos. Position groups at RGB n use row n−1, velocity/commands n−2.

If stuck, compare dense0.2–0.5s human-vs-own observations through approach/contact-candidate/manipulation/release from different episodes, tabulate differences in NOTES and change the approach. Continue trying fresh episodes/new instances even before Q1. No private reasoning, held-out rollout data, live object/contact/scorer state or rewards are included here.
