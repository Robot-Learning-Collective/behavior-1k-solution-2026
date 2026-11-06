# scrubbing_bathroom_floor

## Official instruction

Use the scrub brush to scrub the bathroom floor until the floor is clean.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean3153.83 steps ×1.5, floored: **4730 native30Hz steps** (~157.667sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem scrubbing_bathroom_floor-0)
    (:domain behavior-1k)

    (:objects
        dirt.n.02_1 - dirt.n.02
        floor.n.01_1 - floor.n.01
        scrub_brush.n.01_1 - scrub_brush.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (covered floor.n.01_1 dirt.n.02_1) 
        (ontop scrub_brush.n.01_1 floor.n.01_1) 
        (inroom floor.n.01_1 bathroom) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (not 
                (covered ?floor.n.01_1 ?dirt.n.02_1)
            )
        )
    )
)

```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
