class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split('-'):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Введены корректные даныне'
                else:
                    return f'Введите год в диапозоне от 0 до 2021'
            else:
                return f'Введите месяц в диапозоне от 1 до 12'
        else:
            return f'Введите день в диапазоне от 1 до 31'

    def __str__(self):
        return f'Current date - {Data.extract(self.date)}'


day = Data('11-1-2001')
print(day)
print(Data.validation(3, 11, 2050))
print(day.validation(2, 13, 2011))
print(Data.extract('01-02-2011'))
print(day.extract('3-12-2020'))
print(Data.validation(1, 2, 2021))
