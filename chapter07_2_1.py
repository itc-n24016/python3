def f(a, b):
    try:
        del a[b]
    except IndexError:
        print('Index Not Found')
    except:
        print('Unexpected Error')
    else:
        print('Successfully')

c = ['1', '2', '3', '4']
f(c, '5')
f(c, 5)
f(c, 0)
print(c)
