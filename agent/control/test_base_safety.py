"""CPU regressions for base tracking stops and caller-owned native step caps."""
import copy
import numpy as np
from portable_control import Controller
from test_portable_control import RobotModel,robot_fixture,advance,goal


def run(cap=None,creep=False):
    model=RobotModel();r=robot_fixture(model);c=Controller(model)
    g=goal(r);g['base']=[.3,0.,0.]
    if cap is not None:g['max_steps']=cap
    action,done=c.step({'step':0,'robot':r},g)
    for n in range(1,200):
        old_done=done;applied=action.copy();advance(r,action,model)
        if creep:
            r['base_velocity']=np.array(action[:3]*[.75,.75,1.])
            if creep!='yaw':r['base_velocity'][:2]*=.3
            if creep!='translation':r['base_velocity'][2]+=-.12 if not old_done else 0.
        action,done=c.step({'step':n,'robot':r},g)
        count=len(c.base_feedback);c.step({'step':n,'robot':r},g);assert len(c.base_feedback)==count
        if old_done:
            np.testing.assert_array_equal(applied[:3],0)
            return c,n
    raise AssertionError('Unbounded controller')


def main():
    for limit in (1,3,16):
        c,n=run(limit);assert n==limit and c.reason=='timeout' and not c.result['achieved'],(limit,n,c.result)
        assert c.result['stop_reason_detail']=='caller_step_limit'
    c,n=run();assert c.reason=='reached' and not c.result['base_safety']['triggered']
    for kind in (True,'translation','yaw'):
        c,n=run(creep=kind);assert n<=16 and c.reason=='stalled' and c.result['base_safety']['triggered']
        assert c.result['stop_reason_detail']=='base_velocity_tracking_mismatch'
        if kind=='yaw':assert not c.result['base_safety']['translation_mismatch']
        if kind=='translation':assert not c.result['base_safety']['rotation_mismatch']
    # A one-tick angular release impulse inside the heading tolerance must not
    # veto an otherwise correctly tracking retreat / translation.
    model=RobotModel();r=robot_fixture(model);c=Controller(model);g=goal(r);g['base']=[.3,0.,0.]
    action,done=c.step({'step':0,'robot':r},g)
    for tick in range(1,200):
        old_done=done;advance(r,action,model)
        if tick==15:r['base_velocity'][2]+=.7
        action,done=c.step({'step':tick,'robot':r},g)
        if old_done:break
    assert c.reason=='reached',c.result
    # Alternating lateral release vibration should not be summed as a persistent
    # translation deficit while net commanded progress is being achieved.
    r=robot_fixture(model);c=Controller(model);g=goal(r);g['base']=[.3,0.,0.]
    action,done=c.step({'step':0,'robot':r},g)
    for tick in range(1,200):
        old_done=done;advance(r,action,model);r['base_velocity'][1]+=.015*(-1 if tick%2 else 1)
        action,done=c.step({'step':tick,'robot':r},g)
        if old_done:break
    assert c.reason=='reached',c.result
    # Feedback is retained across short goals: splitting an obstruction into
    # sub-half-second calls must not erase evidence of failed velocity tracking.
    model=RobotModel();r=robot_fixture(model);c=Controller(model);tick=0;tripped=False
    for i in range(8):
        g=goal(r);g.update(id=str(i),base=[.5,0.,0.],max_steps=4)
        action,done=c.step({'step':tick,'robot':r},g)
        while True:
            old_done=done;advance(r,action,model);r['base_velocity']=np.array([action[0]*.75*.3,0.,0.]);tick+=1
            action,done=c.step({'step':tick,'robot':r},g)
            if old_done:break
        if c.result['base_safety'].get('triggered'):tripped=True;break
    assert tripped and tick<=17
    # A new deliberate recovery goal is permitted after a guard stop.
    g=goal(r);g.update(id='retreat',base=[c.odom.xy[0]-.1,c.odom.xy[1],c.odom.yaw])
    action,done=c.step({'step':tick,'robot':r},g);assert not done and action[0]<0
    # Strong heading error forbids simultaneous forward driving.
    r=robot_fixture(model);c=Controller(model);g=goal(r);g['base']=[1.,0.,1.]
    action,done=c.step({'step':0,'robot':r},g);assert np.linalg.norm(action[:2])==0 and action[2]>0
    c=Controller(model);g['base']=[10.,0.,.1]
    action,done=c.step({'step':0,'robot':r},g);assert 0<np.linalg.norm(action[:2])*.75<=.10000001
    # Native free heading-first turns have a few mm cross-axis response. Motion
    # within the advertised5mm position tolerance is not a blocked-base event.
    r=robot_fixture(model);c=Controller(model);g=goal(r);g['base']=[.02,0.,1.]
    action,done=c.step({'step':0,'robot':r},g)
    for tick in range(1,16):
        advance(r,action,model);r['base_velocity'][0]+=.008
        action,done=c.step({'step':tick,'robot':r},g)
    assert not done and not c.base_guard_triggered,c.result
    # Invalid limits must be rejected before actuation.
    for value in (0,-1,True,1.5):
        c=Controller(model);bad=copy.deepcopy(g);bad['max_steps']=value
        try:c.step({'step':0,'robot':r},bad)
        except ValueError:pass
        else:raise AssertionError(value)
    print('PASS free motion, creep/uncommanded yaw stop, short-goal history, recovery, heading hold, hard1/3/16tick caps')


if __name__=='__main__':main()
