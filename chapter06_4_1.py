import random
random.seed(1)
msgs = ['Hi', 'Hello', 'Good morning', 'Good night', 'See you later', 'How are you', 'Have a good day']
with open('some.txt', 'w') as f:
    for i in range(10):
        f.write('{}, {}\n'.format(i, random.choice(msgs)))

f = open('some.txt')
c = 0 
for l in f:
    print(l, end='')
    if c == 4:
        break
    c += 1 
f.close()
