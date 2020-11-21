from functools import reduce

def my_func(a, b):
    return a * b

lst = [el for el in range(100, 1001, 2)]
print(reduce(my_func, lst))
