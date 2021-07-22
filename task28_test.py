#ДЗ 29. Матрица 2

from random import randint


#M = int(input('Input first matrix size:'))
M = 5
lst = [[randint(1, 50) for _ in range(M)] for _ in range(M)]
tmp_lst = [0] * M


def bubble(array, lst1):
    for i in range(len(array) - 1):

        flag = 1
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                for k in range(M):
                    # if k % 2 == 0 and lst1[j][k] > lst1[j+1][k]:
                    #     for l in range(M):
                    #
                    #         print(lst1[l][0])
                    #         #print(lst1[j+1][k])
                    #         lst1[j][l], lst1[j + 1][l] = lst1[j + 1][l], lst1[j][l]
                    #
                    # #else:
                    #     #print('chetn', k)

                    lst1[k][j], lst1[k][j + 1] = lst1[k][j + 1], lst1[k][j]

                array[j], array[j + 1] = array[j + 1], array[j]
                flag = 0
        if flag:
            break

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
print()
print('POSLE SOTRIROVKI ')
print()

bubble(tmp_lst, lst)


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
