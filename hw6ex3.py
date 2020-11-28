class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': input('Wage: '), 'bonus': input('Bonus: ')}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_full_income(self):
        print(f'Полный доход сотрудника: {int(self._income.get("wage")) + int(self._income.get("bonus"))}')


b = Position('Ivan', 'Ivanov', 'CEO')
print(b.name)
print(b.surname)
print(b.position)
print(b._income)
b.get_full_name()
b.get_full_income()
