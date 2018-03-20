file = open('Task_1.txt')
string_count = 0
string_num = 0
for i in file:
    words_count = 0
    string_count += 1
    string_num += 1
    list_of_worlds = i.split(sep=' ')
    print(list_of_worlds)
    words_count = list_of_worlds.index(list_of_worlds[-1]) + 1
    print('In {} string {} symbols and {} worlds'.format(string_num, len(i), words_count  ))

print('Total amount of sting in file is', str(string_count))
file.close()
