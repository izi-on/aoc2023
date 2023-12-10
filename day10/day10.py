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
    'J': {(-1,0), (-1,0)},
    '7': {(1,0), (0,-1)},
    'S': {(-1,0), (0,-1), (1,0), (0,1)},
    '.': {(0,0), (0,0)},
}

def bfs(pos):
    global visited, matrix
    queue = deque([pos])
    longest = -1
    while len(queue) > 0:
        n = len(queue)
        longest += 1
        for _ in range(n):
            cur = queue.popleft()
            if cur in visited: continue
            visited.add(cur)
            for next in get_valid(cur):
                queue.append(next)
    return longest

def get_valid(cur):
    deltas = [(0,1), (0,-1), (1,0), (-1,0)]
    valid = []
    for delta in deltas:
        dest = tuple(sum(x) for x in zip(cur,delta))
        if 0 <= dest[0] < len(matrix) and\
            0 <= dest[1] < len(matrix[0]) and\
                is_valid_connection(cur, dest):
            valid.append(dest)
    return valid
        
def is_valid_connection(cur, next):
    # print("bruh", cur, next)
    i_c, j_c = cur
    i_n, j_n = next
    cur, next = dir_map[matrix[i_c][j_c]], dir_map[matrix[i_n][j_n]]
    cur = set(map(lambda x: tuple([-1*i for i in x]), cur))
    # print(cur, next)
    return len(cur.intersection(next)) > 0 

for i, _ in enumerate(matrix):
    for j, c in enumerate(matrix[i]):
        pos = (i,j)
        if c == 'S':
            print(bfs(pos))
            exit(0)
