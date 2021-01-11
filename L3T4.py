def my_func(x, y):
    return x ** y


a = int(input('Введите действительное положительное число '))
b = int(input('Введите целое отрицательное число'))
print(my_func(a, b))

def my_func_new(x, y):
    c = 1/x
    b = x
    i = 0
    while i < abs(y):
        i += 1
        x = c * (1/b)
    return x


a = int(input('Введите действительное положительное число '))
b = int(input('Введите целое отрицательное число'))
print(my_func_new(a, b))