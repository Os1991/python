from math import factorial

n = int(input())

def fact(a):
    for el in range(n):
             yield factorial(el+1)

for el in fact(n):
    print(el)