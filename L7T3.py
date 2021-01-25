class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'{self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'{sub} ' if sub > 0 else 'Разница клеток меньше или равноа нулю'

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(7)
another_cell = Cell(5)
print(cell + another_cell)
print(cell - another_cell)
print(cell / another_cell)
print(cell * another_cell)
print(another_cell.make_order(5))