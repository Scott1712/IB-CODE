#22/10/25

def rec(A):
    if A >= 2:
        return rec(A-2) + rec(A-1)
    else:
        return 1

print(rec(5))