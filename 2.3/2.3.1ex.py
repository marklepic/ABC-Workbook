Start = input()
StartTasks = int(Start[6:])
n = int(input())

for _ in range(n):
    NewEvent = input()
    NewTasks = int(NewEvent[7:])
    if "FINISH" in NewEvent:
        StartTasks -= NewTasks
    else:
        StartTasks += NewTasks
print(StartTasks)