a = [['0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
        ['0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
        ['0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
        ['0004', 'Male', 'Suzuki', 'Ichirou', '35', 'Hokkaido']]
print('list')
print(a)
b = {}
for i in a:
    key = i[0]
    info = i[1:]
    b[key] = info
print('number', 'information', sep='\t')
for key, info in b.items():
    print(key, info)
