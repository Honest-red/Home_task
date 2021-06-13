#ДЗ 8. Наибольшую целую степень двойки

n = int(input('input value: '))
i = 1
q = 0

while i < n:
    if i*2 > n:
        print (n, '   ', q,' ', i, '   2 ** ', q, ' = ', i, sep='')
        break
    i *= 2
    q +=1
print()

