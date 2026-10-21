n = int(input()) #days\
QualityDay = [int(x) for x in input().split()]
q = int(input()) #amt of choco connoiseurs

for _ in range(q):
    l, r, x = [int(x) for x in input().split()]

    DayBought = -1
    if l == r:
        for z in range(l-1, r):
            if QualityDay[z] >= x:
                DayBought = z+1
                break
    else:
        for z in range(l-1, r-1):
            if QualityDay[z] >= x:
                DayBought = z+1
                break
    print(DayBought)
