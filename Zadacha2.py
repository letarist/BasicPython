seconds = int(input("Введите количество секунд "))
hours = seconds // 3600
ost1 = seconds % 3600
minutes = ost1 // 60
ost2 = ost1 % 60
print(f"{seconds} секунд - это {hours:02}:{minutes:02}:{ost2:02}")
# для отображения секунд в последней строке