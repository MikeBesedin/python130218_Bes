def kash_func(func): #декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
    import time
    def wrapper(*args,**kwargs):
        t = time.time()
        key = args + tuple(sorted(kwargs))
        if key in wrapper.kash:
            t = (time.time() - t)
            print(t, 'сashed')
            return wrapper.kash[key]
        else:
            wrapper.kash[key] = func(*args)
            t = (time.time() - t)
            print(t, 'not сashed')
            return wrapper.kash[key]
    wrapper.kash = {}
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

'''def kash_func(func): #декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
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
print(kash)'''

