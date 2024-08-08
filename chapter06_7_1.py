name = {'tanaka': 35, 'satou': 25, 'suzuki': 27}
def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return 'not found'

print(dict_info(name, 'satou'))
print(dict_info(name, 'yamada'))
