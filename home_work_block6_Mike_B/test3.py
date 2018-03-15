Max = 8
list = []
x = 2
for x in range(2, Max+1):
    list.append(x)
print(list)
print()

x = 0

while x < list[-1]:
    for elem in list[x + 1:Max - 1]:
        if elem % list[x] == 0:
            list.remove(elem)
    x += 1

print(list)

