name = input("Введите имя ")
surname = input("Введите фамилию ")
years = input("Введите год рождения ")
country = input("Введите город проживания ")
email = input("Введите электронную почту ")
phone = input("Введите номер телефона ")


def phonk(*args):
    return " ".join([name, surname, years, country, email, phone])


print(phonk())
