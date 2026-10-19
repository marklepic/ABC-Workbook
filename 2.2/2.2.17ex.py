Jumble = list(input())

Alocation = 0
Blocation = 0
for q in range(len(Jumble)):
    if Jumble[q] == "a":
        Alocation = q
        break

for q in range(len(Jumble)):
    if Jumble[q] == "b":
        Blocation = q
        break

if Blocation > Alocation:
    for q in range(Alocation + 1, Blocation):
        Jumble[q] = "*"
else:
    for q in range(Blocation + 1, Alocation):
            Jumble[q] = "*"

print("".join(Jumble))