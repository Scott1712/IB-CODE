#08/09/25

record = ("Scott De'Ath",2008,"tag",)
try:
    newTag = str(record[1])[2:4]
    record[2] = newTag
except TypeError as error:
    print("You can't do that to a tuple because: ",error)
finally:
    print("Your final tuple is", record)
