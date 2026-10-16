import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def platform_feet(claim, person):
    if not (claim > 0):
        raise ValueError("the claimed reach must be above zero")
    if not (person > 0):
        raise ValueError("the person norm must be above zero")
    if not (person < claim):
        raise ValueError("the person norm must be less than the claimed reach")
    return claim - person

def reach_truth(claim, person):
    platform = platform_feet(claim, person)
    if platform <= 4:
        verdict = "a one-level stack honestly"
    elif platform <= 9:
        verdict = "a two-level stack honestly"
    else:
        verdict = "a tall stack honestly"
    return f"The box claims a {claim}-foot reach; at the {person}-foot person norm the platform stands {fixed1(platform)} {plural(1 if platform == 1 else 0, 'foot', 'feet')} up - {verdict}."

def tower_count(wall, coverage):
    if not (wall > 0):
        raise ValueError("the wall length must be above zero")
    if not (coverage > 0):
        raise ValueError("the tower coverage must be above zero")
    return math.ceil(wall / coverage)

def tower_truth(wall, coverage):
    towers = tower_count(wall, coverage)
    if towers <= 1:
        verdict = "one tower and done"
    elif towers <= 3:
        verdict = "a short row honestly"
    elif towers <= 8:
        verdict = "a working row of towers"
    else:
        verdict = "a scaffold-yard honestly"
    return f"A {wall}-foot wall at {coverage} {plural(coverage, 'foot', 'feet')} a tower is {towers} {plural(towers, 'tower', 'towers')} - {verdict}."

def plank_count(wall, plank):
    if not (wall > 0):
        raise ValueError("the wall length must be above zero")
    if not (plank > 0):
        raise ValueError("the plank length must be above zero")
    return math.ceil(wall / plank)

def plank_truth(wall, plank, levels):
    if not (levels > 0):
        raise ValueError("the level count must be above zero")
    per_level = plank_count(wall, plank)
    total = per_level * levels
    if total <= 1:
        verdict = "one plank and done"
    elif total <= 2:
        verdict = "a pair of planks honestly"
    elif total <= 6:
        verdict = "a stack of planks honestly"
    elif total <= 16:
        verdict = "a lumber pile honestly"
    else:
        verdict = "a rental-yard honestly"
    return f"A {wall}-foot wall takes {per_level} {plural(per_level, 'plank', 'planks')} of {plank} feet a level; {levels} {plural(levels, 'level', 'levels')} is {total} {plural(total, 'plank', 'planks')} - {verdict}."

FNS = {"reachTruth": reach_truth, "towerTruth": tower_truth, "plankTruth": plank_truth}

cases = [
 {"fn":"reachTruth","args":[12,6]},
 {"fn":"reachTruth","args":[7,6]},
 {"fn":"reachTruth","args":[16,6]},
 {"fn":"reachTruth","args":[21,6]},
 {"fn":"reachTruth","args":[12,5]},
 {"fn":"reachTruth","args":[0,6]},
 {"fn":"reachTruth","args":[12,0]},
 {"fn":"reachTruth","args":[6,6]},
 {"fn":"towerTruth","args":[40,7]},
 {"fn":"towerTruth","args":[7,7]},
 {"fn":"towerTruth","args":[14,7]},
 {"fn":"towerTruth","args":[50,7]},
 {"fn":"towerTruth","args":[100,7]},
 {"fn":"towerTruth","args":[30,10]},
 {"fn":"towerTruth","args":[0,7]},
 {"fn":"towerTruth","args":[40,0]},
 {"fn":"plankTruth","args":[40,10,2]},
 {"fn":"plankTruth","args":[10,10,1]},
 {"fn":"plankTruth","args":[20,10,1]},
 {"fn":"plankTruth","args":[30,10,2]},
 {"fn":"plankTruth","args":[50,10,4]},
 {"fn":"plankTruth","args":[24,8,3]},
 {"fn":"plankTruth","args":[0,10,2]},
 {"fn":"plankTruth","args":[40,0,2]},
 {"fn":"plankTruth","args":[40,10,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
