"""
a = []
for i in range(1, 6):
    a.append(i)
"""
a = list(range(1, 6))
del a[-2:]
print(a)
