# cook_a_brisket

## Official instruction

Take the brisket from the refrigerator, cook it in a frying pan on the burner, and place the cooked brisket on the chopping board.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean7334.995 steps ×1.5, floored: **11002 native30Hz steps** (~366.733sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem cook_a_brisket-0)
    (:domain behavior-1k)

    (:objects
        chopping_board.n.01_1 - chopping_board.n.01
        brisket.n.01_1 - brisket.n.01
        frying_pan.n.01_1 - frying_pan.n.01
        countertop.n.01_1 - countertop.n.01
        electric_refrigerator.n.01_1 - electric_refrigerator.n.01
        oven.n.01_1 - oven.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop chopping_board.n.01_1 countertop.n.01_1) 
        (inside brisket.n.01_1 electric_refrigerator.n.01_1) 
        (not 
            (cooked brisket.n.01_1)
        )
        (ontop frying_pan.n.01_1 countertop.n.01_1)
        (inroom electric_refrigerator.n.01_1 kitchen) 
        (inroom oven.n.01_1 kitchen) 
        (inroom floor.n.01_1 kitchen) 
        (inroom countertop.n.01_1 kitchen)
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (cooked ?brisket.n.01_1) 
            (ontop ?brisket.n.01_1 ?chopping_board.n.01_1)
            (ontop ?frying_pan.n.01_1 ?countertop.n.01_1)
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
