a = input().split(' ')
for i in range(len(a)):
    print(i + 1, end = ' ')
    if len(a[i]) > 10:
        print (a[i][0:10])
    else:
        print(a[i])