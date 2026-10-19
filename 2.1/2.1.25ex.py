Q = int(input())
Cards = [input().split() for x in range(Q)]

TopDeck = Cards[:int(Q/2)]
BotDeck = Cards[int(Q/2):]
NewDeck = []

for c in range(len(TopDeck)):
    NewDeck.append(TopDeck[c])
    NewDeck.append(BotDeck[c])

for c in NewDeck:
    print(*c)