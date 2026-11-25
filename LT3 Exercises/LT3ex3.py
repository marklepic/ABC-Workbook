n, b = [int(x) for x in input().split()]
sausages = [int(x) for x in input().split()]

Count = 0
#4 ppl
for a in range(n):
    for z in range(n):
        for c in range(n):
            for d in range(n):
                if (sausages[a] + sausages[z] + sausages[c] + sausages[d]) == b:
                    Count += 1

print(Count)