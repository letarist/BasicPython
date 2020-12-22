def otr(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(otr(float(input("введите x ")), int(input("Введите y "))))