"""Stage only five requested training-10 fixtures and their asset dependencies; never overwrite assets."""
import json
from pathlib import Path
import zipfile
import zlib

TASKS = {
    'scanner-run-007': ('installing_a_scanner', 'office_cubicles_right'),
    'fax-run-008': ('installing_a_fax_machine', 'office_cubicles_right'),
    'pictures-run-009': ('hanging_pictures', 'house_double_floor_lower'),
    'gloves-run-010': ('clean_boxing_gloves', 'house_single_floor'),
    'lunchbox-run-011': ('preparing_lunch_box', 'house_single_floor'),
}

def destination(output, root, name):
    relative=Path(name)
    return output/(relative if relative.parts[0]==root else Path(root)/relative)

def unpack(archive, entries, output, root):
    for e in entries:
        p=destination(output,root,e.filename)
        assert output.resolve() in p.resolve().parents, 'Unsafe archive path'
        if p.exists():
            assert p.stat().st_size==e.file_size and zlib.crc32(p.read_bytes())==e.CRC, f'Existing asset differs: {p}'
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        data=archive.read(e)
        with p.open('xb') as f:f.write(data)

def models_with_parts(models, read_metadata):
    """Include official slicing outputs, recursively, without changing transition rules."""
    models=set(models);pending=list(models)
    while pending:
        parts=read_metadata(*pending.pop()).get('object_parts', [])
        for part in parts.values() if isinstance(parts,dict) else parts:
            model=(part['category'],part['model'])
            if model not in models:models.add(model);pending.append(model)
    return models


def main():
    import argparse
    from prepare_assets import Ranges, BASE, ARCHIVES, REVISION
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--fixtures-only',action='store_true');ap.add_argument('--instance',type=int,default=10);a=ap.parse_args()
    assert 10<=a.instance<=300, 'Only TRAIN instances10..300'
    name='2026-challenge-task-instances.zip';stream=Ranges(BASE+name,ARCHIVES[name])
    selected=[];models=set();templates={};provenance=[]
    with zipfile.ZipFile(stream) as z:
        names=set(z.namelist())
        for run,(task,scene) in TASKS.items():
            prefix=f'scenes/{scene}/json/{scene}_task_{task}'
            fixture=f'{prefix}_instances/{scene}_task_{task}_0_{a.instance}_template-tro_state.json'
            template=prefix+'_0_0_template.json'
            assert fixture in names, f'Missing TRAIN instance{a.instance}: {fixture}'
            assert template in names,template
            selected.extend([z.getinfo(fixture),z.getinfo(template)])
            data=json.loads(z.read(template));templates[run]=template
            for e in data['objects_info']['init_info'].values():
                args=e['args']
                if args.get('category') and args.get('model'):models.add((args['category'],args['model']))
            provenance.append({'run':run,'task':task,'scene':scene,'mode':'train','instance_id':a.instance,'fixture':'2026-challenge-task-instances/'+fixture,'structural_template':'2026-challenge-task-instances/'+template})
        print('TRAIN_FIXTURES_FOUND',json.dumps(provenance),flush=True)
        unpack(z,selected,a.output,'2026-challenge-task-instances')
    manifest={'revision':REVISION,'tasks':provenance,'models':sorted(models),'fixture_fetched_bytes':stream.fetched}
    a.manifest.parent.mkdir(parents=True,exist_ok=True)
    a.manifest.write_text(json.dumps(manifest,indent=2)+'\n')
    if a.fixtures_only:return
    name='behavior-1k-assets-3.9.0.zip';stream=Ranges(BASE+name,ARCHIVES[name],max_fetched_bytes=6_000_000_000);scenes={s for _,s in TASKS.values()}
    with zipfile.ZipFile(stream) as z:
        entries_by_name={e.filename.removeprefix('behavior-1k-assets/'):e for e in z.infolist()}
        def read_metadata(category,model):
            entry=entries_by_name[f'objects/{category}/{model}/misc/metadata.json']
            unpack(z,[entry],a.output,'behavior-1k-assets')
            return json.loads(destination(a.output,'behavior-1k-assets',entry.filename).read_text())
        initial_models=models.copy()
        models=models_with_parts(models,read_metadata)
        manifest.update(models=sorted(models),slicing_dependencies=sorted(models-initial_models),asset_dependency_version=1)
        def wanted(e):
            p=Path(e.filename).parts
            if p and p[0]=='behavior-1k-assets':p=p[1:]
            if not p or e.is_dir():return False
            return (p[0] in ('VERSION','metadata') or
                (len(p)>=3 and p[0]=='objects' and (p[1],p[2]) in models) or
                (len(p)>=2 and p[0]=='scenes' and p[1] in scenes and 'json' not in p) or
                p[0]=='systems')
        entries=[e for e in z.infolist() if wanted(e)]
        missing=[e for e in entries if not destination(a.output,'behavior-1k-assets',e.filename).exists()]
        estimate={'selected_files':len(entries),'missing_files':len(missing),'expanded_missing_bytes':sum(e.file_size for e in missing),'compressed_missing_bytes':sum(e.compress_size for e in missing)}
        print('ASSET_PLAN',json.dumps(estimate),flush=True)
        # Bounded task selection, not the31GB archive. Stop for inspection rather than disk pressure.
        assert estimate['expanded_missing_bytes']<8_000_000_000, 'Unexpected asset expansion; inspect plan'
        unpack(z,entries,a.output,'behavior-1k-assets')
    manifest.update(asset_plan=estimate,asset_fetched_bytes=stream.fetched)
    a.manifest.write_text(json.dumps(manifest,indent=2)+'\n')
    print('FIVE_TASK_ASSETS_READY',str(a.manifest),flush=True)

if __name__=='__main__':main()
