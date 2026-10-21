n = int(input())
PkmnPower = [int(x) for x in input().split()]
FightTotal = [0] * n

pokemen = list(range(n))
winners = []
while len(pokemen) > 1:
    for z in range(0, len(pokemen), 2):
        a = pokemen[z]
        b = pokemen[z+1]
        FightTotal[a] += 1
        FightTotal[b] += 1
        if PkmnPower[a] > PkmnPower[b]:
            winners.append(a)
        else:
            winners.append(b)

    pokemen = winners

print(winners)
print(FightTotal)
           

             