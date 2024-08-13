import os
def delete_dir(name='save'):
    if os.path.exists(name):
        print('exist {}'.format(name))
        os.rmdir(name)
        print('delete {}'.format(name))
    else:
        print('not {}'.format(name))

print(delete_dir())
