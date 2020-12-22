def my_func(per1, per2, per3):
    if per1 > per3 and per2 > per3:
        return per1+per2
    if per2 > per1 and per3 > per1:
        return per2+per3
    else:
        return per1+per3


print(f'{my_func(4,3,7)}')
