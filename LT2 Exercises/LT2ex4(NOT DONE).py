s = int(input())
claps = 0
CurrentNum = s
CurrentNumList = [str(x) for x in str(CurrentNum)]

while (CurrentNum != 42) and (CurrentNum != 1):
    TempCount = 0
    for z in range(len(CurrentNumList)):
        TempCount += int(CurrentNumList[z])**2
    claps += 1
    CurrentNum = TempCount
    CurrentNumList = [str(x) for x in str(CurrentNum)]

print(claps)
print(CurrentNum)