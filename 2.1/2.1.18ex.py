Q = int(input())
Cards = [input() for x in range(Q)]

NewDeck = [Cards[-1]]

for c in range(1, len(Cards)-1):
    NewDeck.append(Cards[c])

NewDeck.append(Cards[0])

for c in NewDeck:
    print(c)