n = int(input())
Flowers = [int(x) for x in input().split()]

NewFlowers = []
for f in range(1,len(Flowers)-1):
    if ((Flowers[f+1] > Flowers[f]) and (Flowers[f-1] < Flowers[f])) or ((Flowers[f+1] < Flowers[f]) and (Flowers[f-1] > Flowers[f])):
        NewFlowers.append(f+1)

print(*NewFlowers)