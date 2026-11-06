# unloading_the_car

## Official instruction

Open the car, take out the briefcase and satchel, and place them on the floor outside the car.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean11323.43 steps ×1.5, floored: **16985 native30Hz steps** (~566.167sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem unloading_the_car-0)
    (:domain behavior-1k)

    (:objects
        car.n.01_1 - car.n.01
        floor.n.01_1 - floor.n.01
        briefcase.n.01_1 - briefcase.n.01
        satchel.n.01_1 - satchel.n.01
        sofa.n.01_1 - sofa.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (inroom car.n.01_1 garage)
        (inside briefcase.n.01_1 car.n.01_1) 
        (inside satchel.n.01_1 car.n.01_1) 
        (inroom sofa.n.01_1 living_room)
        (inroom floor.n.01_1 garage) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (forall 
                (?briefcase.n.01 - briefcase.n.01)
                (nextto ?briefcase.n.01 ?sofa.n.01_1)
            )
            (forall
                (?satchel.n.01 - satchel.n.01)
                (nextto ?satchel.n.01 ?sofa.n.01_1)
            )
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
