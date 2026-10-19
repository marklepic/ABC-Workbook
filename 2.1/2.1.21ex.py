Q = int(input())
Cards = [input().split() for x in range(Q)]

SuitStrength = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
BotCardSuit = Cards[-1][2]
NewDeck = []
for c in Cards:
    StrongerSuit = SuitStrength.index(c[2]) > SuitStrength.index(BotCardSuit)
    if not StrongerSuit:
        NewDeck.append(c)

for c in NewDeck:
    print(*c)
