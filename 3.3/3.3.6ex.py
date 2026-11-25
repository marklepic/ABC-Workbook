n = int(input())

LoggedIn = set()
for event in range(n):
    Login = input()
    PName = Login.split()[1]
    #if "out." in Login:
        #LoggedIn.discard(PName)
    #else:
    LoggedIn.add(PName)

print(len(LoggedIn))