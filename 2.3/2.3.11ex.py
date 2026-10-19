n, m = [int(x) for x in input().split()]

UserList = []
for u in range(n):
    UserList.append(0)

for _ in range(m):
    User1, User2 = [int(x) for x in input().split()]
    UserList[User1-1] += 1
    UserList[User2-1] += 1

print(*UserList)