'''Задача 4
Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.


import os
dir = '/home/linux/GitHub/python130218_Bes/home_work_block6_Mike_B/breakfast'
f = open('dirs.txt', 'w')
for item in os.listdir():
    if os.path.isdir(item):
        print(item, file=f)
f.close()
'''
import os
dir = '/home/linux/GitHub/python130218_Bes/home_work_block6_Mike_B/breakfast'
def walk(dir):
  for item in os.listdir(dir):
    path = os.path.join(dir, item)
    if os.path.isfile(path):
        print(item)
    else:
        walk(path)
walk(dir)
'''
я думал выведет с конца как в задаче с цифрами, вопросик: а почему такая странная последовательность
 вывода списка файлов в директории? 
salo.txt
curd_with_honey.txt
borshch.txt
with_toast.txt
coffee.txt
должно быть: 
curd_with_honey.txt
salo.txt
borshch.txt
with_toast.txt
coffee.txt
'''