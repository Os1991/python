plus = int(input('Выручка компании '))
minus = int(input('Издержки компании '))
if plus >= minus:
    print('Прибыль')
else:
    print('Убыток')
if plus >= minus:
    rentab = (plus - minus) / plus
    print("%.2f" % rentab)
    chisl = int(input('Численность '))
    odin = (plus - minus)/chisl
    print("%.2f" % odin)
