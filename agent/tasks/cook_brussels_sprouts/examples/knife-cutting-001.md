# Knife edge-down preparation and first contact — simulator error, not cutting success

TRAIN10, attempt `practice-restore-container_at_board-3276306c8581490f9bc016e04426c7ce`. Matching protocol6 run client. This is an observed preparation + failed first cutting contact, not a replay macro or verified cut. No automatic retry issued after nonrecoverable simulator error.

## Evidence
Cache `<observation-cache>/brussels-run-031-p6-7d6605/practice-restore-container_at_board-3276306c8581490f9bc016e04426c7ce/`.
- Obs36–40: right knife grasp, lift, second lift and base retreat visibly retained knife.
- Obs41: reoriented blade to BODY +Y, edge downward, fingers +X, closing +Z. Snapshot `knife_edge_down_first` preserves this pre-contact state.
- Obs42: aligned blade above one sprout on board.
- Obs43: **first descent toward contact returned `simulator_error`, recoverable=false, automatic_retry=false, uncertain=true**. Sprout is no longer visible at its prior location in endpoint RGB. This is not evidence of two real halves or task success. Private diagnostic not inspected.
- Error receipt `receipt_01792168883389582000_5fc3d65f185741da9cfebc7b64401429.json`; action59aa7ef0; sim263.93s; native act ended early after~0.63sim seconds.

## Measured recipe and adaptations
Torso `[.45,-.4,-.22,0]` throughout. Knife board support .8831m. Initial knife handle wrist-depth BODY approximately[.717,-.176,.906], blade pointed toward -Y. Closing direction across handle was -X; fingers down. A 3cm base correction put handle inside low workspace.

1. Stage right q `[-1.82672,-.33739,2.02164,-1.14348,-.56113,.68685,1.01558]` while base backed clear. TCP[.679,-.190,1.061], fingers down, closing -X. Advance base .30+.10+.03, checking each endpoint (scene-specific, not universal clearance).
2. `right={'to':[.69,-.176,.905]}` reached[.688,-.176,.906] but swept/rotated knife slightly in plane. Fresh depth placed actual handle around[.672,-.181,.905]; it remained inside open pads.
3. Close grip0: fingers[.0345,0], measured pinch[.671,-.177,.906]. Then lift to[.67,-.176,1.10] and[.67,-.176,1.25]. Knife visibly retained. Retreat base .30 to restore cutting reach.
4. Free-space orientation by right q `[-.41691,-.28420,.27541,-1.93872,-1.75043,-.35149,-.44351]`: TCP[.700,-.250,1.200], fingers+X, close+Z; blade points+Y, edge down. Wrist/edge orientation was chosen using visible blade profile and body-frame geometry. Important: trying to keep the blade pointing-Y demanded backward fingers and no good IK candidate; flipping blade direction while keeping edge-down was reachable. Raised knife before large joint transition.
5. Depth at obs41: sprout top[.7319,-.2190,.9307], central sample[.7174,-.2246,.9269]. Blade body samples[.7183,-.0874,1.1942], [.7163,-.1250,1.1960], [.7136,-.1731,1.2005]. Approx blade plane is TCP.x+.016, useful cutting span TCP.y+.08..+.18, lower edge near TCP.z-.01 (sampling uncertainty; not rigid object ground truth).
6. Align `right={'to':[.705,-.35,1.02]}`, seconds2: reached[.705,-.350,1.021], knife retained; blade above sprout.
7. First downward approach `right={'to':[.705,-.35,.945]}`, seconds1.5, intent `Cutting stroke 1 approach: bring edge to measured sprout top`. **Simulator error at measured TCP[.708,-.348,.955]**. Right q[-.46236,-.19193,-.01691,-.77735,-1.69010,.15035,.61036], largest lag~.017rad, gripper[.0346,0]. Torso measured effort up to47.5Nm; not contact-force proof. Both grip commands became unknown in receipt. No follow-up stroke/lift/observe/reset/restore was sent.

## Stroke count / evidence limits
Exactly ONE commanded downward cutting approach after free-space alignment, no completed repeated stroke, no verified cut. Planned later descent toward board was never dispatched. No cooking or whole-task success. Error timing is consistent with the attempted first blade contact, but only operator-side diagnostics can establish the failure cause.
