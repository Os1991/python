class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, el)) for el in self.matrix])

    def __getitem__(self, i):
        return self.matrix[i]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


c = [[9, 2, 3], [6, 3, 1]]
a = Matrix(c)
q = [[2, 4, 6], [2, 8, 3]]
b = Matrix(q)
print(a + b)
