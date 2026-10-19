NumLength = int(input())
Numbers = [int(input()) for x in range(NumLength)]

for x in Numbers:
    if x % 2 == 0:
        print('EVEN')
    else:
        print('ODD')
