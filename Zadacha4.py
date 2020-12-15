num = int(input("введите целое положительное число "))
min = -1
while num > 0:
    ost = num % 10
    num = num // 10
    if ost > min:
        min = ost
        print("Максимальное число ", ost)
