# ПРИМЕР с ошибкой...и

from random import randint

# M = int(input('Input first matrix size:'))
M = 4
lst = [[randint(1, 50) for _ in range(M)] for _ in range(M)]
tmp_lst = [0] * M


def bubble(array, lst1):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for k in range(M):
                    lst1[k][j], lst1[k][j + 1] = lst1[k][j + 1], lst1[k][j]

    for w in range(len(lst1)):
        for u in range(len(lst1) - 1):
            if w % 2 == 0:
                print(lst1[u][w])
                print(lst1[u + 1][w])
                print()
                if lst1[u][w] > lst1[u + 1][w]:
                    lst1[u][w], lst1[u + 1][w] = lst1[u + 1][w], lst1[u][w]
            else:
                print('---', lst1[u][w])
                print('---', lst1[u + 1][w])
                print()
                if lst1[u][w] < lst1[u + 1][w]:
                    lst1[u][w], lst1[u + 1][w] = lst1[u + 1][w], lst1[u][w]


# Вывод не сортированной матрицы

for i in range(M):
    for j in range(M):
        tmp_lst[j] += lst[i][j]

        if lst[i][j] < 10:
            print(' ', lst[i][j], end='\t')
        else:
            print('', lst[i][j], end='\t')
    print('\t')
print()

for value in tmp_lst:
    if value < 100:
        print('', value, end='\t')
    else:
        print(value, end='\t')

print()
print('POSLE SOTRIROVKI ')
print()

bubble(tmp_lst, lst)

# Вывод сортированной матрицы
for i in range(M):
    for j in range(M):
        if lst[i][j] < 10:
            print(' ', lst[i][j], end='\t')
        else:
            print('', lst[i][j], end='\t')

    print('\t')
print()

for value in tmp_lst:
    if value < 100:
        print('', value, end='\t')
    else:
        print(value, end='\t')
print()






