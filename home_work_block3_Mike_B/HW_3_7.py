string = input('Enter string: ')
symbol = input('Enter any low register symbol in that string: ')
UPstring = string.replace(symbol, symbol.upper())
Symbol = symbol.upper()
last_ind = UPstring.rfind(Symbol)
UPstring = UPstring[:last_ind]

print(UPstring)