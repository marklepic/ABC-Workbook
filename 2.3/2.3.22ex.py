n = int(input())
deck = []
for x in range(n):
    deck.append(x)

TopDeck = deck[:int(n/2)]
BotDeck = deck[int(n/2):]
NewDeck = []

for c in range(len(TopDeck)):
    NewDeck.append(TopDeck[c])
    NewDeck.append(BotDeck[c])

counter = 1

while NewDeck != deck:
    TopDeck = NewDeck[:int(n/2)]
    BotDeck = NewDeck[int(n/2):]
    NewDeck = []
    for c in range(len(TopDeck)):
        NewDeck.append(TopDeck[c])
        NewDeck.append(BotDeck[c])
    counter += 1

print(counter)