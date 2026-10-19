Q = int(input())
Deck = [input().split() for x in range(Q)]

Counter = 0

if len(Deck) == 1:
     Counter = 0
else:
    for c in range(len(Deck)):
        if Deck[c][2] == "Diamonds" or Deck[c][2] == "Hearts":
            Deck[c][2] = "red"
        if Deck[c][2] == "Clubs" or Deck[c][2] == "Spades":
                Deck[c][2] = "black"

    if Deck[0][2] == Deck[1][2]:
        Counter += 1

    if Deck[-1][2] == Deck[-2][2]:
        Counter += 1

    for c in range(1, len(Deck) - 1):
        BeforeSame = Deck[c][2] == Deck[c - 1][2] 
        NextSame = Deck[c][2] == Deck[c + 1][2]
        BothSame = BeforeSame == NextSame
        if (not BothSame) and (BeforeSame or NextSame):
            Counter += 1

print(Counter)