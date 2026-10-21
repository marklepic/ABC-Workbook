s = input()

Alice = ["A","l","i","c","e"]
Bob = ["B","o","b"]
Cindy = ["C","i","n","d","y"]

AliceCount = 0
BobCount = 0
CindyCount = 0
if len(s) == 5:
    for c in range(len(s)):
        if (s[c] != Alice[c]) and (s[c] != Cindy[c]) and (s[c] != "."):
            print("SOMETHING'S WRONG")
            break
        elif s == ".....":
            print("CAN'T TELL")
            break
        elif s[c] == Alice[c]:
            AliceCount += 1
        elif s[c] == Cindy[c]:
            CindyCount += 1
        elif s[c] == ".":
                CindyCount += 1
                AliceCount += 1
elif len(s) == 3:
    for c in range(len(s)):
        if (s[c] != Bob[c]) and (s[c] != "."):
            print("SOMETHING'S WRONG")
              
            break
        elif s[c] == Bob[c]:
            BobCount += 1
        elif s[c] == ".":
            BobCount += 1
else:
    print("SOMETHING'S WRONG")
    

if AliceCount == 5:
    print("Alice")
elif BobCount == 3:
    print("Bob")
elif CindyCount == 5:
    print("Cindy")