class Сell:
    def __init__(self, count):
        self.count = count
        print(f'Клетка с {self.count} ячейками ')

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count - other.count > 0:
            return self.count - other.count
        else:
            return 'количество меньше 0 '

    def __mul__(self, other):
        if self.count > 0 and other.count > 0:
            return self.count * other.count
        else:
            return 'Произведение меньше 0 '

    def __truediv__(self, other):
        return self.count / other.count

    def object(self, seb):
        return '\n'.join(['*' * seb for _ in range(self.count // seb)]) + '\n' + '*' * (self.count % seb)


c1 = Сell(63)
c2 = Сell(8)
a = c1 - c2
print(a)
b = c1 * c2
print(b)
c = c1 / c2
print(c)
d = c1 + c2
print(d)
print(c1.object(5))
