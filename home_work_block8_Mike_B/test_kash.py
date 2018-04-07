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