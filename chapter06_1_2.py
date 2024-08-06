class person:
    def __init__(self, name = '', nationality = '', birth = '', address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address
    def f(self):
        print('名前:', self.name)
        print('国籍:', self.nationality)
        print('生年:', self.birth)
        print('住所:', self.address)
a = person('かぐや姫', '日本', '685', '静岡県富士市')
print(a.f())
b = person('金太郎', '日本', '956', '静岡県駿東郡小山町')
print(b.f())
