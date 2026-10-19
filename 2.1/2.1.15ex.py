Q = int(input())
Flowers = [int(x) for x in input().split()]
RK = [int(x) for x in input().split()]
R = RK[0]-1
K = RK[1]

for f in range(0,R):
    Flowers[f] = K

print(*Flowers)