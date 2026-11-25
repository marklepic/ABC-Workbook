row, col = [int(x) for x in input().split()]
grid = [list(input()) for x in range(row)]
ALoc = []
BLoc = []

for x in range(row):
    for y in range(col):
        if grid[x][y] == "A":
            ALoc = [x, y]
        if grid[x][y] == "B":
            BLoc = [x, y]

ans = abs(ALoc[0]-BLoc[0]) + abs(ALoc[1]-BLoc[1])

print(ans)



