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

for v in range(len(KLoc)):
    for a in range(max(0, KLoc[v][0]-1), min(8, KLoc[v][0]+2)):
        for b in range(max(0, KLoc[v][1]-1), min(8, KLoc[v][1]+2)):
            if board[a][b] == ".":
                board[a][b] = "*"

for row in board:
    print("".join(row))
