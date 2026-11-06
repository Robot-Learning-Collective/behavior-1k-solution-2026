# TRAIN43 house-side path discovery and local clearing

## Scope and result
After coverage002 finished Q0, new public-human comparison identified a concrete spatial omission: the **entire stepping-stone path to the house**, not just the circular patio/path entrance. Different late sweep annotations in7217/TRAIN20 and7218/TRAIN22 show orange on house-side stones and actual cleaning, not merely returning the broom. See `human-path-measurements.md` and NOTES comparison table.

Authorized same-instance snapshot `train43-chair-preapproach-002` restored as **`practice-restore-train43-chair-preapproach-002-7f78c7b8a3d448078f20cbd460a4c81a`**. This is **not a fresh reset, held-out attempt or continuation of coverage002's final world**. Restored clock1790ticks/59.6667s; final3630ticks/121.00s.22 dispatched motor calls add1840ticks/61.3333s. Native finish **false/Q0**, wall368.215743s; patio furniture/entrance mud remains untreated in this restored world. `train43-path003-finish.json` is authority. No active attempt after finish.

## Demonstrated finding
RGB005–008 exposed previously unvisited house-side orange; later changed views distinguished **five local footprint labels A–E**. These are visual labels, not a native particle count. Four centrally aligned strokes reached6–8mm TCP height; the first A target missed with a joint-limit/wrist lag but its orange was absent after withdrawal/stance change010. Native Q does not identify which mud caused earlier failures; this proves an omitted region with removable visible orange, not that it was the sole remaining cause.

## Route and actual zone ledger
|Zone/label|Initial observation / fresh BODY point|Attempted stroke|Independent visibility/status|
|---|---|---|---|
|Patio center/chairs/grill/bench|Restored early snapshot001|None in this segment|Known untreated / some occluded; never marked clear|
|Patio path entrance|Orange visible at003–004|None in this segment|Seen, untreated; distinct from farther path|
|House path A, near edge|008 head(u350,v425),[.804250,.023883,-.005713]|009 target[.444250,.123883,.005]→actual[.483,.198,.035]; shoulder at limit, wrist lag−.236|010 withdrew with back.1/right.2: edge exposed without orange. Solver miss retained, not hidden|
|House path B, curved orange|011 head(u271,v324),[1.063524,.231532,.000734]|012 actual[.705,.330,.007]|013 withdrawal exposed footprint without orange; underlying tan remained|
|House path C, next edge|013 head(u278,v314),[1.090470,.214192,.001091]|014 actual[.731,.312,.008]|015 withdrew/advanced, then changed stance016; no orange in exposed edge, no whole-task claim|
|House path E, farther left stone|016 head(u267,v325),[1.062323,.243619,-.004852]|017 actual[.701,.343,.008]|018 withdrawal/turn, final changed-view023 showed treated house-end stones without orange|
|House path D, farther right stone|019 head(u273,v326),[1.058144,.226081,.000732]|020 actual[.699,.325,.006]|021 withdrawal/back.2 independently exposed full stone without orange|
|House-end remaining stones / pavement|022 raised view,023 compact changed view|No new stroke|Seen without obvious orange in sampled views, not an exhaustive mask or native-clean assertion|

002–006: compact navigation, turn130° timed out after about114° then separate55°; follow actual visible path, not integrated odometry replay.005 snapshot `train43-path-unvisited-003` saved.007 raised staging,008 separate low descent; bush and tree remain clearance constraints.009 A was too medial/near for selected joint branch.010 withdrawal/reposition recovered;011 onward use fresh depth and stance to place patch nearBODY[1.05,.23,ground], yielding central TCP near[.70,.33,.005]. Avoid replacing stance correction with pressure or repeated IK attempts.

015–016 approach left stone E first.018 turn−45° put right stone D centrally reachable without a long lateral move toward the bush;019 fresh alignment,020 stroke,021 independent withdrawal.022 raise unchanged arms,023 compact/turn55° to inspect house end. Saved `train43-house-path-cleared-003`, then finished. No restores after the initial one; snapshots saved only. Grasp retained from coverage002 early snapshot, not reacquired in this segment.

## Reusable correction
The coverage checklist must distinguish **patio entrance / middle path / house-end stones / house pavement** and mark unvisited zones explicitly. After pickup, prefer inspecting and clearing the full open path before spending time on repeated furniture searches. This is now supported by live TRAIN43 discovery/local clearing, not only human analogy. It is not proof of complete TRAIN43 success, a new-instance generalization result, or wall-speed parity. A future full-reset run must independently verify complete coverage within18106ticks.

Same original Pi/session, authorized switching shim, no operator/controller changes, no cross-instance restore. All22 motor calls finite positive remaining-budget caps; final meter includes inherited1790ticks. Native outcomes and failed A reach remain preserved.
