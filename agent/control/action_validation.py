"""Strict BODY Cartesian6/NULL action bounds; no7D fallback or type coercion."""
import numpy as np

class InvalidAction(ValueError):
    pass


def validate(command):
    expected={'seconds','left','right','left_gripper','right_gripper','base','torso_delta'}
    if not isinstance(command,dict) or set(command)!=expected:raise InvalidAction('Unknown/missing action fields')
    if type(command['seconds']) not in (int,float) or not .1<=command['seconds']<=2:raise InvalidAction('Duration must be0.1–2seconds')
    for key,n in (('left',6),('right',6),('base',3),('torso_delta',2)):
        value=command[key]
        if key in ('left','right') and value is None:continue
        if not isinstance(value,list) or len(value)!=n or any(type(v) not in (int,float) for v in value):raise InvalidAction(f'{key} needs{n} finite numeric values (notbool/string/7D)')
        if not np.isfinite(np.asarray(value,dtype=float)).all():raise InvalidAction(f'{key} must be finite')
    for arm in ('left','right'):
        value=command[arm]
        if value is not None and (np.linalg.norm(value[:3])>.3 or np.linalg.norm(value[3:])>1.2):raise InvalidAction(f'{arm} exceeds BODYtranslation0.3m/rotation1.2rad norms')
        grip=command[arm+'_gripper']
        if type(grip) not in (int,float) or not 0<=grip<=1:raise InvalidAction('Gripper outside[0,1]')
    if not np.all(np.abs(command['base'])<=[.2,.2,.4]):raise InvalidAction('Base exceeds component bounds')
    if not np.all(np.abs(command['torso_delta'])<=[.15,.2]):raise InvalidAction('Torso exceeds component bounds')
    return round(command['seconds']*30)
