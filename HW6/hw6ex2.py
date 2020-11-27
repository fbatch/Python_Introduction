class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self, mass, thickness):
        print(f'{int(self._width * self._length * mass * thickness / 1000)} тонн')


a = Road(5000, 20)
a.count(25, 5)
