# TRAIN188: calibrated short sweep + explicit floor coverage

## Tested result and limits

`vacuum-train188-first-001` remains first-attempt zero-shot **FAILURE/Q0**:1353ticks/45.1sim s/560.190485716wall s, no demos/restore/intermediate feedback. Do not replace it with this development result.

After dense paired human study (NOTES table; measured state RGB−1, recorded actions RGB−2, three cameras13814/13815), fresh full-reset `vacuum-train188-practice-002` **SUCCESS/Q1**:2784ticks/92.8sim s/618.780837331wall s, under3617tick target. Snapshot `train188-powered-preclean-002` saved after activation but **never restored**. Intermediate practice feedback at1488 and1800 remainedfalse; after fifth particle2784true, finish reconfirmed. This is one studied development success, not held-out replication or wall-time parity.

## Material procedure changes

1. **Calibrate current head offset, not just the gripping TCP.** This grasp retained~9.2cm aperture after actualTCP`.574,.156,.453` pickup and5cm visible lift. Raised carryTCP`.53,.18,.50`; rightcamera nozzle-top samples z.084–.089 versus adjacent floor−.005. LoweredTCP`.53,.18,.45` attainedz.455; nozzle-topz.040–.046. Small descent residual was replaced with measured armq; no further downward forcing. Top height isn't underside/contact proof, and these z values are not universal.
2. **Short powered forward sweep.** From lower pose (later desiredz.455, attained~.457), anchor current measured armq and move baseforward.08–.12m over a fresh measured patch. Human13814 uses forward.262m/s at stable heldEEFz.415;13815 lowers/adjusts before forward motion. Live interface remains displacement-based; don't replay native velocity action arrays.
3. **Reveal rather than infer removal from occlusion.** Lift/retract backward-left to approximatelyTCP`.43,.30,.54` with fingers`[.64,.06,-.77]`, close`[-.03,1,.05]`. That removes the nozzle from the prior patch pixels in the free-hand camera. Inspect exposed floor and retention before travel. Changed joint branch/clearance needs fresh checking.
4. **Complete floor coverage, including starting footprint.** Three front-of-bed particles were not the whole task. Backing .35m and turning revealed a fourth near original start, BODY`.590,.135,-.005`. After that sweep feedbackstillfalse. Cardinal views from one point still missed a fifth: change viewpoint through known open floor, then back away to expose under-body/near-start blind spot. Fifth observed in rightcamera(423,313),BODY`.627,-.350,-.005`; after raised lateral alignment it was`.627,.109,-.005`. A short lower/forward.10/lift-reveal stroke completed the native goal. **Do not impose a count of five on other episodes.** Maintain sectors/dirty regions seen, identify body/nozzle occlusions, scan from a shifted viewpoint rather than repeat spins at one origin.

## Conditional sequencing

- Acquire lower motor body with fresh RGBD and separate closure; bounded lift proves retention visually.
- Present switch and use measured forward/high precontact then backward/down small press. In002 switch`.603,.069,.964`, stageR`.635,.06,1.00`, press`.607,.066,.963` gavegreen despite residual; release holding-arm preload and withdraw. Values are examples, not universal coordinates.
- Stage/tuck free hand and raise suction head for navigation. First three bed-floor patches measured approximately`[1.348,.022,-.005]`,`[1.452,.555,-.005]`,`[1.562,.948,-.005]` before approach. Fresh depth is necessary after each base move.
- Put nozzle just short of patch, calibrate lower posture, small forward sweep, lift backward/lateral to reveal. Travel raised. No baseguards occurred in002.
- Survey all remaining open floor, particularly original starting footprint and floor formerly under robot/nozzle. Use a changed viewpoint when a sector is occluded. First-attempt evaluation still prohibits intermediate native feedback; use the public coverage lesson without scorer access.
- Finish when visible work and coverage are complete; native feedback only then in first tests. If false, preserve the failure rather than label apparent local removal whole-task success.

## Evidence

Cache `<observation-cache>/vacuuming_floors-train020-p6-f17939/vacuum-train188-practice-002/`:
-017 lower geometry;018 first forward sweep;019 reveal.
-020–023 second;024–027 third; feedbackfalse1488.
-028 backing and029 new fourth reveal;030–032 fourth; feedbackfalse1800.
-033–038 room scans;039 shifted/backed view reveals fifth;040 alignment;041–043 last stroke.
-Final obs043 receipt`receipt_01792178271374669000_b0af805934a9446ea19425cc53692cbe.json`, endpointwall606.0; finish618.780837331.

No claim the forward sweep alone caused improvement: grasp/heading differ and there is no controlled ablation. The additional fourth/fifth visible patches and false→true after fifth stroke provide concrete support for the **coverage/blind-spot correction**. Contact-height diagnosis of first001 remains unproven.
