#ДЗ 7. Квадраты натуральных чисел

n = int(input('input value: '))
i = 1
while i < n:
    if i**2 > n:
        break
    print(i ** 2, end=' ')
    i += 1
print()




