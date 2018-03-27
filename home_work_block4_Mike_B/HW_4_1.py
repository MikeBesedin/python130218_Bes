'''Задача 1
Дана целая матрица А(N,N). Составить программу подсчета среднего арифметического значения элементов матрицы.
'''
#для тестирования этой проги отдельно от HW_5_2 нужно раскоментить 3 строки
#from matrix_module import matrix_with_input_col_and_row_numbers
#matrix = matrix_with_input_col_and_row_numbers()
def do_HW_4_1(matrix):
    S = 0
    cell_numbers = 0
    for row in matrix:
        for elem in row:
            S += elem
            cell_numbers += 1
    average = S / (cell_numbers)
    print()
    print('Среднее арифметическое элементов матрицы: {}'.format(average))
#do_HW_4_1(matrix)


'''
#изначальный вариант, до модульной структуры:
import random
matrix = []
N = 3
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randrange(1,5))
    matrix.append(row)
    print(row)
S = 0
for row in matrix:
    for i in row:
        S += i
M = S / (N * N)
print()
print(M)'''