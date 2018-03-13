a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
if a >= b and b >= c:
    a = a * 2
    b = b * 2
    c = c * 2
else:
    x = a
    y = b
    a = y
    b = x
print(a, b, c)

'''вариант решения выше первым приходит на ум, а более хитрый вариант a,b = b,a
   извлек из примера последовательности Фибоначи с исп. кортежа'''

