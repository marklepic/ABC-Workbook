Q = int(input())
Directions = list(input())

FlipDirections = []
for d in range(len(Directions)):
    FlipDirections.append(Directions[-1*(d+1)])

NewDirections = []
for d in FlipDirections:
    if d == "N":
        NewDirections.append('S')
    elif d == "S":
        NewDirections.append('N')
    elif d == "E":
        NewDirections.append('W')
    elif d == "W":
        NewDirections.append('E')

print("".join(NewDirections))