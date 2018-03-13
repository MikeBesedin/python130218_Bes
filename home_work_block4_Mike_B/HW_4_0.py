import random
length = int(input('Enter length of list as integer: '))
AN_list = []
for i in range(length):
    AN_list.append(random.randint(0, 10))
print(AN_list)

AN_counters = []
for i in AN_list:
    AN_counters.append(AN_list.count(i))
print(AN_counters)

maximum = max(AN_counters)
print(maximum)
print('------')

same_element = []
for j in range(length):
    if AN_counters[j] == maximum and AN_list[j] not in same_element:
        print('Element %s appears in list %s times' % (AN_list[j], maximum))
        same_element.append(AN_list[j])