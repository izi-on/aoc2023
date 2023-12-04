with open("input.txt") as f:
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

def around(coord, ch):
    global total 
    x,y = coord
    for i in range(3):
        for j in range(3):
            
            if i == 1 and j == 1:
                continue

            y_p, x_p = y - 1 + i, x - 1 + j

            if visited[y_p][x_p] or not in_range((x_p, y_p)):
                continue

            visited[y_p][x_p] = True

            if is_digit(matrix[y_p][x_p]):
                res = get_num((x_p, y_p))
                total += res

for y, _ in enumerate(matrix):
    for x, _ in enumerate(matrix[y]):
        if not matrix[y][x].isalnum() and matrix[y][x] != '.':
            around((x,y), matrix[y][x])

print(total)