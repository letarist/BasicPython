def generator(n):
    x = 1
    for el in range(1, n + 1):
        x *= el
        yield x


n = int(input('Введите число '))
for i in generator(n):
    print(i)

#Я пытался эту задачу решить при помощи count, у меня не получилось, есть ли такая возможность?