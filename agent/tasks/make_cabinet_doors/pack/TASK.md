# make_cabinet_doors

## Official instruction

Attach the cabinet door to the cabinet base.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean3442.525 steps ×1.5, floored: **5163 native30Hz steps** (~172.100sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem make_cabinet_doors-0)
    (:domain behavior-1k)

    (:objects
        cabinet_base.n.01_1 - cabinet_base.n.01
        cabinet_door.n.01_1 - cabinet_door.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (inroom floor.n.01_1 living_room) 
        (ontop cabinet_base.n.01_1 floor.n.01_1) 
        (ontop cabinet_door.n.01_1 floor.n.01_1) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (attached ?cabinet_door.n.01_1 ?cabinet_base.n.01_1)
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
