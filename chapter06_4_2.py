def f(x = 2):
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1

import math
def g(x=2):
    while True:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                break
        else:
            yield x
        x += 1

i = f()
for c in range(10):
    print(next(i), end=' ')
print('')
