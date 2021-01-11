def my_func(a1, a2, a3):
    c = [a1, a2, a3]
    c.sort()
    print(sum(c[1:]))


a1 = int(input())
a2 = int(input())
a3 = int(input())
my_func(a1, a2, a3)