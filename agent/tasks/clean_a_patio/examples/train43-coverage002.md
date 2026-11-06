# TRAIN43 coverage002 — completed seen-instance practice, native Q0

`patio-train43-coverage002` finished **success=false / Q0 / fraction0 at17,442 ticks /581.40 simulated seconds**, wall4480.119415994s. The sole native not-covered-floor predicate remains false. This was a fresh assigned TRAIN43 reset after public multi-demo study, not a first attempt, held-out success, official evaluation or human-wall-speed result. No snapshot restored. First-attempt `patio-speed-train43-zero001` remains separately preserved, Q0/8433ticks with unintended bench tilt.

Ended deliberately with664ticks/22.133s remaining: final changed views/crops did not identify another clear orange target; furniture/rack occlusion remained unresolved. **Not budget exhaustion, crash, or proof that the floor was clean.** No active attempt after native finish. Final action `b10122d5`, obs211. `../train43-coverage002-finish.json` is authority.

## Demonstrated additions

- Empty-open-right-hand exposure while retaining broom left revealed chair-occluded orange. First sequence024–038 is detailed in [chair-exposure prefix](train43-chair-exposure002.md). Second-chair sequence077–088 and later overlapping-chair separation162–173 add public local exposure/removal evidence; they do not establish complete coverage or a causal explanation of the first failure.
- **Overlapping silhouettes concealed a distinct chair footprint.** At162–163 fixed torso[1.30,-1.45,-.47,0], open right TCP approximately[.527,-.328,.387], elevated left broom TCP[.682,.490,.964]. Bounded diagonal then .35m forward advance, followed by measured-right release and .85m withdrawal164, exposed orange at head(u465,v454), BODY[1.3863,-.5081,-.00529]. Treat chair identity/count as a visual inventory, not an assumed number: later wider views show three individual chairs, but earlier narrow/overlapping views were ambiguous.
-165–171 backed off, raised unchanged arms, compacted, changed heading, then deliberately backed off again before raised staging→separate descent→low advance. This avoided using cushion-height staging directly next to the exposed footprint. Fresh171 head(u280,v294)=[1.14778,.21278,-.00530]. Stroke172 target[.78778,.31278,.005] achieved[.787,.313,.009]. Withdrawal173 showed orange absent. Native stillQ0 at13516ticks/450.533s.
- **Open-floor coverage was also missed, not merely hidden furniture.** Changed stone-path view180–184 revealed three untouched bright orange patches late in the attempt. Stroke185 (actual[.862,.217,.012]) and186 (actual[.756,.114,.018], joint-limit miss) followed by withdrawal187 showed first two absent. A .65m rightward/.15m forward stance change188 brought the third into central left-arm reach; fresh target189 fromhead(289,317)=[1.08413,.18646,-.00503], actual TCP[.724,.286,.006]. Withdrawal190 showed it absent. Native stillQ0 at15018ticks/500.6s. Do not infer local removal from solver status alone;185/186 were not fully achieved targets.
- This is substantive local capability evidence, **not a full-task upgrade claim**. The frozen `d85c6294` is not replaced by this file without Astra's explicit selection.

## Full route and preserved failures

|Observations|Public evidence and limits|
|---|---|
|001–017|Fresh-depth pickup: separate open approach/insertion/closure/lift; retained left broom. Preapproach snapshot saved, never restored.|
|018–039|First controlled chair exposure/removal; preliminary right Cartesian poses not reached. Boundary shortcut/low turn produced arm/torso lag and tilted view. One measured torso reseed was rejected before dispatch. Recovered with legal raised torso, measured arms and inward retreat. Q0 at3484ticks.|
|040–056|Open center/grill-side fresh-depth strokes044/047/051/055 and withdrawals.053 lateral request missed height/reach; changed stance instead of repeating.|
|057–088|Second-chair route: left high-side targets062/064 failed; prior achieved branch reused065/066 still had wrist lag, released067. Right reach069/071 missed even after bent-elbow seed070. Bounded side/contact moves077–082; fresh orange under chair at082. Separate raised stage/lower, stroke086 actual[.491,.168,.011], withdrawal087 and changed view088 locally clear. No exact chair displacement from odometry.|
|089–100|Grill-corner turn constraint090, measured release/back/lateral091, alternate route and fresh stroke099/withdraw100. Q0 at7840ticks.|
|101–117|Bench-back approach; stroke112 actual[.834,.396,.020]. Withdrawal113 accompanied **unintended bench movement**.114 release/backoff; low inward Cartesian115 failed withq4lag~-.406.116 release+raise then117 compact. Bench later appeared upright; disturbance is not erased or retrospectively called planned relocation.|
|118–128|Far bench-end attempt. Reducing shoulder abduction before descent121 caused lag: not a validated low-safe branch.123/124 floor targets missed height (~33–34mm).125 requested short withdrawal[.6,.3,.16] diverged to[.694,.818,.493] despite small joint lag.126 measured hold/raise/backoff,127 upright rise,128 compact recovered. Q0 at9941ticks.|
|129–143|Changed survey and tan-candidate test.135/138 low targets remained31–36mm high. Changed stance139 enabled140 actual[.574,.270,.008]. Withdrawal141/142 still showed tan candidate. No proof tan was removable mud or explained Q0; no removal credit.|
|144–161|Further chair exposure. Earlier high-side broom posture still constrained at148;149 released/backed away.150 higher Cartesian request produced measured wrist values at/beyond limits.151 used explicit nearby legal joints, not invalid measured reseeding.152–158 advances/withdrawals exposed no obvious orange; base translation alone is not chair-motion proof.159–161 approached overlapping chairs.|
|162–173|Newly exposed overlapping-chair orange, fresh-depth stroke and independent withdrawal as detailed above. Q0 at13516ticks.|
|174–190|Revisit toward bench diverted through grill; forward178 stalled, back/lateral179 widened route,180 passed. Stone-path discovery and three local removals above. Q0 at15018ticks.|
|191–200|Upright compact bench-end/back survey. Bench-relative motion during197–198 was uncertain: tracking did not exclude body/furniture interaction.199 widened clearance. No clear orange found from these views; no complete under-bench coverage claim.|
|201–204|Deliberate bounded open-right bench-panel exposure with broom elevated. Fixed torso[1.15,-1.45,-.47,0], rightTCP~[.515,-.325,.477], .35m/.30m base moves then measured-right release/.8m retreat. Bench shifted/rotated in RGB toward grill; no obvious orange exposed in inspected footprint. Do not infer successful cleaning or collision-free furniture rearrangement.|
|205–211|Upright/compact final changed-view pass past bench end and grill side. Cropped public grill/chair views show no clear orange in inspected areas; rack/seat occlusion remains. No subsequent cleaning action or native success. Native finish Q0 at17442ticks.|

## Reusable correction versus unresolved work

1. Maintain an actual zone ledger, not a verbal intention to survey. Explicitly distinguish **not visited / seen but occluded / stroke attempted / exposed footprint visually clear**. Coverage002 focused on furniture and left three conspicuous stone-path patches until~480s. Human chair study does not imply furniture is the only failure cause.
2. Resolve overlapping furniture with changed views; inspect each vacated footprint. Expose only as needed with achieved open-hand pose, fixed torso, broom held spatially clear, bounded motion and withdrawal. Do not infer exact displacement from integrated base odometry.
3. For small/lateral reach misses, change stance; check achieved TCP/orientation and postwithdrawal image. Tiny joint lag can coexist with a severely wrong Cartesian endpoint. Legal command limits take precedence over measured reseeding.
4. Back away before raised staging near cushions; lower separately, then approach at sweep height. Raise unchanged arms before compaction. A historical joint branch is not a clearance certificate.
5. Still unresolved: remaining native mud location, reliable complete inventory, and efficient whole-task TRAIN43 completion. No Q1/repeat/generalization claim, no reason to overwrite the first failure. Any next work should diagnose recorded public coverage omissions before another long furniture-search loop.

## Evidence and audit

- Raw public cache: `<observation-cache>/patio-run-027-p6-cabfd1/patio-train43-coverage002/` (`obs_NNNN_raw.jpg`, depth NPZ and receipts).
- Final receipt: `receipt_01792184185825014000_b08d1b3b981a4aac95ccb8afe1643f98.json`.
- Run `control-action-results.jsonl` filtered by exact attempt: **211 records =210 dispatched actions +1 pre-dispatch torso rejection; dispatched steps sum17442**. Every dispatched call had finite positive integer cap and `steps<=cap<=remaining18106`; closure011 deliberately used30ticks rather than the full remaining cap. Outcome counts:168 reached,23 timeout,19 stalled. These labels do not prove environmental effects.
- Feedback files: `train43-coverage002-{chair,second-chair,bench,third-chair,stones}-feedback.json`; native finish above. Snapshots `train43-chair-preapproach-002` and `train43-chair-exposed-cleared-002` saved only, never restored.
- Detailed audit/hashes: `../train43-coverage002-checkpoint.json`.
- Public human study: [human-chair-measurements.md](human-chair-measurements.md), [human-sweep-measurements.md](human-sweep-measurements.md), NOTES phase table. No privileged object geometry/contact or remaining-mud coordinates were used.
