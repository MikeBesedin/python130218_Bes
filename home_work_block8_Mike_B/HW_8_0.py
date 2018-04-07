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

def benchmark_file_write(func): #декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
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

def test_input_for_int(func): #декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
    def wrapper(*args):
        input_elem_numb = 0
        for i in args:
            input_elem_numb +=1
            if isinstance(i, int)==True: #таким образом я бы проверял аргументы на тип словаря, списка и т.д.
                print('%s inputed element is integer' % input_elem_numb)
            else:
                print('%s inputed element is NOT an integer, it is %s' % (input_elem_numb,type(i)))
        func(*args)
    return wrapper

@test_input_for_int
def lots_of_numbers(*args):
    import time
    time.sleep(1)
    for num in args:
        for x in range(0, num):
            print(x, end=" ")
        print()

def kash_func(func): #вторая улучшенная версия декоратора, который кэширует результат работы функции,
                    #  тем самым обеспечивает единственный вызов функции
                    # использовать @lru_cache(maxsize= ) вместо самодельных
    import time
    import functools
    @functools.wraps(func) #сохраняет func.__name__ / func.__doc__
    def wrapper(*args,**kwargs):
        t = time.time()
        key = args + tuple(sorted(kwargs)) # для правильного сохранения ключей, т.к. в словаре элементы не упорядочнены
        #  и могут получаться при одинаковых аргументах разные ключи
        if key in wrapper.kash:
            t = (time.time() - t)
            print(t, 'сashed')
            return wrapper.kash[key]
        else:
            wrapper.kash[key] = func(*args)
            t = (time.time() - t)
            print(t, 'not сashed')
            return wrapper.kash[key]
    wrapper.kash = {}    # объявить данный метод можно только в этом месте! относится только к этому декоратору
    return wrapper

@kash_func
def sums(*args):
    import time
    x = 0
    for num in args:
        for i in range(0, num):
            x += i
    time.sleep(1)
    return x

print(sums(88, 88))
print(sums(88, 88))
print(sums.kash)
'''                  # мой первоначальный вариант
def kash_func(func): #декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
                    #с доступом к кэшу через глобал
    import time
    global kash
    kash = {}
    def wrapper(*args):
        t = time.time()
        if args in kash:
            t = (time.time() - t)
            print(t, 'сashed')
            return kash[args]
        else:
            kash[args] = func(*args)
            t = (time.time() - t)
            print(t, 'not сashed')
            return kash[args]
    return wrapper

@kash_func
def sums(*args):
    import time
    x = 0
    for num in args:
        for i in range(0, num):
            x += i
        print(x)
    time.sleep(1)
    return x

print(sums(88, 88))
print(sums(88, 88))
print(kash)
'''
