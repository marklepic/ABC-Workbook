Keyboard = [list(input()) for x in range(3)]
Type = list(input())

TypeLocs = [[0, 0]]
for t in range(len(Type)):
    for r in range(3):
        for c in range(len(Keyboard[r])):
            if Keyboard[r][c] == Type[t]:
                TypeLocs.append([r, c])

InputsNeeded = 1
for loc in range(0, len(Type)):
    InputNum = abs(TypeLocs[loc][0] - TypeLocs[loc + 1][0]) + abs(TypeLocs[loc][1] - TypeLocs[loc + 1][1])
    InputsNeeded += InputNum + 1

print(InputsNeeded)

