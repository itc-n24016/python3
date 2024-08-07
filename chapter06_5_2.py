with open('my_math2.py', 'w') as g:
    g.write('''def my_pow(x, y):
    return x ** y
if __name__ == 'main':
    x, y, exp = 2, 5, 32
    ans = my_pow(x, y)
    print('test my_pow({}, {}) -> {}, exp:{} ---'.format(x, y, ans, exp), end='')
    if ans == exp:
        print('test OK')
    else:
        print('test FAIL')\n''')

import my_math2
print(my_math2.my_pow(2, 5))
