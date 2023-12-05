# read from input.txt and split "\n"

nums = [str(i) for i in range(10)]

num_map = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

total = 0;

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    ptr1, ptr2 = 0, len(line)-1
    d1, d2 = -1, -1
    while ptr1 < len(line):
        if line[ptr1] in nums:
            d1 = int(line[ptr1])
            break

        for j in range(3, 6):
            sub_str = line[ptr1:min(ptr1+j, len(line))]
            if sub_str in num_map.keys():
                d1 = num_map[sub_str]
                break
        
        if d1 != -1:
            break

        ptr1 += 1
    while 0 <= ptr2:
        if line[ptr2] in nums:
            d2 = int(line[ptr2])
            break

        for j in range(3, 6):
            sub_str = line[max(ptr2-j+1,0):ptr2+1]
            if sub_str in num_map.keys():
                d2 = num_map[sub_str]
                break
        
        if d2 != -1:
            break

        ptr2 -= 1

    total += d1*10 + d2

print(total)