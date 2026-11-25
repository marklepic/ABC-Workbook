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
            BLoc.append([x, y])
        if board[x][y] == "Q":
            QLoc.append([x, y])

Moves = [
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

for Pieces in range(len(QLoc)):
    for move in Moves:
        a = QLoc[Pieces][0] + move[0]
        b = QLoc[Pieces][1] + move[1]

        while 0 <= a < 8 and 0 <= b < 8:

            if board[a][b] == ".":
                board[a][b] = "*"

            a += move[0]
            b += move[1]

    for v in range(8):
        if board[v][QLoc[Pieces][1]] == ".":
            board[v][QLoc[Pieces][1]] = "*"

    for p in range(8):
        if board[QLoc[Pieces][0]][p] == ".":
            board[QLoc[Pieces][0]][p] = "*"

    for k in range(max(0, QLoc[Pieces][0]-1), min(8, QLoc[Pieces][0]+2)):
        for l in range(max(0, QLoc[Pieces][1]-1), min(8, QLoc[Pieces][1]+2)):
            if board[k][l] == ".":
                board[k][l] = "*"

for row in board:
    print("".join(row))