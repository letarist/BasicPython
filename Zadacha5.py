izderjki = int(input("Введите издержки фирмы "))
profit = int(input("Введите выручку фирмы "))
if izderjki > profit:
    print("предприятие работает в убыток")
elif izderjki < profit:
    dohod = profit - izderjki
    print(f"предприятие работает с прибылью в {dohod} у.е.")
else:
    print("предприятие работает в 0")
sotrudniki = int(input("Введите количество сотрудников "))
dohod = (dohod / sotrudniki)
print(f"прибыль на одного сотрудника составляет {dohod} у.е.")
