class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                znach = int(input('Вводите значения поочередно через Enter '))
                self.my_list.append(znach)
                print(f'Введенный список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")


try_except = Error()
print(try_except.my_input())
