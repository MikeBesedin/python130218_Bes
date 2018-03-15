file = open('Task_2.txt')
print(file.readlines())
print()
file.seek(0)
sum_grade = 0
count = 0
for i in file:
    string = i.replace('\n','')
    list = string.split(sep=' ')
    grade = 0
    if float(list[-1]) < 3:
        print('{} {} can be belarussian president, because grade is {}'.format(*list))
    sum_grade += float(list[-1])
    count += 1
midle_ariphm = 0
midle_ariphm = sum_grade/count
print('Average grade in group is %f' % midle_ariphm)
file.close()
