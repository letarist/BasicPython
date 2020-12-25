spisok = [300, 2, 12, 10, 50, 60, 20, 9, 10]
spisok = [spisok[n] for n in range(1, len(spisok)) if spisok[n] > spisok[n - 1]]
print(spisok)
