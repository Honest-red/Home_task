#ДЗ 9. Последовательности целых чисел

k_num = 0
s_num = 0
n_max = 0
n_min = 0
s_arif_num = 0
n = 1
while n != 0:
    if n > n_max:
        n_max = n
    if n < n_max:
        n_min = n
    n = int(input('input value: '))
    k_num += 1
    s_num += n


else:
    s_arif_num = s_num / k_num
    print('количесво введенных', k_num)
    print('Сумма', s_num)
    print('Средне арифмет', s_arif_num)
    print('Максимальное', n_max)
    print('Минимальное', n_min)

# количество введённых чисел - это i
# их сумму это q
# среднее арифметическое всех введённых чисел = общую сумму поделить на кол-во введенных попыток
# максимальное через иф наверно большее или меньшее
# минимальное значение
# количество чётных
# не чётных значений - в цикл загнать переменную которая будет проверять четные и не четные и отдельно их счтитаь
# print(n, '   ', q, ' ', i, '   2 ** ', q, ' = ', i, sep='')

