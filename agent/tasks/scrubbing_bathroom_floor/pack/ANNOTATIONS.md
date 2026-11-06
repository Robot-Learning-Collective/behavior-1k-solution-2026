# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode12010 / TRAIN20

Length86.767s; valid interval[0, 2603]; raw ID600200; `annotations/task-0060/episode_00600200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 420] → [[0, 420]]|14.000|move to|[['scrub_brush']] / []|
|[420, 750] → [[420, 750]]|11.000|pick up from|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[750, 990] → [[750, 990]]|8.000|hand over|[['scrub_brush']] / ['scrub_brush']|
|[990, 1230] → [[990, 1230]]|8.000|move to|[['floors']] / []|
|[1230, 1650] → [[1230, 1650]]|14.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[1650, 2220] → [[1650, 2220]]|19.000|move to|[['floors']] / []|
|[2220, 2580] → [[2220, 2580]]|12.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode12011 / TRAIN21

Length92.300s; valid interval[0, 2769]; raw ID600210; `annotations/task-0060/episode_00600210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 240] → [[0, 240]]|8.000|move to|[['scrub_brush']] / []|
|[240, 690] → [[240, 690]]|15.000|pick up from|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[690, 840] → [[690, 840]]|5.000|hand over|[['scrub_brush']] / ['scrub_brush']|
|[840, 1260] → [[840, 1260]]|14.000|move to|[['floors']] / []|
|[1260, 1650] → [[1260, 1650]]|13.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[1650, 1950] → [[1650, 1950]]|10.000|move to|[['floors']] / []|
|[1950, 2250] → [[1950, 2250]]|10.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[2250, 2460] → [[2250, 2460]]|7.000|move to|[['floors']] / []|
|[2460, 2760] → [[2460, 2760]]|10.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode12012 / TRAIN22

Length99.300s; valid interval[0, 2979]; raw ID600220; `annotations/task-0060/episode_00600220.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 420] → [[0, 420]]|14.000|move to|[['scrub_brush']] / []|
|[420, 1020] → [[420, 1020]]|20.000|pick up from|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[1020, 1170] → [[1020, 1170]]|5.000|hand over|[['scrub_brush']] / ['scrub_brush']|
|[1170, 1770] → [[1170, 1770]]|20.000|move to|[['floors']] / []|
|[1770, 2070] → [[1770, 2070]]|10.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[2070, 2220] → [[2070, 2220]]|5.000|move to|[['floors']] / []|
|[2220, 2490] → [[2220, 2490]]|9.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|
|[2490, 2670] → [[2490, 2670]]|6.000|move to|[['floors']] / []|
|[2670, 2970] → [[2670, 2970]]|10.000|wipe hard|[['scrub_brush', 'floors']] / ['scrub_brush']|

First annotated manipulation: **pick up from**, objects `[['scrub_brush', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → hand over → move to → wipe hard → move to → wipe hard**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
