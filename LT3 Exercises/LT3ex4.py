n = int(input())

FamDict = {}
for _ in range(n):
    Event = input().split()
    TempParent = Event[0]
    TempChild = Event[5][:-1]
    FamDict[TempChild] = TempParent

FindName = input()
GrandKids = []
FamList = list(FamDict)
FamSet = set(FamList)
FamSet.add(FamDict.values())
FamValues = set(FamDict.values())
if FindName in FamSet:
    if FindName in FamValues:
        for x in range(len(FamList)):
            Parent = FamDict[FamList[x]]
            if FamDict[FamList[x]] == FindName:
                pass
            elif FamDict[FamDict[FamList[x]]] == FindName:
                GrandKids.append(FamList[x])
        if GrandKids == []:
            print("NO GRANDCHILDREN")
        else:
            Ans = sorted(GrandKids)
            print(*Ans)
    else:
        print("NO GRANDCHILDREN")
else:
    print("NOT A RELATIVE")



#famlist[x] = cidny
#FamDict[famlist[x]] = bob
