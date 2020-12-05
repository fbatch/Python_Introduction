class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = []
b = 0
while b != 'q':
    b = input('Введите число для добавления в список: ')
    a.append(b)
    try:
        if not b.isdigit():
            raise MyError('Вводите только числа!!!')
    except MyError as err:
        a.remove(b)
        print(err)
    else:
        print(f'Всё ок!')

print(f'Получившийся список из чисел:\n{list(map(int, a))}')

