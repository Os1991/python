class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'



class Printer(Warehouse):
    def print(self, colour):
        self.colour  = colour
        return f'Цвет печати {self.colour}'


class Scanner(Warehouse):
    def scan(self, speed):
        self.speed = speed
        return f'Скорость сканирования {self.speed}'


class Copier(Warehouse):
    def copier(self, format):
        self.format= format
        return f'Формат копирования {self.format}'


unit_1 = Printer('hp', 2000, 5, 10, 'черно-белый')
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.print('черно-белый'))
print(unit_3.copier('A3/A4'))
print(unit_1)