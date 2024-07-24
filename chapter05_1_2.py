stack = []
stack.append(1)
print(stack)
stack.append(2)
print(stack)
for i in range(2):
    print("stack:", stack.pop())
    print(stack)
