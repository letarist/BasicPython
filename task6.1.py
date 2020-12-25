from itertools import cycle, count

chislo = int(input('введите число, с которого начать перебор '))


def chisla():
    for el in count(chislo):
        yield el


for i in chisla():
    print(i)
