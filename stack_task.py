'''ЗАДАНИЕ
Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
push n Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
pop Удалить из стека последний элемент. Программа должна вывести его значение.
back Программа должна вывести значение последнего элемента, не удаляя его из стека.
size Программа должна вывести количество элементов в стеке.
clear Программа должна очистить стек и вывести ok.
exit Программа должна вывести bye и завершить работу.
Входные данные
Команды управления стеком вводятся в описанном ранее формате по 1 на строке.

Гарантируется, что набор входных команд удовлетворяет следующим требованиям:
максимальное количество элементов в стеке в любой момент не превосходит 100,
все команды pop и back корректны, то есть при их исполнении в стеке содержится хотя бы один элемент.

Пример выполнения программы:
входные данные
push 3
push 14
'''
L = []
while True:
    action = input('For working with stack print one of these: push, pop, back, clear, exit: ')
    if action == 'push':
        count = 0
        for i in L:
            count += 1
        if count == 100:
            print('You have been reached maximum stack size! We are tired and quitting now.')
            raise SystemExit
        else:
            #elem =
            L = L +[input('enter element to add to stack:')]
            print('Your stack is %s' % L)
    elif action == 'pop':
        if L == []:
            print('cant pop anything from empty stack!')
            continue
        else:
            print(L[-1])
            L = L[:-1]
            print('Your stack is %s' % L)
    elif action == 'back':
        if L == []:
            print('cant do back action with empty stack!')
            continue
        else:
            print(L[-1])
    elif action == 'size':
        count = 0
        for i in L:
            count += 1
        print(count)
    elif action == 'clear':
        L = []
        print('ok, you have empty stack now')
    elif action == 'exit':
        print('buy')
        raise SystemExit
