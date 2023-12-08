from collections import defaultdict
from functools import reduce

with open("input.txt") as f:
    card_bid_pairs = f.read().split("\n")

strength_map = {str(i):i for i in range(2,10)}
strength_map.update({
    "T":10,
    "Q":12,
    "K":13,
    "A": 14,
    "J": 1,
})

type_strength_map = {
    "h":1,
    "op":2,
    "tp":3,
    "tk":4,
    "fh":5,
    "fok":6,
    "fik":7,
}

type_strength_gap = 14*(15**5)*5 # assures that the gap of power between each card is right

def try_joker(hand):
    if "J" not in hand:
        return type_strength_map[get_type(hand)]
    
    card_set = {c for c in hand if c != "J"}
    max_strength = -1
    for attempt in card_set:
        for i,c in enumerate(hand):
            if c != "J":
                continue
            new_hand = hand[:i] + attempt + hand[i+1:]
            max_strength = max(max_strength, try_joker(new_hand))    
    return max_strength


def get_type(hand):
    if all(x == hand[0] for x in hand):
        return "fik"
    
    def counter(x,y):
        x[y]+=1
        return x
    c_count = reduce(counter, hand, defaultdict(int))

    if len(list(filter(lambda x: x==4, c_count.values()))) == 1:
        return "fok"
    
    if len(list(filter(lambda x: x==3, c_count.values()))) == 1:
        if len(list(filter(lambda x: x==2, c_count.values()))) == 1:
            return "fh"
        else:
            return "tk"
    
    if len(list(filter(lambda x: x==2, c_count.values()))) == 2:
        return "tp"
    if len(list(filter(lambda x: x==2, c_count.values()))) == 1:
        return "op"
    else:
        return "h"


def rank_hand(hand):
    # get strength from type:
    strength = try_joker(hand)*type_strength_gap
    print(hand, try_joker(hand))

    # add strength from the card types
    for i,c in enumerate(reversed(hand)):
        strength += strength_map[c] * 15**i
    
    return strength

# rank the cards 
ranks = []
for pair in card_bid_pairs:
    hand, bid = tuple(pair.split(' '))
    bid = int(bid)
    ranks.append((rank_hand(hand), bid))

result = sorted(ranks, key=lambda x: x[0])

ans = 0
for i, pair in enumerate(result):
    _, bid = pair
    print(i+1, bid)
    ans += (i+1)*pair[1]
print(ans)