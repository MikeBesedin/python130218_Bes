
def recursion_n(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10)+' '+str(recursion_n(n//10))

print(recursion_n(4568))

#str - это уже строковый метод и его использовать нельзя? 