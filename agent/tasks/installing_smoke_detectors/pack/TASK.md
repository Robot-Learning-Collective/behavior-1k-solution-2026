# installing_smoke_detectors

## Official instruction

Attach the two smoke detectors to the wall nails.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean2568.77 steps ×1.5, floored: **3853 native30Hz steps** (~128.433sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem installing_smoke_detectors-0)
    (:domain behavior-1k)

    (:objects
        wall_nail.n.01_1 - wall_nail.n.01
        floor.n.01_1 - floor.n.01
        table.n.02_1 - table.n.02
        fire_alarm.n.02_1 - fire_alarm.n.02
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop fire_alarm.n.02_1 table.n.02_1) 
        (inroom wall_nail.n.01_1 living_room)
        (inroom table.n.02_1 living_room)
        (inroom floor.n.01_1 living_room)
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (attached fire_alarm.n.02_1 wall_nail.n.01_1)
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
