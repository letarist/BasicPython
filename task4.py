my_list = input("введите значения через пробел ").split()
for i, num in enumerate(my_list, 1):
    if len(num) > 10:
        num = num[0:10]
    print(f"{i}. - {num}")
