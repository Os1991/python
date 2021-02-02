class Error:
    def __init__(self, *args):
        self.my_list = []

    def vvod(self):

        while True:
            try:
                self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                selection = input(f'Попробовать еще раз? Y/N ')

                if selection == 'Y' or selection == 'y':
                    print(try_except.vvod())
                elif selection == 'N' or selection == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


training = Error(1)
print(training.vvod())