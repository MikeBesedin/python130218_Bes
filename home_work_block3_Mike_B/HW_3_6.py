'''Задача 6
Преобразовать массив так, чтобы сначала шли все отрицательные элементы,
а потом положительные(0 считать положительным). Порядок следования должен быть сохранен.
'''
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
print(minus+plus)

'''
хотел изночально так:
print(minus.extend(plus))
но возвращает None
почему?
'''
