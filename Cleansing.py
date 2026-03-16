#12/09/25

# T-1 Immutable ID Tag (Tuple)

tag = ""
x = 0

record = ("Drew Cassels",2009,tag,) #Original tuple

print("Original tuple ->",record)

while x == 0:
    try:
        newYear = int(input("Enter in your new birthyear: "))
        while len(str(newYear)) != 4 or newYear < 1900 or newYear > 2025:
            newYear = int(input("Sorry, enter in a valid birthyear: ")) #Validate the input
        name = record[0].split(" ")
        newTag = str(newYear)[2:4]+name[0][0:1]+name[1][0:1] #Create the new tag
        x = 1

    except ValueError: #If the input for the year is invalid
        print("Sorry, you have to enter digits for birthyear: ")


newTuple = (record[0],newYear,newTag,) #Create a new tuple with correct info
print("New tuple ->",newTuple)
'''
record[1] = newYear #Try and edit the tuple
    except TypeError: #When you try and edit the tuple
        print("You can't edit a tuple")
    finally:
        newTuple = (record[0],newYear,newTag,) #Create a new tuple with correct info
        print("New tuple ->",newTuple)
        print("We made a new tuple instead")
'''