n = int(input())
Flowers = [int(x) for x in input().split()]

NewFlowers = []
if Flowers[1] == Flowers[0]:
    NewFlowers.append(Flowers[0]+3)
else:
    NewFlowers.append(Flowers[0])

for f in range(1,len(Flowers)-1):
    if (Flowers[f+1] == Flowers[f]) or (Flowers[f-1] == Flowers[f]):
        NewFlowers.append(Flowers[f]+3)
    else:
        NewFlowers.append(Flowers[f])

if Flowers[-1] == Flowers[-2]:
    NewFlowers.append(Flowers[-1]+3)
else:
    NewFlowers.append(Flowers[-1])

print(*NewFlowers)