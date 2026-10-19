import math

x = int(input())
xsquared = list(str(x * x))

SquareSum = 0

for x in range(len(xsquared)):
    SquareSum += int(xsquared[x])

print(SquareSum)

