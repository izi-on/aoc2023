from collections import defaultdict
from pprint import pprint
with open("input.txt") as f:
    blocks = f.read().split("\n\n")

seeds = list(map(lambda x: int(x), blocks[0].split(": ")[1].split(" ")))

type_to_list = defaultdict(list)
lowest_loc = float("inf")
for i, block in enumerate(blocks):
    if i == 0:
        continue
    rules = [list(map(lambda x: int(x), rule.split(' '))) for rule in block.split(":\n")[1].split('\n')]
    type_to_list[i-1] += rules

for seed in seeds:
    cur = seed
    for idx_t in type_to_list.keys():
        for rule in type_to_list[idx_t]:
            if rule[1] <= cur < rule[1] + rule[2]:
                cur = cur - rule[1] + rule[0]
                break
    lowest_loc = min(lowest_loc, cur)

print(lowest_loc)