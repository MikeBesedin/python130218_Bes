'''Задача 0
Реализовать модуль, содержащий следующие функции декораторы:
декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
'''

def benchmark(func): #декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
    import time
    def wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        print()
        print("time to do this func: %s" % (time.time() - t))
    return wrapper

def benchmark_file_write(func): #позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
    import time
    def wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        t = (time.time() - t)
        with open('benchmark_results.txt', 'w') as f:
            print()
            print("time to do this func: %s" % t, file=f)
            print('name func is: %s' % func.__name__, file=f)
            print('given arg:', *args, **kwargs, file=f)
    return wrapper

@benchmark_file_write
def lots_of_numbers(max):
    import time
    time.sleep(1)
    for x in range(0, max):
        print(x, end=" ")


lots_of_numbers(777)
"""
def benchmark(func): #декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        func_result = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return func_result
    return wrapper
"""