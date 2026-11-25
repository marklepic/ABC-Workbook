n = int(input())

LoggedIn = set()
NameNum = {}
AnsList = []
digit = 0
for event in range(n):
    Login = input()
    PName = Login.split()[1]
    if "out." in Login:
        LoggedIn.discard(PName)
    elif PName not in LoggedIn:
        if PName not in NameNum:
            NameNum[PName] = digit
            digit += 1    
        LoggedIn.add(PName)
        
LogInList = list(LoggedIn)

for name in LogInList:
    AnsList.append(NameNum[name])

print(*sorted(AnsList))