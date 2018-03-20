file = open('HW_6_3_list.txt')
list_students = []
list_of_keys = ['name', 'surname', 'sex', 'age']
for line in file:
    string = line.replace('\n', '')
    list_line = string.split(sep=' ')
    dict_line = dict(zip(list_of_keys, list_line))
    list_students.append(dict_line)

print(list_students)
from HW_4_3 import find_stud
#пока читаю Лутца по модулям, чтобы сделать вызов функции не из папки с исполняемым файлом,
# а из папки home_work_block4_Mike_B, где функция find_stud изночально лежала

find_stud(list_students)
file.close()
'''
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