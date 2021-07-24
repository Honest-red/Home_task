#ДЗ 28. Матрица 1

from random import randint

M = int(input('Input first matrix size:'))
lst = [[randint(1, 50) for _ in range(M)] for _ in range(M)]
tmp_lst = [0] * M
print()


def bubble(array, lst1):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                for k in range(M):
                    lst1[k][j], lst1[k][j + 1] = lst1[k][j + 1], lst1[k][j]

    for w in range(M):
        for u in range(M-1):
            for p in range(M):
                if p % 2 == 0:
                    if lst1[u][p] > lst1[u + 1][p]:
                        lst1[u][p], lst1[u + 1][p] = lst1[u + 1][p], lst1[u][p]
                else:
                    if lst1[u][p] < lst1[u + 1][p]:
                        lst1[u][p], lst1[u + 1][p] = lst1[u + 1][p], lst1[u][p]


def print_lst(lst2):
    for i in range(M):
        for j in range(M):
            tmp_lst[j] += lst2[i][j]
            if lst2[i][j] < 10:
                print(' ', lst2[i][j], end='\t')
            else:
                print('', lst2[i][j], end='\t')

        print('\t')
    print()

    for value in tmp_lst:
        if value < 100:
            print('', value, end='\t')
        else:
            print(value, end='\t')
    print()
    return print()



print('До сортировки:')
print_lst(lst)

bubble(tmp_lst, lst)
tmp_lst = [0] * M

print('После сортировки:')
print_lst(lst)






