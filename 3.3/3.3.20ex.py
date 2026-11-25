n, m = [int(x) for x in input().split()]
AliceHand = [int(x) for x in input().split()]
BobHand = [int(x) for x in input().split()]

AliceDict = {}
BobDict = {}
for card in AliceHand:
    if card not in AliceDict:
        AliceDict[card] = 1
    else:
        digit = AliceDict[card]
        digit += 1
        AliceDict[card] = digit

for card in BobHand:
    if card not in BobDict:
        BobDict[card] = 1
    else:
        digit = BobDict[card]
        digit += 1
        BobDict[card] = digit

Discards = 0
AliceUniList = sorted(set(AliceHand))
BobUniList = sorted(set(BobHand))
AliceSet = set(AliceHand)
BobSet = set(BobHand)
for card in AliceUniList:
    if card not in BobSet:
        Discards += AliceDict[card]
    else:
        Discards += (abs(AliceDict[card] - BobDict[card]))

for card in BobUniList:
    if card not in AliceSet:
        Discards += BobDict[card]

print(Discards)
