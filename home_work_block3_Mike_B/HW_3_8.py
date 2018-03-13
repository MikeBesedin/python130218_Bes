grades = [('Ann', 9),('John', 7),('Smith', 5),('George', 6)]
'''
#пытался решить задачу простыми методами, мутил-крутил, потратил уйму времени,
#но лучшее, до чего дошел ниже 

mark = []
for i in range(len(grades)):
    mark.append(grades[i][1])
mark.sort()
print(mark)
j = 0
while j < len(grades):
    for i in range(len(grades)):
        if grades[i][1] == mark[j]:
            print(grades[i])
            print('Hello {0}! Your grade is {1}'.format(grades[i]))
#принт с форматом вызывает ошибку выхода за диапозон индексов, почему??
            j +=1
            grades.pop(i)
            break
            
#но задачу так и не решил, сдался, и решил использовать sorted
'''
grades = sorted(grades, key=lambda x: x[::-1])
for i in grades:
    print('Hello %s! Your grade is %s' % i)
 #   print('Hello {a[0]}, your grade is {a[1]}'.format(a = i))
 # формат более гибкий, но и более сложный пока для меня, приходиться над ним посидеть, чтобы не выбивало ошибку