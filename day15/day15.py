with open("input.txt") as f:
    inputs = f.read().split(",")
inputs[-1] = inputs[-1][:-1]
print(inputs)
answer = 0
for input in inputs:
    current_val = 0
    for c in input:
        if not input:
            continue
        current_val += ord(c)
        current_val *= 17
        current_val %= 256
    print(input, current_val)
    answer += current_val
print(answer)
