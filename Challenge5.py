code = int(input("Enter a 4 digit code (1111-9999): "))
while code < 1111 or code > 9999:
    code = int(input("Outside of range, re-enter (1111-9999): "))
code = str(code)
total = 0
for i in range(0,4):
    total += int(code[i])
if total%2 == 0:
    print("Even")
else:
    print("Odd")