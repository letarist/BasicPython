spisok = [7, 6, 4, 3, 1, 1]
print(f'У нас есть набор натуральных чисел: {spisok}')

while True:

    num = int(input('Введите число: '))
    for i in range(len(spisok)):
        if num > spisok[i]:
            spisok.insert(i, num)
            break
        elif num <= spisok[-1]:
            spisok.append(num)
            break
    print(spisok)
