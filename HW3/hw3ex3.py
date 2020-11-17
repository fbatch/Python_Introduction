# Exercise 3
def my_func(a, b, c):
    """Возвращает сумму наибольших двух из трёх аргументов

    Позиционные аргументы:
    a, b, c -- числа
    >>> my_func(3, 5, 7)
    12

    """
    if min(a, b, c) == a:
        return b + c
    elif min(a, b, c) == b:
        return a + c
    else:
        return a + b
