'''Задача 2
Для решений задач занятия №5 вынести общие части в модули. Сделать единую точку входа app.py.
Необходимо реализовать возможность старта выполнения кода одного из заданий сразу после запуска программы,
 а также после его выполнения предоставить возможность выполнить другое задание без повторного запуска программы.'''
#Легче всего когда все модули лежать в одной папке, но я попробовал,
#когда модули лежат в папках верхнего уровня, не включенного в стандартный путь посиска модулей.
import sys
sys.path.insert(0, '/home/linux/GitHub/python130218_Bes')
#from home_work_block4_Mike_B.matrix_module import matrix_with_input_col_and_row_numbers
#matrix = matrix_with_input_col_and_row_numbers()
'''
#хотел сделать, чтобы подгружало модуль матрицы в шапке программы 1 раз
#удалил закоментированных 2 строки из модулей
# но как ни крутил выдает: name 'matrix' is not defined
# но я ведь его только что определил!
# Почему импортированные модули на задачи с матрицами не видят переменную matrix?
# Пришлось по тупому закинуть в одну папку с этой программой модуль с матрицой.
# Впорос - а как правильно делать структуру модулей для сторонних пользовотелей?
'''
task_N = 0
print('Данная программа выполняет пять задач из блока задач к занятию №5.\n'
      'Можно вводить только целые цифры от 0 до 4, соответствующие номеру задачи,\n'
      'либо цифру 5, если хотите остановить программу!')
while task_N != 5:
    test_input = 0
    task_N = input('Введите номер задания для выполнения, либо 5 для остановки: ')
    while test_input != 1:
        try:
            task_N = int(task_N)
            test_input = 1
        except ValueError:
            print('Введена не целая цифра!')
            break
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
    elif task_N == 5:
        print('Программа завершена, спасибо за внимамние и буду рад увидеть ваши пожелания.')
        break
    else:
        if task_N not in (0, 1, 2, 3, 4, 5):
            print('Введите только указанные в начале программы цифры!')
