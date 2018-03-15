file = open('Task_2.txt')
sum_grade = 0
count = 0
for i in file:
    string = i.replace('\n','')

    list = string.split(sep=' ')
    for j in list[-1]:
        grade = 0
#        try:
#            grade = int(j)
#        except ValueError:
#            continue
        if list[1] < 3:
            print('{} {} can be belarussian president, becouse grade is {}'.format(*list))
        sum_grade += grade
        count += 1
midle_ariphm = 0
midle_ariphm = sum_grade/count
print('Average grade in group is %d' % midle_ariphm)
file.close()
''' Должен быть более эллегантный подход к удаление \n из списка,
ведь если оценки будут состоять из 2 цифр, код работает не корректно 
Каков путь самурая по борьбе с \n? Или тут пора применять модуль string?
вроде бы мы его еще не проходили...
'''

