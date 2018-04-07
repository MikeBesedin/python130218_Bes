'''Задача 5*
Реализовать программу, позволяющую осуществлять управление файлами:
копирование, создание, удаление, переименование.
Необходимо предусмотреть возможность смен директории.
Изначально используется текущий каталог запуска скрипта программы.
'''
import os
import shutil

def file_to_do():
    while True:
        file = input()
        home_path = input('Please, enter a path to your file:\n')
        if not home_path:
            pass
        else:
            os.chdir(home_path)
        if file in os.listdir():
            file_path = os.path.abspath(file)
            file_to_do.name = file
            file_to_do.file_path = file_path
        else:
            print('There is no such file. Please, try again')
            continue
        return file_path

# function to copy file from one dir to another
def copy_file(path_to_new_folder):
    print('Please, enter the name of the file to copy:')
    shutil.copy(r'{}'.format(file_to_do()), r'{}'.format(path_to_new_folder))
    copy_file.path_to_new_folder = path_to_new_folder


# function to create a new file
def create_file(file_name, file_folder):
    os.chdir(file_folder)
    fn = file_name
    with open(file_name, 'w') as user_file:
        pass
    create_file.fn=file_name


# function to delete the file
def del_file():
    print('Please, enter the name of the file your would like to delete:')
    file_path = file_to_do()
    os.remove(file_path)

# function to rename the file
def rename_file():
    print('Please, enter the name of the file your would like to rename:')
    file_path = file_to_do()
    new_name = input('Please, enter a new name of file:\n')
    os.rename(file_path, new_name)
    rename_file.new_name = new_name
    return new_name


# circle to input operations
while True:
    what_to_do = input('Please, enter the number of operation you would like to do:\n'
                       '1. create\n'
                       '2. copy\n'
                       '3. delete\n'
                       '4. rename\n'
                       '5. quit\n')
    if what_to_do[0] == '1' or what_to_do == 'create':
        create_file(input('Please, enter the name of a new file:\n'), input('Please, enter a new path to your file:\n'))
        print('file {} created'.format(create_file.fn))
    elif what_to_do[0] == '2' or what_to_do == 'copy':
        copy_file(input('Please, enter a new path to your file:\n'))
        print('file {} coppied to {}'.format(file_to_do.name, copy_file.path_to_new_folder))
    elif what_to_do[0] == '3' or what_to_do == 'delete':
        del_file()
        print('file {} deleted'.format(file_to_do.name))
    elif what_to_do[0] == '4' or what_to_do == 'rename':
        rename_file()
        print('file {} was renamed to {}'.format(os.path.basename(file_to_do.file_path), rename_file.new_name))
    elif what_to_do[0] == '5' or what_to_do == 'quit':
        print('byu')
        quit()

