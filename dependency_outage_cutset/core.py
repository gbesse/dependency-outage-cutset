import itertools
from .common import unique_ids,identifier,integer

def run(data):
    nodes=data['nodes'];root=data['root'];ids=set(unique_ids(nodes));by={n['id']:n for n in nodes};costs=data.get('costs',{})
    if root not in ids or len(nodes)>200:raise ValueError('size_or_root')
    for k,v in costs.items():identifier(k);integer(v,0,10**12)
    visiting=set();memo={}
    def minimal(options):
        out=[]
        for option in sorted(set(options),key=lambda x:(len(x),sorted(x))):
            if not any(existing<=option for existing in out):out.append(option)
            if len(out)>4096:raise ValueError('cutset_limit')
        return out
    def cuts(key,depth=0):
        if key not in ids or key in visiting or depth>100:raise ValueError('cycle_or_unknown')
        if key in memo:return memo[key]
        n=by[key];kind=n['kind'];visiting.add(key)
        if kind=='component':answer=[frozenset([key])]
        elif kind in ('all','any'):
            children=n['children']
            if len(children)>100 or len(children)!=len(set(children)):raise ValueError('children')
            parts=[cuts(c,depth+1) for c in children]
            if kind=='all':answer=minimal([x for part in parts for x in part])
            else:
                answer=[frozenset()]
                for part in parts:
                    if len(answer)*len(part)>100000:raise ValueError('product_limit')
                    answer=minimal([a|b for a,b in itertools.product(answer,part)])
        else:raise ValueError('kind')
        visiting.remove(key);memo[key]=answer;return answer
    result=cuts(root);failed=set(data.get('observed_failed',[]));components={n['id'] for n in nodes if n['kind']=='component'}
    if not failed<=components:raise ValueError('failure')
    rows=[{'components':sorted(c),'declared_cost':sum(costs.get(k,1) for k in c)} for c in result];rows.sort(key=lambda r:(r['declared_cost'],len(r['components']),r['components']))
    return {'minimal_cutsets':rows,'root_failed_under_observation':any(c<=failed for c in result),'observed_failed':sorted(failed),'scope':'monotone Boolean availability graph, shared components deduplicated; no failure probabilities or capacity model'}
