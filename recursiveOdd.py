#11/09/25

def oddFact(n):
    if n==1:
        return n
    else:
        return n+oddFact(n-2)

try:
    number = int(input("Enter a positive odd number: "))
    while number < 1 or number%2==0:
        number = int(input("Sorry, the number needs to be odd and positive: "))
    print("The result of this calculation with",number,"is",oddFact(number))
except ValueError:
    print("Sorry, you have to enter a number")
finally:
    print("Thank you for using this calculator")