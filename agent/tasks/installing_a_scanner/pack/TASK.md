# installing_a_scanner

## Official instruction

Install the scanner by turning it on and leaving it on the desk near the laptop.

Source: HF `meta/tasks.jsonl` at `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2` (not a generated paraphrase).

## Official step budget

Human mean4258.535 steps ×1.5, floored: **6387 native30Hz steps** (~212.900sim s). Native evaluator owns termination; current terminal-step convention can report cap+1. The assigned evaluator/runner supplies wall/query deadlines; these are separate from simulated duration. Continue until evaluator termination, user stop or genuine safety/runtime boundary.

## Exact installed problem0.bddl: objects, init and goal

```lisp
(define (problem installing_a_scanner-0)
    (:domain behavior-1k)

    (:objects
     	scanner.n.02_1 - scanner.n.02
        laptop.n.01_1 - laptop.n.01
    	table.n.02_1 - table.n.02
    	floor.n.01_1 - floor.n.01
    	agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop scanner.n.02_1 table.n.02_1)
        (not 
            (toggled_on scanner.n.02_1)
        )
        (ontop laptop.n.01_1 table.n.02_1)
        (inroom table.n.02_1 private_office) 
        (inroom floor.n.01_1 private_office) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (toggled_on ?scanner.n.02_1) 
            (nextto ?scanner.n.02_1 ?laptop.n.01_1)
        )
    )
)
```

Public init facts define task relations, not privileged coordinates in the new evaluation world. Measure fresh RGBD; action completion is not goal success.
