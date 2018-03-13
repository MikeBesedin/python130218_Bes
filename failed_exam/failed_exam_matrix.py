
x = []
N = int(input('enter matrix dimension like integer: '))
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(input('enter matix cell: ')))
    x.append(row)
print('before {}'.format(x))
y = []
j1 = int(input('enter first column number to swap(starting with 1): ')) - 1
j2 = int(input('enter second column number to swap with first: ')) - 1
for i in range(N):
    row = []
    for j in range(N):
        if j == j1:
            row.append(x[i][j2])
        elif j == j2:
            row.append(x[i][j1])
        else:
            row.append(x[i][j])
    y.append(row)
x = y
print('after {}'.format(x))
