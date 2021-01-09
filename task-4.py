a = input()
b = 0
while b == 0:
    for i in a:
        if int(i) > b:
            b = int(i)

print(b)