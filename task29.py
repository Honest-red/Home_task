#ДЗ 29. Матрица 2

from random import randint

M = int(input('Input first matrix size:'))
N = int(input('Input second matrix size:'))
print()
lst = [[randint(1, 50) for _ in range(N)] for _ in range(M)]
tmp_lst = [0] * N

for i in range(M):
    s = 0
    for j in range(N):
        s += lst[i][j]
        tmp_lst[j] += lst[i][j]
        if lst[i][j] < 10:
            print(' ', lst[i][j], end='\t')
        else:
            print('', lst[i][j], end='\t')
    print('\t', s)
print()

for value in tmp_lst:
    if value < 100:
        print('', value, end='\t')
    else:
        print(value, end='\t')
print()
