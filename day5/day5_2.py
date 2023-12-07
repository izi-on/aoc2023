from functools import reduce
from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    blocks = f.read().split("\n\n")

seeds = list(map(lambda x: int(x), blocks[0].split(": ")[1].split(" ")))

type_to_list = []
lowest_loc = float("inf")
for i, block in enumerate(blocks):
    if i == 0:
        continue
    rules = [list(map(lambda x: int(x), rule.split(' '))) for rule in block.split(":\n")[1].split('\n')]
    rules = sorted(rules, key=lambda x: x[1])
    type_to_list.append(rules)

def group_pairs(x,y):
    l, i = x
    if i%2==0:
        l.append([y])
        return (l, i+1)
    else:
        l[-1].append(y)
        return (l, i+1)

seed_pairs = reduce(group_pairs, seeds, ([], 0)); seed_pairs = seed_pairs[0]

# print('all_maps', len(type_to_list))
# pprint(type_to_list)

# apply mappings
def f_m(cur, rule):
        return cur - rule[1] + rule[0]

# reduce mappings: reduce(seed to soil, soil to fertilizer) -> seed to fertilizier
def map_reduce(cur_map, next_map):
    new_map = []
    for mapping in cur_map:
        cur = mapping[1]
        x_range_end = mapping[1] + mapping[2]
        while cur != x_range_end: #explore all partitions 
            # find corresponding range in new mapping
            try:
                next_rule = next((rule for rule in next_map if (rule[1] <= f_m(cur, mapping) < rule[1] + rule[2])))
            except: # x = f(x) otherwise
                new_map.append([f_m(cur, mapping), cur, mapping[1] + mapping[2] - cur])
                cur += mapping[1] + mapping[2] - cur 
                continue
            next_cur = f_m(cur, mapping)
            new_range = min(mapping[1] + mapping[2] - cur, next_rule[1] + next_rule[2] - next_cur)
            new_map.append([f_m(next_cur, next_rule),cur,new_range])
            cur += new_range

    return new_map
            
new_map = reduce(map_reduce, type_to_list) # seed to location
new_map = sorted(new_map, key=lambda x: x[0])
print("new_map", new_map)
# scan seed ranges and get first 
print(seed_pairs)
smallest = float("inf")
for rule in new_map:        
    for pair in seed_pairs:
        seed_start, seed_range = pair
        if max(rule[1]+rule[2], seed_start+seed_range) - min(rule[1], seed_start)\
            < rule[2] + seed_range:
            smallest = min(max(rule[0], f_m(seed_start, rule)), smallest)
print(smallest)

