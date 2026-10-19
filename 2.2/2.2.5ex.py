Q = int(input())
Deck = [input().split() for x in range(Q)]

FirstCardValue = Deck[0][0]
Counter = 0

for c in Deck:
    if c[0] == FirstCardValue:
        Counter += 1

print(Counter)