'''Задача 2
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
Скрипт программы должен принимать параметр, который определяет формат хранения и реализации БД:
в текстовом файле с определенной структурой; в файле json.
'''
import json
import sys
sys.path.insert(0, '/home/linux/GitHub/python130218_Bes')
from home_work_block4_Mike_B.HW_4_3 import find_stud

# read data from database_file in format where elements are dict
stud_list = []
with open('stud_list.json') as db:
    for line in db:
        stud_list.append(json.loads(line))
print('From file stud_list.json we have following:')
for line in stud_list:
    print(line)
# with circle found needful information
while True:
    find_stud(stud_list)
    request = input('if you want to stop enter "ex": ')
    if request == 'ex':
        quit()