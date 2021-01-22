class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


delimoe = input("введите делимое ")
delitel = input("введите делитель ")
try:
    delimoe = int(delimoe)
    delitel = int(delitel)
    if delitel == 0:
        raise MyErr("На ноль делить нельзя")
except (MyErr, ValueError) as err:
    print(err)
else:
    res = delimoe / delitel
    print(res)
