n, k, x = [int(x) for x in input().split()]
ChestTables = []
for z in range(n):
    ChestTables.append([int(x) for x in input().split()])


SortedChests = []
for c in ChestTables:
    SortedChests.append(sorted(c))



MinSum = 0
MaxSum = 0

for c in SortedChests:
  
    MinSum += int(c[0])
    MaxSum += int(c[-1])



if (MinSum > x) or (MinSum == x):
    print('ALWAYS')
elif (MinSum < x) and (MaxSum >= x):
    print('SOMETIMES')
else:
    print('NEVER')
