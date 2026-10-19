m, n = [int(x) for x in input().split()]
Classmates = [False for _ in range(m)]
Classmates[0] = True

for _ in range(n):
    x, y = [int(x) for x in input().split()]
    if (Classmates[x] == True) or (Classmates[y] == True):
            Classmates[x] = True
            Classmates[y] = True

Count = 0
for K in Classmates:
    if K == True:
        Count += 1

print(Count)