with open("input.txt") as f:
    instructions = f.readline()[:-1]
    f.readline()
    map_data = f.read().split("\n")
neighbours = {data.split('=')[0][:3] : [data.split('=')[1].split(',')[0][-3:], data.split('=')[1].split(',')[1][1:4]] for data in map_data}

concurrent = list(filter(lambda x: x[2]=='A', neighbours.keys()))
map_instr = { 'L': 0, 'R': 1 }
lcm = 1
gcd = 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
for start in concurrent:
    cur = start
    instr_ptr = 0
    step_count = 0
    while cur[2] != 'Z':
        cur = neighbours[cur][map_instr[instructions[instr_ptr]]]
        step_count += 1
        instr_ptr = (instr_ptr + 1) % len(instructions)
    lcm = lcm * step_count / gcd(lcm, step_count)

print(lcm)
        




