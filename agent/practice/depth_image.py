"""One existing HEAD axial-depth panel; no simulator/scorer/geometry dependency."""
import hashlib
from pathlib import Path
import time
import numpy as np
from PIL import Image, ImageDraw


def depth_rgb(depth):
    values = np.asarray(depth)
    if values.ndim == 3 and values.shape[-1] == 1: values = values[...,0]
    assert values.ndim == 2, 'Expected one axial depth image'
    valid = np.isfinite(values) & (values > 0)
    gray = np.zeros(values.shape,dtype=np.uint8)
    gray[valid] = np.rint(np.clip(values[valid],0,2.4)/2.4*255).astype(np.uint8)
    rgb = np.repeat(gray[...,None],3,axis=-1)
    rgb[~valid] = (255,0,255)
    return rgb


def compose_depth(endpoint, depth, camera):
    began = time.monotonic()
    raw = np.asarray(depth)
    panel = Image.fromarray(depth_rgb(raw)).resize((480,480),Image.Resampling.NEAREST)
    source = Path(endpoint['image'])
    path = source.with_name(source.stem+'_head_depth.jpg')
    with Image.open(source) as rgb:
        assert rgb.size == (1440,480), 'Unexpected onboard RGB triptych'
        canvas = Image.new('RGB',(1920,480))
        canvas.paste(rgb.convert('RGB'),(0,0))
        canvas.paste(panel,(1440,0))
        draw = ImageDraw.Draw(canvas)
        draw.rectangle((1440,0,1919,32),fill='black')
        draw.text((1446,3),'HEAD axial depth: black 0m -> white 2.4m / farther',fill='white')
        draw.text((1446,17),'MAGENTA invalid | lossy JPEG; not exact distance',fill='white')
        canvas.save(path,quality=86)
    result = dict(endpoint)
    result['image'] = str(path)
    result['image_layout'] = {'layout':'LEFT WRIST RGB | HEAD RGB | RIGHT WRIST RGB | HEAD axial depth',
        'dimensions':[1920,480],'camera':camera,'depth_modality':'depth_linear','depth_units':'axial camera-plane metres',
        'fixed_grayscale_range_metres':[0,2.4],'invalid_color':'magenta for nonfinite/nonpositive; finite farther is white',
        'action_id':endpoint['action_id'],'step':round(endpoint['simulated_seconds']*30),
        'pre_picture_worker_wall_seconds':endpoint['wall_seconds'],'rgb_post_save_monotonic_ns':endpoint['capture_monotonic_ns'],
        'timestamp_note':'Same HEAD get_obs dictionary for RGB/depth; PRE-picture stamp and RGB post-save are not shutter timestamps.',
        'source_rgb_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'delivered_image_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'composition_seconds':time.monotonic()-began,
        'precision_note':'~9.4mm/code before JPEG/model resampling; no exact distance/contact or bitwise RGB guarantee.'}
    diagnostic = {'observation_id':endpoint['observation_id'],'action_id':endpoint['action_id'],
        'camera':camera,'step':result['image_layout']['step'],'pre_picture_worker_wall_seconds':endpoint['wall_seconds'],
        'rgb_post_save_monotonic_ns':endpoint['capture_monotonic_ns'],'raw_depth_dtype':str(raw.dtype),
        'raw_depth_shape':list(raw.shape),'raw_depth_sha256':hashlib.sha256(raw.tobytes()).hexdigest(),
        'finite_positive_count':int((np.isfinite(raw)&(raw>0)).sum()),
        'finite_far_count':int((np.isfinite(raw)&(raw>2.4)).sum()),'nonfinite_count':int((~np.isfinite(raw)).sum()),
        'nonpositive_finite_count':int((np.isfinite(raw)&(raw<=0)).sum()),'image_layout':result['image_layout']}
    diagnostic['helper_seconds_including_diagnostics'] = time.monotonic()-began
    return result, diagnostic


def compose_rgbd(endpoint, depths, rgbs):
    """Native pixels for policy RGBD; old 1440×480 RGB/video files stay unchanged."""
    names=('left','head','right')
    assert len(depths)==len(rgbs)==3, 'Expected LEFT WRIST, HEAD, RIGHT WRIST RGBD'
    clean=[]
    for rgb,depth in zip(rgbs,depths):
        depth=np.asarray(depth,dtype=np.float32)
        if depth.ndim==3 and depth.shape[-1]==1:depth=depth[...,0]
        assert depth.ndim==2 and rgb.shape[:2]==depth.shape, 'Native RGB/depth dimensions disagree'
        clean.append(depth)
    widths=[d.shape[1] for d in clean];height=max(d.shape[0] for d in clean)
    source=Path(endpoint['image']);path=source.with_name(source.stem+'_rgbd.jpg')
    depth_path=source.with_name(source.stem+'_depth.npz')
    np.savez_compressed(depth_path,**dict(zip(names,clean)))
    canvas=Image.new('RGB',(sum(widths),2*height+24));draw=ImageDraw.Draw(canvas)
    panels={};x=0
    for name,rgb,depth in zip(names,rgbs,clean):
        h,w=depth.shape
        canvas.paste(Image.fromarray(rgb),(x,0))
        canvas.paste(Image.fromarray(depth_rgb(depth)),(x,height+24))
        draw.text((x+6,height+4),f'{name.upper()} {w}x{h} | DEPTH 0-2.4m | exact floats saved',fill='white')
        panels[name]={'rgb_xywh':[x,0,w,h],'depth_xywh':[x,height+24,w,h]}
        x+=w
    canvas.save(path,quality=88)
    return {**endpoint,'image':str(path),'depth_file':str(depth_path),'image_layout':{
        'layout':'Native RGB above depth; LEFT WRIST | HEAD | RIGHT WRIST; black padding is not camera pixels',
        'dimensions':list(canvas.size),'camera_panels':panels,'depth_modality':'depth_linear',
        'depth_units':'axial optical-camera metres','fixed_grayscale_range_metres':[0,2.4],
        'invalid_color':'magenta for nonfinite/nonpositive; finite farther is white',
        'precision_note':'JPEG depth is visualization only; use saved native float32 NPZ and calibration for geometry',
        'timestamp_note':'RGB and float depth from each same get_obs call, no intervening physics/render step; stamp is post-save, not shutter time.'}}
