f = open('task2.txt','r', encoding='utf-8')
line = 0
for i in f:
    line += 1
    sumbol = 0
    word = 0
    for j in i:
        if j != ' ' and sumbol == 0:
            word += 1
            sumbol = 1
        elif j == ' ':
            sumbol = 0

    print(i, len(i), 'символов', word, 'слова')

print(line, 'строчек')
f.close()
