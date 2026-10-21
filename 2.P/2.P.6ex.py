n = int(input())
Flowers = [int(x) for x in input().split()]

for f in range(len(Flowers)):
    Flowers[f] *= 2

print(*Flowers)