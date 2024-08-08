x = 'Happy'
def e1():
    print('In event1:', x, end=' -> ')

def e2():
    x = 'Sad '
    print('In event2:', x, end=' -> ')
def e3():
    global x
    x = 'Tired '
    print('In event3:', x, end=' -> ')

def e4():
    x = 'Excite'
    def happening():
        print('In event4:', x, end=' -> ')
    happening()

def e5():
    x = 'Fun '
    def happening():
        nonlocal x
        x = 'Scare '
    happening()
    print('In event5:', x, end=' -> ')

li = [e1, e2, e3, e4, e5]
for f in li:
    f()
    print('After {}: {}'.format(f.__name__, x))
