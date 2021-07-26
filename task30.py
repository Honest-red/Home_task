#ДЗ 30. Конвертер чисел

from string import ascii_uppercase

x = int(input('Input number:'))
sys = int(input('Input systems:'))
lst = []


def convert(x, sys):
    while x != 0:
        i = 0
        if sys >= 16 and x % sys >= 10:
            lst.insert(i, str(ascii_uppercase[x % sys - 10]))
        else:
            lst.insert(i, str(x % sys))
        x = int(x / sys)
        i += 1
    return ''.join(lst)


print(convert(x, sys))
