#25/09/25

nums = []
for new in range(0,100):
    nums.append(new+1)

words = ["Arrays","Boolean","Computers","Data","Equals","Functions","Gears","Hardware","Integer","Jeffrey","Kilobyte","Linear","Mechanics","Networks","Operators","Programs","Quick","Recursive","String","True","Unicode","Variable","Website","X","Yobibyte","Zebibyte"]

def linear(array,aim,index): #Recursive function
    if index == len(array):
        return -1
    if array[index] == aim:
        return index
    return linear(array,aim,index+1)

'''
def linear(array,aim) #Non-Recursive function
    for index in range(0,len(array)):
        if array[index] == aim:
            return index
    return -1
'''

def binary(array,aim):
    low = 0
    high = len(array)
    mid = (low+high)//2
    while low <= high:
        if aim == array[mid]:
            return mid
        if aim > array[mid]:
            low = mid+1
        if aim < array[mid]:
            high = mid-1
        mid = (low+high)//2
    return -1


aim = int(input("Give me my number for linear! "))

if linear(nums,aim,0) != -1:
    print("Index is",linear(nums,aim,0))
else:
    print(aim,"was not found")


aim = int(input("Give me my number for binary! "))

if binary(nums,aim) != -1:
    print("Index is",binary(nums,aim))
else:
    print(aim,"was not found")