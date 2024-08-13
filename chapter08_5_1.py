import math
import random
total = 0
num = 0
a = 0
while not math.isclose(a, math.pi, abs_tol=1e-5):
    x = random.random()
    y = random.random()
    l = pow(x ** 2 + y ** 2, 0.5)
    total += 1
    if l <= 1:
        num += 1
        a = 4 * num / total
print(a)
print(total)
