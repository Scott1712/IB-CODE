#18/08/25

'''
drew = "You can't guard me"

truth = drew[0:7] + drew[9:18]

start = drew.find("can't")
end = drew.find("guard")
sliced = drew[start:end].strip()

real = drew.replace("can't","can")

wordList = drew.split(" ")
middle = wordList[1] + " " + wordList[2]

print(truth)
print(sliced)
print(real)
print(middle)
'''

data = "Contact:  alice.smith23@email.com; backup: bob@work.org"

aliceEmail = data[10:33]
bobEmail = data[43:55]

aliceName = aliceEmail.split("@")
bobName = bobEmail.split("@")


print(aliceEmail, bobEmail)
print("")
print(aliceName[0],bobName[0])
print("")
print(aliceName[1],bobName[1])
