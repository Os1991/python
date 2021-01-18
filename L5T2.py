count = 0
with open("testtext.txt", "r") as test:
    while True:
        a = test.readline()
        count += 1
        if len(a) > 0:
            print(f"Количество слов в строке {count} - ", end='')
            print(1 + (a.count(' ')))
        else:
            break

with open("testtext.txt", "r") as test:
    text = test.readlines()
    c = len(text)
    print(f"Количество строк в тексте - {c}")