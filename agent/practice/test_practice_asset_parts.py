"""CPU regression: slicing dependencies are transitive, deduplicated and cycle-safe."""
from prepare_practice_assets import models_with_parts

whole=('pizza_dough','jguwbv');left=('half_pizza_dough','spvbal');right=('half_pizza_dough','xzkcwu')
child=('quarter','test');unrelated=('chair','test')
metadata={whole:{'object_parts':[dict(category=c,model=m) for c,m in [left,right,left]]},
          left:{'object_parts':{'0':dict(category=child[0],model=child[1])}},
          right:{},child:{'object_parts':[dict(category=whole[0],model=whole[1])]},unrelated:{}}
seen=[]
def read(category,model):
    key=(category,model);seen.append(key);return metadata[key]
assert models_with_parts({whole,unrelated},read)==set(metadata)
assert len(seen)==len(set(seen))==5
print('practice asset parts PASS')
