row, col = [int(x) for x in input().split()]
grid = [list(input()) for x in range(row)]

RLoc = []
BLoc = []
for r in range(row):
    for c in range(col):
        if grid[r][c] == "R":
            RLoc.append([r, c])
        if grid[r][c] == "B":
            BLoc.append([r, c])


if RLoc[0][0] == RLoc[1][0]:
    for c in range(RLoc[0][1] + 1, RLoc[1][1]):
        if grid[RLoc[0][0]][c] == ".":
            grid[RLoc[0][0]][c] = "R"
        elif grid[RLoc[0][0]][c] == "B":
            grid[RLoc[0][0]][c] = "P"
else:
    for r in range(RLoc[0][0] + 1, RLoc[1][0]):
        if grid[r][RLoc[0][1]] == ".":
            grid[r][RLoc[0][1]] = "R"
        elif grid[r][RLoc[0][1]] == "B":
            grid[r][RLoc[0][1]] = "P"

if BLoc[0][0] == BLoc[1][0]:
    for c in range(BLoc[0][1] + 1, BLoc[1][1]):
        if grid[BLoc[0][0]][c] == ".":
            grid[BLoc[0][0]][c] = "B"
        elif grid[BLoc[0][0]][c] == "R":
            grid[BLoc[0][0]][c] = "P"
else:
    for r in range(BLoc[0][0] + 1, BLoc[1][0]):
        if grid[r][BLoc[0][1]] == ".":
            grid[r][BLoc[0][1]] = "B"
        elif grid[r][BLoc[0][1]] == "R":
            grid[r][BLoc[0][1]] = "P"

for row in grid:
    print("".join(row))
