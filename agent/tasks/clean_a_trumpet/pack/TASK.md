# clean_a_trumpet

## Official instruction

In the bedroom, pick up the scrub brush from the desk and scrub the cornet (trumpet) on the desk until it's no longer covered in dust.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean5307.16 steps ×1.5, floored: **7960 native30Hz steps** (~265.333sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem clean_a_trumpet-0)
    (:domain behavior-1k)

    (:objects
        dust.n.01_1 - dust.n.01
        cornet.n.01_1 - cornet.n.01
        scrub_brush.n.01_1 - scrub_brush.n.01
        desk.n.01_1 - desk.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (covered cornet.n.01_1 dust.n.01_1) 
        (ontop scrub_brush.n.01_1 desk.n.01_1) 
        (ontop cornet.n.01_1 desk.n.01_1) 
        (inroom desk.n.01_1 bedroom) 
        (inroom floor.n.01_1 bedroom) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (not 
                (covered ?cornet.n.01_1 ?dust.n.01_1)
            )
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
