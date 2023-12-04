from functools import reduce

with open("input2.txt") as f:
    matrix = f.read().split("\n")
    
visited = [[False for _ in matrix[0]] for _ in matrix] 

nums = {str(i) for i in range(10)}

total = 0

def in_range(coord):
    x,y = coord
    return 0 <= x and x < len(matrix[0]) and 0 <= y and y < len(matrix)

def is_digit(c):
    return c in nums

def get_num(coord):
    x,y = coord
    ptr = 1
    num = [matrix[y][x]]
    while in_range((x+ptr,y)) and not visited[y][x+ptr] and is_digit(matrix[y][x+ptr]):
        num.append(matrix[y][x+ptr])
        visited[y][x+ptr] = True
        ptr += 1
    ptr = -1
    while in_range((x+ptr,y)) and not visited[y][x+ptr] and is_digit(matrix[y][x+ptr]):
        num.insert(0, matrix[y][x+ptr])
        visited[y][x+ptr] = True
        ptr -= 1
    return int("".join(num))

def around(coord):
    global total 
    x,y = coord

    slots = [0,0]
    sl_idx = 0

    for i in range(3):
        for j in range(3):
            
            if i == 1 and j == 1:
                continue

            y_p, x_p = y - 1 + i, x - 1 + j

            if not in_range((x_p, y_p)) or visited[y_p][x_p]:
                continue

            visited[y_p][x_p] = True

            if is_digit(matrix[y_p][x_p]):
                slots[sl_idx] = int(get_num((x_p, y_p)))
                sl_idx = min(1, sl_idx+1)
    
    # print(slots)
    return reduce(lambda x,y: x*y, slots, 1)


for y, _ in enumerate(matrix):
    for x, _ in enumerate(matrix[y]):
        if matrix[y][x] == '*':
            total += around((x,y))

print(total)