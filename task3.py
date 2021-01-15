class Сell:
    def __init__(self, count):
        self.count = count

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
            return 'один из аргументов является 0 '

    def object(self, seb):
        return '\n'.join(['*' * seb for _ in range(self.count // seb)]) + '\n' + '*' * (self.count % seb)


c1 = Сell(63)
c2 = Сell(8)
a = c1 - c2
b = c1 * c2
c = c1 / c2
d = c1 + c2
print(c1.object(5))
