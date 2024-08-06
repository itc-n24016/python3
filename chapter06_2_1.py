class c:
    x = 3.14
    def __init__(self, half=1, hight=1):
        self.half = float(half)
        self.hight = float(hight)

    def f(self):
        x = c.x
        r = self.half
        return x * r * r

    def g(self):
        x = c.x
        r = self.half
        h = self.hight
        return 2 * x * r * h

    def s(self):
        ba = self.f()
        si = self.g()
        return ba * 2 + si

    def v(self):
        ba = self.f()
        h = self.hight
        return ba * h
    def show(self):
        r = self.half
        h = self.hight
        a = self.s()
        b = self.v()
        print('半径:{},高さ:{},表面積:{},体積:{}'.format(r, h, a, b))


c1 = c(2, 1)
c1.show()
