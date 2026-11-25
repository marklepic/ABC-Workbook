Q = int(input())
LRK = [input().split() for x in range(Q)]
N = int(input())
Flowers = [int(x) for x in input().split()]

for question in range(Q):
    count = 0
    for f in range(int(LRK[question][0])-1, int(LRK[question][1])):
        if Flowers[f] <= int(LRK[question][2]):
            count += 1
    print(count)

