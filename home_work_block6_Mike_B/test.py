
list = [
   {'name': 'Ivan', 'surname': 'Borisenko', 'sex': 'male', 'age': '29'},
   {'name': 'Alex', 'surname': 'Zabolockii', 'sex': 'male', 'age': '28'},
    {'name': 'Nadzja', 'surname': 'Kapko', 'sex': 'female', 'age': '27'},
   {'name': 'Alex', 'surname': 'Buiko', 'sex': 'male', 'age': '27'},
    {'name': 'Vitali', 'surname': 'Buiko', 'sex': 'male', 'age': '27'}
]
for dic in list:
    print(list.index(dic)+1)

'''
def find_stud(list):
   dict_check = {'name': '', 'surname': '', 'sex': '', 'age': ''}    # Function to input information to search
   def search_info():
       for key in dict_check.keys():
           print('Please, enter an information about {}, or press "Enter" to skip:'.format(key.upper()))
           dict_check[key] = input()
       return dict_check    # Ask function search_info
   dict_check = search_info()    # Count how many parameters we use to search the student
   find_numbers = 0

   for value in dict_check.values():
       if value: find_numbers += 1    # Check if there are students in our list with input information
   for dic in list:
       if dic.items() & dict_check.items() and len(dic.items() & dict_check.items()) == find_numbers:
           print('{} {}, {} years old, {}'.format(dic['surname'], dic['name'], dic['age'], dic['sex']))
           print(list.index(dic))
'''