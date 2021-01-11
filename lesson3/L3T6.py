import re
def int_func(c):
    result = re.findall(r'[a-z]+', c)
    if len(result) > 0:
        for i in result:
            x = len(i)
    else:
         return 'Ошибка при вводе слова'
    if c.islower() and c.isalpha() and len(c) == x:
        return c.capitalize()
    else:
        return 'Ошибка при вводе слова'


a = input('Введите слово латиницей в нижнем регистре ')
print(int_func(a))


