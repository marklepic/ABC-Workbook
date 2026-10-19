Q = int(input())
Cards = [input().split() for x in range(Q)]

ClubDeck = []
DiamondDeck = []
HeartDeck = []
SpadeDeck = []

for c in Cards:
    if c[2] == 'Clubs':
        ClubDeck.append(c)

for c in Cards:
    if c[2] == 'Diamonds':
        DiamondDeck.append(c)

for c in Cards:
    if c[2] == 'Hearts':
        HeartDeck.append(c)

for c in Cards:
    if c[2] == 'Spades':
        SpadeDeck.append(c)
NewDeck = ClubDeck+DiamondDeck+HeartDeck+SpadeDeck

for c in NewDeck:
    print(*c)