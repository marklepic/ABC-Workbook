n = int(input()) #number of vinyls
VinylsPrice = [int(x) for x in input().split()]
VinylsYear = [int(x) for x in input().split()]

Total = 0
for x in range(n):
    if VinylsYear[x] >= 2000:
        Total += VinylsPrice[x]/2
    elif VinylsYear[x] > 1960:
        Total += VinylsPrice[x]*(1.105**(2024-VinylsYear[x]))

print(f'{Total:.2f}')

