def devision(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print('Error!')

#devision(5, 3)
#devision(3, 0)