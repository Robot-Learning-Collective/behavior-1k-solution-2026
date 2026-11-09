# TRAIN207 native-reset009 — raised empty-hand transition, full chain attached

`cabinet-train207-high-clearance-009` is CLOSED: native attached=true/Q1 at2932ticks; after measured-q cancellation/opening and8cm withdrawal, finish **true/Q1,2952ticks/98.4sim s/1316.9776071960077task-wall s**.2211ticks below5163 practice meter. Reset RPC independently measured1.946440875s; repeated backend setup497.0953s is metadata, not reset latency.

75 sequential execution-certain/fault-null motor actions (64reached,11ordinary stalled),76RGB endpoints including initial observation; no timeout, snapshot/restore, backend change, base guard, uncertain transport or local rejected action. Sum of action ticks2952 matches native finish. First training feedback only after final seating. Four successful studied-world native-reset chains003/004/008/009, with005–007 failed optimizations retained: not4/4 reliability, held-out generalization, official-budget qualification, or a TRAIN10-crash repair claim.

## What changed and what did not

Exposed-edge acquisition, outside-rim tipping, early40+20cm cabinet relocation, retained alternate-wrist reorientation and broad ottoman support all transferred again. Fresh rim axis differed from008: insertion used(.599,-.222,.236), closing axis(.866,.5,0), achievedz.240 below rim.2477;4cm probe visibly moved cabinet. Measured-q refresh removed renewed lift preload during relocation. Cabinet released on floor before panel reorientation.

The changed hypothesis was **raise/retract the empty hand before downward orientation over the supported panel**.008's historical intermediate→pregrasp linear-q FK dipped to.456m despite clear endpoints.009 tested torso-raised orientation rather than attempting that near the support. This is a controlled-path improvement candidate, not proof of full-hand collision-free motion.

### Clearance transition

- obs047: broadly supported panel released with measured-q cancellation, deep torso[1.744,-2.75,-1.3,0].
- obs048: requested empty-hand−12cm forward/+18cm up; elbow bound stopped atTCP[.399,.147,.545], about24mm below requested height. Ordinary certain joint-limit miss; did not repeat or push harder.
- obs049: canceled measured arm, inset elbow q4 to−2.0544, raised torso to[1.4505,-2.227,-.818,0]; TCP[.410,.143,.783].
- obs050: base−25° yaw while empty hand remained retracted/high.
- obs051: intermediate A `[-.497668,.417288,-.71256,-1.564772,.519922,-.605756,-.93076]`, TCP[.428,.017,.846].
- obs052: downward B `[-1.35547,.89879,-1.07197,-1.24321,-.34357,-.89132,-1.5308]`, TCP[.609,.424,.802].
- Offline linear-q sampling predicted TCP minimum.783m for current→A and.741m forA→B with raised torso; **not collision checking**. Endpoint head views showed no obvious supported-panel displacement through this transition.
- obs053: lowered torso back to deep posture only after orientation, yieldingTCP[.595,.424,.502]. Fresh wrist/head depth then registered handle, not008's displaced coordinates.

### Handle registration still needed recovery

The high-clearance transition did not make grasp automatic:

1. Fresh bar[.609,.432,.405], panel plane.390. Requested shallowTCP[.610,.432,.406], achieved[.611,.429,.408]. Cancel/close left aperture4.9cm.12mm unloading returned after only2ticks; immediate4cm lift emptied fingers and panel stayed supported. **Failed first handle grip**, not retention.
2. Reopened. Remeasured bar[.614,.426,.408], plane.392. Changed registration to[.614,.426,.398], fingersdown, closingaxis[.4,-.917,0],2mm tolerance. Achieved[.615,.423,.400]; canceled ordinary miss and deliberately accepted partial closure, rather than pressing deeper.
3.12mm unloading again took2ticks. This time issued explicit `left={'grip':0}` at unloading height, allowing20ticks of closure settling. Aperture settled~6.3mm, then separate4cm lift visibly moved the panel. Subsequent65/90cm raises confirmed retention. Aperture was not the proof.

Deeper/fresher registration and explicit closure settling both changed, so this is **not isolated causal evidence** that settling alone fixed the first failed grasp. `seconds` is an upper tick cap, not guaranteed dwell; an already-satisfied or small motion can finish in1–2ticks.

### Fresh final alignment

After two raised yaw stages and base[−.20,+.20] away from ottoman, descended to60 then40cm inspection. Panel shortedge approximately55°, cabinet visible shortedge approximately51°: chose **−4°**, unlike008's+22°. Fresh corner after yaw[.695,.302] versus rim[.717,.463] requiredbase[+.022,+.162]. Corresponding shortedge direction and mating-end relation agreed. Corrected XY before descent, not postrelease pushing.

Final close axis[−.60522365,−.79605548,0], TCP[.5,.45,z]:
-40cm torso[1.75,-2.65,-1.2,0], q `[-1.69019,1.06066,-2.2647,-1.46478,-1.85636,-.699,.17907]`.
-35cm deep torso, q `[-1.60342,.95631,-2.25561,-1.30379,-1.84054,-.63174,.22406]`.
-28cm deep torso, q `[-1.39219,.80469,-2.23999,-1.03506,-1.8108,-.47968,.2583]`.
-Native attached=true2932; measured cancel/open, withdraw8cm, native finishtrue2952. No extra pressure or door opening required.

## Evidence

- `../train207-high-clearance-009-{reset,seating-feedback,finish}.json`
- `../control-action-results.jsonl`, exact attempt filter above.
- Cache namespace`cabinet-run-023-p6-d689c6`, final obs076 receipt`receipt_01792191704763552000_020ef9e1c85e4e29964ef5da5ebc2126.json`.

Next useful seen-world test: retain raised orientation, avoid the failed shallow grasp by fresh below-bar/above-panel registration and explicit closure settling before the independent lift. Keep all failures, fresh geometry and lifecycle boundaries; no universal numeric macro.
