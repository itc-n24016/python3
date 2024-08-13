import os 
def prepare_dir(name='save'):
    if os.path.exists(name):
        print('exist')
    else:
        os.mkdir(name)
        print('make {}'.format(name))

print(prepare_dir())
