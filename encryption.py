#Scott De'Ath
import random

original = str(input("Enter in a message: "))
new = ""
crypt = random.randint(5,10)

for i in range(0,len(original)):
    character = ord(original[i]) + crypt
    new = new + chr(character)

print(new)
