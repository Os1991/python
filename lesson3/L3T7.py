def int_func(c):
    fs = c[0]
    fb = chr(ord(fs) - ord('a') + ord('A'))
    return fb + word[1:]


a = input('Введите слова латиницей в нижнем регистре ').split()
res = []
for word in a:
    res.append(int_func(word))
print(' '.join(res))