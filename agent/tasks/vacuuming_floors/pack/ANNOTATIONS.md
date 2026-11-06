# Public human annotation summary

Pinned dataset `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Three first available demonstrations with TRAIN instance>=20, excluding evaluation11–19 and practice10. Labels are annotations, not contact sensors. Durations use clipped half-open frame intervals at30Hz. Missing coarse annotations are reported, not synthesized.

## Episode13814 / TRAIN20

Length41.733s; valid interval[0, 1252]; raw ID690200; `annotations/task-0069/episode_00690200.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 267] → [[0, 267]]|8.900|move to|[['vacuum']] / []|
|[267, 570] → [[267, 570]]|10.100|pick up from|[['vacuum', 'floors']] / ['vacuum']|
|[570, 780] → [[570, 780]]|7.000|turn on switch|[['vacuum']] / ['vacuum']|
|[780, 850] → [[780, 850]]|2.333|move to|[['dirt']] / []|
|[850, 871] → [[850, 871]]|0.700|sweep surface|[['dirt']] / []|
|[871, 1006] → [[871, 1006]]|4.500|move to|[['dirt']] / []|
|[1006, 1070] → [[1006, 1070]]|2.133|sweep surface|[['dirt']] / []|
|[1070, 1118] → [[1070, 1118]]|1.600|move to|[['dirt']] / []|
|[1118, 1132] → [[1118, 1132]]|0.467|sweep surface|[['dirt']] / []|
|[1132, 1252] → [[1132, 1252]]|4.000|place on|[['vacuum', 'floors']] / ['vacuum']|

First annotated manipulation: **pick up from**, objects `[['vacuum', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode13815 / TRAIN21

Length59.233s; valid interval[0, 1777]; raw ID690210; `annotations/task-0069/episode_00690210.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 240] → [[0, 240]]|8.000|move to|[['vacuum']] / []|
|[240, 480] → [[240, 480]]|8.000|pick up from|[['vacuum', 'floors']] / ['vacuum']|
|[480, 780] → [[480, 780]]|10.000|turn on switch|[['vacuum']] / ['vacuum']|
|[780, 875] → [[780, 875]]|3.167|move to|[['dirt']] / []|
|[875, 997] → [[875, 997]]|4.067|sweep surface|[['dirt']] / []|
|[997, 1106] → [[997, 1106]]|3.633|move to|[['dirt']] / []|
|[1106, 1132] → [[1106, 1132]]|0.867|sweep surface|[['dirt']] / []|
|[1132, 1167] → [[1132, 1167]]|1.167|move to|[['dirt']] / []|
|[1167, 1189] → [[1167, 1189]]|0.733|sweep surface|[['dirt']] / []|
|[1189, 1475] → [[1189, 1475]]|9.533|move to|[['dirt']] / []|
|[1475, 1519] → [[1475, 1519]]|1.467|sweep surface|[['vacuum', 'floors']] / ['vacuum']|
|[1519, 1563] → [[1519, 1563]]|1.467|move to|[['dirt']] / []|
|[1584, 1594] → [[1584, 1594]]|0.333|sweep surface|[['vacuum', 'floors']] / ['vacuum']|
|[1594, 1777] → [[1594, 1777]]|6.100|place on|[['vacuum', 'floors']] / ['vacuum']|

First annotated manipulation: **pick up from**, objects `[['vacuum', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Episode13816 / TRAIN23

Length89.767s; valid interval[0, 2670]; raw ID690230; `annotations/task-0069/episode_00690230.json`.

### Coarse

Not supplied in this public sidecar.

### Fine

|Original frames → clipped frames|Seconds|Label|Objects / manipulated object|
|---|---:|---|---|
|[0, 510] → [[0, 510]]|17.000|move to|[['vacuum']] / []|
|[510, 832] → [[510, 832]]|10.733|pick up from|[['vacuum', 'floors']] / ['vacuum']|
|[832, 1110] → [[832, 1110]]|9.267|turn on switch|[['vacuum']] / ['vacuum']|
|[1110, 1359] → [[1110, 1359]]|8.300|move to|[['dirt']] / []|
|[1359, 1417] → [[1359, 1417]]|1.933|sweep surface|[['dirt']] / []|
|[1417, 1565] → [[1417, 1565]]|4.933|move to|[['dirt']] / []|
|[1565, 1592] → [[1565, 1592]]|0.900|sweep surface|[['dirt']] / []|
|[1592, 1622] → [[1592, 1622]]|1.000|move to|[['dirt']] / []|
|[1622, 1710] → [[1622, 1710]]|2.933|sweep surface|[['dirt']] / []|
|[1710, 1848] → [[1710, 1848]]|4.600|move to|[['dirt']] / []|
|[1848, 1881] → [[1848, 1881]]|1.100|sweep surface|[['dirt']] / []|
|[1881, 2006] → [[1881, 2006]]|4.167|move to|[['dirt']] / []|
|[2006, 2070] → [[2006, 2070]]|2.133|sweep surface|[['dirt']] / []|
|[2070, 2514] → [[2070, 2514]]|14.800|move to|[['dirt']] / []|
|[2514, 2610] → [[2514, 2610]]|3.200|sweep surface|[['dirt']] / []|
|[2610, 2670] → [[2610, 2670]]|2.000|place on|[['vacuum', 'floors']] / ['vacuum']|

First annotated manipulation: **pick up from**, objects `[['vacuum', 'floors']]`. Subsequent destinations/partners are listed in ordered fine rows above; these demonstration IDs are not live object handles.

## Shared order and decision points

Shared ordered motif (longest common subsequence of fine labels; optional/repeated stages may be omitted): **move to → pick up from → turn on switch → move to → sweep surface → move to → sweep surface → move to → sweep surface → place on**. This is a descriptive motif, not a compulsory policy.

Use TASK.md to decide required object counts, common destinations, closures, cooking/cleaning or attachment conditions. Compare the per-episode first manipulation and partner objects before choosing which object to handle first. Remeasure current geometry, reachability and clearance; verify object motion, supported release and retention separately from TCP completion. Label timing is not a physical contact or success guarantee.
