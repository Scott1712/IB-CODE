#Scott De'Ath
#29/08/25
#Coding Challenges for lists and functions (Every 4th one)


''' # Coding Challenge 4

integers = [1,2,3,4,5,6,7,8,9,10]

def squareAll(numbers):
    squared = []
    for i in numbers:
        squared.append(i*i)
    return squared

print(squareAll(integers))
'''

''' #Coding Challenge 8
integers = [1,2,3,4,5,6,7,8,9,10]

def runningTotal(numbers):
    totals = []
    total = 0
    for i in numbers:
        total += i
        totals.append(total)
    return totals

print(runningTotal(integers))
'''

''' #Coding Challenge 12
Array1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
Array2 = [
    [10,11,12],
    [13,14,15],
    [16,17,18]
    ]

def AddArrays(array1,array2):
    arrayNew = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
    for i in range(0,3):
        for j in range(0,3):
            arrayNew[i][j] = array1[i][j] + array2[i][j]
    return arrayNew

print(AddArrays(Array1,Array2))
'''

''' #Coding Challenge 16
def borderOnes(Rows,Columns):
    array = [[0 for _ in range(Columns)] for _ in range(Rows)]

    for i in range(0,Rows):
        for j in range(0,Columns):
            if i == 0 or j == 0 or i == Rows-1 or j == Columns-1:
                array[i][j] = 1
    return array

rows, cols = 5,8
new = borderOnes(rows,cols)
for row in range(0,rows):
    print("")
    for col in range(0,cols):
        print(new[row][col],end=" ")
'''

''' #Coding Challenge 20 (This one took way too long)
Array = [
    [1,2,3,4,5,6],
    [18,19,20,21,22,7],
    [17,28,29,30,23,8],
    [16,27,26,25,24,9],
    [15,14,13,12,11,10]
    ]

def spiralList(array):
    spiral = []
    way = 0
    while len(spiral) != len(array)*len(array[0]):
        way+=1
        if way%4==1:
            for i in range(0+way//4,len(array[0])-way//4):
                spiral.append(array[way//4][i])
        if way%4==2:
            for i in range(1+way//4,len(array)-way//4-1):
                spiral.append(array[i][len(array[0])-way//4-1])
        if way%4==3:
            for i in range(len(array[0])-way//4-1,-1+way//4,-1):
                spiral.append(array[len(array)-1-way//4][i])
        if way%4==0:
            for i in range(len(array)-1-way//4,way//4-1,-1):
                spiral.append(array[i][way//4-1])
    return spiral

print(spiralList(Array))
'''
''' # Extra One (Get Prime Numbers from 1-'amount')
amount = 100
numbers = []
for i in range(1,amount+1):
    numbers.append(i)
for i in range(amount-1,-1,-1):
    willRemove = False
    for j in range(2,i):
        if numbers[i]%j==0:
            willRemove = True
    if willRemove == True:
        numbers.pop(i)

print(numbers)
'''
