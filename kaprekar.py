#18/09/25

import time
#
'''
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
'''

counter = 0

def kool(n):
    global counter
    digits = []
    digits.append((n%10000)//1000)
    digits.append((n%1000)//100)
    digits.append((n%100)//10)
    digits.append((n%10)//1) #Get all the digits

    minD = []
    for j in range(0,4):
        Min = 10
        for i in range(0,4-j):
            if digits[i] < Min:
                Min = digits[i]
        minD.append(Min)
        digits.remove(Min) #Order them from smallest to largest

    maxNum = 0
    minNum = 0
    for i in range(0,4):
        maxNum += minD[i] * 10**i
        minNum += minD[i] * 10**(3-i) #Put the numbers together

    result = maxNum-minNum
    counter += 1
    print(maxNum,"-",minNum,"=",result)
    x = input("")

    if result == 6174:
        print(" 6174 ("+str(counter)+" steps)")
        return
    else:
        kool(result)

try:
    number = input("Give me any 4 digit number: ")
    x = int(number)
    while len(number)!=4:
        number = input("Make sure the number is 4 digits: ")
        x = int(number)
    print("")
    number = int(number)
    kool(number)

except ValueError:
    print("")
    print("Sorry, you have to enter a number")

finally:
    print("")
    print("Thank you for using this Kaprekar's Constant machine")
