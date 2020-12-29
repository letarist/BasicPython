import re

result = {}
summa = 0
with open('task6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.split()
        for n in a:
            chisla = re.findall('\d+', n)
            if not chisla:
                continue
            else:
                summa += int(chisla[0])
        result[a[0][:-1]] = summa
        summa = 0
print(result)
