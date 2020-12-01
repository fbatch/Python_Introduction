class Matrix:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        a = 0
        s = ''
        for i in self.x:
            a += 1
            s += '      '.join(map(str, i)) + '\n'
        return s

    def __add__(self, matrix_2):
        raw = len(self.x)
        col = len(matrix_2.x[0])
        for i in range(raw):
            for j in range(col):
                self.x[i][j] = self.x[i][j] + matrix_2.x[i][j]
            result = self.x
        return Matrix(result)


m_1 = Matrix([[1, 2, 7],
              [1, 5, 4],
              [5, 6, 3],
              [9, 2, 8]])

m_2 = Matrix([[1, 2, 7],
              [1, 5, 4],
              [5, 6, 3],
              [9, 2, 8]])

print(m_1.__add__(m_2))
