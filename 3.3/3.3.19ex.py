n = int(input())
grid = [list(input()) for x in range(n)]
FLatGrid = [element for row in grid for element in row]

LetterCount = {'a': 0, 
        'b': 0, 
        'c': 0, 
        'd': 0, 
        'e': 0, 
        'f': 0, 
        'g': 0, 
        'h': 0, 
        'i': 0, 
        'j': 0, 
        'k': 0, 
        'l': 0, 
        'm': 0, 
        'n': 0, 
        'o': 0, 
        'p': 0, 
        'q': 0, 
        'r': 0, 
        's': 0, 
        't': 0, 
        'u': 0, 
        'v': 0, 
        'w': 0, 
        'x': 0, 
        'y': 0, 
        'z': 0, 
        } 

for letter in FLatGrid:
        digit = LetterCount[letter]
        digit += 1
        LetterCount[letter] = digit

LetterList = ['a', 
        'b', 
        'c', 
        'd', 
        'e', 
        'f', 
        'g', 
        'h', 
        'i', 
        'j', 
        'k', 
        'l', 
        'm', 
        'n', 
        'o', 
        'p', 
        'q', 
        'r', 
        's', 
        't', 
        'u', 
        'v', 
        'w', 
        'x', 
        'y', 
        'z', 
        ] 


BeautyList = []
for letter in LetterList:
    BeautyList.append(LetterCount[letter] + 1)

BiggestNum = max(BeautyList)
BeautyList.remove(BiggestNum)
BeautyList.append(BiggestNum-1)

SmallestNum = min(BeautyList)
BeautyList.remove(SmallestNum)
BeautyList.append(SmallestNum+1)

BeautyValue = 1
for num in BeautyList:
    BeautyValue *= (num)

print(BeautyValue)



        
