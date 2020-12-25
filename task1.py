from sys import argv

name, time, stavka, premiya = argv
try:
    time = int(time)
    stavka = int(stavka)
    premiya = int(premiya)
    res = time * stavka + premiya
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
