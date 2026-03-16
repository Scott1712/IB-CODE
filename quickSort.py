#27/10/2025
import random


def quickSort(lst):

    if len(lst) == 0: #Base case
        return lst

    #To explain
    small = 100
    big = 0
    for item in lst:
        if item<small:
            small = item
        if item>big:
            big = item

    print(str(small)+"-"+str(big)+" ->",lst)
    x = input("")


    if len(lst) == 1: #Base case
        return lst

    pivot = lst[0] #Set the pivot
    less = [] #Make an array for values less than pivot
    equal = [] #Make an array for values equal to pivot
    more = [] #Make an array for values greater than pivot
    for item in lst:
        if item < pivot: #Value less than pivot
            less.append(item)
        if item == pivot: #Value equal to pivot
            equal.append(item)
        if item > pivot: #Value greater than pivot
            more.append(item)

    return quickSort(less) + equal + quickSort(more)

listt = []
for i in range(0,50):
    listt.append(random.randint(1,100))
print("")
print("Original ->",listt)
x = input("")
print("")
print("After ->",quickSort(listt))
