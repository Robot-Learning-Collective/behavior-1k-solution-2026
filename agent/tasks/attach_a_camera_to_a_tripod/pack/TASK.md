# attach_a_camera_to_a_tripod

## Official instruction

Attach the digital camera to the camera tripod in the bedroom.

## Official native budget

Human mean 3911.575 steps; floor(mean × 1.5) = **5867 steps** at30Hz (~195.567sim s). Native evaluator termination is authoritative; its current terminal-step convention can report cap+1. Episode wall allowance=5867s; per-query limit600s; constructor time excluded. No early actor finish.

## Installed problem0.bddl — exact public objects, init and goal

```lisp
(define (problem attach_a_camera_to_a_tripod-0)
    (:domain behavior-1k)

    (:objects
        digital_camera.n.01_1 - digital_camera.n.01
        camera_tripod.n.01_1 - camera_tripod.n.01
        floor.n.01_1 - floor.n.01
        agent.n.01_1 - agent.n.01
    )
    
    (:init 
        (ontop digital_camera.n.01_1 floor.n.01_1)
        (ontop camera_tripod.n.01_1 floor.n.01_1)
        (inroom floor.n.01_1 bedroom) 
        (ontop agent.n.01_1 floor.n.01_1)
    )
    
    (:goal 
        (and 
            (attached ?digital_camera.n.01_1 ?camera_tripod.n.01_1)
        )
    )
)
```

A reached TCP target, jaw opening, or visual proximity does not establish task success. Verify visible object changes, retention/support and safe withdrawal. Init facts describe the task, not exact poses in your evaluation world.
