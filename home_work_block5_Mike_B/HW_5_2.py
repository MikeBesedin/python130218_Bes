'''Задача 2
Для решений задач занятия №5 вынести общие части в модули. Сделать единую точку входа app.py.
Необходимо реализовать возможность старта выполнения кода одного из заданий сразу после запуска программы,
 а также после его выполнения предоставить возможность выполнить другое задание без повторного запуска программы.'''
import sys
sys.path.insert(0, '/home/linux/GitHub/python130218_Bes')
task_N = 0
print('Данная программа выполняет пять задач из блока задач к занятию №5.\n'
      'Можно вводить только целые цифры от 0 до 4, соответствующие номеру задачи,\n'
      'либо цифру 5, если хотите остановить программу!')
while task_N != 5:
    task_N = int(input('Введите номер задания для выполнения: '))
    if task_N == 0:
        from home_work_block4_Mike_B.HW_4_0 import do_HW_4_0
    elif task_N == 1:
        from home_work_block4_Mike_B.HW_4_1 import do_HW_4_1
    elif task_N == 2:
        from home_work_block4_Mike_B.HW_4_2 import do_HW_4_2
    elif task_N == 3:
        from home_work_block4_Mike_B.HW_4_3 import do_HW_4_3
    elif task_N == 4:
        from home_work_block4_Mike_B.HW_4_4 import do_HW_4_4
    else:
        if task_N not in (0, 1, 2, 3, 4, 5):
            print('Введите только указанные в начале программы цифры! Вы ввели иной символ.')
