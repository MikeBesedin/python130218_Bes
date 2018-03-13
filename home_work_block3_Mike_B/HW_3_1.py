import string
identifier = input('enter any world: ')
if identifier[0].isalpha() == True or identifier[0] == '_':
    for i in list(identifier):
        if i in list(string.ascii_lowercase) or i in list(string.ascii_uppercase) or i.isdigit() == True or i == '_':
            if i == identifier[len(identifier)-1]:
                print('this world can be an identifiers!')
                break
        else:
            print("use only symbols allowed for identifiers")
            break
else:
    print("use only symbols allowed for identifiers")
