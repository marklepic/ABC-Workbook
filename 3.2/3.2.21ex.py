board = [list(input()) for x in range(8)]
KLoc = []
NLoc = []
RLoc = []
BLoc = []
QLoc = []

for x in range(8):
    for y in range(8):
        if board[x][y] == "K":
            KLoc.append([x, y])
        if board[x][y] == "N":
            NLoc = [x, y]
        if board[x][y] == "R":
            RLoc = [x, y]
        if board[x][y] == "B":
            BLoc = [x, y]
        if board[x][y] == "Q":
            QLoc = [x, y]



for v in range(8):
    if board[v][RLoc[1]] == ".":
        board[v][RLoc[1]] = "*"

for p in range(8):
    if board[RLoc[0]][p] == ".":
        board[RLoc[0]][p] = "*"

for row in board:
    print("".join(row))
