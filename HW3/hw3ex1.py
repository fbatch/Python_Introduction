def devision(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print('Error!')

devision(3, 1)