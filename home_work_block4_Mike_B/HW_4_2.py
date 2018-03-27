'''Задача 2
Дана вещественная матрица А(3,4). Составить программу подсчета количества элементов матрицы,
удовлетворяющих условию р1<=a(i,j)<=p2. Значения р1 и р2 запрашиваются у пользователя.
'''
#для тестирования этой проги отдельно от HW_5_2 нужно раскоментить 3 строки
#from matrix_module import matrix_with_input_col_and_row_numbers
#matrix = matrix_with_input_col_and_row_numbers()
def do_HW_4_2(matrix):
    p1 = int(input('enter floor integer in range (1, 10): '))
    p2 = int(input('enter ceiling range integer in range (1, 10): '))
    numbers_of_elem = 0
    for row in matrix:
        for elem in row:
            if p1 <= elem <= p2:
                numbers_of_elem += 1
    print()
    print('Amount of elements in matrix between {} and {} is {}'.format(p1, p2, numbers_of_elem))
#do_HW_4_2()
'''
#изначальный вариант, до модульной структуры:
import random
matrix = []
NROW = 3
NCOL = 4
print('Your random matrix is:')
for i in range(NROW):
    row = []
    for j in range(NCOL):
        row.append(random.randrange(1,11))
    matrix.append(row)
    print(row)
    
p1 = int(input('enter floor integer in range (1, 10): '))
p2 = int(input('enter ceiling range integer in range (1, 10): '))
numbers_of_elem = 0
for row in matrix:
    for elem in row:
        if p1 <= elem <= p2:
            numbers_of_elem += 1
print()
print('Amount of elements in matrix between {} and {} is {}'.format(p1, p2, numbers_of_elem))'''
