class Storage:
    """Класс Склад"""
    def __init__(self):  # space - number of free places in the warehouse
        self.space = input(f'How many free places in the warehouse? ')
        while True:
            try:
                self.space = int(self.space)
                if self.space > 0:
                    break
                else:
                    while True:
                        print('Enter a positive number!')
                        self.space = input(f'How many free places in the warehouse? ')
                        break
            except ValueError:
                print('Enter number!')
                self.space = input(f'How many free places in the warehouse? ')
        self.lst = []
        self.in_marketing = []
        self.in_finance = []

    def add_item(self, item):
        """Добавление элемента на склад"""
        if self.space == 0:
            print('Sorry, no free places available. Use "remove_item" in order to free up space.')
        else:
            num = input(f'There are {self.space} free place(s) in the warehouse. '
                        f'How many {item.name}s do you want to add to the warehouse? ')
            while True:
                try:
                    num = int(num)
                    if num <= self.space:
                        break
                except ValueError:
                    print('Enter number!')
                    num = input(f'How many {item.name}s do you want to add to the warehouse? ')
                else:
                    print(f'Enter a number, less than the number of free places in the warehouse ({self.space})!')
                    num = input(f'How many {item.name}s do you want to add to the warehouse? ')
            for _ in range(num):
                self.lst.append(item.name)
            self.space -= num
            return f'List of items in the warehouse: {self.lst}.'

    def remove_item(self, item):
        """Удаление элемента со склада"""
        num = input(f'How many {item.name}s do you want to remove from the warehouse? ')
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                print('Enter number!')
                num = input(f'How many {item.name}s do you want to remove from the warehouse? ')
        for _ in range(num):
            self.lst.remove(item.name)
        self.space += num
        return f'List of items in the warehouse: {self.lst}.'

    def num_items(self, item):
        """Колисество элементов на складе"""
        if item == 'all':
            print(f'Number of items in the warehouse: {len(self.lst)}. '
                  f'Number of free places in the warehouse: {self.space}.')
        else:
            print(f'Number of {item.name}s in the warehouse: {self.lst.count(item.name)}. '
                  f'Number of free places in the warehouse: {self.space}.')

    def list_items(self):
        """Список всех элементов на складе"""
        print(f'List of items in the warehouse: {self.lst}')

    def move_to(self, item):
        """Перемещение элемента со склада в отдел по маркетингу или финансам"""
        num = input(f'How many {item.name}s do you want to move to a special department? ')
        while True:
            try:
                num = int(num)
                break
            except ValueError:
                print('Enter number!')
                num = input(f'How many {item.name}s do you want to move? ')
        while num > self.lst.count(item.name):
            num = input(f'There are only {self.lst.count(item.name)} {item.name}s available. '
                        f'You entered a greater value. How many {item.name}s do you want to move? ')
            while True:
                try:
                    num = int(num)
                    break
                except ValueError:
                    print('Enter number!')
                    num = input(f'There are only {self.lst.count(item.name)} {item.name}s available. '
                                f'You entered a greater value. How many {item.name}s do you want to move? ')
        a = input(f'If you want to move {item.name}s to the department of marketing, enter M. '
                  f'\nIf you want to move {item.name}s to the department of finance, enter F: ')
        while a.upper() != 'M' and a.upper() != 'F':
            a = input(f'You entered invalid values. If you want to move {item.name}s to the department of marketing, '
                      f'enter M. \nIf you want to move {item.name}s to the department of finance, enter F: ')
        if a.upper() == 'M':
            for _ in range(num):
                self.in_marketing.append(item.name)
                self.lst.remove(item.name)
            self.space += num
            return f'Elements in the marketing department: {self.in_marketing}.'
        if a.upper() == 'F':
            for _ in range(num):
                self.in_finance.append(item.name)
                self.lst.remove(item.name)
            self.space += num
            return f'Elements in the finance department: {self.in_finance}.'


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
scanner_1 = Scanner(98, 'Scanner-X')
printer_1 = Printer(45, 'Printer-Y')
xerox_1 = Xerox(287, 'Xerox-Z')

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


# just checking