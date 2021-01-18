with open("testtext.txt", "w") as test:
    while True:
        text = input('Введите текст. Для отмены введите пустую строку')
        if text.isspace():
            break
        else:
            test.writelines(text + '\n')
