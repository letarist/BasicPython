class Data:
    def __init__(self, day_month_year):
        self.dmy = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        spis = []

        for i in day_month_year.split():
            if i != ' ': spis.append(i)

        return int(spis[0]), int(spis[1]), int(spis[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.dmy)}'


tomorrow = Data('15 01 2011')
print(tomorrow)
print(Data.valid(21, 16, 2022))
print(tomorrow.valid(11, 13, 2011))
print(Data.extract('19 10 2016'))
print(tomorrow.extract('15 13 2021'))