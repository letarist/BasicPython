def my_sum():
    res = 0
    ex = True
    while ex == True:
        number = input('Введите числа через пробел. Для выхода введите #').split()

        res1 = 0
        for elem in range(len(number)):
            if number[elem] == '#':
                ex = False
                break
            else:
                res = res + int(number[elem])
        res = res + res1
        print(f'Сумма элементов = {res}')
    print(f'Конечная сумма элементов = {res}')


my_sum()
