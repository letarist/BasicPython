class Transport:
    def __init__(self, name, model, year):
        self.n = name
        self._m = model
        self.y = year
        print(name, model, year)

    def on_start(self, speed):
        print(f"Go-go car {self.y} with speed {speed}")

    def off_start(self):
        print("STOP!")


class Auto(Transport):
    def __init__(self, name, model, year, pass_):
        self.n = name
        self._m = model
        self.y = year
        self.p = pass_
        print(name, model, year)
    def destroy(self, time):
        print(f"=(( через {time}")

auto_1=Auto("LADA", "OKA", 1980, 5)
#auto_1 = Auto("Jiga", "2107", 1990)
auto_1.on_start(100)
auto_1.destroy(200)
# print(auto_1.n, auto_1.m, auto_1.y, auto_1.count_a)
auto_2 = Auto("BMW", "6", 1999, 2)
# auto_2.name = "Niva"
auto_2.on_start(10)
# print(auto_2.n, auto_2.m, auto_2.y, auto_1.count_a)
# print(auto_1.name)
