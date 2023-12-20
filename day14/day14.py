from collections import defaultdict
from pprint import pprint
with open("input.txt") as f:
    input = f.read().split("\n")
input = list(map(list, input))[:-1]

total_count = 0
cycles = 1000000000

mem = defaultdict(tuple)

def do_cycle():
    global input 
    for t in ("n", "w", "s", "e"):
        match t:
            case "n":
                input = list(map(tuple, zip(*input)))
            case "w":
                pass 
            case "s":
                input = list(map(tuple ,map(reversed , list( zip(*input) )) ))
            case "e":
                input = list(  map(lambda x: tuple( reversed(x) ), input) ) #type: ignore

        new_input = []
        for inp in input:
            inp = tuple( "#" ) + inp + tuple( "#" ) # type: ignore
            rocks_idx = (i for i, val in enumerate(inp) if val == "#")
            prev = 0
            new_inp = []
            for idx in rocks_idx:
                rocks_amount = sum([ 1 for val in inp[prev:idx] if val == 'O' ])
                new_inp.append(['O'] * rocks_amount + ["."] * (idx - prev - rocks_amount))
                prev = idx + 1
            new_inp = tuple( "#".join( map("".join, new_inp) ) )
            new_input.append(new_inp[1:])
        input = new_input

        match t:
            case "n":
                input = list(map(tuple, zip(*input)))
            case "w":
                pass
            case "s":
                input =list (reversed(list(map(tuple, list( zip(*input) ) ))) )
            case "e":
                input = list(  map(lambda x: tuple( reversed(x) ), input) ) #type: ignore
        # print("after")

def count_inp(input):
    total_count = 0
    input = tuple( map(tuple, zip(*input)) )
    for i, inp in enumerate( input ):
        total_count += sum(len(inp) - i for i, val in enumerate(inp) if val == 'O')
    return total_count


j = -1
for i in range(cycles):
    d_inp_b =tuple(map(tuple, input))
    if d_inp_b not in mem.keys():
        print("before", i)
        pprint(d_inp_b)
        do_cycle()
        d_inp = tuple(map(tuple, input))
        print("after", i)
        pprint(d_inp)
        mem[d_inp_b] = (d_inp, i)
    else:
        j = i
        break

d_inp_b = tuple( map(tuple, input) ) 
if j != -1:
    next_state, first_visit = mem[d_inp_b]
    cycle_length = j - first_visit
    cycles_left = (cycles - j - 1) % cycle_length
    for _ in range( cycles_left ):
        next_state, _ = mem[next_state]
    print(count_inp(next_state))
else:
    pprint(d_inp_b)
    print(count_inp(d_inp_b))

exit(0)

