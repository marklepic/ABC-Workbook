n,m,L,R = [int(x) for x in input().split()]
xCords = [0] + [int(x) for x in input().split()]
yCords = [0] + [int(x) for x in input().split()]
Count = 0

#rectangle 1234
for yrec in range(m):
    for xrec in range(n):
            x1 = xCords[xrec]
            y1 = yCords[yrec] 
            x2 = xCords[xrec+1]
            y2 = yCords[yrec+1]
            area = (x1-x2)*(y1-y2)
            if (area >= L) and (area <= R):
                Count += 1

print(Count)