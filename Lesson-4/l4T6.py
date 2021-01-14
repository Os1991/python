from itertools import count, cycle

def counts(a):
    for el in count(a):
        if el > 20:
            break
        else:
            print(el)


a = int(input('Enter number - '))
counts(a)

def tcikl(a):
    schetchik = 0
    for el in cycle(a):
        if schetchik > 3:
            break
        print(el)
        schetchik += 1

a = input()
tcikl(a)