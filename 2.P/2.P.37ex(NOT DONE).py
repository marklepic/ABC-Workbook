n = int(input())

Primes = []
for x in range(1, n, -1): #for each number 10
    for g in range(x): #for each number before+the number 10times
        Factors = []
        for z in range(0, x-1): #range 0, 9
            num = x/(z+1) # 10%(0+1) = 10
            if num%1 == int(num):
                Factors.append(z)
            print(Factors)
        if (x in Factors) and (0 in Factors) and (len(Factors) == 3):
            Primes.append(x)

print(*Primes)