
def memoize(function):
    global memo
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(25))
print(memo)


'''def dec_sum(f):
    def wrapper(x,y):
        print(x+y)
        f(x,y)
        print(x*y)
    return wrapper

@dec_sum
def printxy(x,y):
    print(x,y)

printxy(10,5)
'''

'''def dec(f):
    def wrapper():
        print('before')
        f()
        print('after')
    return wrapper

def dec_inside(f):
    def wrapper():
        print('before_inside')
        f()
    return wrapper

@dec
@dec_inside
def show():
    print('middle_new')

show()
'''