print('----#0----')
alist = [1, 2, 3, 4]
alist.reverse()
print(alist, end='\n')

print('----#1----')
alist.sort()
alist.pop()
print(alist)

print('----#2----')
b = 'Hello!Anthony!Have!A!Good!Day!'.upper()
b = b.split('!')
b.pop()
print(b)

print('----#3----')
b.sort()
print('\n'.join(b))

'''Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“. Необходимо определить и вывести пол человека, 
которому данное письмо адресовано. Приглашение письма запрашивается у пользователя.'''
print('----#4----')
gender = input('''Would you be so kind to enter one of these:
                    "Dear Mr.", "Dear Mrs.", "Dear Miss", "Dear Ms."''')
if gender == "Dear Mr.":
    print('addressee is Male')
else:
    print('addressee is Female')

#возможноб последнюю задачу яне верно понял, и вводиться большое предложение
#тогда надо применять gender.startswith("Dear Mr.")





