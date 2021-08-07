# ДЗ 32. Список студентов

file = open('src_14.txt', 'rt', encoding='utf-8')

while True:

    data = file.readline()
    if data != '':
        lst = data.split()
        print(lst[0], lst[1])
        for i in range(len(lst)):
            if i > 1:
                print(lst[i], end=' ')
        print()
    else:
        break
file.close()

