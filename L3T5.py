print("Для выхода из программы введите букву")
count = 0
x = [1]
while len(x) > 0:
    a = list(input("Введите числа через пробел ").split(" "))
    for i in a:
        if i.isdigit():
         count += int(i)
        else:
            print('Работа программы завершена')
            x.clear()
    print(f"Результат {count}")



