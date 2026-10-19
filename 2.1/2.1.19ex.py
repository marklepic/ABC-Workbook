Q = int(input())
Cards = [input().split() for x in range(Q)]

NewDeck = []
for c in Cards:
    SameValue = Cards[0][0] == c[0]
    SameSuit = Cards[0][2] == c[2]
    if not SameValue and not SameSuit:
        NewDeck.append(c)

if NewDeck == []:
    print('empty deck')
else:
    for c in NewDeck:
        print(*c)
