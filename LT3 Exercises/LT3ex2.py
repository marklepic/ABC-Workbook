n = int(input())

StudentSet = set()
StudentDict = {}
for _ in range(n):
    Event = input().split()
    TempName = Event[0]
    StudentSet.add(TempName)
    StudentDict[TempName] = 0
    if "GRADE" in Event:
        TempGrade = Event[2]
        StudentDict[TempName] = TempGrade
    else:
        TempMate = Event[2]
        if TempMate in StudentSet:
            StudentDict[TempName] = StudentDict[TempMate]

SortStudent = sorted(StudentDict)
for name in SortStudent:
    print(f'{name} {StudentDict[name]}')

