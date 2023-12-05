from functools import reduce
from collections import defaultdict, deque

with open("input.txt", 'r') as f:
    cards = f.read().split("\n")

cards = list(map(lambda x: x.split(':')[1], cards))

total = 0

result = {}
count = defaultdict(int)

for i, card in enumerate(cards):
    total += count[i] + 1
    def get_count(x,y):
        if y:
            x[int(y)] += 1 
        return x
    count_w = reduce(get_count, card.split('|')[0].split(' '), defaultdict(int))
    count_c = reduce(get_count, card.split('|')[1].split(' '), defaultdict(int))
    count_match = reduce(lambda x,y: x+min(count_w[y], count_c[y]), set(count_w.keys()) & set(count_c.keys()), 0)
    for j in range(i+1, i+1+count_match):
        count[j] += count[i]+1

print(total)