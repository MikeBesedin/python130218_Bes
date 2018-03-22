def recursion_n(n):
    if n < 10:
        return n
    else:
        return n % 10 + recursion_n(n//10)
print(recursion_n(777))

#удобный для изучения данного вопроса ресурс с построчным выполнением кода http://pythontutor.ru/lessons/functions/
