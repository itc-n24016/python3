class nigiri:
    ca = 'にぎり'
    to = 'ねた'
    ba = 'しゃり'
    def show(self):
        print('top:{}, base:{}, category:{},'.format(self.to, self.ba, self.ca))


class k(nigiri):
    a = 'カツオ'
    b = '生姜ネギ'
    c = 100

    def show(self):
        super().show()
        print('price:{}'.format(self.c))
        print('topping:{}'.format(self.b))
k1 = k()
k1.show()
