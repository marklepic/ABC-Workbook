i = int(input())
n = [int(x) for x in input().split()]

Total = 0
if i == 1:
    if n[0] == 7:
        Total += 7
else:
    if n[0] == 7:
        Total += n[0]
    elif n[1] == 7:
        Total += n[0]

    for s in range(1, len(n)-1):
        if n[s] == 7:
            Total += n[s]
        elif (n[s-1] == 7) or (n[s+1] == 7):
            Total += n[s]

    if n[-1] == 7:
        Total += n[-1]
    elif n[-2] == 7:
        Total += n[-1]

print(Total)