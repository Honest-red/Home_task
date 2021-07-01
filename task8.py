#ДЗ 8. Наибольшую целую степень двойки

n = int(input('input value: '))
i = 1
q = 1


while i < n:

    i = 2 * i
    q += 1
    #print(q)

else:
    print(n, '   ', q, ' ', i, '   2 ** ', q, ' = ', i, sep='')

