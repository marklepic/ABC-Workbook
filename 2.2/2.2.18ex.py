n, WinNum = [int(x) for x in input().split()]
Players = [input().split() for x in range(n)]

NumOnlyList = []
for x in range(len(Players)):
    NumOnlyList.append(int(Players[x][1]))

PlayerNum = 0
WinnerAmt = 0
for x in range(len(NumOnlyList)):
    if NumOnlyList[x] == WinNum:
        WinnerAmt += 1
        PlayerNum = x

if WinnerAmt == 1:
    print("".join(Players[PlayerNum][0]))
else:
    print('no winner')
