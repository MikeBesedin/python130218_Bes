import random
L = []
for i in range(10):
    n = random.randint(-7, 7)
    L.append(n)
print(L)
minus = []
plus = []
for i in L:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
minus.extend(plus)
print(minus)

'''
хотел сократить и из двух последних строк сделать одну
print(minus.extend(plus))
но возвращает None
почему?
'''
