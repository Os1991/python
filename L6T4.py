class Car:
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def showspeed():
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        if self.speed > 60:
            TownCar.showspeed()


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        if self.speed > 40:
            WorkCar.showspeed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

ford = WorkCar(50, 'black', 'ford')
print(ford.name, ford.color, ford.speed, ford.is_police)

