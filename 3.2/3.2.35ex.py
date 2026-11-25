grid = [list(input()) for x in range(6)]

ZeroToNineLoc = []
for digit in range(10):
    for y in range(6):
        for x in range(6):
            if grid[y][x] == str(digit):
                ZeroToNineLoc.append([x, y])

Moves = [
    [0, 1, "S"],
    [0, -1, "N"],
    [1, 0, "E"],
    [-1, 0, "W"] #NSEW
]
DirectionList = []
for num in range(9):
    for move in range(4):
        a = ZeroToNineLoc[num][0] + Moves[move][0]
        b = ZeroToNineLoc[num][1] + Moves[move][1]

        if (a == ZeroToNineLoc[num+1][0]) and (b == ZeroToNineLoc[num+1][1]):
            DirectionList.append(Moves[move][2])

print("".join(DirectionList))
    