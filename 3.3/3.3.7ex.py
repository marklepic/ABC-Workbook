n = int(input())

LoggedIn = set()
NameNum = {}
AnsList = []
digit = 0
for event in range(n):
    Login = input()
    PName = Login.split()[1]
    if PName not in NameNum:
        NameNum[PName] = digit
        digit += 1
    AnsList.append(NameNum[PName])

print(*AnsList)