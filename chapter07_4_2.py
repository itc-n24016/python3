def f():
    try:
        print('try')
        return
    except:
        print('except')
    else:
        print('else')
    finally:
        print('finally')

print(f())
print('1')
