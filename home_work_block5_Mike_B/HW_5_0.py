def task(text=input('enter any text: '), y = input('enter separator: ')):
    text = text.split(sep = y)
    length = list(map(lambda x: len(x), text))
    task = list(map(lambda x,y: str(x)+y, length, text))
    return(task)

task()

def test_task():
    if ['5hello', '4mike'] == task(text='hello mike', y=' '):
        print('all tests passed')
    else:
        print('noOOOO!!1111')

test_task()
'''
возможно, я не верно понял, и нужно было тэсты прописать отельные тэсты на split / len / ....
но мне проще принтами проверять результат:
логический блок написал - принтом с вводом разных данных прогнал, может в каких то случаях результат меня удивит )
Т.е. в начале я написал и проверил работоспособность вот так:

def task(text=input('enter any text: '), y = input('enter separator: ')):
    text = text.split(sep = y)
    print(text)
    length = list(map(lambda x: len(x), text))
    task = list(map(lambda x,y: str(x)+y, length, text))
    print(task)
    
task()
приедерживаюсь этому прниципу постоянно
'''