# Вариант с перебором ЛСТ списка по каждому числу но не полной Аккуратностью

from random import randint

m = 5
lst2 = []

lst = [[randint(1, 50) for i in range(m)] for j in range(m)]

# lst = [randint(1, 50) for i in range(m)]
print(lst)
print()

def v_print(lsk):
    for i in range(m):
        # print(lst[i])
        sum_num = 0
        for j in range(m):
            #print(lst[j][i])

            sum_num = sum_num + lst[j][i]
            #sum_num = sum([int(lst[j][i])])
            #sum_num = sum(lst[j][i])
            #print(lst[i][j], end=' ')
            if sum_num <= 0b1100100:
                if lst[i][j] < 0b1010:
                    k = str('   ' + str(lst[i][j]))
                else:
                    k = str('  ' + str(lst[i][j]))
            else:
                if lst[i][j] < 0b1010:
                    k = str(' ' + str(lst[i][j]))
                else:
                    k = str('' + str(lst[i][j]))

            print(k, end=' ')
            #print(j, end='')
        #break
        lst2.append(sum_num)

        print()

    return lst2
    # return sum_num
print(v_print(lst))
