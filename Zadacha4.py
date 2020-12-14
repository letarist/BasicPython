num = int(input("введите целое положительное число "))
ost = num % 10
num = num // 10
while num > 0:
    if num % 10 > ost:
        ost = num % 10
        num = num // 10
        print("Максимальное число ", ost)
