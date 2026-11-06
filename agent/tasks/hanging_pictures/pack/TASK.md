# hanging_pictures

## Official instruction

Pick up the poster from the kitchen countertop and hang it on one of the wall nails in the kitchen.

## Official native budget

Human mean 2387.415 steps; floor(mean × 1.5) = **3581 steps** at30Hz (~119.367sim s). Native evaluator termination is authoritative; its current terminal-step convention can report cap+1. Episode wall allowance=3581s; per-query limit600s; constructor time excluded. No early actor finish.

## Installed problem0.bddl — exact public objects, init and goal

```lisp
(define (problem hanging_pictures-0)
    (:domain behavior-1k)

    (:objects
        poster.n.01_1 - poster.n.01
        floor.n.01_1 - floor.n.01
        countertop.n.01_1 - countertop.n.01
        wall_nail.n.01_1 wall_nail.n.01_* - wall_nail.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop poster.n.01_1 countertop.n.01_1)
        (inroom floor.n.01_1 kitchen)
        (inroom countertop.n.01_1 kitchen)
        (inroom wall_nail.n.01_1 kitchen)
        (inroom wall_nail.n.01_* kitchen)
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (exists
                (?wall_nail.n.01 - wall_nail.n.01)
                (attached ?poster.n.01_1 ?wall_nail.n.01)
            )
        )
    )
)
```

A reached TCP target, jaw opening, or visual proximity does not establish task success. Verify visible object changes, retention/support and safe withdrawal. Init facts describe the task, not exact poses in your evaluation world.
