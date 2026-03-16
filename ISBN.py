#Scott De'Ath
'''
code = ""
overall = 0

while len(code) != 12:
    code = str(input())

for i in range(0,6):
    overall = overall + int(code[2*i])
    overall = overall + (int(code[2*i+1])*3)

check = overall%10
check = 10-check

if check == 10:
    check = 0

print("")
print("Check Digit ->",check)
'''

code = ""
overall = 0

while len(code) != 13:
    code = str(input())

OGCheck = code[12]


for i in range(0,6):
    overall = overall + int(code[2*i])
    overall = overall + (int(code[2*i+1])*3)

check = overall%10
check = 10-check

if check == 10:
    check = 0

if check == OGCheck:
    print("Check digit is correct")
else:
    print("Check digit is incorrect")