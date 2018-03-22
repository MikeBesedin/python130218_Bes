file = open('HW_6_3_list.txt')
list_students = []
list_of_keys = ['name', 'surname', 'sex', 'age']
for line in file:
    string = line.replace('\n', '')
    list_line = string.split(sep=' ')
    dict_line = dict(zip(list_of_keys, list_line)) # dict(zip(keyz, valuez))
    list_students.append(dict_line)

print(list_students)

import sys
sys.path.insert(0, '/home/linux/GitHub/python130218_Bes')
print(sys.path)
from home_work_block4_Mike_B.HW_4_3 import find_stud

file.close()
'''
другой вариант ипорта модуля выполняется, но с ошибкой, почему?
import sys
sys.path.insert(0, '/home/linux/GitHub/python130218_Bes/home_work_block4_Mike_B')
print(sys.path)
from HW_4_3.py import find_stud
             \/
Traceback (most recent call last):
  File "/home/linux/GitHub/python130218_Bes/home_work_block6_Mike_B/HW_6_3.py", line 15, in <module>
    from HW_4_3.py import find_stud
ImportError: No module named 'HW_4_3.py'; 'HW_4_3' is not a package

просто копия кода из HW_4_3.py чтобы было перед глазами:
list_students = [
    {'name': 'Ivan', 'surname': 'Borisenko', 'sex': 'male', 'age': '29'},
    {'name': 'Alex', 'surname': 'Zabolockii', 'sex': 'male', 'age': '28'},
    {'name': 'Nadzja', 'surname': 'Kapko', 'sex': 'female', 'age': '27'},
    {'name': 'Alex', 'surname': 'Buiko', 'sex': 'male', 'age': '27'},
    {'name': 'Vitali', 'surname': 'Buiko', 'sex': 'male', 'age': '27'}
]
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

find_stud(list_students)
'''