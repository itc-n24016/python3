class re:
    angle = 90

    def __init__(self, width, height):
        self.name = 'rectangle'
        self.width = width
        self.height = height
        self.perimeter = self.ca_perimeter()
        self.area = self.ca_area()

    def ca_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2
    def ca_area(self):
        w = self.width
        h = self.height
        return w * h
    def show(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print('name:{}, width:{}, height:{}, angle:{}'.format(n, w, h, ang))
        print('perimeter:{}, area:{}'.format(p, a))

class sq(re):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = 'square'

r1 = re(4, 3)
r1.show()
s1 = sq(4)
s1.show()
