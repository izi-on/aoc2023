from copy import deepcopy
from pprint import pprint
with open("input.txt") as f:
    matrix = f.read().split("\n")[:-1]
print(matrix)

#expand rows
i = 0
ex_row = set()
while i < len(matrix):
    row = matrix[i]
    if '#' not in row: 
        ex_row.add(i)
        matrix.insert(i, row)
        i += 1
    i += 1

#expand colkmns
cols = list(zip(*matrix))
inserted = 0
i = 0
ex_col = set()
while i < len(cols):
    col = cols[i]
    if '#' not in col:
        ex_col.add(i)
        cols.insert(i, col)
        i += 1
    i += 1

matrix = list(map(lambda x: list(x), zip(*cols)))
print(matrix)

starts = []
expansion = 1000000
pos_i = 0
for i in range(len(matrix)):
    if i in ex_row:
        pos_i += expansion-2
    pos_j = 0
    for j in range(len(matrix[0])):
        if j in ex_col:
            pos_j += expansion-2
        if matrix[i][j]=='#':
            starts.append((pos_i,pos_j))
        pos_j += 1
    pos_i += 1

print(sum([abs(a[0]-b[0])+abs(a[1]-b[1]) for a in starts for b in starts])//2)
