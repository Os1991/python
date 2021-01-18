with open('oklad.txt', 'r') as ok:
    staff = ok.readlines()
    b = len(staff)
    ok.seek(0)
    cc = 0
    k = 0
    while k < b:
        a = ok.readline()
        word_list = a.split()
        c = float(word_list[1])
        cc += c
        if c < 20000.00:
            print(f"У сотрудника по фамилии {word_list[0]} оклад меньше 20000 рублей")
        k += 1
    print("Средняя зарпалата - ", int(cc/b), "р")



