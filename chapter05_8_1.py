a = {
        'iceland': {'code': '354', 'capital': 'reykjavik'},
        'ireland': {'code': '353', 'capital': 'dublin'},
        'azerbaidjan':{'code': '994', 'capital': 'baku'}
}
def f(x):
    if not isinstance(x, dict):
        return x

    c = ''
    for key, val in x.items():
        c += (' ' + str(key) + ' ' + f(val))
    return c

for key1, val1 in a.items():
    print(key1, f(val1))

print('answer:4')
