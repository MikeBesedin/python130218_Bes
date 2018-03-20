def recursion_n(n):
    if n < 10:
        return n
    else:
        return n % 10, recursion_n(n//10)
print(recursion_n(4568))