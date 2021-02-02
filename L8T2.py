class Divide:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider/denominator
        except:
            return (f"Ошибка: деление на ноль")


div = Divide(1, 0)
print(Divide.divide_by_null(5, 0))
print(Divide.divide_by_null(10, 1))
print(div.divide_by_null(1, 0))