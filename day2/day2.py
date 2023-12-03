with open("input.txt") as f:
    games = f.read().split("\n")

answer = 0

for i, game in enumerate(games):
    rounds = game.split(":")[1].split(';')
    impossible = False
    count_max = {
        "blue" : 0,
        "green": 0,
        "red": 0
    }
    for r in rounds:
        def hand(x):
            count_max[x.split(' ')[2]] = max(count_max[x.split(' ')[2]], int(x.split(' ')[1]))
        
        for h in r.split(','):
            hand(h)
    prod = 1
    for c in count_max.values():
        prod *= c
    print(prod)
    answer += prod

print(answer)