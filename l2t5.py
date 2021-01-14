my_list = [9, 8, 3, 2, 2, 1]
new_list = []
ostatok = []
count = 1
a = int(input('Введите натуральное число'))
for i in my_list:
    if a > i:
        new_list.append(a)
        new_list.append(i)
        break
    else:
        new_list.append(i)
    count += 1
    ostatok = my_list[count:]
print(new_list + ostatok)

