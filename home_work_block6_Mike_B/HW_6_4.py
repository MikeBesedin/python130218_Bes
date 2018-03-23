'''Задача 4
Реализовать программу, которая выводит содержимое каталога в файловой системе (директории и файлы?).
Путь к каталогу запрашивается у пользователя.
'''

# у меня вышло 2 варианта решения, первый записывает в файл полностью содержание: директории и файлы
import os
dir = input('Enter path to some dir which content you want write into dirs.txt: ')
f = open('dirs.txt', 'w')
def walk(dir):
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if os.path.isfile(path):
            print(item, file=f)
        else:
            print(item, file=f)
            walk(path)
walk(dir)
f.close()
# i need help!
# my path for example: /home/linux/GitHub/python130218_Bes/home_work_block6_Mike_B/breakfast
# внутри breakfast лежит два файла coffee.txt и with_toast.txt и папка Lunch,
# в которой лежат salo.txt и borshch.txt, а также директория Dinner,
# внутри которой одинокий curd_with_honey.txt
# Первым записывается в файл Lunch. Окей.
# Но почему второй строкой идет не имя вложенной в Lunch директории  Dinner, а файл salo.txt? Вот как он затесался...
# А уже потом идет Dinner и функция нормально разворачивается с конца дописывает файлы в предсказуемой последовательности
'''
# Вариант 2 принтует только название внутренних файлов:
import os
dir = input('Enter path to some dir which content you want write into dirs.txt: ')
def walk(dir):
  for item in os.listdir(dir):
    path = os.path.join(dir, item)
    if os.path.isfile(path):
        print(item)
    else:
        walk(path)
walk(dir)

