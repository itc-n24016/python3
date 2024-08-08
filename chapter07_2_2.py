def square(x):
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.f():
            x = int(x)
        else:
            raise ValueError('square', x)
    return x ** 2

print(square(2))
print(square('a'))
