n, m = [int(x) for x in input().split()]
Students = []
for x in range(n):
    Students.append(0)

for _ in range(m):
    a = int(input())
    Attendees = [int(x) for x in input().split()]
    for b in range(len(Attendees)):
        Students[Attendees[b]-1] += 1

GoodNoodles = []
SuperGoodNoodles = []
for x in range(n):
    if m % 2 == 1:
        if Students[x] >= int(m/2)+1:
            GoodNoodles.append(x+1)
        if Students[x] == m:
            SuperGoodNoodles.append(x+1)
    else:
        if Students[x] >= int(m/2):
            GoodNoodles.append(x+1)
        if Students[x] == m:
            SuperGoodNoodles.append(x+1)

print(len(GoodNoodles))
print(*GoodNoodles)
print(len(SuperGoodNoodles))
print(*SuperGoodNoodles)