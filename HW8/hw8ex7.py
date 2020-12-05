class Complex:
    def __init__(self, r, i=0):
        self.r = r
        self.i = i

    def __add__(self, other):
        return f'{self.r + other.r} + {self.i + other.i}j'

    def __mul__(self, other):
        return f'{self.r * other.r - self.i * other.i} + {self.i * other.r + self.r * other.i}j'


a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a * b)
