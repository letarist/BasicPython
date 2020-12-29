with open('task3.txt', 'r', encoding='utf-8') as f:
    slovar = {}
    for i in f:
        key, znachenie = i.split()
        slovar[key] = znachenie
        if int(znachenie) < 20000:
            print(f'{key}: зарплата меньше 20000')
