"""Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы. Результат выводить в удобочитаемом виде
с порядковым номером записи. Скрипт программы должен принимать параметр, который определяет формат хранения и
реализации БД: в текстовом файле с определенной структурой; в файле json."""

import json

class Finder: #базовый клас с созданием словаря параметров поиска и метода поиска совпадений
    def __init__(self):
        self.dict_check = {'name': '', 'surname': '', 'sex': '', 'age': ''}  # create a dictionary with empty values
        self.dict_check = self.search_info()  # Ask function search_info

    def search_info(self):  # function to input information to search
        for key in self.dict_check.keys():
            print('Please, enter an information about {}, or press "Enter" to skip:'.format(key.upper()))
            self.dict_check[key] = input()
        return self.dict_check

    def find(self):
        find_numbers = 0
        flag_of_matches = 0
        for value in self.dict_check.values():
            if value: find_numbers += 1
        for dic in self.stud_dict:
            if dic.items() & self.dict_check.items() and len(dic.items() & self.dict_check.items()) == find_numbers:
                flag_of_matches += 1
                print('Position in list #{}, surname {}, name {}, age {} , {}.'.format(self.stud_dict.index(dic) + 1,
                                                                                       dic['surname'],
                                                                                       dic['name'], dic['age'],
                                                                                       dic['sex']))
        if flag_of_matches == 0:
            print('There are no students with input data')

class TextFile(Finder): # создаем словарь из тхтфайла
    def __init__(self):
        super().__init__()
        with open(file_name) as text_file:
            self.stud_list = [line.rstrip().split() for line in text_file]
        keys = ['surname', 'name', 'sex', 'age']
        self.stud_dict = [dict(zip(keys, values)) for values in self.stud_list]

class JsonFile(Finder): # создаем словарь из джейсонфайла
    def __init__(self):
        super().__init__()
        self.stud_dict = []
        with open(file_name) as json_file:
            for line in json_file:
                self.stud_dict.append(json.loads(line))

while True: # цикл для определиния формата вводимого к обработке файла
    file_name = input('Please, input the file name or "0" to quit: ')
    if file_name == '0':
        break
    file_name_list = file_name.split('.')
    if file_name_list[-1] == 'txt':
        file_to_process = TextFile()
        file_to_process.find()
    elif file_name_list[-1] == 'json':
        file_to_process = JsonFile()
        file_to_process.find()
    else:
        print('Only .txt ot .json files can be processed!')
        continue
