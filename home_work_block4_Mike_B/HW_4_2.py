import random
matrix = []
NROW = 3
NCOL = 4
p1 = int(input('enter floor integer in range (1, 10): '))
p2 = int(input('enter ceiling range integer in range (1, 10): '))
print('Your random matrix is:')
for i in range(NROW):
    row = []
    for j in range(NCOL):
        row.append(random.randrange(1,11))
    matrix.append(row)
    print(row)

numbers_of_elem = 0
for row in matrix:
    for elem in row:
        if p1 <= elem <= p2:
            numbers_of_elem += 1
print()
print('Amount of elements in matrix between {} and {} is {}'.format(p1, p2, numbers_of_elem))