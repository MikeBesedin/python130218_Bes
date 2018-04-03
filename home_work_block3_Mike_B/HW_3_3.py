'''Вводятся строки. Определить самую длинную строку и вывести ее номер на экран.
Если самая длинная строка повторяется несколько раз, то вывести номера всех таких строк.'''

numbers_of_strings = 4
string_list = []
for i in range(numbers_of_strings):
    print('enter string #', i + 1, ':  ')
    string_list.append(input())

index = 0
for i in range(1, numbers_of_strings):
    if len(string_list[i]) > len(string_list[index]):
        index = i

longest_stirngs_list = []
for i in range(numbers_of_strings):
    if len(string_list[i]) == len(string_list[index]):
        longest_stirngs_list.append(i+1)

print('The list of longest entered strings numbers: {}'.format(longest_stirngs_list))

''' Первоначальный код без гугла был не так лаконичен:
string_num = 4
string_list = []
for i in range(string_num):
    print('enter string ', i + 1, ':  ')
    string_list.append(input())

biggest_string_lenth = 0
list_num_print = []
string_list_num = 0

nomer_stroki = 0
for i in string_list:
    nomer_stroki += 1
    if len(i) > biggest_string_lenth:
        biggest_string_lenth = len(i)
        list_num_print.clear()
        list_num_print.append(nomer_stroki)

list_num_print = set(list_num_print)
nomer_stroki = 0
for i in string_list:
    nomer_stroki += 1
    if len(i) == biggest_string_lenth:
        list_num_print.add(nomer_stroki)

print(list_num_print)
'''
