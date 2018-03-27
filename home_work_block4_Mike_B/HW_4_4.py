'''Задача 4*
Дана квадратная матрица А(N,N). Составить программу подсчета количества положительных элементов,
расположенных выше главной диагонали.
'''
#для тестирования этой проги отдельно от HW_5_2 нужно раскоментить 3 строки
#from matrix_module import matrix_with_input_col_and_row_numbers
#matrix = matrix_with_input_col_and_row_numbers()
def do_HW_4_4(matrix):
    N = int(input('Введите кол-во строк = кол-ву столбцов одним целым числом и далее в матрице вводите тоже число: '))
    amount = 0
    if N == len(matrix):
        for i in range(N):
            for j in range(N):
                if i < j and matrix[i][j] >= 0:
                    amount += 1
        print('Amount of positive elements above main diag: ' + str(amount))
    else:
        print('')
#do_HW_4_4(matrix)
'''
#изначальный вариант, до модульной структуры:
import random
matrix = []
N = 4
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randrange(-4,5))
    matrix.append(row)
    print(row)
amount = 0
for i in range(N):
    for j in range(N):
        if i < j and matrix[i][j] >= 0:
            amount += 1
print('Amount of positive elements above main diag: ' + str(amount))'''