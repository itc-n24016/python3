def to_int(x):
    try:
        return sum(x)/len(x)
    except:
        print('length:', len(x))
        return None

print(to_int([3.9, 4.5, 2, 3]))
print(to_int([]))

