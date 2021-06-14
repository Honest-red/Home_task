#ДЗ 9. Последовательности целых чисел

k_num = 0
s_num = 0
s_arif_num = 0
k_chet = 0
k_nchet = 0
n = int(input('input value: '))
n_max = n
n_min = n
while n != 0:
    if n == 0:
        continue
    if n > n_max:
        n_max = n
    if n < n_min:
        n_min = n
    if n % 2 == 0:
        k_chet += 1
    else:
        k_nchet += 1
    k_num += 1
    s_num += n
    n = int(input('input value: '))
else:
    s_arif_num = s_num / k_num
    print()
    print('Количесво введенных чисел', k_num)
    print('Сумма введенных чисел', s_num)
    print('Средне арифметическое', s_arif_num)
    print('Максимальное число', n_max)
    print('Минимальное число', n_min)
    print('Количесво четных', k_chet)
    print('Количесво нечетных', k_nchet)
