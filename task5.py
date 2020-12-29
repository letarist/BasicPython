with open('task5.txt', 'w') as file:
    line = input('Введите ЦИФРЫ через пробел \n')
    file.writelines(line)
    num = line.split()

    print(sum(map(int, num)))