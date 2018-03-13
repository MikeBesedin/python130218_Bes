text = input('Enter several worlds without punctuation marks, separated via space: ')
text = text.split()
shortest = text[0]
finded_vowels = set()
vowels = ['e', 'y', 'u', 'i', 'o', 'a']

for i in text:
    if len(i) < len(shortest):
        shortest = i

for i in shortest.lower():
    if i in vowels:
        finded_vowels.add(i)

for elem in finded_vowels:
    print(elem, end=' ')

#рассматривать случай, когда встречаются два и более слова одинаковой длинны
#считаю не следуют, т.к. не хватает конкретики в задаче, которое из них тогда рассматривать.
