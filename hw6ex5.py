from termcolor import colored


class Stationary:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):
    def draw(self):
        print(colored('Запуск ручки.', 'blue'))


class Pencil(Stationary):
    def draw(self):
        print(colored('Запуск карандаша.', 'red'))


class Handle(Stationary):
    def draw(self):
        print('\x1b[0;30;43m' + 'Запуск маркера.' + '\x1b[0m')


a = Pen()
a.draw()

b = Pencil()
b.draw()

c = Handle()
c.draw()
