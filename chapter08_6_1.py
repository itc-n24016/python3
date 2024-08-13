from datetime import datetime
t = '20180105120130'
d = datetime.strptime(t, '%Y%m%d%H%M%S')
print(d)
print(d.strftime('%Y%m%d%H%M%S'))
