class Worker:


    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        self._income = {'wage': self.wage, 'bonus': self.bonus}
        return sum(self._income.values())


a = Position('ser', 'okr', 'geo', 500, 200)
print(a.get_full_name())
print(a.get_total_income())
