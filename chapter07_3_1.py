drink = {1: 'tea', 2: 'coffee', 3: 'water', 4: 'cocoa', 5: 'soda'}
class myerror(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '登録無し{0}'.format(self.key)

def f(tbl, key):
    if key not in tbl:
        raise myerror(key)
    else:
        return tbl[key]

my_dict = {1: 'tea', 2: 'coffee', 3: 'water'}
try:
    my_drink = f(my_dict, 5)
except myerror as err:
    print(err)
    key = err.args[0]
    my_dict[key] = drink[key]
    print(key, drink[key], 'を追加')
    my_drink = drink[key]
print(my_drink)
