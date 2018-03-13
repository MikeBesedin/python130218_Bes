print('Input three digit, that will be a, d, c in equation a*x^4+d*x^2+c=0')
a = float(input('Enter a: '))
d = float(input('Enter d: '))
c = float(input('Enter c: '))
print('Input 2 digit that needed to check, if they are root of equation a*x^4+d*x^2+c=0')
X = float(input('Enter first desirable number: '))
Y = float(input('Enter second desirable number: '))

if a*(X**4) + d*(X**2) + c == 0:
    print('X is root of equation indeed')
else:
    print('X is not root of equation')

if a*(Y**4) + d*(Y**2) + c == 0:
    print('Y is root of equation')
else:
    print('Y is not root of equation')

