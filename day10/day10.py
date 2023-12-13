from collections import deque
from pprint import pprint
from functools import reduce
with open("input.txt") as f:
    matrix = f.read().split("\n")

visited = set()
dir_map = {
    '|': {(-1, 0), (1,0)},
    '-': {(0,1), (0,-1)},
    'L': {(-1,0), (0,1)},
    'F': {(1,0), (0,1)},
    'J': {(-1,0), (0,-1)},
    '7': {(1,0), (0,-1)},
    'S': {(-1,0), (0,-1), (1,0), (0,1)},
    '.': {(0,0), (0,0)},
}

part_of_cycle = set()

def bfs(pos):
    global visited, matrix
    queue = deque([pos])
    longest = -1
    while len(queue) > 0:
        increment = 0
        n = len(queue)
        for _ in range(n):
            cur = queue.popleft()
            if cur in visited: continue
            part_of_cycle.add(cur)
            increment = 1
            visited.add(cur)
            for nxt in get_valid(cur):
                queue.append(nxt)
        longest += increment
    return longest

def get_valid(cur):
    i_c, j_c = cur
    deltas = {(0,1), (0,-1), (1,0), (-1,0)}.intersection(dir_map[matrix[i_c][j_c]])
    valid = []
    for delta in deltas:
        dest = tuple(sum(x) for x in zip(cur,delta))
        i_d, j_c = dest
        if 0 <= dest[0] < len(matrix) and\
            0 <= dest[1] < len(matrix[0]) and\
                (dest[0], dest[1]) not in visited and\
                    delta in set(map(lambda x: tuple([-1*i for i in x]), dir_map[matrix[i_d][j_c]])):
            valid.append(dest)
    return valid

def upscale(matrix):
    new_matrix = []
    for row in matrix:
        row = reduce(lambda x,y : x+y, map(lambda x: [x, '.'], row), [])
        new_matrix.append(row)
        new_matrix.append(['.' for _ in range(len(row))])
    marked = set()
    for i,row in enumerate(new_matrix):
        if i % 2 == 1: continue
        for j,c in enumerate(row):
            if j % 2 == 1: continue
            dirs = dir_map[c]
            for d in dirs:
                if d[0] != 0: #vertical bar
                    if (i+d[0], j) not in marked: new_matrix[i+d[0]][j] = '|'
                    marked.add((i+d[0], j))
                elif d[1] != 0: #horizontal bar
                    if (i, j+d[1]) not in marked: new_matrix[i][j+d[1]] = '-'
                    marked.add((i, j+d[1]))
    
    return new_matrix

matrix = upscale(matrix)
# pprint(matrix)

filled = set()

def fill_bfs(cur, symbol):
    global matrix
    queue = deque()
    queue.append(cur) 
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            cur = queue.popleft()
            i_c, j_c = cur
            if cur in part_of_cycle or cur in filled: 
                continue
            matrix[i_c][j_c] = symbol
            filled.add(cur)
            for d in [(0,1), (1,0), (0,-1), (-1,0)]:
                if 0 <= i_c + d[0] < len(matrix) and\
                    0 <= j_c + d[1] < len(matrix[0]):
                        queue.append((i_c + d[0], j_c + d[1]))
            

#find cycle 
for i, _ in enumerate(matrix):
    for j, c in enumerate(matrix[i]):
        pos = (i,j)
        if c == 'S':
            bfs(pos) 

# fill the outside first 
for i in range(len(matrix[0])):
    fill_bfs((0,i), 'O')
    fill_bfs((len(matrix)-1, i), 'O')
for i in range(len(matrix)):
    fill_bfs((i,0), '0')
    fill_bfs((i,len(matrix[0])-1), '0')


# fill inside of cycle
for coord in part_of_cycle:
    i,j = coord
    for d in [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]:
        if 0 <= i + d[0] < len(matrix) and\
            0 <= j + d[1] < len(matrix[0]):
                fill_bfs((i+d[0], j+d[1]), 'I')

# count I instances on strictly even tuples (tuples where all numbers are even)
count_i = 0
for i, _ in enumerate(matrix):
    if i % 2 == 1: continue
    for j, c in enumerate(matrix[i]):
        if j % 2 == 1: continue
        count_i += 1 if matrix[i][j] == 'I' else 0

for row in matrix:
    print(row)
print(count_i)