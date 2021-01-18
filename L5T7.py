import re
import json

with open("firm.txt", "r") as f:
    rasp = {}
    itog = []
    count = 0
    while True:
        a = f.readline()
        if len(a) > 0:
            asf = re.findall('(\d+)', a)
            ok = (int(asf[1]) - int(asf[2]))
            a = a.split()
            c = a[0]
            if ok > 0:
                rasp[c]=ok
            else:
                continue
        else:
            break
    for items in rasp.values():
        count += items
    dl = len(rasp)
    it = count/dl
    c = {'average': it}
    itog = [rasp, c]
    print(itog)

with open("my_file.json", "w") as write_f:
    json.dump(itog, write_f)