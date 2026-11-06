"""Absolute7D endpoint validation/ramped finite native motor targets; no IK/teleport."""
import numpy as np
from action_validation import validate as validate_nonarm, InvalidAction

def validate(command, bounds):
    if not isinstance(command,dict): raise InvalidAction('Action must be a dictionary')
    # Reuse established duration/base/torso/gripper/field validation ONLY; fakezeros
    # never reach actuation. Cartesian policy arrays never fall back to IK.
    nonarm=dict(command)
    for arm in ('left','right'):
        if arm not in command: raise InvalidAction('Missing arm endpoint')
        endpoint=command[arm]
        if endpoint is not None:
            if not isinstance(endpoint,list) or len(endpoint)!=7 or any(type(v) not in (int,float) for v in endpoint):raise InvalidAction(f'{arm} requires NULL or7numeric radians')
            try:q=np.asarray(endpoint,dtype=float)
            except (TypeError,ValueError):raise InvalidAction(f'{arm} requires NULL or7finite radians')
            if q.shape!=(7,) or not np.isfinite(q).all():raise InvalidAction(f'{arm} requires NULL or7finite radians')
            low,high=bounds[arm]
            if np.any(q<low) or np.any(q>high):raise InvalidAction(f'{arm} outside published safe joint endpoint limits; no clipping')
        nonarm[arm]=[0.]*6
    return validate_nonarm(nonarm)

def target(initial,previous_command,endpoint,fraction,low,high,max_step=.025):
    """Slew absolute setpoints, never cap commanded-minus-measured tracking lag."""
    desired=initial if endpoint is None else initial+fraction*(np.asarray(endpoint)-initial)
    previous_command=np.asarray(previous_command,dtype=float)
    return np.clip(previous_command+np.clip(desired-previous_command,-np.asarray(max_step),max_step),low,high)
