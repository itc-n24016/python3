with open('my_math.py', 'w') as g:
    g.write('''def f(x, y):
    return x ** y\n''')


import my_math
print(my_math.f(2, 5))
