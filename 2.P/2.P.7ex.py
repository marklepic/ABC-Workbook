n = int(input())
Flowers = [int(x) for x in input().split()]

NewFlowers = []
for f in range(0,len(Flowers)-1):
    if Flowers[f+1] > Flowers[f]:
        NewFlowers.append(Flowers[f]-1)
    else:
        NewFlowers.append(Flowers[f])
NewFlowers.append(Flowers[-1])

print(*NewFlowers)