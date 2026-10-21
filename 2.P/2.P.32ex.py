n = int(input())
Deck = [int(x) for x in input().split()]

TopDeck = []
for x in range(0, len(Deck), 2):
    TopDeck.append(Deck[x])

BotDeck = []
for x in range(1, len(Deck), 2):
    BotDeck.append(Deck[x])

NewDeck = TopDeck + BotDeck
print(*NewDeck)