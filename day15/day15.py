from collections import defaultdict, deque

with open("input.txt") as f:
    inputs = f.read().split(",")
inputs[-1] = inputs[-1][:-1]
hm = [deque() for _ in range(256)]
for input in inputs:
    current_val = 0
    if "-" in input:
        input = input.split("-")[0]
        op = 1
    else:
        print(input)
        input, label = input.split("=")[0], input.split("=")[1]
        op = 0
    for c in input:
        if not input:
            continue
        current_val += ord(c)
        current_val *= 17
        current_val %= 256
    if op == 1:
        entry = hm[current_val]
        try:
            entry = deque(list(filter(lambda x: x[0] != input, entry)))
            hm[current_val] = entry
        except:
            pass
    else:
        entry = hm[current_val]
        found = False
        for obj in entry:
            if obj[0] == input:
                obj[1] = label
                found = True
                break
        if not found:
            entry.append([input, label])
answer = 0
for i, entry in enumerate(hm):
    for j, obj in enumerate(entry):
        answer += (i + 1) * (j + 1) * int(obj[1])
print(answer)
