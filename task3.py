class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._inc = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.n + " " + self.s

    def get_total_income(self):
        return self._inc.get("wage") + self._inc.get("bonus")


working = Position(name=input("Введите имя "), surname=input("Введите Фамилию "),
                   position=input("Введите должность "),
                   wage=int(input("Введите зарплату ")), bonus=int(input("Введите премию ")))
print(working.get_full_name())
print(working.get_total_income())
