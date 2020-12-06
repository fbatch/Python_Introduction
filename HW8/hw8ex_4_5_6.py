class Storage:
    """Класс Склад"""
    def __init__(self):  # space - кол-во мест на складе
        self.space = input(f'Сколько свободных мест на складе? ')
        while True:
            try:
                self.space = int(self.space)
                break
            except ValueError:
                print('Введите число!')
                self.space = input(f'Сколько свободных мест на складе? ')
        self.lst = []
        self.in_marketing = []
        self.in_finance = []
        
    def add_item(self, item):
        """Добавление элемента на склад"""
        if self.space == 0:
            print('Увы, на складе нет мест. Чтобы освободить место, воспользуйтесь методом "remove_item".')
        else:
            num = input(f'На складе {self.space} мест(а). Сколько элементов {item.name} добавить на склад? ')
            while True:
                try:
                    num = int(num)
                    if num <= self.space:
                        break
                except ValueError:
                    print('Введите число!')
                    num = input(f'Сколько элементов {item.name} добавить на склад? ')
                else:
                    print(f'Введите число, меньшее количества мест на складе ({self.space})!')
                    num = input(f'Сколько элементов {item.name} добавить на склад? ')
            for _ in range(num):
                self.lst.append(item.name)
            self.space -= num
            return f'Список предметов на складе: {self.lst}.'

    def remove_item(self, item):
        """Удаление элемента со склада"""
        num = input(f'Сколько элементов {item.name} убрать со склада? ')
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                print('Введите число!')
                num = input(f'Сколько элементов {item.name} убрать со склада? ')
        for _ in range(num):
            self.lst.remove(item.name)
        self.space += num
        return f'Список предметов на складе: {self.lst}.'

    def num_items(self, item):
        """Колисество элементов на складе"""
        if item == 'all':
            print(f'Количество предметов на складе: {len(self.lst)}. Свободных мест на складе: {self.space}.')
        else:
            print(f'Количество предметов {item.name} на складе: {self.lst.count(item.name)}. '
                  f'Свободных мест на складе: {self.space}.')

    def list_items(self):
        """Список всех элементов на складе"""
        print(f'Список предметов на складе: {self.lst}')

    def move_to(self, item):
        """Перемещение элемента со склада в отдел по маркетингу или финансам"""
        num = input(f'Сколько элементов {item.name} переместить в отдел? ')
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                print('Введите число!')
                num = input(f'Сколько элементов {item.name} переместить? ')
        while num > self.lst.count(item.name):
            num = input(f'Доступно всего {self.lst.count(item.name)} {item.name}. Вы указали больше. '
                        f'Сколько элементов {item.name} переместить? ')
            while True:
                try:
                    num = int(num)
                    break
                except ValueError:
                    print('Введите число!')
                    num = input(f'Доступно всего {self.lst.count(item.name)} {item.name}. Вы указали больше. '
                                f'Сколько элементов {item.name} переместить? ')
        a = input(f'Если нужно переместить {item.name} в отдел маркетинга, введите M,'
                  f' если в отдел финансов, введите F: ')
        while a.upper() != 'M' and a.upper() != 'F':
            a = input(f'Вы ввели недопустимые значения. Если нужно переместить {item.name} в отдел'
                      f' маркетинга, введите M, если в отдел финансов, введите F: ')
        if a.upper() == 'M':
            for _ in range(num):
                self.in_marketing.append(item.name)
                self.lst.remove(item.name)
            self.space += num
            return f'Предметы в отделе маркетинга: {self.in_marketing}.'
        if a.upper() == 'F':
            for _ in range(num):
                self.in_finance.append(item.name)
                self.lst.remove(item.name)
            self.space += num
            return f'Предметы в отделе финансов: {self.in_finance}.'


class Equipment:
    """Класс-родитель оргтехника"""
    def __init__(self, price):
        self.price = price


class Printer(Equipment):
    """Класс-наследник Принтер"""
    def __init__(self, price, name, color='black'):
        super().__init__(price)
        self.color = color
        self.name = name


class Scanner(Equipment):
    """Класс-наследник Сканер"""
    def __init__(self, price, name):
        super().__init__(price)
        self.name = name


class Xerox(Equipment):
    """Класс-наследник Ксерокс"""
    def __init__(self, price, name, year=2010):
        super().__init__(price)
        self.year = year
        self.name = name


# Тестирование программы

storage_1 = Storage()
scanner_1 = Scanner(98, 'Great Scanner')
printer_1 = Printer(45, 'Cool Printer')
xerox_1 = Xerox(287, 'Super Xerox')

storage_1.add_item(scanner_1)
storage_1.add_item(printer_1)
storage_1.add_item(xerox_1)

print(storage_1.lst)
storage_1.num_items(printer_1)
print(storage_1.move_to(printer_1))
print(storage_1.move_to(xerox_1))
storage_1.list_items()
storage_1.num_items('all')
storage_1.num_items(scanner_1)
