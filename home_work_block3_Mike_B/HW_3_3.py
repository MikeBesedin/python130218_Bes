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

#Сергей, хэлп плз! Изначально код, ниже закоментированный, был не красив, зато свой:
''' 
Почему при вводе двух или более идентичных строк, программа выдает только номер первой встречаемой длинной строки?
Например, если ввести во всех строках по единице. Потратил уйму времени, но так ошибку и не осознал. 
Хочу разобраться, уже дело чести, как говориться =)

string_num = 4
string_list = []
for i in range(string_num):
    print('enter string ', i + 1, ':  ')
    string_list.append(input())

biggest_string_lenth = 0
list_num_print = []
string_list_num = 0

for i in string_list:
    if len(i) > biggest_string_lenth:
        biggest_string_lenth = len(i)
        string_list_num = string_list.index(i) + 1
        list_num_print.clear()
        list_num_print.append(string_list_num)
print(list_num_print)

list_num_print = set(list_num_print)

for i in string_list:
    if len(i) == biggest_string_lenth:
        index = string_list.index(i) + 1
        list_num_print.add(index)

print(list_num_print)
'''