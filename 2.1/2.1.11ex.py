Q = int(input())
Flowers = [int(x) for x in input().split()]

tall = []

if Flowers[0] > Flowers[1]:
    tall.append(0)

for flower in range(1, len(Flowers) - 1):
    if Flowers[flower] > Flowers[flower + 1] and Flowers[flower] > Flowers[flower - 1]:
        tall.append(flower)

if Flowers[-1] > Flowers[-2]:
    tall.append(len(Flowers) - 1)

for flower in tall:
    Flowers[flower] -= 2

print(*Flowers)