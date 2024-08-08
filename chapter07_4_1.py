a = 'out_test.txt'
b = 'Hello out_test.txt'
with open(a, 'w') as f:
    f.write(b)

with open(a, 'r') as f:
    for i in f:
        print(i, end='\n')

