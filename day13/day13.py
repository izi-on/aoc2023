with open("input.txt") as f:
    input = f.read().split("\n")
gen = (i for i, val in enumerate(input) if not val)

prev = 0
matrices = []
for i in gen:
    matrices.append(input[prev:i])
    prev = i + 1
print(matrices)


def vertical(matrix, i):
    smudges = 0
    for j in range(min(i + 1, len(matrix[0]) - i - 1)):
        for k in range(len(matrix)):
            if matrix[k][i - j] != matrix[k][i + j + 1]:
                if smudges == 1:
                    return 0
                else:
                    smudges += 1
    return i + 1 if smudges == 1 else 0


def horizontal(matrix, i):
    smudges = 0
    for j in range(min(i + 1, len(matrix) - i - 1)):
        for k in range(len(matrix[0])):
            if matrix[i - j][k] != matrix[i + j + 1][k]:
                if smudges == 1:
                    return 0
                else:
                    smudges += 1
    return i + 1 if smudges == 1 else 0


total = 0
for matrix in matrices:
    # check vertical reflection
    for i in range(len(matrix[0]) - 1):
        total += vertical(matrix, i)
    # check horizontal reflection
    for i in range(len(matrix) - 1):
        total += 100 * horizontal(matrix, i)

print(total)
