import random
matrix = []
N = 4
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randrange(-4,5))
    matrix.append(row)
    print(row)
amount = 0
for i in range(N):
    for j in range(N):
        if i < j and matrix[i][j] >= 0:
            amount += 1


print('Amount of positive elements above main diag: ' + str(amount))