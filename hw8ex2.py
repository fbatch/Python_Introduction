class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    if b == 0:
        raise MyError("Вы пытаетесь делить на ноль!")
except ValueError:
    print("Стоило ввести число!")
except MyError as err:
    print(err)
else:
    print(f"Часное от деления a на b = {a / b}")
