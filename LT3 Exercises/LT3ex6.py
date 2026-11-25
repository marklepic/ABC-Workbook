n, k = [int(x) for x in input().split()]
Locs = [int(x) for x in input().split()]

LocsSet = set(Locs)
count = 0
for x in range(n):
    for y in range(Locs[x] - k, Locs[x] + k):
        if (y in LocsSet) and (y != Locs[x]):
            count += 0.5

print(count)