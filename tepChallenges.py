#Scott De'Ath
#28/08/25

'''
try: #Always do this
    cookies = str(input("How many cookies do you have? "))
    friends = str(input("How many friends do you have? "))
    if int(friends) == 0:
        raise ZeroDivisionError
    else: #If no error, do this
        print("Each friend gets",int(cookies)//int(friends),"cookies")
except ZeroDivisionError: #Tell them this is an error occured
    print("You can't share cookies with 0 friends")
finally: #Always say this
    print("Thank you for using this program")
'''
'''
try:
    password = str(input("Enter in your new password: "))
    if len(password)<5:
        raise ValueError
    else:
        print("That password is very strong")
except ValueError:
    print("That password is too short")
finally:
    print("Thank you for using our password checker")
'''
'''
try:
    exp = input("Enter in a math expression: ")
    exp = eval(exp)
    print(exp)
    print("Good expression")
except SyntaxError:
    print("Type an actual expression please")
finally:
    print("Thank you for using our expression checker")
'''
'''
try:
    cats = int(input("How many cats do you have? "))
    dogs = int(input("How many dogs do you have? "))
except ValueError:
    print("Write it as a number please")
finally:
    print("Thank you for using the pet log")
'''