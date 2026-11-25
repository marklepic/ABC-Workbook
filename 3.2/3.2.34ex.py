r, c, t = [int(x) for x in input().split()]
students = [input().split() for x in range(r)]

FixedStudents = []
for x in range(r):
    if (x+1)%2 == 0: #starts odd
        FixedStudents.append(students[x][::-1])
    else:
        FixedStudents.append(students[x])

FlatStudents = [element for row in FixedStudents for element in row]

FinalStudents = []
for group in range(t):
    templist = []
    for s in range(0+group, len(FlatStudents), 4):
        templist.append(FlatStudents[s])
    FinalStudents.append(templist)



for row in FinalStudents:
    print(" ".join(row))

