n = int(input())
PaperPerm = [int(x) for x in input().split()]

PaperStatus = []
for s in range(n):
    PaperStatus.append(0)

for x in range(n):
    Index = PaperPerm[x]
    if Index == 1:
        BigNeighbor = PaperStatus[Index]
    elif Index == n:
        BigNeighbor = PaperStatus[Index-2]
    else:
        BigNeighbor = max([PaperStatus[Index], PaperStatus[Index-2]])
    PaperStatus[Index-1] = BigNeighbor + 1

print(*PaperStatus)