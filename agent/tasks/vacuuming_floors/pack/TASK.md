# vacuuming_floors

## Official instruction

Use the vacuum to clean the dirty floor until the floor is no longer covered in dirt.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean2411.785 steps ×1.5, floored: **3617 native30Hz steps** (~120.567sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem vacuuming_floors-0)
    (:domain behavior-1k)

    (:objects
        dust.n.01_1 - dust.n.01
     	floor.n.01_1 - floor.n.01
    	vacuum.n.04_1 - vacuum.n.04
    	agent.n.01_1 - agent.n.01
    )

    (:init
        (covered floor.n.01_1 dust.n.01_1)
        (ontop vacuum.n.04_1 floor.n.01_1)
        (inroom floor.n.01_1 bedroom)
        (ontop agent.n.01_1 floor.n.01_1)
    )

    (:goal
        (and
            (not
                (covered ?floor.n.01_1 ?dust.n.01_1)
            )
        )
    )
)

```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
