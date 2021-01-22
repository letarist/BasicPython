class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


ch_1 = ComplexNumber(8, 9)
ch_2 = ComplexNumber(23, 6)
print(ch_1)
print(ch_1 + ch_2)
print(ch_1 * ch_2)