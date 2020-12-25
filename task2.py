spisok = [100, 50, 60, 20, 9, 10]
spisok = [el for n, el in enumerate(spisok) if spisok[n - 1] < spisok[n]]
print(spisok)
