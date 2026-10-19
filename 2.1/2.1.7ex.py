Q = int(input())
plates = [int(x) for x in input().split()]

OddPlates = []
EvenPlates = []

for plate in plates:
    if plate % 2 == 0:
        EvenPlates.append(plate)
    else:
        OddPlates.append(plate)         

print(*sorted(OddPlates))
print(*sorted(EvenPlates))