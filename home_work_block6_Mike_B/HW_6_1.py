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
    print('In {}-st string {} symbols and {} worlds'.format(string_num, len(i), words_count  ))

print('Total amount of sting in file is', str(string_count))
file.close()
''' 
В сети нашел такое решение, но для меня не ясен момент с флагами, можно объяснить на лекции?
Выглядит интересно:
f = open('text.txt')
line = 0
for i in f:
    line += 1
 
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
 
    print(i,len(i),'симв.',word,'сл.')
 
print(line,'стр.')
f.close()
'''