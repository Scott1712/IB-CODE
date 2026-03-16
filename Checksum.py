#Scott De'Ath
#09/01/25

message = str(input("Please enter a message: "))
overall = 0

for i in range(0,len(message)):
    overall = overall + ord(message[i])*(i+1)

print("The checksum is",overall)