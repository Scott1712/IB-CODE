#10/10/25

stack = [0,3,1,5,1,10,0,6,1,4]

while len(stack) != 0:
    steps = stack[len(stack)-1]
    print("Take",steps,"Steps forward")
    stack.pop()
    direction = stack[len(stack)-1]
    if direction == 1:
        print("Turn right")
    else:
        print("Turn left")
    stack.pop()