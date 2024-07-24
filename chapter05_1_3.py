queue = []
queue.append(1)
print(queue)
queue.append(2)
print(queue)
for i in range(2):
    print("queue:" , queue.pop(0))
    print(queue)
