'''
Первый код работает, только если не будет задваиваться информация о студентах,
но если будут два студента, например, одинакового возраста и мы будем искать именно по возрасту,
 код ниже в коментах более адекватен. Но с выводом его и порядкового номера записи в удобочитаемый формат , если
не вводить доп.графу "номер записи" в ключи с Student_data, у меня проблема )
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

print()
print('#%d in Student_data list' %a nswer[1])
print("\n".join(["%s - %s" % (k, v) for k, v in answer[0].items()]))

'''
def searching(key, value, Student_data):
    return [elem for elem in Student_data if elem[key] == value]

print(searching(key, value, Student_data))
'''