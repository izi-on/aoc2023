from math import ceil, floor, sqrt


with open("input.txt") as f:
    def filt(x):
        if x:
            return x
    rows = f.read().split('\n')
    time_data = list(map(lambda x: x, list(filter(filt, rows[0].split(':')[1].split(' ')))))
    time = int("".join(time_data))
    dist_data = list(map(lambda x: x, list(filter(filt, rows[1].split(':')[1].split(' ')))))
    dist = int("".join(dist_data))


# solve (time - x ) * x = dist
# = - x^2 + x*time - dist = 0
middle = -time/(2*-1)
plus_minus = sqrt(time**2 - 4*-1*-dist)/(2*-1)
first = int(ceil(middle-plus_minus))
last = int(floor(middle+plus_minus))
print(abs(last-first+1))

