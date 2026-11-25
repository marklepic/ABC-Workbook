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
            QLoc = [x, y]

Moves = [
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

for Pieces in range(len(BLoc)):
    for move in Moves:
        a = BLoc[Pieces][0] + move[0]
        b = BLoc[Pieces][1] + move[1]

        while 0 <= a < 8 and 0 <= b < 8:

            if board[a][b] == ".":
                board[a][b] = "*"

            a += move[0]
            b += move[1]

for row in board:
    print("".join(row))