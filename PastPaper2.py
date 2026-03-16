#22/10/25

def fibo(N):
    if N == 0 or N == 1:
        return N
    else:
        return fibo(N-1) + fibo(N-2)

print(fibo(4))

num = int(input("Tell me a number: "))
term = num
if num!=0 and num!=1:
    a = 1
    b = 1
    loops = num
    num = 1
    for i in range(2,loops):
        num = num + a
        a = num - a
        b = num - a
print("The",str(term)+"th Fibonacci number is",num)

terms = int(input("Tell me a number of terms: "))
for i in range(1,terms+1):
    print("Term number",i,"is",fibo(i))