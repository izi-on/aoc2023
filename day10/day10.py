from functools import partial
from collections import deque
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

def bfs(pos):
    global visited, matrix
    queue = deque([pos])
    longest = -1
    while len(queue) > 0:
        increment = 0
        n = len(queue)
        print(longest, list(map(lambda x: matrix[x[0]][x[1]], queue)))
        for _ in range(n):
            cur = queue.popleft()
            if cur in visited: continue
            increment = 1
            visited.add(cur)
            for nxt in get_valid(cur):
                queue.append(nxt)
        longest += increment
    return longest

def get_valid(cur):
    i_c, j_c = cur
    deltas = {(0,1), (0,-1), (1,0), (-1,0)}.intersection(dir_map[matrix[i_c][j_c]])
    print(deltas)
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
        
def is_valid_connection(cur, nxt):
    # print("bruh", cur, next)
    i_c, j_c = cur
    i_n, j_n = nxt 
    cur, nxt = dir_map[matrix[i_c][j_c]], dir_map[matrix[i_n][j_n]]
    nxt = set(map(lambda x: tuple([-1*i for i in x]), nxt))
    print(matrix[i_c][j_c], matrix[i_n][j_n], cur, nxt)
    # print(cur, next)
    return len(cur.intersection(nxt)) > 0 

for i, _ in enumerate(matrix):
    for j, c in enumerate(matrix[i]):
        pos = (i,j)
        if c == 'S':
            print(bfs(pos))
            exit(0)
