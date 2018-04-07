'''Задача 3
Реализовать программу с базой учащихся группы. Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
'''
# даный код слишком крут, чтобы быть моим: разобрался в механике и немного доработал до верного отображения номера записи
# буду рад увидеть более дзеновское решение поставленной задачи, т.к. она, видимо, часто будет встречаться в работе

list_students = [
    {'name': 'Ivan', 'surname': 'Borisenko', 'sex': 'male', 'age': '29'},
    {'name': 'Alex', 'surname': 'Zabolockii', 'sex': 'male', 'age': '28'},
    {'name': 'Nadzja', 'surname': 'Kapko', 'sex': 'female', 'age': '27'},
    {'name': 'Alex', 'surname': 'Buiko', 'sex': 'male', 'age': '27'},
    {'name': 'Vitali', 'surname': 'Buiko', 'sex': 'male', 'age': '27'}
]
# мне кажется, максимально близкое к идеалу решение таких задач можно разобрать в классе, или опубликовать в домашках/хэлпе
#print('Для удобства отображаем заданную базу студентов:')
#for i in list_students:
#    print(i)
def find_stud(list_students):
    dict_check = {'name': '', 'surname': '', 'sex': '', 'age': ''}
    def search_info():
        for key in dict_check.keys():
            print('Please, enter an information about {}, or press "Enter" to skip:'.format(key.upper()))
            dict_check[key] = input()
        return dict_check
    dict_check = search_info()
    find_numbers = 0
    flag_no_match = 0
    entree_list_numb = 0
    for value in dict_check.values():
        if value: find_numbers += 1
    for dic in list_students:
        if dic.items() & dict_check.items() and len(dic.items() & dict_check.items()) == find_numbers:
            flag_no_match += 1
            entree_list_numb = list_students.index(dic)+1
            print('Position in list #{}, surname {}, name {}, age {} , {}.'.format(entree_list_numb, dic['surname'], dic['name'], dic['age'], dic['sex']))
    if flag_no_match == 0:
        print('There are no students with input data')
#find_stud(list_students)

'''
Если первый раз читается этот комент ниже два варианта моего кода. Работают с поиском по одному полю.
Первый варик работает только если не будет задваиваться информация о студентах,
но если будут два студента, например, одинакового возраста и мы будем искать именно по возрасту,
 второй код в конце  более адекватен. Но с выводом его и порядкового номера записи в удобочитаемый формат , если
не вводить доп.графу "номер записи" в ключи с Student_data, у меня проблема.
'''
'''
key = input('where to find, enter one of this: name, last_name, gender, age: ')
value = input('what to find in column that you have just entered: ')
Student_data = [{'name': 'Claude', 'last_name': 'Monet', 'gender': 'male', 'age': '86'},
                    {'name': 'Frida', 'last_name': 'Kahlo', 'gender': 'female', 'age': '47'}]

def searching(key, value, Student_data):
    i = 1
    for elem in Student_data:
        if elem[key] == value:
            return elem, i
        else:
            i += 1
    print('No such student in list!')
answer = searching(key, value, Student_data)
print(answer)

print()
print('#%d in Student_data list:' % answer[1])
print("\n".join(["%s - %s" % (k, v) for k, v in answer[0].items()]))
'''
'''
def searching(key, value, Student_data):
    return [elem for elem in Student_data if elem[key] == value]

print(searching(key, value, Student_data))
'''