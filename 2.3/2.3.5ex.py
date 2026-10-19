n = int(input())
Flowers = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    FlowerRange = Flowers[L - 1:R]
    print(max(FlowerRange))