a = {x for x in range(21) }
b = {y for y in range(21) if y % 2 == 0}
c = a - b
print(c)
