import collections
a = 'すもももももももものうち'
b = collections.Counter(a)
c = collections.defaultdict(list)
for i, j in b.items():
    c[j].append(i)
print(c[1])
