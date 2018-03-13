import random
N = 10
L = []
for i in range(N):
    n = random.randint(0, 2)
    L.append(n)
print(L)
j = 0
for i in L:
    if i == 0:
        j += 1
for elem in range(j):
    L.remove(0)
    L.append(-1)
print(L)