# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode17814 / TRAIN20

Length80.133s; valid interval[0, 2404]; raw ID890200; `annotations/task-0089/episode_00890200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 120] → [[0, 120]]|4.000|move to|[['facsimile']] / []|
|[120, 643] → [[120, 643]]|17.433|pick up from|[['facsimile', 'floors']] / ['facsimile']|
|[643, 790] → [[643, 790]]|4.900|turn on switch|[['facsimile']] / ['facsimile']|
|[790, 1850] → [[790, 1850]]|35.333|move to|[['chair']] / []|
|[1850, 2074] → [[1850, 2074]]|7.467|push to|[['chair', 'cubicle']] / ['chair']|
|[2074, 2404] → [[2074, 2404]]|11.000|place on|[['facsimile', 'cubicle']] / ['facsimile']|

First annotated manipulation: **pick up from**, objects `[['facsimile', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode17815 / TRAIN21

Length153.100s; valid interval[0, 4593]; raw ID890210; `annotations/task-0089/episode_00890210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 1820] → [[0, 1820]]|60.667|move to|[['facsimile']] / []|
|[1820, 2634] → [[1820, 2634]]|27.133|pick up from|[['facsimile', 'floors']] / ['facsimile']|
|[2634, 2940] → [[2634, 2940]]|10.200|turn on switch|[['facsimile']] / ['facsimile']|
|[2940, 3750] → [[2940, 3750]]|27.000|move to|[['chair']] / []|
|[3750, 3943] → [[3750, 3943]]|6.433|push to|[['chair', 'cubicle']] / ['chair']|
|[3943, 4593] → [[3943, 4593]]|21.667|place on|[['facsimile', 'cubicle']] / ['facsimile']|

First annotated manipulation: **pick up from**, objects `[['facsimile', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode17816 / TRAIN22

Length91.000s; valid interval[0, 2730]; raw ID890220; `annotations/task-0089/episode_00890220.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 240] → [[0, 240]]|8.000|move to|[['facsimile']] / []|
|[240, 878] → [[240, 878]]|21.267|pick up from|[['facsimile', 'floors']] / ['facsimile']|
|[878, 1176] → [[878, 1176]]|9.933|turn on switch|[['facsimile']] / ['facsimile']|
|[1176, 2040] → [[1176, 2040]]|28.800|move to|[['cubicle']] / []|
|[2040, 2220] → [[2040, 2220]]|6.000|push to|[['chair', 'cubicle']] / ['chair']|
|[2220, 2730] → [[2220, 2730]]|17.000|place on|[['facsimile', 'cubicle']] / ['facsimile']|

First annotated manipulation: **pick up from**, objects `[['facsimile', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → turn on switch → move to → push to → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
