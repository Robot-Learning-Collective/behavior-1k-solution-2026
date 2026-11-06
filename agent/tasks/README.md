# What the agent learned, per task

One directory per routed task, written by that task's practicer during practice and frozen with its session:

```
<task>/
├── NOTES.md            the practicer's notes; EVAL PROCEDURE at the top is what the evaluation fork follows
├── EVAL-PROCEDURE.md   (some tasks) the same procedure as a separate file
├── examples/           one file per practised success: act() sequences, key poses, xyz measurements, outcomes
└── pack/               the public task pack it started from: instruction, BDDL goal, budget, annotated demos
```

`tasks.json` lists the routed tasks with their official step budget, the SHA-256 and gzip parts of each frozen
session, and the hash of every support file. Files listed under `"bundle"` (recorded trajectories, keyframes) are too
large for git and travel with the frozen sessions ([eval/frozen.py](../eval/frozen.py)).

The notes are raw working notes, dense with tick counts and attempt ids ("TRAIN127" is training instance 127; "Q1" a
full q-score). They mention receipts, observation images, files and infrastructure of the practice machines that are
not in this repository. Home-directory paths, host and pod names were replaced by placeholders such as
`<observation-cache>`; nothing else was edited.

| task | id | budget (steps) | files |
|---|---:|---:|---|
| `attach_a_camera_to_a_tripod` | 35 | 5,867 | [NOTES](attach_a_camera_to_a_tripod/NOTES.md) · 13 examples · [pack](attach_a_camera_to_a_tripod/pack/README.md) |
| `clean_a_patio` | 36 | 18,106 | [NOTES](clean_a_patio/NOTES.md) · 22 examples · [pack](clean_a_patio/pack/README.md) |
| `clean_a_trumpet` | 37 | 7,960 | [NOTES](clean_a_trumpet/NOTES.md) · 10 examples · [pack](clean_a_trumpet/pack/README.md) |
| `cook_cabbage` | 41 | 21,217 | [NOTES](cook_cabbage/NOTES.md) · 13 examples · [pack](cook_cabbage/pack/README.md) |
| `make_cabinet_doors` | 78 | 5,163 | [NOTES](make_cabinet_doors/NOTES.md) · 17 examples · [pack](make_cabinet_doors/pack/README.md) |
| `cook_brussels_sprouts` | 95 | 23,492 | [NOTES](cook_brussels_sprouts/NOTES.md) · 15 examples · [pack](cook_brussels_sprouts/pack/README.md) |
| `unloading_the_car` | 65 | 16,985 | [NOTES](unloading_the_car/NOTES.md) · [EVAL-PROCEDURE](unloading_the_car/EVAL-PROCEDURE.md) · 9 examples · [pack](unloading_the_car/pack/README.md) |
| `installing_a_scanner` | 92 | 6,387 | [NOTES](installing_a_scanner/NOTES.md) · 52 examples · [pack](installing_a_scanner/pack/README.md) |
| `cook_a_brisket` | 51 | 11,002 | [NOTES](cook_a_brisket/NOTES.md) · [EVAL-PROCEDURE](cook_a_brisket/EVAL-PROCEDURE.md) · 7 examples · [pack](cook_a_brisket/pack/README.md) |
| `installing_smoke_detectors` | 63 | 3,853 | [NOTES](installing_smoke_detectors/NOTES.md) · 19 examples · [pack](installing_smoke_detectors/pack/README.md) |
| `hanging_pictures` | 34 | 3,581 | [NOTES](hanging_pictures/NOTES.md) · 81 examples · [pack](hanging_pictures/pack/README.md) |
| `vacuuming_floors` | 69 | 3,617 | [NOTES](vacuuming_floors/NOTES.md) · [EVAL-PROCEDURE](vacuuming_floors/EVAL-PROCEDURE.md) · 5 examples · [pack](vacuuming_floors/pack/README.md) |
| `installing_a_fax_machine` | 89 | 6,115 | [NOTES](installing_a_fax_machine/NOTES.md) · 45 examples · [pack](installing_a_fax_machine/pack/README.md) |
| `scrubbing_bathroom_floor` | 60 | 4,730 | [NOTES](scrubbing_bathroom_floor/NOTES.md) · 1 example · [pack](scrubbing_bathroom_floor/pack/README.md) |
