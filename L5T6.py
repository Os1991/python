import re

with open("lessons.txt", "r") as su:
    rasp = {}
    list_num = []
    count = 0
    while True:
        a = su.readline()
        asf = re.findall('(\d+)', a)
        ok = sum(map(int, asf))
        count += 1
        if len(a) > 0:
            a = a.split()
            c = a[0][:-1]
            rasp[c]=ok
        else:
            break
    print(rasp)
