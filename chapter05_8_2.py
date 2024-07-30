a = [['01', '0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
        ['02', '0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
        ['03', '0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
        ['04', '0001', 'Male', 'Smith', 'Mike', '22', 'NewJersey'],
        ['05', '0002', 'Male', 'Turner', 'Tom', '27', 'Kansas'],
        ['06', '0003', 'Male', 'Jackson', 'David', '25', 'Florida']]
b = {}
for x in a:
    key = x[0],x[1]
    info = x[2:]
    b[key] = info

print('number' , 'information', sep='\t')
for key, info in b.items():
    print(key, info)
