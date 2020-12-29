f = open('task1.txt', 'w', encoding='utf-8')
while True:
    s = input()
    if s == '':
        break
    f.write(s + '\n')
f.close()
f = open('task1.txt', 'r')
content = f.read()
print(content)
f.close()