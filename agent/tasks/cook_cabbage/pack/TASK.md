# cook_cabbage

## Official instruction

From the kitchen refrigerator, take the cabbage and the chili, dice them on the chopping board with the knife, cook the diced cabbage and diced chili in the frying pan on the stove, and leave the cooked, diced cabbage and cooked, diced chili in the frying pan.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean14144.81 steps ×1.5, floored: **21217 native30Hz steps** (~707.233sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem cook_cabbage-0)
    (:domain behavior-1k)

    (:objects
        head_cabbage.n.02_1 - head_cabbage.n.02
        cooked__diced__chili.n.01_1 - cooked__diced__chili.n.01
        cooked__diced__head_cabbage.n.01_1 - cooked__diced__head_cabbage.n.01
        electric_refrigerator.n.01_1 - electric_refrigerator.n.01
        chili.n.02_1 - chili.n.02
        chopping_board.n.01_1 - chopping_board.n.01
        carving_knife.n.01_1 - carving_knife.n.01
        frying_pan.n.01_1 - frying_pan.n.01
        plate.n.04_1 - plate.n.04
        stove.n.01_1 - stove.n.01
        countertop.n.01_1 - countertop.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (inside head_cabbage.n.02_1 electric_refrigerator.n.01_1)
        (ontop frying_pan.n.01_1 countertop.n.01_1) 
        (ontop plate.n.04_1 countertop.n.01_1) 
        (inside chili.n.02_1 electric_refrigerator.n.01_1) 
        (not 
            (cooked head_cabbage.n.02_1)
        ) 
        (ontop chopping_board.n.01_1 countertop.n.01_1)
        (ontop carving_knife.n.01_1 countertop.n.01_1)
        (future cooked__diced__chili.n.01_1)
        (inroom electric_refrigerator.n.01_1 kitchen) 
        (inroom stove.n.01_1 kitchen) 
        (inroom floor.n.01_1 kitchen) 
        (inroom countertop.n.01_1 kitchen)
        (future cooked__diced__head_cabbage.n.01_1)
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (real ?cooked__diced__head_cabbage.n.01_1)
            (real ?cooked__diced__chili.n.01_1)
            (contains ?frying_pan.n.01_1 ?cooked__diced__head_cabbage.n.01_1)
            (contains ?frying_pan.n.01_1 ?cooked__diced__chili.n.01_1) 
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
