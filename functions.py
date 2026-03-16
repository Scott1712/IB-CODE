#01/09/25
#Scott De'Ath

a = 7
b = 2
flag = (a % b == 1)
if flag:
    a = a + b
    b *= 3
flag = (a > 8 and not flag) or (b == 6)
print(a, b, flag)