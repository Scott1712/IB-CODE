#26/02/26

import random

class crate:
    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_safety_protocol(self):
        pass

class hazard(crate):
    def get_safety_protocol(self): #Polymorphism
        return("not safe to lift (Hazardous material)")

    def get_name(self):
        return("H")

class safe(crate):
    def get_safety_protocol(self):
        return("safe to lift")

    def get_name(self):
        return("S")

floor = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]

for row in range (0,5):
    for column in range (0,5):
        if random.randint(1,2)==1:
            floor[row][column] = hazard()
        else:
            floor[row][column] = safe()

print("")
print("Warehouse Floor")
print("----------------")
for row in range(0,5):
    print(" ",end="")
    for column in range(0,5):
        print(floor[row][column].get_name(),end="  ")
    print("")

print("")
print("H = Hazardous Material")
print("S = Safe to Lift")
print("")
print("What box do you want to lift?")
print("------------------------------")
for row in range(0,5):
    print(" ",end="")
    for column in range(0,5):
        print(str(row*5+(column+1)),end=" ")
        if row*5+(column+1) < 10:
            print(" ",end="")
    print("")

choice = 0
while choice < 1 or choice > 25:
    try:
        choice = int(input(" -> "))
        if choice < 1 or choice > 25:
            print("Enter number 1-25 please")
    except ValueError:
        print("Enter an integer please")

print("That box is ",end="")
print(floor[(choice-1)//5][choice%5].get_safety_protocol())