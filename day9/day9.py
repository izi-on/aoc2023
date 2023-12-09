from functools import reduce
with open("input.txt") as f:
    sequences = f.read().split("\n")
sequences = list(map(lambda x: list(map(lambda x: int(x), x.split(' '))), sequences))
total = 0
for sequence in sequences:
    pyramid = [sequence]
    cur = sequence
    while list(filter(lambda x: x!=0, cur)):
        new_seq = reduce(lambda x,y: (x[0]+[y-x[1]], y), cur, ([],0))[0][1:]
        pyramid.append(new_seq)
        cur = new_seq
    print(pyramid)
    new_val = 0
    for row in reversed(pyramid[:-1]):
        new_val = new_val + row[-1]
    total += new_val
print(total)