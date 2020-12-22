def inc_func(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


def inc_func_use():
    print(inc_func(input('Input text: ').split()))

print (inc_func_use())