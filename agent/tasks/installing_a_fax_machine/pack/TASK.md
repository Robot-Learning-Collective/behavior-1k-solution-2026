# installing_a_fax_machine

## Official instruction

Install the fax machine by placing it on the cubicle desk and turning it on.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean4076.89 steps ×1.5, floored: **6115 native30Hz steps** (~203.833sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem installing_a_fax_machine-0)
    (:domain behavior-1k)

    (:objects
     	facsimile.n.02_1 - facsimile.n.02
    	floor.n.01_1 floor.n.01_2 - floor.n.01
    	carrel.n.02_1 carrel.n.02_* - carrel.n.02
    	agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop facsimile.n.02_1 floor.n.01_1) 
        (not 
            (toggled_on facsimile.n.02_1)
        ) 
        (inroom floor.n.01_1 shared_office)
        (inroom carrel.n.02_1 shared_office) 
        (inroom carrel.n.02_* shared_office) 
        (inroom floor.n.01_2 corridor) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (toggled_on ?facsimile.n.02_1)
            (exists 
                (?carrel.n.02 - carrel.n.02)
                (ontop ?facsimile.n.02_1 ?carrel.n.02)
            )
        )
    )
)

```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
