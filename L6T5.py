class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Начало отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):

    def draw(self):
        print('Рукоятка')


a = Stationery(1)
a.draw()
