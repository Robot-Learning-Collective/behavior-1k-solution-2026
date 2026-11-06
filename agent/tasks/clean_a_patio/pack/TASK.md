# clean_a_patio

## Official instruction

Pick up the broom in the garden and sweep the mud off the patio floor until the floor is no longer covered in mud.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean12070.81 steps ×1.5, floored: **18106 native30Hz steps** (~603.533sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem clean_a_patio-0)
    (:domain behavior-1k)

    (:objects
        mud.n.03_1 - mud.n.03
        broom.n.01_1 - broom.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (covered floor.n.01_1 mud.n.03_1) 
        (ontop broom.n.01_1 floor.n.01_1) 
        (inroom floor.n.01_1 garden) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (not 
                (covered ?floor.n.01_1 ?mud.n.03_1)
            ) 
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
