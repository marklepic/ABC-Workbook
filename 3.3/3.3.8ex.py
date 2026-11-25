n = int(input())

LoggedIn = set()
NameNum = {}
AnsList = []
digit = 0
for event in range(n):
    Login = input()
    PName = Login.split()[1]
    if PName not in LoggedIn:
        LoggedIn.add(PName)
        NameNum[digit] = PName
        digit += 1

x = int(input())

if x >= digit:
    print("ID not found")
else:
    print(NameNum[x])

