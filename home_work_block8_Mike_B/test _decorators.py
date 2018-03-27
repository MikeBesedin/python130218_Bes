def dec_sum(f):
    def wrapper(x,y):
        print(x+y)
        f(x,y)
        print(x*y)
    return wrapper

@dec_sum
def printxy(x,y):
    print(x,y)

printxy(10,5)

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