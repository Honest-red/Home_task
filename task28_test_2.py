from random import randint


m = 10  # rows stroki
n = 12  # cols stolbchi

tmp_lst = [0*5]  
lst = [[randint(10, 99) for _ in range(n)] for _ in range(m)]

tmp = '{:5}'
for i in range(m):
    s = 0
    for j in range(n):
        print(tmp.format(lst[i][j]), end='')
        s += lst[i][j]
        tmp_lst[j] += lst[i][j]
    print('\t\t', s)
print()

for value in tmp_lst:
    print(tmp.format(value), end='')
print()