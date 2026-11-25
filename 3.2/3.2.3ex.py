n = int(input())
grid = []

for s in range(n):
    k = int(input())
    grid.append(input().split())

q = int(input())
CheckList = [input() for x in range(q)]

for name in range(q):
    count = 0
    for day in range(n):
        if CheckList[name] in grid[day]:
            count += 1
    if count == n:
        print("ALL")
    elif count == 0:
        print("NONE")
    else:
        print("SOME")

