'''
Задача 2
Реализовать программу подсчета площади, периметра, объема геометрических фигур (треугольник, прямоугольник, квадрат,
 трапеция, окружность). Если одна из фигур не поддерживает вычисление одного из свойств, в программе должно быть
 вызвано исключение с человеко-читабельным сообщением и корректно обработано.
'''
import math

def exeptions_dec(func):  # декоратор для обработки исключений ввода данных и рассчета параметров фигур
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except (NotImplementedError, TypeError, AttributeError) as er:
            print('There is no volume for figure like rectangle and triangle\nError:', er)
        return func
    return inner

class Figure: # класс для вывода рассчитанных данных и отработки исключений декоратором

    @exeptions_dec
    def print_square(self):
        print('The square of {name} is {res:.2f}'.format(name=self.name, res=self.square()))

    @exeptions_dec
    def print_perimeter(self):
        print('The perimeter of {name} is {res:.2f}'.format(name=self.name, res=self.perimeter()))

    @exeptions_dec
    def print_volume(self):
        print('The volume of {name} is {res:.2f}'.format(name=self.name, res=self.volume()))

class Circle(Figure):
    def __init__(self, name):
        self.name = name
        self.diameter = float(input('Please, enter the diameter: '))

    def square(self):
        square = math.pi * self.diameter ** 2
        print()
        return square

    def perimeter(self):
        perimeter = math.pi * self.diameter
        return perimeter

    def volume(self):
        volume = (4/3) * math.pi * (self.diameter/2)**3
        return volume

class Square(Figure):
    def __init__(self, name):
        self.name = name
        self.side_a = float(input('Please, enter the side "a": '))

    def square(self):
        square = self.side_a ** 2
        return square

    def perimeter(self):
        perimeter = self.side_a * 4
        return perimeter

    def volume(self):
        volume = self.side_a ** 3
        return volume

class Rectangle(Figure):
    def __init__(self, name):
        self.name = name
        self.side_a = float(input('Please, enter the side "a": '))
        self.side_b = float(input('Please, enter the side "b": '))

    def square(self):
        square = self.side_a * self.side_b
        return square

    def perimeter(self):
        perimeter = (self.side_a + self.side_b) * 2
        return perimeter

class Triangle(Figure):
    def __init__(self, name):
        self.name = name
        self.side_a = float(input('Please, enter the side "a": '))
        self.side_b = float(input('Please, enter the side "b": '))
        self.side_c = float(input('Please, enter the side "c": '))
        self.check_triangle()

    def check_triangle(self):  # проверим, может ли быть треугольник с введенными длинам сторон
        triangle_sides = [self.side_a, self.side_b, self.side_c]
        max_side = max(triangle_sides)
        triangle_sides.pop(triangle_sides.index(max_side))
        if max_side >= sum(triangle_sides):
            print('Triangle with such sides doesn\'t exist. Please, try again.')
            self.__init__(self.name) # если фэйнл, запускаем ввод длин сторон заново

    def square(self):
        p = self.perimeter() / 2
        square = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return square

    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

while True:
    figure = input('Please, choose figure:\n' 
                   'input 1  for Circle\n'
                   'input 2  for Square\n'
                   'input 3  for. Rectangle\n'
                   'input 4  for Triangle\n'
                   'input 5  for Exit\n')
    if figure == '1':
        figure = Circle('Circle')
    elif figure == '2':
        figure = Square('Square')
    elif figure == '3':
        figure = Rectangle('Rectangle')
    elif figure == '4':
        figure = Triangle('Triangle')
    elif figure == '5':
        break
    else:
        print('Invalid input')
        continue
    to_do = input('Please, choose what would you like to calculate:\n' 
                  'input 1 for Square\n'
                  'input 2 for Perimeter\n'
                  'input 3 for Volume\n')
    if to_do == '1':
        figure.print_square()
    elif to_do == '2':
        figure.print_perimeter()
    elif to_do == '3':
        figure.print_volume()