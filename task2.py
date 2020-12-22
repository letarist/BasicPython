my_list = input('Введите значения через пробел ').split()
i = 0
while i < len(my_list)-1:
    q = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = q
    i += 2
print(my_list)
