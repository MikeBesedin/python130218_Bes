a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
maximum = 0
minimum = 0
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    if a > b and a > c:
        maximum = a
    elif b > a and b > c:
        maximum = b
    else:
        maximum = c
    print("maximum is %s" % maximum)
else:
    if a < b and a < c:
        minimum = a
    elif b < c and b < a:
        minimum = b
    else:
        minimum = c
    print("minimum is %s" % minimum)


