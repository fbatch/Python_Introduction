# Exercise 4
def my_func(x, y):
    if ((type(x) == int) or (type(x) == float)) and (x > 0) and (type(y) == int) and (y < 0):
        result = 1
        for i in range(abs(y)):
            result *= x
        print(1 / result)
    else:
        print('Error, incorrect parameters entered!')

my_func(3, -4)