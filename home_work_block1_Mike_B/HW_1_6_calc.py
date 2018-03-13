print('''
            Инструкция: "0 = exit". 
            Вводим символ + - / * , означающий требуюмую арифметическую операции над числами.
            Вводим первую переменную x, потом вторую y.
            ''')
while True:
    s = input("Введите арифметический знак + или - или * или /: ")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = input("x=")
        y = input("y=")

        while True:
                if not x.isdigit():
                    try:
                        float(x)
                    except ValueError:
                        print('вводите цифры, а не всякую муть')
                        break
                if not y.isdigit():
                    try:
                        float(y)
                    except ValueError:
                        print('вводите цифры, а не всякую муть')
                        break

                x = float(x)
                y = float(y)
                if s == '+':
                    print("Result: %.4f" % (x + y))
                    break
                elif s == '-':
                    print("Result: %.4f" % (x - y))
                    break
                elif s == '*':
                    print("Result: %.4f" % (x * y))
                    break
                elif s == '/':
                    if y != 0:
                        print("Result: %.4f" % (x / y))
                        break
                    else:
                        print("Неавторизированное деление на 0 - УНИЧТОЖИТЬ!")
                        break
    else:
        print("Вводите <strong>только</strong> указанные арифметические знаки")