from functools import reduce
spisok = [el for el in range(100, 1001)]
print(reduce(lambda x, y: x*y, spisok))
