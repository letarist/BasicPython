my_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
month_list = list(my_dict.values())
mounth = int(input("Введите месяц "))
if 1 <= mounth <= 12:
        for key in my_dict.keys():
            if mounth in my_dict[key]:
                print(key)
else:
    print("введите корректное количество, от 1 до 12")
