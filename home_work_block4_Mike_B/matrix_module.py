# решил потренироваться в проверке ввода значений через exception
def matrix_with_input_col_and_row_numbers():
    import random
    test_input_row_col = 0
    while True:
        while test_input_row_col != 1:
            row = input("Введите кол-во рядов матрицы, целое число в разумных пределах: ")
            col = input("Введите кол-во столбцов матрицы, целое число в разумных пределах: ")
            if not row.isdigit():
                try:
                    int(row)
                except ValueError:
                    print('вводите целую цифру для кол-ва рядов')
                    break
            if not col.isdigit():
                try:
                    int(col)
                except ValueError:
                    print('вводите целую цифру для кол-ва столбцов')
                    break
            row = abs(int(row))
            col = abs(int(col))
            matrix = [[random.randrange(-10,10) for x in range(col)] for y in range(row)]
            test_input_row_col = 1
        else:
            print('Отрандомило такую матрицу: ')
            for i in matrix:
                print(i)
            return(matrix)




