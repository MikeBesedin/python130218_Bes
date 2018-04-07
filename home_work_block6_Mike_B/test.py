import os
import shutil

def file_to_do():
    while True:
        file = input()
        home_path = input('Please, enter a path to your file:\n')

        if not home_path:
            pass
        else:
            home_path = os.chdir(home_path)
        if file in os.listdir():
            file_path = os.path.abspath(file)
        else:
            print('There is no such file. Please, try again')
            continue
        file_to_do.name = file
        file_to_do.file_path = file_path
        return file_path
print(file_to_do())