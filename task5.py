class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"вы рисуете {self.t}"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"вы чертите {self.t}"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"вы взяли {self.t}"


mark = Handle("Маркер")
pencil = Pencil("Карандаш")
pen = Pen("Ручка")
print(mark.draw())
print(pencil.draw())
print(pen.draw())
