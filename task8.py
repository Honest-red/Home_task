#ДЗ 8. Наибольшую целую степень двойки

n = int(input('input value: '))
i = 1
q = 0

while i*2 <= n:
    i *= 2
    q += 1
else:
    print(n, '   ', q, ' ', i, '   2 ** ', q, ' = ', i, sep='')