Word = list(input())
n = int(input())

for _ in range(n):
    student = input()
    k = int(student[:-2]) - 1
    x = student[-1]
    Word[k] = x

print("".join(Word))