class Matrix:
    def __init__(self, spisok_1, spisok_2):
        self.s1 = spisok_1
        self.s2 = spisok_2

#    def __str__(self):
#        return str('\n'.join(['    '.join([str(j) for j in i]) for i in mtrx]))

    def __add__(self):
        mtrx = [[0, 0, 0],  # массив для первоначальной суммы
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.s1)):  # перебор списка списков 1
            for j in range(len(self.s2)):  # перебор списка списков 2
                mtrx[i][j] = self.s1[i][j] + self.s2[i][j]  # складываем по одинаковым индексам
        return str('\n'.join(['    '.join([str(j) for j in i]) for i in mtrx]))


my_matrix = Matrix([[63, 89, 11],
                    [6, 65, 23],
                    [41, 50, 9]],
                   [[44, 13, 76],
                    [69, 43, 23],
                    [26, 77, 43]])
print(my_matrix.__add__())
