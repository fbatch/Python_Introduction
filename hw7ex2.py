from abc import abstractmethod


class Wear:
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def count(self, x):
        if self.name.lower() == 'suit':
            return f'Материалы на костюм (класс Wear): {x * 2 + 0.3}.'
        elif self.name.lower() == 'coat':
            return f'Материалы на пальто (класс Wear): {"{:.2}".format(x / 6.5 + 0.5)}.'


suit = Wear('Suit')
coat = Wear('coat')
print(suit.count(10))
print(coat.count(6.5))


class Coat(Wear):
    def __init__(self, size, name='coat'):
        super().__init__(name)
        self.size = size

    @property
    def count(self):
        return f'В классе Coat: {self.size * 2 + 0.3}.'


class Suit(Wear):
    def __init__(self, height, name='coat'):
        super().__init__(name)
        self.height = height

    def count(self):
        return f'В классе Suit: {"{:.2f}".format(self.height / 6.5 + 0.5)}.'


coat_1 = Coat(10)
print(coat_1.count)  # при помощи @property без скобок

suit_1 = Suit(6.5)
print(suit_1.count())  # со скобками без использования @property
