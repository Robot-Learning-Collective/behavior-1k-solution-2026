# Cabinet tipping while retaining door — TRAIN10

Two same-snapshot-root successes, RGBD geometric evidence, not a separate goal predicate. Human15600 tip interval48–63.733s informed right hand's downward-angled upper-opening engagement. Top sliding failed; enter from OUTSIDE and BELOW top, then push away from opening at upper edge. Direct diagonal precontact→engagement crossed top and stalled on repeat; correct waypoint order matters.

## Start and exact successful components
Restore `carried-door-near-cabinet` only on matching own worker. Base odom[-.112,-.315],yaw-5.992; high torso[1.025,-1.45,-.47,0]; left door retained grip0 with q[-1.03388,.54529,-1.33942,-1.66169,-.48348,.29445,-1.52716]. Right hanging q0/open. Door must remain retained visually at every step.

Commands below compose the successful segments. The actual second trajectory contained one failed diagonal-contact attempt and retreat BEFORE the outside-lowering waypoint; removing those is a simplification, not an independently completed replay yet. Inspect every endpoint and actual achievement; never blindly run through a miss.

```python
s.act(right={'preset':'ready'},seconds=3)  # MUST unfold before crouch
s.act(torso={'q':[1.4505,-2.227,-.818,0]},seconds=3)
s.act(base={'fwd':.31},seconds=4)
s.act(right={'q':[-.56571,-.59988,.24254,-.87404,.04208,.70416,.56755]},seconds=3)
# Outside precontact TCP[.611,-.490,.549]; F[.50,-.04,-.86]
s.act(right={'q':[-.77771,-.39425,.30167,-.01963,.08172,.09287,.40054]},seconds=2)
# Lower outside first: TCP[.591,-.478,.431], same downward orientation.
s.act(right={'q':[-.66288,-.2537,.05998,-.02574,-.15844,-.35401,.26739]},seconds=2)
# Enter upper opening: TCP[.637,-.394,.447], F[.85,0,-.53], C[0,1,0], open.
# FOUR individually inspected pushes, not an unobserved loop:
s.act(base={'fwd':.06,'left':.04},seconds=2)
s.act(base={'fwd':.06,'left':.04},seconds=2)
s.act(base={'fwd':.06,'left':.04},seconds=2)
s.act(base={'fwd':.06,'left':.04},seconds=2)
s.act(right={'preset':'ready'},seconds=3)
```

## Second trial measurements / image pointers
Attempt `practice-restore-carried-door-near-cabinet-36da4748a63e4a33a9e5f3235ce5cd10`, local cache same named subdirectory.
- Before base approach, head floor samples(v610,u350/400/450): Z-.005, X.845, Y.032/-.137/-.307. Cabinet top head(455,445)/(485,460): Z.452, X1.136/1.054.
- Stance after .31m: base[.181,-.227],yaw-5.991; torso tracked. Cabinet top remained Z.452.
- obs5 outside precontact. obs6 FAILED direct diagonal contact, q4lag.048, TCPZ.465 (above requested.447). obs7 retreat. obs8 lower-outside successful. obs9 entry successful.
- obs10–13 four pushes: base[.223,-.174]→[.266,-.122]→[.309,-.070]→[.352,-.018]. Right q tracked, no base guard; not force proof.
- Head top-plane SVD normals after pushes1–3: [-.1173,-.1136,-.9866],[-.1867,-.1812,-.9655],[-.2580,-.2511,-.9329]. Fourth push produced complete tip, opening up.
- obs14 right ready, cabinet rests independently. Head rim samples(u403,v503), (u356,v549), (u488,v679)≈[1.0584,-.1627,.2478],[.8750,.0111,.2478],[.5687,-.2874,.2477]. These are observed BODY coordinates at that endpoint, not general targets.
- Final receipt `receipt_01792158347837248000_a516e48222ec4f6aa0dcd5a2dfa68fd4.json`; before-contact obs8 receipt `receipt_01792158265428583000_28d63b3cf18a401788fc5a15e3f4e15d.json`.
- Second trial restored sim66.433→ready84.433:18.0sim s including failed probe+retreat; wall175s at receipt. Clean-shortened performance not yet measured. Four pushes alone5.233sim s.
- Snapshot `cabinet-tipped-repeat-ready`; previous successful `cabinet-tipped-ready` also preserved.
