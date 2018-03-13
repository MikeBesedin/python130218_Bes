Max = 100
list = []
def list_gen(Max, list):
    for x in range(2, Max+1):
        list.append(x)
    return(list)

def test_list_gen():
    if [2, 3, 4] == list_gen(4, []):
        print('list_gen test passed')
    else:
        print('list_gen test failed')

test_list_gen()
list_gen(Max, list)
x = 0

def Eratosfen(Max, list, x):
    while x <= list[-1]:
        for elem in list[x + 1:Max - 1]:
            if elem % list[x] == 0:
                list.remove(elem)
        x += 1
    return(list)

def test_Eratosfen():
    if [2, 3, 5, 7] == Eratosfen(8, [2, 3, 4, 5, 6, 7, 8], 0):
        print('Eratosfen test passed')
    else:
        print('Eratosfen test failed')

test_Eratosfen()

Eratosfen(Max, list, x)
print(list)





'''пофанился с этим кодом, но прямо получил удовольствие и горд собой )
вопросик: а где подразумевается применение lambda в этом коде и оправдано ли это с точки зрения улучшения 
логической структуры кода? 
пробовал заменить
     for elem in list[x + 1:Max - 2]:
        if elem % list[x] == 0:
            list.remove(elem)
            
на однострочную  list.remove(filter(lambda elem:elem % list[x] == 0, list[x + 1:Max - 2]))
но что то не срослось, да и не думаю, что подобную конструкцию одобрил бы Гвидо )  
'''
