# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode7419 / TRAIN20

Length201.900s; valid interval[0, 5650]; raw ID370200; `annotations/task-0037/episode_00370200.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 5650] → [[0, 5650]]|188.333|pick up from/wipe hard/place on|[['scrub_brush_86', 'desk_aduafr_0'], ['scrub_brush_86', 'trumpet_87'], ['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86', 'scrub_brush_86', 'scrub_brush_86']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 107] → [[0, 107]]|3.567|move to|[['scrub_brush_86']] / []|
|[376, 1278] → [[376, 1278]]|30.067|pick up from|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|
|[1292, 1875] → [[1292, 1875]]|19.433|hand over|[['scrub_brush_86', 'left', 'right']] / ['scrub_brush_86']|
|[1889, 2078] → [[1889, 2078]]|6.300|move to|[['trumpet_87']] / []|
|[2082, 5136] → [[2082, 5136]]|101.800|wipe hard|[['scrub_brush_86', 'trumpet_87']] / ['scrub_brush_86']|
|[5154, 5650] → [[5154, 5650]]|16.533|place on|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush_86', 'desk_aduafr_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode7420 / TRAIN21

Length215.733s; valid interval[101, 6354]; raw ID370210; `annotations/task-0037/episode_00370210.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[101, 6354] → [[101, 6354]]|208.433|pick up from/wipe hard/place on|[['scrub_brush_86', 'desk_aduafr_0'], ['scrub_brush_86', 'trumpet_87'], ['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86', 'scrub_brush_86', 'scrub_brush_86']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[101, 717] → [[101, 717]]|20.533|move to|[['scrub_brush_86']] / []|
|[717, 1989] → [[717, 1989]]|42.400|pick up from|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|
|[1989, 2682] → [[1989, 2682]]|23.100|hand over|[['scrub_brush_86', 'left', 'right']] / ['scrub_brush_86']|
|[2682, 2715] → [[2682, 2715]]|1.100|move to|[['trumpet_87']] / []|
|[2715, 5790] → [[2715, 5790]]|102.500|wipe hard|[['scrub_brush_86', 'trumpet_87']] / ['scrub_brush_86']|
|[5790, 6354] → [[5790, 6354]]|18.800|place on|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush_86', 'desk_aduafr_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode7421 / TRAIN22

Length159.300s; valid interval[0, 4498]; raw ID370220; `annotations/task-0037/episode_00370220.json`.

### Coarse

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 4498] → [[0, 4498]]|149.933|pick up from/wipe hard/place on|[['scrub_brush_86', 'desk_aduafr_0'], ['scrub_brush_86', 'trumpet_87'], ['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86', 'scrub_brush_86', 'scrub_brush_86']|

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 459] → [[0, 459]]|15.300|move to|[['scrub_brush_86']] / []|
|[800, 1362] → [[800, 1362]]|18.733|pick up from|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|
|[1381, 1878] → [[1381, 1878]]|16.567|hand over|[['scrub_brush_86', 'left', 'right']] / ['scrub_brush_86']|
|[1884, 2016] → [[1884, 2016]]|4.400|move to|[['trumpet_87']] / []|
|[2281, 4268] → [[2281, 4268]]|66.233|wipe hard|[['scrub_brush_86', 'trumpet_87']] / ['scrub_brush_86']|
|[4268, 4498] → [[4268, 4498]]|7.667|place on|[['scrub_brush_86', 'desk_aduafr_0']] / ['scrub_brush_86']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush_86', 'desk_aduafr_0']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → hand over → move to → wipe hard → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
