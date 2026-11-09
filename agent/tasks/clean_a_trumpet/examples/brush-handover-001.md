# Left-to-right brush transfer — first success

Continues brush-pickup-001.md, attempt trumpet-practice-001. Snapshot `brush-right-handover-001` at obs30, right-only retention. Not yet repeated.

Exact successful endpoints (failures retained in control log):
- Lq[-.8086,-.16,-.4329,-1.3953,1.1883,-.0258,.1059] while retaining grip0, then Lq[-.8087,-.16,-.495,-1.3375,1.7442,-.0386,-.0686]. Brush lifted to TCP[.794,-.023,1.219]. Human uses shoulder2≈-.172; clipped *chosen target* to legal-.16 rather than bypass endpoint limits.
- Direct Rq[-.6787,.0403,-.3056,-1.5385,-.6064,1.03,.2619] from hanging **failed under desk lip**. Release with measured q, retract Rq[0,0,0,0,0,0,0]. Elbow-first Rq[0,0,0,-1.5,0,0,0] still hit lip at TCP[.509,-.252,.725].
- Correct recovery: `act(right={'q':measured_right},accept_partial=True,base={'fwd':-.20})`; base odom became[1.056,-.445],yaw1.157. Then Rq[0,0,0,-1.8,0,0,0] reached TCP[.634,-.252,1.010]. Raise before entering lip, not after.
- `act(right={'q':[-.7829,.0723,-.0388,-1.3444,-1.4302,.9614,.3692]})` reached near brush but brushed opposite hand (suspected), right q5lag.046. Release BOTH arms with measured q.
- Right RGBD visible free brush end: pixel(400,320) BODY[.759,-.080,1.196]; (415,270)[.768,-.074,1.196]. `act(right={'to':[.768,-.08,1.20]})` reached.
- `act(right={'grip':0})` fingers[.0002,.0379]. Then `act(left={'q':measured_left,'grip':1},right={'q':measured_right})`; `act(left={'fwd':-.10,'left':.10})`.
- Obs30 left fully separate; brush retained by right alone at TCP[.765,-.081,1.205], pads[.766,-.080,1.203]/[.781,-.073,1.174], Rq[-.83753,-.00594,.00483,-1.19399,-1.36322,.92144,.51978]. Left open TCP[.695,.077,1.220].
- `act(right={'q':[-.65,-.094,-.461,-1.542,.286,1.03,.872]},left={'q':[0,0,0,-1.8,0,0,0]})` reoriented brush bristles down, retained at obs31. R TCP[.740,-.328,1.008], pads[.740,-.331,1.007]/[.744,-.362,.996].

Human public demo7409, handover1191–1840 informed posture; adapted to our brush grasp and RGBD rather than copying end grasp blindly. Key observation images25 (precorrection),27 (aligned),28(close),29(release),30(independent retention),31(bristles down). Receipt root is same as pickup example.

## Fresh speed001 transfer failure — do not infer retention from aperture
Speed001 obs17 aligned right to [.765,-.095,1.215], then obs18 closed for exactly15ticks/.5s (`timeout`), fingers[.00018,.03764]. Obs19 opened left while holding right measured q: aperture[.00019,.03595]. At obs20 right lifted.03 while left withdrew; right fingers became fully closed and brush was back on the desk. This did NOT repeat the original transfer.

The successful original close ran24ticks/.8s until `stalled`, fingers[.00018,.03794]; after giver release its aperture stayed~.0382 and remained so through giver withdrawal. Thus the similar initial aperture was not retention proof. **Candidate, not established cause:** .5s close may have released the giver before grasp settling; allow closure/settling before release, then verify right-only lift. The new brush orientation and alignment also differed, so do not attribute failure solely to timing.

Saved public RGBD comparison: original27 red-back median[.7880,-.0605,1.2002], plane normal[.4622,-.7992,.3842]; speed00117 median[.7884,-.0725,1.2112], normal[.6505,-.6797,.3389]. These are visible-plane fits (not object/contact state), and establish that repeating arm q did not repeat the brush orientation. Original TCP[.7665,-.0798,1.2020] versus speed001[.7635,-.0950,1.2156]. Select the actual free-end grasp from fresh RGBD, not either saved absolute target.
