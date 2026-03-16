Value = 0
while Value != -1:
    Value = int(input())
    if Value != -1:
        Answer = Value
        for Count in range(Value-1,1,-1):
            Answer = Answer * Count
        print(Answer)
