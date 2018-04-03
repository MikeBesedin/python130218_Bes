'''Задача 8
Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
Вывести информацию об оценках по возрастанию в виде:
‘Hello Ann! Your grade is 9’
'''

#первоначальный мой вариант
grades = [('Ann', 9),('John', 7),('Smith', 5),('George', 6)]
mark = []
for i in range(len(grades)):
    mark.append(grades[i][1])
mark.sort()
j = 0
while j < len(grades):
    for i in range(len(grades)):
        if grades[i][1] == mark[j]:
            print('Hello {a[0]}! Your grade is {a[1]}'.format(a = grades[i]))
            #print('Hello {[0]}! Your grade is {[1]}'.format(grades[i]))
#закоменчиная строка выше вызывает ошибку выхода за диапозон индексов, почему??
            j +=1
            break
print("---------------------------")

#модное решение через сортед по последнему символу видал в гугле
grades = [('Ann', 9),('Aa', 7),('Smith', 5),('George', 6)]
grades = sorted(grades, key=lambda x: x[::-1])
#Стандартное поведение при сравнении списков/кортежей:
#(a1, b1) > (a2, b2) если a1 > a2, или b1 > b2 при a1 = a2
#[::-1] разворачивает пары задом-наперед, чтобы сравнивались сначала вторые элементы
for i in grades:
    print('Hello %s! Your grade is %s' % i)
 #   print('Hello {a[0]}, your grade is {a[1]}'.format(a = i))
