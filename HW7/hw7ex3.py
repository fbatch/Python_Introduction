class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return f'Поличившееся при сложении количество клеток: {self.num_cells + other.num_cells}.'

    def __sub__(self, other):
        if (self.num_cells - other.num_cells) >= 0:
            return f'Поличившееся при вычитании количество клеток: {self.num_cells - other.num_cells}.'
        else:
            return 'При вычитании получается отрицательное число.'

    def __mul__(self, other):
        return f'Поличившееся при умножении количество клеток: {self.num_cells * other.num_cells}.'

    def __truediv__(self, other):
        return f'Поличившееся при делении количество клеток: {self.num_cells // other.num_cells}.'

    def make_order(self, num_cells_per_row):
        print('Представление клетки в виде звёздочек:')
        while self.num_cells > num_cells_per_row:
            a = '*' * num_cells_per_row
            print(a)
            self.num_cells -= num_cells_per_row
        print('*' * (self.num_cells))


cell_1 = Cell(11)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_1.make_order(3)
