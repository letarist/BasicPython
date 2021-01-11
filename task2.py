class Road:
    def __init__(self, lenght, width, mass, depth):
        self._l = lenght
        self._w = width
        self.m = mass
        self.d = depth

    def mas(self):
        return self._l * self._w * self.m * self.d


a = Road(lenght=int(input("Введите длину ")), width=int(input("Введите ширину ")),
         mass=int(input("Введите массу асфальта для покрытия 1 кв.м. дороги")),
         depth=int(input("Введите толщину полотна ")))
print(a.mas())
