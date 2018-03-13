import random
matrix = []
N = 3
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randrange(1,5))
    matrix.append(row)
    print(row)
S = 0
for row in matrix:
    for i in row:
        S += i
M = S / (N * N)
print()
print(M)