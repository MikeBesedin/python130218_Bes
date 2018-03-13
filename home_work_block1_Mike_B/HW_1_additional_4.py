a = float(input('Enter a: '))
b = float(input('Enter b: '))
lesser = (a + b)/2
bigger = a * b * 2
if a < b:
    a = lesser
    b = bigger
else:
    b = lesser
    a = bigger

print('a = %s and b = %s ' % (a,b))