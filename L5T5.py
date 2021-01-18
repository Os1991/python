import random

with open("summa.txt", "w") as su:
    for i in range(int(input('How many to generate?: '))):
        line = str(random.randint(1, 100))
        su.writelines(line + ' ')

with open("summa.txt", "r") as su:
    ans = sum(number for word in su for number in map(int, word.split()))
    print(ans)