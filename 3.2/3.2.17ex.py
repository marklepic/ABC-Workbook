board = [list(input()) for x in range(8)]
KLoc = []
NLoc = []
RLoc = []
BLoc = []
QLoc = []

for x in range(8):
    for y in range(8):
        if board[x][y] == "K":
            KLoc = [x, y]
        if board[x][y] == "N":
            NLoc = [x, y]
        if board[x][y] == "R":
            RLoc = [x, y]
        if board[x][y] == "B":
            BLoc = [x, y]
        if board[x][y] == "Q":
            QLoc = [x, y]
    
for a in range(max(0, KLoc[0]-1), min(8, KLoc[0]+2)):
    for b in range(max(0, KLoc[1]-1), min(8, KLoc[1]+2)):
        if board[a][b] == ".":
            board[a][b] = "*"

for row in board:
    print("".join(row))
