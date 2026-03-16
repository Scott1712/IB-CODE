#11/09/25
'''
def Factorial(n):
    if n==1: #base case
        return 1
    else: #recursive case
        return n*Factorial(n-1)

try:
    number = int(input("Give me a number to factorial: "))
    while number < 1:
        number = int(input("Sorry, you can't factorize anything under 1, redo: "))
    print("The factorial of",number,"is",Factorial(number))
except ValueError:
    print("Sorry, only numbers are allowed")
finally:
    print("Thank you for using the factorial calculator")
'''