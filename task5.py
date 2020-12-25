from functools import reduce


def umnozh(el1, el2):
    return (el1 * el2)


def gen():
    spisok = [el for el in range(100, 1001) if el % 2 == 0]
    return spisok


print(f'список четных элементов {gen()}')
print(f'произведение равно {reduce(umnozh, gen())}')
