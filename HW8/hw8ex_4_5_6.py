class Storage:
    def __init__(self, space=100):  # space - кол-во мест на складе
        self.space = space
        self.lst = []
        self.in_marketing = []
        self.in_finance = []
        
    def add_item(self, item, num=1):
        num = input(f'Сколько элементов {item.name} добавить на склад? ')
        try:
            num = int(num)
        except ValueError:
            print('Введите число!')
            num = int(input(f'Сколько элементов {item.name} добавить на склад? '))
        for _ in range(num):
            self.lst.append(item.name)
        self.space -= num
        return f'Список предметов на складе: {self.lst}.'

    def remove_item(self, item, num=1):
        try:
            num = int(input(f'Сколько элементов {item.name} убрать со склада? '))
        except ValueError:
            print('Введите число!')
            num = int(input(f'Сколько элементов {item.name} убрать со склада? '))
        for _ in range(num):
            self.lst.remove(item.name)
        self.space += num
        return f'Список предметов на складе: {self.lst}.'

    def num_items(self, item):
        if item == 'all':
            return f'Количество предметов на складе: {len(self.lst)}.'
        else:
            return f'Количество предметов {item.name} на складе: {self.lst.count(item.name)}.'

    def move_to(self, item, num=1):
        try:
            num = int(input(f'Сколько элементов {item.name} перемещаем? '))
        except ValueError:
            print('Введите число!')
            num = int(input(f'Сколько элементов {item.name} перемещаем? '))
        while num > self.lst.count(item.name):
            num = int(input(f'Доступно всего {self.lst.count(item.name)} {item.name}. Вы указали больше. '
                            f'Сколько элементов {item.name} перемещаем? '))
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
    def __init__(self, price):
        self.price = price


class Printer(Equipment):
    def __init__(self, price, name, color='black'):
        super().__init__(price)
        self.color = color
        self.name = name


class Scanner(Equipment):
    def __init__(self, price, name):
        super().__init__(price)
        self.name = name


class Xerox(Equipment):
    def __init__(self, price, name, year=2010):
        super().__init__(price)
        self.year = year
        self.name = name


storage_1 = Storage()
scanner_1 = Scanner(98, 'Great Scanner')
printer_1 = Printer(45, 'Cool Printer')
xerox_1 = Xerox(287, 'Super Xerox')

storage_1.add_item(scanner_1)
storage_1.add_item(printer_1)
storage_1.add_item(xerox_1)
print(storage_1.lst)
print(storage_1.num_items(printer_1))
print(storage_1.move_to(printer_1))
print(storage_1.move_to(xerox_1))
print(f'Список предметов на складе: {storage_1.lst}')
print(storage_1.num_items('all'))
