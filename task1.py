def delenie(*args):
    try:
        s1 = int(input("Введите делимое "))
        s2 = int(input("Введите делитель "))
        rezultat = s1 / s2
    except ZeroDivisionError:
        return "на ноль делить нельзя)"
    except ValueError:
        return 'введите корректные значения'
    return rezultat


print(f"результат: {delenie()}")
