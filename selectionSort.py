#31/10/25

import random

listt = []

for i in range(1,101):
    listt.append(i)

array = []

for i in range(99,-1,-1):
    k = random.randint(0,i)
    array.append(listt[k])
    listt.remove(array[len(array)-1])

print("Original ->",array)
print("")

for i in range(0,len(array)):
    minPos = i #assume its the new smallest

    for j in range(i+1,len(array)):
        if array[j] < array[minPos]: #if not the smallest
            minPos = j #new smallest

    if minPos != i: #if theres a new smallest
        array[i],array[minPos] = array[minPos],array[i] #then swap

print("After ->",array)