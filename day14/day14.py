with open("input.txt") as f:
    input = f.read().split("\n")
input = list(map(list, input))[:-1]
input = list(map(list, zip(*input)))

total_count = 0

for inp in input:
    inp = ["#"] + inp + ["#"]  # type: ignore
    rocks_idx = (i for i, val in enumerate(inp) if val == "#")
    prev = 0
    for idx in rocks_idx:
        s_weight = len(inp) - prev - 1
        rock_count = sum([1 for val in inp[prev:idx] if val == "O"])
        end_sum = s_weight - rock_count
        total_count += s_weight * (s_weight + 1) // 2 - end_sum * (end_sum + 1) // 2
        prev = idx + 1
print(total_count)
