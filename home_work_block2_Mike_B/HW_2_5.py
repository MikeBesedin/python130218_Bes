print('----#5----')
str1 = input('Please, enter first string: ')
str2 = input('And now second string: ')
index = str1.find(str2)
if index != -1:
    print('overlap has been found')
else:
    print('no overlap detected')