from itertools import cycle

spisok = ['Я хочу уволиться, или меня доканают студенты, помогите плз', 'уже нервы ни к черту',
          'эта сессия была жестче, чем в прошлом году', 'студенты мелкие надоедливые демоны', 'зарплата', 20000,
          'вообще жесть','я хочу есть)00)']
for i in cycle(spisok):
    print(i)
