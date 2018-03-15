path = '/home/linux/python130218_Bes/home_work_block6_Mike_B/hw_0.txt'
hw_0_file = open(path,'x')
while True:
    users_string = input('enter any string, if you want to end it just press Enter: ')
    if users_string == '':
        break
    else:
        hw_0_file.write(users_string+'\n')
hw_0_file.close()

'''или первых две строки
file_name = input('Enter some cool file name: ')
hw_0_file = open(file_name,'x')
'''