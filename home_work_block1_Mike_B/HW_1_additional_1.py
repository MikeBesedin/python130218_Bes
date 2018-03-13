print('Input three differen digit, please!')
a = float(input('Enter first desirable integer: '))
b = float(input('Enter second desirable integer: '))
c = float(input('Enter third desirable integer: '))
maximum = 0
minimum = 0

if a > b and a > c:
    maximum = a
elif b > a and b > c:
    maximum = b
else:
    maximum = c

if a < b and a < c:
    minimum = a
elif b < c and b < a:
    minimum = b
else:
    minimum = c

print('The sum of min amd max digit is %s ' % (minimum + maximum))
