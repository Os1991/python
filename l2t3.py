calendar = [0, 'winter', 'winter', 'spring', 'spring', 'spring',
            'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
month = int(input('Введите номер месяца '))
if month > 12 or month < 1:
    print('Введите число от 1 до 12')
else:
    print(calendar[month])


calendar = {1: 'winter', 2: 'winter', 12: 'winter',
            3: 'spring', 4: 'spring', 5: 'spring',
            6: 'summer', 7: 'summer', 8: 'summer',
            9: 'fall', 10: 'fall', 11: 'fall'}
month = int(input('Введите номер месяца '))
if month > 12 or month < 1:
    print('Введите число от 1 до 12')
else:
    print(calendar.get(month))
