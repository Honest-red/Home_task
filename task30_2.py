#ДЗ 30. Конвертер чисел (рекурсия)

from string import ascii_uppercase

x = int(input('Input number:'))
sys = int(input('Input systems:'))
lst = []


def convert(x, sys):
    if x == 0:
        return ''.join(lst)
    i = 0
    if sys >= 16 and x % sys >= 10:
        lst.insert(i, str(ascii_uppercase[x % sys - 10]))
    else:
        lst.insert(i, str(x % sys))
    i += 1
    return convert(int(x / sys), sys)


print(convert(x, sys))
