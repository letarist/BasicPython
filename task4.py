slovar = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
file = []
with open('task4.txt', 'r', encoding='utf-8') as file1:
    for i in file1:
        i = i.split(' ', 1)
        file.append(slovar[i[0]] + '  ' + i[1])
    print(file)

with open('resulttask4.txt', 'w') as file2:
    file2.writelines(file)