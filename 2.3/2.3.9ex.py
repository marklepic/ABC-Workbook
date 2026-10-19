n = int(input())
Flowers = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    Operation = input()
    if Operation == "AVERAGE":
        L, R = [int(x) for x in input().split()]
        FlowerRange = Flowers[L - 1:R]
        ans = sum(FlowerRange)/len(FlowerRange)
        print(f'{ans:.2f}')
    elif Operation == "COUNT":
        L, R, k = [int(x) for x in input().split()]
        FlowerRange = Flowers[L - 1:R]
        Count = 0
        for f in FlowerRange:
            if k >= f:
                Count += 1
        print(Count)
    elif Operation == "INCREASE":
        L, R, k = [int(x) for x in input().split()]
        for t in range(L - 1, R):
            Flowers[t] += k
    elif Operation == "SORT":
        Direction = input()
        if Direction == "+":
            Flowers = sorted(Flowers)
        else:
            Flowers = sorted(Flowers, reverse = True)
